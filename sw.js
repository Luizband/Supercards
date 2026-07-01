importScripts("https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.sw.js");

const CACHE_NAME = "supercards-cache-v4";
const urlsToCache = [
  "./",
  "./index.html",
  "./fundotela.png"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
  self.skipWaiting();
});

self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

const BYPASS_HOSTS = [
  "googleapis.com",
  "firebaseio.com",
  "firebaseapp.com",
  "gstatic.com",
  "onesignal.com",
  "google.com"
];

function deveIgnorarCache(request) {
  if (request.method !== "GET") return true;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return true;

  return BYPASS_HOSTS.some(host => url.hostname === host || url.hostname.endsWith("." + host));
}

self.addEventListener("fetch", event => {
  if (deveIgnorarCache(event.request)) return;

  event.respondWith(
    caches.match(event.request).then(cached => cached || fetch(event.request))
  );
});
