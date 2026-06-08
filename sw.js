importScripts("https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.sw.js");

const CACHE_NAME = "supercards-cache-v2";
const urlsToCache = [
  "./",
  "./index.html",
  "./fundotela.png"
  // Depois podemos adicionar mais coisas aqui se quiser
];

// Instala o Service Worker e salva os arquivos iniciais
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Intercepta as requisições para deixar o jogo mais rápido
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      // Retorna do cache se existir, senão baixa da internet
      return response || fetch(event.request);
    })
  );
});
