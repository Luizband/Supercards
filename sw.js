// Importa o Firebase para rodar em segundo plano
importScripts('https://www.gstatic.com/firebasejs/10.12.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.12.0/firebase-messaging-compat.js');

// Configurações do seu projeto
firebase.initializeApp({
  apiKey: "AIzaSyCU3lFTgfrDMaD9jwR7X7ivYPmGQh4VE1g",
  authDomain: "supercards-tcg.firebaseapp.com",
  projectId: "supercards-tcg",
  storageBucket: "supercards-tcg.firebasestorage.app",
  messagingSenderId: "862316380615",
  appId: "1:862316380615:web:b3f28056ebc967673999e2"
});

// Ativa o ouvinte de notificações com o jogo fechado
const messaging = firebase.messaging();

// ----------------------------------------------------

const CACHE_NAME = "supercards-cache-v1";
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
