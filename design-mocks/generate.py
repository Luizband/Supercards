#!/usr/bin/env python3
"""Gera HTMLs estáticos de mock para revisão de design."""

from pathlib import Path

OUT = Path(__file__).parent

def page(title: str, screen: str, body: str, extra_head: str = "", body_class: str = "bg-app has-mock-banner"):
    return f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mock — {title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="_mock.css">
    {extra_head}
</head>
<body class="{body_class}">
    <div class="mock-banner">mock estático · {screen} · dados fictícios · supercards</div>
{body}
</body>
</html>
"""

def header_player():
    return """
    <header class="flex items-center gap-3 mt-4 mb-6 w-full flex-shrink-0">
        <div class="relative flex-shrink-0">
            <div class="bg-[#dca3e8] w-20 h-20 rounded-full flex items-center justify-center shadow-lg border-2 border-[#bc7bd4] overflow-hidden">
                <img src="../avatar01.png" alt="" class="w-full h-full object-cover" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
                <span class="hidden text-[#7a32a8] font-black text-sm w-full h-full items-center justify-center">RF</span>
            </div>
            <div class="absolute -bottom-2 left-1/2 -translate-x-1/2 bg-[#bc7bd4] w-7 h-7 rounded-full flex items-center justify-center shadow-md border-2 border-[#dca3e8] z-30">
                <span class="text-[#7a32a8] font-black text-xs">12</span>
            </div>
        </div>
        <div class="flex flex-col flex-grow gap-2.5 justify-center overflow-hidden">
            <div class="flex items-center gap-1.5 w-full">
                <div class="bg-[#dca3e8] rounded-full px-3 py-1.5 flex items-center gap-1 shadow-md flex-shrink-0">
                    <span class="text-[#7a32a8] font-black text-sm">1.250</span>
                    <img src="../moedas.png" class="w-4 h-4 object-contain" alt="">
                </div>
                <nav class="bg-[#dca3e8] rounded-full flex justify-between items-center px-2 py-1 shadow-md flex-grow">
                    <button class="bg-[#7a32a8] rounded-full w-7 h-7 flex items-center justify-center"><img src="../perfil.png" class="w-3.5 h-3.5" alt=""></button>
                    <button class="bg-[#7a32a8] rounded-full w-7 h-7 flex items-center justify-center"><img src="../shop.png" class="w-3.5 h-3.5" alt=""></button>
                    <button class="bg-[#7a32a8] rounded-full w-7 h-7 flex items-center justify-center"><img src="../missao.png" class="w-3.5 h-3.5" alt=""></button>
                </nav>
            </div>
            <div class="flex items-center gap-1.5 w-full">
                <div class="bg-[#dca3e8] rounded-full px-2 py-1 w-1/2 h-7 flex items-center justify-center shadow-md">
                    <span class="text-[#7a32a8] font-black text-[10px] uppercase truncate">REINALDO</span>
                </div>
                <div class="flex flex-col items-center flex-grow w-1/2">
                    <div class="w-full border border-[#dca3e8] rounded-full h-2.5 overflow-hidden shadow-inner">
                        <div class="bg-[#dca3e8] h-full" style="width:68%"></div>
                    </div>
                    <span class="text-[#dca3e8] text-[9px] font-bold mt-1">340/500 xp</span>
                </div>
            </div>
        </div>
    </header>"""

def btn_voltar(label="Retornar"):
    return f"""
    <footer class="fixed bottom-8 left-1/2 -translate-x-1/2 w-full flex justify-center z-[100]">
        <a href="index.html" class="bg-[#7a32a8] text-white font-black py-2.5 px-12 rounded-full shadow-2xl border-2 border-[#dca3e8] uppercase text-sm tracking-wider">{label}</a>
    </footer>"""

PAGES = {}

PAGES["login.html"] = page("Login", "index.html / login", """
    <div class="flex items-center justify-center min-h-screen p-4 pt-8">
        <div class="bg-[#bd83d4]/20 backdrop-blur-md border border-[#bd83d4]/50 p-6 md:p-8 rounded-3xl shadow-2xl w-full max-w-md flex flex-col items-center">
            <img src="../logo.png" alt="Supercards" class="w-56 mb-4 drop-shadow-xl">
            <div class="w-full flex flex-col gap-3">
                <input type="email" value="reinaldo@email.com" placeholder="Seu E-mail" class="w-full px-4 py-3 rounded-xl bg-white/80 text-purple-900 font-bold" readonly>
                <input type="password" value="••••••••" placeholder="Sua Senha" class="w-full px-4 py-3 rounded-xl bg-white/80 text-purple-900 font-bold" readonly>
                <label class="flex items-center gap-2 text-white text-sm font-semibold pl-1">
                    <input type="checkbox" checked class="w-4 h-4 accent-purple-600"> Lembrar meu e-mail
                </label>
                <button class="w-full py-3 mt-1 bg-gradient-to-r from-purple-600 to-green-500 text-white font-black text-lg rounded-xl shadow-lg">ENTRAR</button>
                <p class="text-center text-white font-semibold mt-2">Ainda não tem conta? <span class="text-green-300 underline">Crie aqui</span></p>
            </div>
        </div>
    </div>
    <p class="fixed bottom-4 left-0 right-0 text-center text-white/60 text-xs">Variante cadastro: nome, e-mail, senha + botão CRIAR CONTA</p>
""")

PAGES["menu.html"] = page("Menu Principal", "menu.html", f"""
    <div class="fixed inset-0 px-4 pt-4 flex justify-center overflow-hidden w-screen">
        <div class="w-full max-w-sm flex flex-col h-full relative">
            {header_player()}
            <div class="px-2 w-full mb-4">
                <div class="bg-[#7a32a8] border-2 border-[#bc7bd4] rounded-full py-1.5 overflow-hidden shadow-lg flex items-center w-full relative">
                    <div class="absolute left-1 z-10 bg-[#7a32a8] px-2"><img src="../logobrasileirao.png" class="h-5 w-auto" alt=""></div>
                    <div class="w-full overflow-hidden ml-10 mr-10">
                        <span class="text-white font-black text-[10px] uppercase tracking-widest block text-center">Rodada 1 em andamento — acesse e jogue suas partidas!</span>
                    </div>
                </div>
            </div>
            <main class="grid grid-cols-2 gap-x-4 gap-y-8 flex-grow content-center mb-32">
                <div class="flex flex-col items-center"><span class="text-[#dca3e8] font-black text-lg mb-1">Coleção</span><div class="bg-[#dca3e8] w-[80%] aspect-square rounded-[24px] flex items-center justify-center p-4 shadow-lg"><img src="../colecao.png" class="w-full h-full object-contain" alt=""></div></div>
                <div class="flex flex-col items-center"><span class="text-[#dca3e8] font-black text-lg mb-1">Inventário</span><div class="bg-[#dca3e8] w-[80%] aspect-square rounded-[24px] flex items-center justify-center p-4 shadow-lg"><img src="../inventario.png" class="w-full h-full object-contain" alt=""></div></div>
                <div class="flex flex-col items-center"><span class="text-[#dca3e8] font-black text-lg mb-1">Trocas</span><div class="bg-[#dca3e8] w-[80%] aspect-square rounded-[24px] flex items-center justify-center p-4 shadow-lg"><img src="../troca.png" class="w-full h-full object-contain" alt=""></div></div>
                <div class="flex flex-col items-center"><span class="text-[#dca3e8] font-black text-lg mb-1">Batalha</span><div class="bg-[#dca3e8] w-[80%] aspect-square rounded-[24px] flex items-center justify-center p-4 shadow-lg"><img src="../vs.png" class="w-full h-full object-contain" alt=""></div></div>
            </main>
            <footer class="absolute bottom-16 left-0 w-full flex justify-center">
                <div class="bg-[#dca3e8] rounded-full flex items-center p-2 px-3 gap-3 shadow-2xl border-2 border-[#bc7bd4]">
                    <button class="relative bg-[#7a32a8] rounded-full w-12 h-10 flex items-center justify-center"><img src="../notificacoes.png" class="w-7 h-7" alt=""><span class="absolute -top-1 -right-1 h-3.5 w-3.5 bg-red-600 rounded-full border border-white"></span></button>
                    <button class="bg-[#7a32a8] rounded-full w-12 h-10 flex items-center justify-center"><img src="../amigos.png" class="w-7 h-7" alt=""></button>
                    <button class="bg-[#7a32a8] rounded-full w-12 h-10 flex items-center justify-center"><img src="../whats.png" class="w-7 h-7" alt=""></button>
                    <button class="bg-[#7a32a8] rounded-full w-12 h-10 flex items-center justify-center"><img src="../wiki.png" class="w-7 h-7" alt=""></button>
                </div>
            </footer>
        </div>
    </div>
""")

PAGES["batalha.html"] = page("Batalhas", "batalha.html", f"""
    <div class="fixed inset-0 px-4 pt-4 flex justify-center overflow-hidden w-screen">
        <div class="w-full max-w-sm flex flex-col h-full relative">
            {header_player()}
            <main class="flex flex-col items-center w-full flex-grow overflow-y-auto no-scrollbar pb-32">
                <div class="flex items-center gap-3 mb-6">
                    <h1 class="text-[#dca3e8] font-black text-2xl uppercase tracking-wider">BATALHAS</h1>
                    <button class="bg-[#7a32a8] text-white font-black rounded-full w-7 h-7 border-2 border-[#bc7bd4]">?</button>
                </div>
                <div class="w-full max-w-[280px] grid grid-cols-2 gap-4 mb-6">
                    <div class="flex flex-col items-center"><div class="bg-[#dca3e8] w-full aspect-square rounded-[24px] flex items-center justify-center p-4 shadow-xl"><img src="../vs.png" class="w-full h-full object-contain" alt=""></div><span class="text-[#dca3e8] font-black text-sm mt-3 uppercase text-center">Buscar<br>Partida Solo</span></div>
                    <div class="flex flex-col items-center"><div class="bg-[#dca3e8] w-full aspect-square rounded-[24px] flex items-center justify-center p-4 shadow-xl"><img src="../duo.png" class="w-[80%] object-contain" alt=""></div><span class="text-[#dca3e8] font-black text-sm mt-3 uppercase text-center">Arena<br>DUO</span></div>
                    <div class="flex flex-col items-center"><div class="bg-[#dca3e8] w-full aspect-square rounded-[24px] flex items-center justify-center p-4 shadow-xl"><img src="../logotorneio.png" class="w-[80%] object-contain" alt=""></div><span class="text-[#dca3e8] font-black text-sm mt-3 uppercase text-center">Eventos</span></div>
                    <div class="flex flex-col items-center"><div class="bg-[#dca3e8] w-full aspect-square rounded-[24px] flex items-center justify-center p-4 shadow-xl"><img src="../colecao.png" class="w-[80%] object-contain" alt=""></div><span class="text-[#dca3e8] font-black text-sm mt-3 uppercase text-center">Meus<br>Decks</span></div>
                </div>
                <div class="relative bg-[#7a32a8] w-full max-w-[280px] rounded-full py-3 shadow-lg border-2 border-[#bc7bd4] text-center mb-8">
                    <span class="text-white font-black text-sm uppercase tracking-widest">Desafiar Jogador</span>
                    <span class="absolute top-0 right-0 -mt-1 -mr-1 h-4 w-4 bg-red-600 rounded-full border-2 border-white"></span>
                </div>
                <div class="bg-[#dca3e8] rounded-[24px] w-full max-w-[280px] p-5 shadow-2xl border-4 border-[#bc7bd4]">
                    <h2 class="text-[#7a32a8] font-black text-base text-center uppercase tracking-widest mb-4">Ranking Global</h2>
                    <div class="flex flex-col gap-2 text-[#7a32a8] font-bold text-xs">
                        <div class="flex justify-between bg-white/40 rounded-lg px-3 py-2"><span>🥇 ShadowKnight</span><span>142 vit.</span></div>
                        <div class="flex justify-between bg-white/40 rounded-lg px-3 py-2"><span>🥈 Jessie</span><span>128 vit.</span></div>
                        <div class="flex justify-between bg-white/30 rounded-lg px-3 py-2 ring-2 ring-[#7a32a8]"><span>🥉 REINALDO (você)</span><span>87 vit.</span></div>
                        <div class="flex justify-between px-3 py-1 opacity-70"><span>4. Carlos</span><span>76 vit.</span></div>
                        <div class="flex justify-between px-3 py-1 opacity-70"><span>5. Player123</span><span>71 vit.</span></div>
                    </div>
                </div>
            </main>
            {btn_voltar()}
        </div>
    </div>
""")

PAGES["arena.html"] = page("Arena 1v1", "arena.html", """
    <div class="fixed inset-0 overflow-hidden w-screen h-screen bg-arena">
        <div class="w-full h-full max-w-sm mx-auto relative flex flex-col border-x-2 border-[#dca3e8]/30 shadow-2xl">
            <div class="absolute top-4 w-[95%] left-1/2 -translate-x-1/2 flex items-center justify-between bg-[#dca3e8] rounded-full shadow-lg z-50 h-12 px-4 border-2 border-[#bc7bd4]">
                <span class="text-[#7a32a8] font-black text-[11px] uppercase truncate flex-1">JESSIE</span>
                <div class="absolute left-1/2 -translate-x-1/2 -top-3 w-16 h-16 bg-[#dca3e8] rounded-full border-2 border-[#bc7bd4] overflow-hidden flex items-center justify-center text-[#7a32a8] font-black text-[10px]">FOTO</div>
                <button class="bg-red-600 text-white font-black text-[9px] px-3 py-1.5 rounded-full border-2 border-red-800 uppercase">DESISTIR</button>
            </div>
            <div class="w-full h-[45%] relative z-20 mt-16">
                <div class="absolute top-4 left-1/2 -translate-x-1/2 flex justify-center -space-x-4">
                    <div class="card-mock-back w-14"></div><div class="card-mock-back w-14"></div><div class="card-mock-back w-14"></div><div class="card-mock-back w-14"></div><div class="card-mock-back w-14"></div>
                </div>
                <div class="absolute bottom-4 right-4 text-center"><div class="card-mock-back w-14 brightness-50"></div><span class="text-white font-black text-xl -mt-9 block drop-shadow-lg">12</span></div>
            </div>
            <div id="indicador-centro" class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[60%] max-w-[320px] z-40">
                <div class="w-full relative">
                    <div class="w-full text-center mb-4 px-3">
                        <p class="text-[#4ade80] font-black text-2xl uppercase tracking-wider drop-shadow-lg">JESSIE GANHOU O TURNO!</p>
                    </div>
                    <div class="bg-black/75 border-2 border-[#dca3e8] rounded-3xl px-8 py-5 text-center shadow-2xl flex flex-col items-center gap-3">
                        <p class="text-[#4ade80] font-black text-2xl uppercase animate-pulse">SUA VEZ</p>
                        <p class="text-[#dca3e8] font-bold text-[10px] uppercase tracking-widest">Escolha carta e atributo</p>
                    </div>
                </div>
            </div>
            <div class="w-full h-[55%] relative z-20 border-t-2 border-[#dca3e8]/20 bg-black/10">
                <div class="absolute top-4 left-4 text-center"><div class="card-mock-back w-14 brightness-50"></div><span class="text-white font-black text-xl -mt-9 block">10</span></div>
                <div class="absolute bottom-20 left-1/2 -translate-x-1/2 flex justify-center -space-x-4">
                    <div class="card-mock w-20"></div><div class="card-mock w-20" style="background:linear-gradient(135deg,#ec4899,#f472b6)"></div><div class="card-mock w-20" style="background:linear-gradient(135deg,#3b82f6,#60a5fa)"></div><div class="card-mock w-20" style="background:linear-gradient(135deg,#eab308,#facc15)"></div><div class="card-mock w-20" style="background:linear-gradient(135deg,#22c55e,#4ade80)"></div>
                </div>
            </div>
        </div>
    </div>
""", body_class="has-mock-banner")

# --- demais telas ---

shell = lambda title, content, back=True: f"""
    <div class="fixed inset-0 px-4 pt-4 flex justify-center overflow-hidden w-screen">
        <div class="w-full max-w-sm flex flex-col h-full relative pb-24">
            {header_player()}
            {content}
            {btn_voltar() if back else ''}
        </div>
    </div>
"""

PAGES["colecao.html"] = page("Coleção", "colecao.html", shell("Coleção", """
            <div class="bg-[#2a2a2a] rounded-2xl p-4 mb-4 border border-white/10">
                <div class="flex justify-between items-center mb-3">
                    <h1 class="text-[#dca3e8] font-black text-xl uppercase">Coleção</h1>
                    <span class="text-white/70 text-xs font-bold">45/94 únicas</span>
                </div>
                <div class="flex gap-2 text-[10px] font-bold uppercase">
                    <span class="bg-[#7a32a8] text-white px-2 py-1 rounded-full">Grade</span>
                    <span class="bg-white/10 text-white/60 px-2 py-1 rounded-full">Lista</span>
                </div>
            </div>
            <div class="grid grid-cols-3 gap-2 overflow-y-auto no-scrollbar flex-grow">
                """ + "".join([f'<div class="card-mock w-full {"opacity-30 grayscale" if i>8 else ""}"></div>' for i in range(12)]) + """
            </div>
"""))

PAGES["decks.html"] = page("Decks", "decks.html", shell("Decks", """
            <h1 class="text-[#dca3e8] font-black text-2xl text-center uppercase mb-6">Decks</h1>
            <div class="grid grid-cols-3 gap-3 mb-6">
                <div class="bg-[#dca3e8] rounded-2xl p-2 flex flex-col items-center border-4 border-[#7a32a8]"><img src="../baralho01.png" class="w-12 h-12 object-contain mb-1" alt=""><span class="text-[#7a32a8] font-black text-[8px] uppercase text-center leading-tight">Competitivo</span></div>
                <div class="bg-[#dca3e8] rounded-2xl p-2 flex flex-col items-center"><img src="../baralho02.png" class="w-12 h-12 object-contain mb-1" alt=""><span class="text-[#7a32a8] font-black text-[8px] uppercase text-center">Casual</span></div>
                <div class="bg-[#dca3e8] rounded-2xl p-2 flex flex-col items-center border-2 border-dashed border-[#7a32a8]/50"><span class="text-[#7a32a8] font-black text-2xl">+</span><span class="text-[#7a32a8] font-black text-[8px] uppercase">Novo</span></div>
            </div>
            <div class="bg-[#dca3e8] rounded-2xl p-4 border-4 border-[#bc7bd4]">
                <h2 class="text-[#7a32a8] font-black text-center uppercase mb-2">Deck Competitivo</h2>
                <p class="text-[#7a32a8] text-xs text-center font-bold">WR Solo: 62% · 48 partidas · 20 cartas</p>
            </div>
"""))

PAGES["construtor.html"] = page("Construtor de Deck", "construtor.html", shell("Construtor", """
            <div class="text-center mb-4">
                <h1 class="text-[#dca3e8] font-black text-lg uppercase">MEU DECK</h1>
                <p class="text-white font-bold text-sm">18 / 20 cartas</p>
                <p class="text-[#dca3e8] text-[10px] font-bold mt-1">1 Épica · 2 Lendárias · 5 Raras</p>
            </div>
            <div class="grid grid-cols-4 gap-2 flex-grow content-start">
                """ + "".join(['<div class="card-mock w-full"></div>' if i<18 else '<div class="border-2 border-dashed border-[#dca3e8]/40 rounded-lg aspect-[2.5/3.5] flex items-center justify-center text-[#dca3e8] font-black text-xl">+</div>' for i in range(20)]) + """
            </div>
            <div class="flex gap-3 mt-4">
                <button class="flex-1 bg-gray-500 text-white font-black py-3 rounded-full uppercase text-xs">Retornar</button>
                <button class="flex-1 bg-[#7a32a8] text-white font-black py-3 rounded-full uppercase text-xs">Salvar</button>
            </div>
""", back=False))

PAGES["shop.html"] = page("Loja", "shop.html", """
    <div class="h-[100dvh] p-4 pt-8 flex justify-center overflow-hidden">
        <div class="w-full max-w-sm flex flex-col h-full">
            <header class="flex justify-between items-center mb-6 mt-2">
                <button class="bg-[#dca3e8] rounded-full w-10 h-10 text-[#7a32a8] font-black text-xl">←</button>
                <h1 class="text-white font-black text-2xl drop-shadow-md">LOJA</h1>
                <div class="bg-[#dca3e8] rounded-full px-3 py-1.5 flex items-center gap-1"><span class="text-black font-black text-sm">850</span><img src="../moedas.png" class="w-5 h-5" alt=""></div>
            </header>
            <main class="flex flex-col gap-4 overflow-y-auto no-scrollbar pb-20">
                <div class="bg-gradient-to-br from-[#bc7bd4] to-[#7a32a8] rounded-3xl p-4 border-2 border-[#dca3e8] flex flex-col items-center">
                    <h2 class="text-white font-black text-xl mb-1">Bônus Diário</h2>
                    <p class="text-[#7a32a8] bg-[#dca3e8] px-3 py-0.5 rounded-full text-xs font-black mb-2">1 Pacote Básico Grátis</p>
                    <img src="../pacotegratis.png" class="w-20 h-28 object-contain mb-3" alt="">
                    <div class="bg-[#22c55e] text-white font-black py-2 w-full text-center rounded-full text-sm">PEGAR PACOTE</div>
                </div>
                <div class="bg-[#dca3e8] rounded-3xl p-4 flex items-center gap-4 border-4 border-[#bc7bd4]">
                    <img src="../pacotebasico.png" class="w-16 h-24 object-contain" alt="">
                    <div class="flex-grow"><h3 class="text-[#7a32a8] font-black uppercase">Pacote Básico</h3><p class="text-[#7a32a8]/80 text-xs font-bold">5 cartas</p><p class="text-[#7a32a8] font-black mt-2">100 <img src="../moedas.png" class="inline w-4 h-4"></p></div>
                </div>
                <div class="bg-[#dca3e8] rounded-3xl p-4 flex items-center gap-4 border-4 border-[#bc7bd4]">
                    <img src="../pacotepremium.png" class="w-16 h-24 object-contain" alt="">
                    <div class="flex-grow"><h3 class="text-[#7a32a8] font-black uppercase">Pacote Premium</h3><p class="text-[#7a32a8]/80 text-xs font-bold">5 cartas · 1 rara+</p><p class="text-[#7a32a8] font-black mt-2">300 <img src="../moedas.png" class="inline w-4 h-4"></p></div>
                </div>
            </main>
            <a href="index.html" class="fixed bottom-8 left-1/2 -translate-x-1/2 bg-[#7a32a8] text-white font-black py-2.5 px-12 rounded-full border-2 border-[#dca3e8] uppercase text-sm">Índice mocks</a>
        </div>
    </div>
""")

PAGES["missoes.html"] = page("Missões", "missoes.html", shell("Missões", """
            <h1 class="text-[#dca3e8] font-black text-2xl text-center uppercase mb-4">Missões Diárias</h1>
            <div class="flex justify-between mb-6 px-2">
                """ + "".join([f'<div class="flex flex-col items-center"><div class="w-8 h-8 rounded-full {"bg-[#4ade80]" if i<4 else "bg-white/20"} flex items-center justify-center text-[10px] font-black text-[#7a32a8]">{i+1}</div></div>' for i in range(7)]) + """
            </div>
            <div class="flex flex-col gap-3">
                <div class="bg-[#dca3e8] rounded-xl p-3 border-2 border-[#bc7bd4]"><div class="flex justify-between"><span class="text-[#7a32a8] font-black text-xs uppercase">Fazer login</span><span class="text-[#7a32a8] font-bold text-xs">1/1 ✓</span></div><div class="w-full bg-white/40 h-2 rounded-full mt-2"><div class="bg-[#7a32a8] h-full w-full rounded-full"></div></div></div>
                <div class="bg-[#dca3e8] rounded-xl p-3 border-2 border-[#bc7bd4]"><div class="flex justify-between"><span class="text-[#7a32a8] font-black text-xs uppercase">Jogar 1 partida</span><span class="text-[#7a32a8] font-bold text-xs">0/1</span></div><div class="w-full bg-white/40 h-2 rounded-full mt-2"><div class="bg-[#7a32a8] h-full w-0 rounded-full"></div></div></div>
                <div class="bg-[#dca3e8] rounded-xl p-3 border-2 border-[#bc7bd4]"><div class="flex justify-between"><span class="text-[#7a32a8] font-black text-xs uppercase">Realizar uma troca</span><span class="text-[#7a32a8] font-bold text-xs">2/3</span></div><div class="w-full bg-white/40 h-2 rounded-full mt-2"><div class="bg-[#7a32a8] h-full w-2/3 rounded-full"></div></div></div>
            </div>
"""))

PAGES["perfil.html"] = page("Perfil", "perfil.html", shell("Perfil", """
            <div class="flex flex-col items-center mb-6">
                <div class="relative"><div class="w-24 h-24 bg-[#dca3e8] rounded-full border-4 border-[#bc7bd4] flex items-center justify-center text-[#7a32a8] font-black text-2xl">RF</div><span class="absolute -bottom-1 left-1/2 -translate-x-1/2 bg-[#bc7bd4] text-[#7a32a8] font-black text-xs px-2 py-0.5 rounded-full">Nv. 15</span></div>
                <h1 class="text-[#dca3e8] font-black text-xl uppercase mt-3">REINALDO</h1>
                <div class="w-48 border border-[#dca3e8] rounded-full h-2 mt-2"><div class="bg-[#dca3e8] h-full rounded-full" style="width:55%"></div></div>
                <span class="text-[#dca3e8] text-[10px] font-bold mt-1">825 / 1600 xp</span>
            </div>
            <div class="grid grid-cols-3 gap-2 mb-4">
                <div class="bg-[#dca3e8] rounded-xl p-3 text-center"><p class="text-[#7a32a8] font-black text-lg">2.400</p><p class="text-[#7a32a8] text-[9px] font-bold uppercase">Moedas</p></div>
                <div class="bg-[#dca3e8] rounded-xl p-3 text-center"><p class="text-[#7a32a8] font-black text-lg">180</p><p class="text-[#7a32a8] text-[9px] font-bold uppercase">Fragmentos</p></div>
                <div class="bg-[#dca3e8] rounded-xl p-3 text-center"><p class="text-[#7a32a8] font-black text-lg">87</p><p class="text-[#7a32a8] text-[9px] font-bold uppercase">Vitórias</p></div>
            </div>
            <h2 class="text-[#dca3e8] font-black text-sm uppercase mb-2">Badges (8/14)</h2>
            <div class="grid grid-cols-4 gap-2 mb-4">""" + "".join(['<div class="bg-[#dca3e8] aspect-square rounded-lg flex items-center justify-center text-lg">' + ('🏆' if i<8 else '🔒') + '</div>' for i in range(8)]) + """</div>
"""))

PAGES["amigos.html"] = page("Amigos", "amigos.html", shell("Amigos", """
            <div class="flex justify-between items-center mb-4">
                <h1 class="text-[#dca3e8] font-black text-2xl uppercase">Amigos</h1>
                <button class="bg-[#7a32a8] text-white font-black text-[10px] px-4 py-2 rounded-full uppercase">Adicionar</button>
            </div>
            <div class="flex flex-col gap-2 overflow-y-auto no-scrollbar flex-grow">
                <div class="flex items-center justify-between bg-white/90 rounded-lg p-3 border border-[#7a32a8]/20"><div><span class="text-[#7a32a8] font-black text-xs uppercase">Jessie</span><span class="text-green-600 text-[9px] font-bold block">● Online · Nv. 14</span></div><button class="bg-[#7a32a8] text-white text-[9px] font-black px-3 py-1.5 rounded-full uppercase">Desafiar</button></div>
                <div class="flex items-center justify-between bg-white/90 rounded-lg p-3 border border-[#7a32a8]/20"><div><span class="text-[#7a32a8] font-black text-xs uppercase">Carlos</span><span class="text-gray-500 text-[9px] font-bold block">Offline · Nv. 9</span></div><button class="bg-[#7a32a8] text-white text-[9px] font-black px-3 py-1.5 rounded-full uppercase">Desafiar</button></div>
            </div>
            <p class="text-[#dca3e8] text-[10px] font-bold text-center mt-4">1 convite pendente de Player123</p>
"""))

PAGES["troca.html"] = page("Trocas", "troca.html", shell("Trocas", """
            <div class="flex justify-between items-center mb-2"><h1 class="text-[#dca3e8] font-black text-xl uppercase">Trocas</h1><span class="text-[#dca3e8] font-black text-sm">42 frag.</span></div>
            <div class="bg-[#dca3e8]/30 rounded-2xl p-4 border-2 border-[#bc7bd4] mb-4">
                <p class="text-center text-[#dca3e8] font-black text-xs uppercase mb-4">Mesa com Jessie</p>
                <div class="flex justify-around items-center gap-2">
                    <div class="text-center"><p class="text-white text-[9px] font-bold mb-1 uppercase">Enviar</p><div class="card-mock w-16 mx-auto"></div></div>
                    <span class="text-white font-black text-2xl">⇄</span>
                    <div class="text-center"><p class="text-white text-[9px] font-bold mb-1 uppercase">Receber</p><div class="border-2 border-dashed border-white/40 w-16 aspect-[2.5/3.5] rounded-lg mx-auto flex items-center justify-center text-white/50 text-[8px] font-bold">Aguardando</div></div>
                </div>
                <button class="w-full mt-4 bg-[#7a32a8] text-white font-black py-3 rounded-full uppercase text-xs">Trocar (5 fragmentos)</button>
            </div>
"""))

PAGES["torneios.html"] = page("Eventos / Torneios", "torneios.html", shell("Torneios", """
            <h1 class="text-[#dca3e8] font-black text-2xl text-center uppercase mb-6">Eventos</h1>
            <div class="bg-[#dca3e8] rounded-2xl p-4 border-4 border-[#bc7bd4] mb-4">
                <div class="flex items-center gap-3 mb-2"><img src="../logobrasileirao.png" class="h-8" alt=""><h2 class="text-[#7a32a8] font-black uppercase">Brasileirão 2026</h2></div>
                <p class="text-[#7a32a8] font-bold text-xs">Status: <span class="text-red-600">AO VIVO</span> · 8/10 inscritos</p>
                <p class="text-[#7a32a8] text-[10px] mt-1">Início: 28/06/2026 · Rodada 1</p>
                <button class="w-full mt-3 bg-[#7a32a8] text-white font-black py-2 rounded-full text-xs uppercase">Entrar</button>
            </div>
            <div class="bg-[#dca3e8] rounded-2xl p-4 border-4 border-[#bc7bd4]">
                <h2 class="text-[#7a32a8] font-black uppercase mb-1">Superblackjackcards</h2>
                <p class="text-[#7a32a8] text-xs font-bold">Blackjack multiplayer · até 6 jogadores</p>
                <button class="w-full mt-3 bg-[#7a32a8] text-white font-black py-2 rounded-full text-xs uppercase">Ver salas</button>
            </div>
"""))

PAGES["inventario.html"] = page("Inventário", "inventario.html", shell("Inventário", """
            <h1 class="text-[#dca3e8] font-black text-2xl text-center uppercase mb-6">Meus Pacotes</h1>
            <div class="flex flex-col gap-3">
                <div class="bg-[#dca3e8] rounded-xl p-4 flex items-center gap-4 border-2 border-[#bc7bd4]"><img src="../pacotebasico.png" class="w-14 h-20 object-contain" alt=""><div><p class="text-[#7a32a8] font-black uppercase">Pacote Básico</p><p class="text-[#7a32a8] text-xs font-bold">×2</p></div><button class="ml-auto bg-[#7a32a8] text-white font-black text-xs px-4 py-2 rounded-full uppercase">Abrir</button></div>
                <div class="bg-[#dca3e8] rounded-xl p-4 flex items-center gap-4 border-2 border-[#bc7bd4]"><img src="../pacotepremium.png" class="w-14 h-20 object-contain" alt=""><div><p class="text-[#7a32a8] font-black uppercase">Pacote Premium</p><p class="text-[#7a32a8] text-xs font-bold">×1</p></div><button class="ml-auto bg-[#7a32a8] text-white font-black text-xs px-4 py-2 rounded-full uppercase">Abrir</button></div>
            </div>
"""))

PAGES["notificacoes.html"] = page("Notificações", "notificacoes.html", """
    <div class="fixed inset-0 px-4 pt-8 flex justify-center">
        <div class="w-full max-w-sm flex flex-col h-full">
            <header class="flex justify-between items-center mb-6"><button class="text-[#dca3e8] font-black text-2xl">←</button><h1 class="text-[#dca3e8] font-black text-lg uppercase">Caixa de Entrada</h1><button class="text-[#dca3e8] text-[10px] font-bold uppercase">Limpar</button></header>
            <div class="flex flex-col gap-2 overflow-y-auto no-scrollbar pb-20">
                <div class="bg-[#dca3e8] rounded-xl p-4 border-l-4 border-red-500"><p class="text-[#7a32a8] font-black text-xs uppercase">Nova rodada liberada!</p><p class="text-[#7a32a8]/70 text-[10px] font-bold mt-1">01/07/2026 · 06:00</p></div>
                <div class="bg-white/80 rounded-xl p-4 opacity-80"><p class="text-[#7a32a8] font-black text-xs uppercase">Troca aceita por Jessie</p><p class="text-[#7a32a8]/70 text-[10px] font-bold mt-1">30/06/2026</p></div>
                <div class="bg-white/80 rounded-xl p-4 opacity-80"><p class="text-[#7a32a8] font-black text-xs uppercase">Bem-vindo ao Supercards!</p><p class="text-[#7a32a8]/70 text-[10px] font-bold mt-1">28/06/2026</p></div>
            </div>
            <a href="index.html" class="fixed bottom-8 left-1/2 -translate-x-1/2 bg-[#7a32a8] text-white font-black py-2.5 px-12 rounded-full border-2 border-[#dca3e8] uppercase text-sm">Índice mocks</a>
        </div>
    </div>
""")

PAGES["detalhe-notificacao.html"] = page("Detalhe Notificação", "detalhe-notificacao.html", """
    <div class="fixed inset-0 px-4 pt-8 flex justify-center">
        <div class="w-full max-w-sm flex flex-col">
            <header class="flex justify-between items-center mb-6"><button class="text-[#dca3e8] font-black text-2xl">←</button><h1 class="text-[#dca3e8] font-black text-lg uppercase">Mensagem</h1><span class="w-8"></span></header>
            <div class="bg-[#dca3e8] rounded-2xl p-5 border-4 border-[#bc7bd4] flex-grow">
                <h2 class="text-[#7a32a8] font-black text-lg uppercase mb-1">Nova Rodada!</h2>
                <p class="text-[#7a32a8]/70 text-[10px] font-bold mb-4">01/07/2026 às 06:00</p>
                <p class="text-[#7a32a8] font-bold text-sm leading-relaxed">A Rodada 2 do Brasileirão foi liberada. Entre em Batalhas → Eventos e jogue suas partidas antes do prazo. Boa sorte!</p>
            </div>
            <div class="flex gap-3 mt-6 pb-8">
                <button class="flex-1 bg-red-600 text-white font-black py-3 rounded-full uppercase text-xs">Apagar</button>
                <a href="notificacoes.html" class="flex-1 bg-[#7a32a8] text-white font-black py-3 rounded-full uppercase text-xs text-center leading-[2.5rem]">Voltar</a>
            </div>
        </div>
    </div>
""")

PAGES["lobby-2x2.html"] = page("Lobby 2x2", "lobby2x2.html", shell("Lobby 2x2", """
            <h1 class="text-[#dca3e8] font-black text-xl text-center uppercase mb-1">Saguão 2×2</h1>
            <p class="text-white/80 text-[10px] font-bold text-center mb-6">Aguardando 2 jogadores</p>
            <div class="grid grid-cols-2 gap-4 mb-4">
                <div class="bg-blue-600/40 rounded-xl p-3 border-2 border-blue-400"><p class="text-white font-black text-[10px] uppercase text-center mb-2">Equipe Azul</p><div class="bg-white/20 rounded-lg p-2 mb-1 text-white text-[9px] font-bold">Você · Não pronto</div><div class="border border-dashed border-white/40 rounded-lg p-2 text-white/50 text-[9px] text-center">+ Slot vazio</div></div>
                <div class="bg-red-600/40 rounded-xl p-3 border-2 border-red-400"><p class="text-white font-black text-[10px] uppercase text-center mb-2">Equipe Vermelha</p><div class="bg-white/20 rounded-lg p-2 mb-1 text-white text-[9px] font-bold">Carlos · Pronto</div><div class="border border-dashed border-white/40 rounded-lg p-2 text-white/50 text-[9px] text-center">+ Convidar</div></div>
            </div>
            <button class="w-full bg-[#4ade80] text-[#7a32a8] font-black py-3 rounded-full uppercase text-sm mb-2">Estou Pronto</button>
            <button class="w-full bg-[#7a32a8]/50 text-white/50 font-black py-3 rounded-full uppercase text-sm" disabled>Iniciar (host)</button>
"""))

PAGES["arena-duo.html"] = page("Arena DUO", "arenaDUO.html", """
    <div class="fixed inset-0 bg-arena overflow-hidden" style="min-height:100dvh">
        <div class="mock-banner" style="position:fixed">mock · arenaDUO.html · landscape · gire o celular no app real</div>
        <div class="pt-10 px-4 max-w-4xl mx-auto grid grid-cols-4 gap-2 text-center text-white text-[9px] font-black uppercase">
            <div class="bg-green-600/50 rounded-lg p-2 border border-green-400">Você<br>Pronto</div>
            <div class="bg-green-600/50 rounded-lg p-2 border border-green-400">Jessie<br>Pronta</div>
            <div class="bg-red-600/50 rounded-lg p-2 border border-red-400">Rival 1</div>
            <div class="bg-red-600/50 rounded-lg p-2 border border-red-400">Rival 2</div>
        </div>
        <p class="text-center text-white font-black text-2xl mt-4">Placar 2 × 1</p>
        <div class="flex justify-center gap-4 mt-6"><div class="card-mock w-20"></div><div class="card-mock w-20"></div><span class="text-white font-black text-3xl self-center">VS</span><div class="card-mock w-20"></div><div class="card-mock w-20"></div></div>
        <div class="fixed bottom-4 left-1/2 -translate-x-1/2 flex gap-2"><div class="card-mock w-14"></div><div class="card-mock w-14"></div><div class="card-mock w-14"></div><div class="card-mock w-14"></div></div>
        <a href="index.html" class="fixed bottom-4 right-4 bg-[#7a32a8] text-white text-xs font-black px-4 py-2 rounded-full">Índice</a>
    </div>
""", body_class="has-mock-banner")

PAGES["superblackjack.html"] = page("Superblackjack", "superblackjackcards.html", """
    <div class="fixed inset-0 bg-gradient-to-b from-[#1a1a2e] to-[#7a32a8] pt-10 px-4">
        <h1 class="text-[#dca3e8] font-black text-center uppercase text-sm mb-4">Superblackjackcards · Mesa Tigrinho</h1>
        <div class="flex justify-center gap-2 mb-6 flex-wrap">
            <div class="bg-black/40 rounded-lg px-3 py-2 text-white text-[10px] font-bold">J1<br>❤️❤️</div>
            <div class="bg-black/40 rounded-lg px-3 py-2 text-white text-[10px] font-bold">J2<br>❤️❤️</div>
            <div class="bg-black/40 rounded-lg px-3 py-2 text-white text-[10px] font-bold">J3<br>❤️❤️❤️</div>
            <div class="bg-black/40 rounded-lg px-3 py-2 text-white text-[10px] font-bold">J4<br>❤️❤️❤️</div>
        </div>
        <p class="text-center text-white font-black text-4xl mb-2">17</p>
        <p class="text-center text-[#dca3e8] text-xs font-bold mb-6">Contagem da mesa</p>
        <div class="flex justify-center gap-2 mb-8"><div class="card-mock w-16"></div><div class="card-mock w-16"></div><div class="card-mock w-16"></div></div>
        <p class="text-center text-white text-xs font-bold mb-2">Minhas cartas (3) · Deck: 80</p>
        <div class="flex justify-center gap-2"><div class="card-mock w-14"></div><div class="card-mock w-14"></div><div class="card-mock w-14"></div></div>
        <button class="fixed bottom-8 left-1/2 -translate-x-1/2 bg-red-600 text-white font-black px-8 py-3 rounded-full uppercase text-xs">Abandonar</button>
        <a href="index.html" class="fixed bottom-8 right-4 bg-[#7a32a8] text-white text-xs font-black px-4 py-2 rounded-full">Índice</a>
    </div>
""")

PAGES["manutencao.html"] = page("Manutenção", "manutencao.html", """
    <div class="flex items-center justify-center min-h-screen p-4 pt-8">
        <div class="bg-[#dca3e8] border-4 border-[#7a32a8] rounded-2xl p-8 max-w-sm w-full text-center shadow-2xl">
            <span class="text-5xl mb-4 block">🛠️</span>
            <h1 class="text-[#7a32a8] font-black text-2xl uppercase mb-4">Manutenção</h1>
            <p class="text-[#7a32a8] font-bold text-sm leading-relaxed">Estamos atualizando os servidores. Volte em breve para continuar jogando!</p>
            <button class="mt-8 w-full bg-[#7a32a8] text-white font-black py-3 rounded-full uppercase">Tentar reconectar</button>
        </div>
    </div>
""")

PAGES["admin.html"] = page("Admin", "admin.html (admin only)", """
    <div class="min-h-screen bg-gray-900 text-white p-4 pt-10 max-w-lg mx-auto font-mono text-sm">
        <h1 class="text-purple-400 font-black text-xl mb-6 uppercase">God Mode · Admin</h1>
        <div class="bg-gray-800 rounded-lg p-4 mb-4 border border-gray-600">
            <p class="text-gray-400 text-xs mb-2">Status do jogo</p>
            <div class="flex gap-2"><button class="bg-red-600 px-3 py-2 rounded font-bold text-xs">Trancar manutenção</button><button class="bg-green-600 px-3 py-2 rounded font-bold text-xs">Liberar jogo</button></div>
        </div>
        <div class="bg-gray-800 rounded-lg p-4 mb-4 border border-gray-600">
            <p class="text-gray-400 text-xs mb-2">Localizar jogador</p>
            <input class="w-full bg-gray-900 p-2 rounded mb-2 border border-gray-600" value="REINALDO" readonly>
            <p class="text-xs">UID: abc123 · Moedas: <input class="w-20 bg-gray-900 p-1 rounded inline" value="5000"> · Nível: 12</p>
        </div>
        <div class="bg-gray-800 rounded-lg p-4 border border-gray-600">
            <p class="text-gray-400 text-xs mb-2">Superblackjack · Mesa Tigrinho</p>
            <p class="text-xs">Custo: 10 frag · Prêmio: 200 moedas · <span class="text-green-400">Online</span></p>
        </div>
        <a href="index.html" class="block mt-8 text-center text-purple-400 underline text-xs">← Voltar ao índice de mocks</a>
    </div>
""", body_class="has-mock-banner bg-gray-900")

INDEX = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Supercards — Mocks para Design</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="_mock.css">
</head>
<body class="bg-app has-mock-banner min-h-screen p-6 pt-10">
    <div class="mock-banner">índice de mocks · revisão de design · supercards</div>
    <div class="max-w-lg mx-auto">
        <img src="../logo.png" alt="" class="w-40 mx-auto mb-4 drop-shadow-lg">
        <h1 class="text-[#dca3e8] font-black text-2xl text-center uppercase mb-2">Mocks de Telas</h1>
        <p class="text-white/80 text-sm text-center mb-8 font-semibold">HTML estático com dados fictícios. Abra cada link para revisar o layout.</p>
        <ul class="flex flex-col gap-2 text-sm">
            {links}
        </ul>
        <p class="text-white/50 text-[10px] text-center mt-10">Assets em <code class="text-[#dca3e8]">../</code> · Sem Firebase · Março 2026</p>
    </div>
</body>
</html>
"""

SCREEN_LABELS = {
    "login.html": "01 · Login / Cadastro",
    "menu.html": "02 · Menu principal",
    "batalha.html": "03 · Hub de batalhas",
    "arena.html": "04 · Arena 1v1 (partida)",
    "arena-duo.html": "05 · Arena DUO",
    "lobby-2x2.html": "06 · Lobby 2×2",
    "colecao.html": "07 · Coleção",
    "decks.html": "08 · Meus decks",
    "construtor.html": "09 · Construtor de deck",
    "shop.html": "10 · Loja",
    "missoes.html": "11 · Missões diárias",
    "perfil.html": "12 · Perfil",
    "amigos.html": "13 · Amigos",
    "troca.html": "14 · Trocas",
    "torneios.html": "15 · Eventos / Torneios",
    "inventario.html": "16 · Inventário (pacotes)",
    "notificacoes.html": "17 · Notificações",
    "detalhe-notificacao.html": "18 · Detalhe da notificação",
    "superblackjack.html": "19 · Superblackjackcards",
    "manutencao.html": "20 · Manutenção",
    "admin.html": "21 · Admin (interno)",
}

if __name__ == "__main__":
    for name, html in PAGES.items():
        (OUT / name).write_text(html, encoding="utf-8")
        print(f"  ✓ {name}")

    links = "\n".join(
        f'            <li><a href="{f}" class="block bg-[#dca3e8]/90 hover:bg-[#dca3e8] text-[#7a32a8] font-black px-4 py-3 rounded-xl border-2 border-[#bc7bd4] transition-colors">{SCREEN_LABELS.get(f, f)}</a></li>'
        for f in SCREEN_LABELS
    )
    (OUT / "index.html").write_text(INDEX.format(links=links), encoding="utf-8")
    print("  ✓ index.html")
    print(f"\n{len(PAGES)+1} arquivos em {OUT}")
