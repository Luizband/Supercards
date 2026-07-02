import { chromium } from 'playwright';
import { createServer } from 'http';
import { readFileSync, existsSync, mkdirSync } from 'fs';
import { join, extname, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dir = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dir, '..');
const OUT_DIR = join(__dir, 'pdf');

const PAGES = [
  'index.html',
  'login.html',
  'menu.html',
  'batalha.html',
  'arena.html',
  'arena-duo.html',
  'lobby-2x2.html',
  'colecao.html',
  'decks.html',
  'construtor.html',
  'shop.html',
  'missoes.html',
  'perfil.html',
  'amigos.html',
  'troca.html',
  'torneios.html',
  'inventario.html',
  'notificacoes.html',
  'detalhe-notificacao.html',
  'superblackjack.html',
  'manutencao.html',
  'admin.html',
];

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.json': 'application/json',
};

function startServer() {
  return new Promise((resolve) => {
    const server = createServer((req, res) => {
      let path = decodeURIComponent(req.url.split('?')[0]);
      if (path === '/') path = '/design-mocks/index.html';
      const filePath = join(ROOT, path.replace(/^\//, ''));
      if (!filePath.startsWith(ROOT) || !existsSync(filePath)) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      const ext = extname(filePath);
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
      res.end(readFileSync(filePath));
    });
    server.listen(0, '127.0.0.1', () => {
      const { port } = server.address();
      resolve({ server, baseUrl: `http://127.0.0.1:${port}` });
    });
  });
}

async function main() {
  mkdirSync(OUT_DIR, { recursive: true });
  const { server, baseUrl } = await startServer();

  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
  });

  for (const file of PAGES) {
    const url = `${baseUrl}/design-mocks/${file}`;
    const pdfName = file.replace('.html', '.pdf');
    const page = await context.newPage();
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    await page.waitForTimeout(800);
    await page.pdf({
      path: join(OUT_DIR, pdfName),
      width: '390px',
      height: '844px',
      printBackground: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 },
    });
    await page.close();
    console.log(`✓ ${pdfName}`);
  }

  await browser.close();
  server.close();
  console.log(`\n${PAGES.length} PDFs em ${OUT_DIR}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
