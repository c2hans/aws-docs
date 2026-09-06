---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram-js.html
---

# Using Tangram with Amazon Location Service
<a name="tutorial-tangram-js"></a>

[Tangram](https://tangrams.readthedocs.io/) is a flexible mapping engine, designed for real-time rendering of 2D and 3D maps from vector tiles. It can be used with Mapzen-designed styles and the HERE tiles provided by the Amazon Location Service Maps API. This guide describes how to integrate Tangram with Amazon Location within a basic HTML/JavaScript application, although the same libraries and techniques also apply when using frameworks like React and Angular.

Tangram is built atop [Leaflet](https://leafletjs.com/), an open-source JavaScript library for mobile-friendly interactive maps. This means that many Leaflet-compatible plugins and controls also work with Tangram.

Tangram styles built to work with the [Tilezen schema](https://tilezen.readthedocs.io/en/latest/layers/) are largely compatible with Amazon Location when using maps from HERE. These include:
+ [Bubble Wrap](https://github.com/tangrams/bubble-wrap) – A full-featured wayfinding style with helpful icons for points of interest
+ [Cinnabar](https://github.com/tangrams/cinnabar-style) – A classic look and go-to for general mapping applications
+ [Refill ](https://github.com/tangrams/refill-style) – A minimalist map style designed for data visualization overlays, inspired by the seminal Toner style by Stamen Design
+ [Tron](https://github.com/tangrams/tron-style) – An exploration of scale transformations in the visual language of TRON
+ [Walkabout ](https://github.com/tangrams/walkabout-style) – An outdoor-focused style that's perfect for hiking or getting out and about

This guide describes how to integrate Tangram with Amazon Location within a basic HTML/JavaScript application using the Tangram Style called [Bubble Wrap](https://github.com/tangrams/bubble-wrap). This sample is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).

While other Tangram styles are best accompanied by raster tiles, which encode terrain information, this feature is not yet supported by Amazon Location.

**Important**
The Tangram styles in the following tutorial are only compatible with Amazon Location map resources configured with the `VectorHereContrast` style.

## Building the application: Scaffolding
<a name="tutorial-tangram-js-scaffolding"></a>

The application is an HTML page with JavaScript to build the map on your web application. Create an HTML page (`index.html`) and create the map's container:
+ Enter a `div` element with an `id` of map to apply the map's dimensions to the map view.
+ The dimensions are inherited from the viewport.

```
<html>
  <head>
    <style>
      body {
        margin: 0;
      }

      #map {
        height: 100vh; /* 100% of viewport height */
      }
    </style>
  </head>
  <body>
    <!-- map container -->
    <div id="map" />
  </body>
</html>
```

## Building the application: Adding dependencies
<a name="tutorial-tangram-js-add-dependencies"></a>

Add the following dependencies:
+ Leaflet and its associated CSS.
+ Tangram.
+ AWS SDK for JavaScript.

```
<!-- CSS dependencies -->
<link
  rel="stylesheet"
  href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
  integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
  crossorigin=""
/>
<!-- JavaScript dependencies -->
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
<script src="https://unpkg.com/tangram"></script>
<script src="https://sdk.amazonaws.com/js/aws-sdk-2.784.0.min.js"></script>
<script>
  // application-specific code
</script>
```

This creates an empty page with the necessary prerequisites. The next step guides you through writing the JavaScript code for your application.

## Building the application: Configuration
<a name="tutorial-tangram-js-configuration"></a>

To configure your application with your resources and credentials:

1. Enter the names and identifiers of your resources.

   ```
   // Cognito Identity Pool ID
   const identityPoolId = "{{us-east-1:54f2ba88-9390-498d-aaa5-0d97fb7ca3bd}}";
   // Amazon Location Service map name; must be HERE-backed
   const mapName = "{{TangramExampleMap}}";
   ```

1. Instantiate a credential provider using the unauthenticated identity pool you created in [Using maps - Step 2, Set up authentication](map-prerequisites.md#using-maps-set-up-authentication). Since this uses credentials outside the normal AWS SDK work flow, sessions expire after **one** hour.

   ```
   // extract the region from the Identity Pool ID; this will be used for both Amazon Cognito and Amazon Location
   AWS.config.region = identityPoolId.split(":", 1)[0];

   // instantiate a Cognito-backed credential provider
   const credentials = new AWS.CognitoIdentityCredentials({
     IdentityPoolId: {{identityPoolId}},
   });
   ```

1. While Tangram allows you to override the URL(s) used to fetch tiles, it doesn't include the ability to intercept requests so that they can be signed.

   To work around this, override `sources.mapzen.url` to point to Amazon Location using a synthetic host name `amazon.location`, which will be handled by a [service worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API). The following is an example of scene configuration using [Bubble Wrap](https://github.com/tangrams/bubble-wrap):

   ```
   const scene = {
     import: [
       // Bubble Wrap style
       "https://www.nextzen.org/carto/bubble-wrap-style/10/bubble-wrap-style.zip",
       "https://www.nextzen.org/carto/bubble-wrap-style/10/themes/label-7.zip",
       "https://www.nextzen.org/carto/bubble-wrap-style/10/themes/bubble-wrap-road-shields-usa.zip",
       "https://www.nextzen.org/carto/bubble-wrap-style/10/themes/bubble-wrap-road-shields-international.zip",
     ],
     // override values beneath the `sources` key in the style above
     sources: {
       mapzen: {
         // point at Amazon Location using a synthetic URL, which will be handled by the service
         // worker
         url: `https://amazon.location/${mapName}/{z}/{x}/{y}`,
       },
       // effectively disable raster tiles containing encoded normals
       normals: {
         max_zoom: 0,
       },
       "normals-elevation": {
         max_zoom: 0,
       },
     },
   };
   ```

## Building the application: Request transformation
<a name="tutorial-tangram-js-request-transformation"></a>

To register and initialize the service worker, create a `registerServiceWorker` function to be called before the map is initialized. This registers the JavaScript code provided in a separate file called `sw.js` as the service worker controlling `index.html`.

Credentials are loaded from Amazon Cognito and are passed into the service worker alongside the Region to provide information to sign tile requests with [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

```
/**
 * Register a service worker that will rewrite and sign requests using Signature Version 4.
 */
async function registerServiceWorker() {
  if ("serviceWorker" in navigator) {
    try {
      const reg = await navigator.serviceWorker.register("./sw.js");

      // refresh credentials from Amazon Cognito
      await credentials.refreshPromise();

      await reg.active.ready;

      if (navigator.serviceWorker.controller == null) {
        // trigger a navigate event to active the controller for this page
        window.location.reload();
      }

      // pass credentials to the service worker
      reg.active.postMessage({
        credentials: {
          accessKeyId: {{credentials.accessKeyId}},
          secretAccessKey: {{credentials.secretAccessKey}},
          sessionToken: {{credentials.sessionToken}},
        },
        region: AWS.config.region,
      });
    } catch (error) {
      console.error("Service worker registration failed:", error);
    }
  } else {
    console.warn("Service worker support is required for this example");
  }
}
```

The Service Worker implementation in `sw.js` listens for `message` events to pick up credential and Region configuration changes. It also acts as a proxy server by listening for `fetch` events. `fetch` events targeting the `amazon.location` synthetic host name will be rewritten to target the appropriate Amazon Location API and signed using Amplify Core's `Signer`.

```
// sw.js
self.importScripts(
  "https://unpkg.com/@aws-amplify/core@3.7.0/dist/aws-amplify-core.min.js"
);

const { Signer } = aws_amplify_core;

let credentials;
let region;

self.addEventListener("install", (event) => {
  // install immediately
  event.waitUntil(self.skipWaiting());
});

self.addEventListener("activate", (event) => {
  // control clients ASAP
  event.waitUntil(self.clients.claim());
});

self.addEventListener("message", (event) => {
  const {
    data: { credentials: newCredentials, region: newRegion },
  } = event;

  if (newCredentials != null) {
    credentials = newCredentials;
  }

  if (newRegion != null) {
    region = newRegion;
  }
});

async function signedFetch(request) {
  const url = new URL(request.url);
  const path = url.pathname.slice(1).split("/");

  // update URL to point to Amazon Location
  url.pathname = `/maps/v0/maps/${path[0]}/tiles/${path.slice(1).join("/")}`;
  url.host = `maps.geo.${region}.amazonaws.com`;
  // strip params (Tangram generates an empty api_key param)
  url.search = "";

  const signed = Signer.signUrl(url.toString(), {
    access_key: credentials.accessKeyId,
    secret_key: credentials.secretAccessKey,
    session_token: credentials.sessionToken,
  });

  return fetch(signed);
}

self.addEventListener("fetch", (event) => {
  const { request } = event;

  // match the synthetic hostname we're telling Tangram to use
  if (request.url.includes("amazon.location")) {
    return event.respondWith(signedFetch(request));
  }

  // fetch normally
  return event.respondWith(fetch(request));
});
```

To automatically renew credentials and send them to the service worker before they expire, use the following function within `index.html`:

```
async function refreshCredentials() {
  await credentials.refreshPromise();

  if ("serviceWorker" in navigator) {
    const controller = navigator.serviceWorker.controller;

    controller.postMessage({
      credentials: {
        accessKeyId: credentials.accessKeyId,
        secretAccessKey: credentials.secretAccessKey,
        sessionToken: credentials.sessionToken,
      },
    });
  } else {
    console.warn("Service worker support is required for this example.");
  }

  // schedule the next credential refresh when they're about to expire
  setTimeout(refreshCredentials, credentials.expireTime - new Date());
}
```

## Building the application: Map initialization
<a name="tutorial-tangram-js-request-map-init"></a>

For the map to display after the page is loaded, you must initialize the map. You have the option to adjust the initial map location, add additional controls, and overlay data.

**Note**
You must provide word mark or text attribution for each data provider that you use, either on your application or your documentation. Attribution strings are included in the style descriptor response under the `sources.esri.attribution`, `sources.here.attribution`, and `source.grabmaptiles.attribution` keys.
Because Tangram doesn't request these resources, and is only compatible with maps from HERE, use "© 2020 HERE". When using Amazon Location resources with [data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html), make sure to read the [service terms and conditions](https://aws.amazon.com/service-terms/).

```
/**
 * Initialize a map.
 */
async function initializeMap() {
  // register the service worker to handle requests to https://amazon.location
  await registerServiceWorker();

  // Initialize the map
  const map = L.map("map").setView([49.2819, -123.1187], 10);
  Tangram.leafletLayer({
    scene,
  }).addTo(map);
  map.attributionControl.setPrefix("");
  map.attributionControl.addAttribution("© 2020 HERE");
}

initializeMap();
```

## Running the application
<a name="tutorial-tangram-js-writing-js"></a>

To run this sample, you can:
+ Use a host that supports HTTPS,
+ Use a local web server to comply with service worker security restrictions.

To use a local web server, you can use npx, because it's installed as a part of Node.js. You can use `npx serve` from within the same directory as `index.html` and `sw.js`. This serves the application on [localhost:5000](http://localhost:5000/).

The following is the `index.html` file:

```
<!-- index.html -->
<html>
  <head>
    <link
      rel="stylesheet"
      href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
      integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
      crossorigin=""
    />
    <style>
      body {
        margin: 0;
      }

      #map {
        height: 100vh;
      }
    </style>
  </head>

  <body>
    <div id="map" />
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
    <script src="https://unpkg.com/tangram"></script>
    <script src="https://sdk.amazonaws.com/js/aws-sdk-2.784.0.min.js"></script>
    <script>
      // configuration
      // Cognito Identity Pool ID
      const identityPoolId = "<Identity Pool ID>";
      // Amazon Location Service Map name; must be HERE-backed
      const mapName = "<Map name>";

      AWS.config.region = identityPoolId.split(":")[0];

      // instantiate a credential provider
      credentials = new AWS.CognitoIdentityCredentials({
        IdentityPoolId: identityPoolId,
      });

      const scene = {
        import: [
          // Bubble Wrap style
          "https://www.nextzen.org/carto/bubble-wrap-style/10/bubble-wrap-style.zip",
          "https://www.nextzen.org/carto/bubble-wrap-style/10/themes/label-7.zip",
          "https://www.nextzen.org/carto/bubble-wrap-style/10/themes/bubble-wrap-road-shields-usa.zip",
          "https://www.nextzen.org/carto/bubble-wrap-style/10/themes/bubble-wrap-road-shields-international.zip",
        ],
        // override values beneath the `sources` key in the style above
        sources: {
          mapzen: {
            // point at Amazon Location using a synthetic URL, which will be handled by the service
            // worker
            url: `https://amazon.location/${mapName}/{z}/{x}/{y}`,
          },
          // effectively disable raster tiles containing encoded normals
          normals: {
            max_zoom: 0,
          },
          "normals-elevation": {
            max_zoom: 0,
          },
        },
      };

      /**
       * Register a service worker that will rewrite and sign requests using Signature Version 4.
       */
      async function registerServiceWorker() {
        if ("serviceWorker" in navigator) {
          try {
            const reg = await navigator.serviceWorker.register("./sw.js");

            // refresh credentials from Amazon Cognito
            await credentials.refreshPromise();

            await reg.active.ready;

            if (navigator.serviceWorker.controller == null) {
              // trigger a navigate event to active the controller for this page
              window.location.reload();
            }

            // pass credentials to the service worker
            reg.active.postMessage({
              credentials: {
                accessKeyId: credentials.accessKeyId,
                secretAccessKey: credentials.secretAccessKey,
                sessionToken: credentials.sessionToken,
              },
              region: AWS.config.region,
            });
          } catch (error) {
            console.error("Service worker registration failed:", error);
          }
        } else {
          console.warn("Service Worker support is required for this example");
        }
      }

      /**
       * Initialize a map.
       */
      async function initializeMap() {
        // register the service worker to handle requests to https://amazon.location
        await registerServiceWorker();

        // Initialize the map
        const map = L.map("map").setView([49.2819, -123.1187], 10);
        Tangram.leafletLayer({
          scene,
        }).addTo(map);
        map.attributionControl.setPrefix("");
        map.attributionControl.addAttribution("© 2020 HERE");
      }

      initializeMap();
    </script>
  </body>
</html>
```

The following is the `sw.js` file:

```
// sw.js
self.importScripts(
  "https://unpkg.com/@aws-amplify/core@3.7.0/dist/aws-amplify-core.min.js"
);

const { Signer } = aws_amplify_core;

let credentials;
let region;

self.addEventListener("install", (event) => {
  // install immediately
  event.waitUntil(self.skipWaiting());
});

self.addEventListener("activate", (event) => {
  // control clients ASAP
  event.waitUntil(self.clients.claim());
});

self.addEventListener("message", (event) => {
  const {
    data: { credentials: newCredentials, region: newRegion },
  } = event;

  if (newCredentials != null) {
    credentials = newCredentials;
  }

  if (newRegion != null) {
    region = newRegion;
  }
});

async function signedFetch(request) {
  const url = new URL(request.url);
  const path = url.pathname.slice(1).split("/");

  // update URL to point to Amazon Location
  url.pathname = `/maps/v0/maps/${path[0]}/tiles/${path.slice(1).join("/")}`;
  url.host = `maps.geo.${region}.amazonaws.com`;
  // strip params (Tangram generates an empty api_key param)
  url.search = "";

  const signed = Signer.signUrl(url.toString(), {
    access_key: credentials.accessKeyId,
    secret_key: credentials.secretAccessKey,
    session_token: credentials.sessionToken,
  });

  return fetch(signed);
}

self.addEventListener("fetch", (event) => {
  const { request } = event;

  // match the synthetic hostname we're telling Tangram to use
  if (request.url.includes("amazon.location")) {
    return event.respondWith(signedFetch(request));
  }

  // fetch normally
  return event.respondWith(fetch(request));
});
```

 This sample is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).
