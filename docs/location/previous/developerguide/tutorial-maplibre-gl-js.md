---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre-gl-js.html
---

# Using MapLibre GL JS with Amazon Location Service
<a name="tutorial-maplibre-gl-js"></a>

Use [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js) to embed client-side maps into web applications.

MapLibre GL JS is an open-source JavaScript library that's compatible with the styles and tiles provided by the Amazon Location Service Maps API. You can integrate MapLibre GL JS within a basic HTML or JavaScript application to embed customizable and responsive client-side maps.

This tutorial describes how to integrate MapLibre GL JS with Amazon Location within a basic HTML and JavaScript application. The same libraries and techniques presented in this tutorial also apply to frameworks, such as [React](https://reactjs.org/) and [Angular](https://angular.io/).

The sample application for this tutorial is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).

## Building the application: Scaffolding
<a name="tutorial-maplibre-js-scaffolding"></a>

This tutorial creates a web application that uses JavaScript to build a map on an HTML page.

Begin by creating an HTML page (`index.html`) that includes the map's container:
+ Enter a `div` element with an `id` of `map` to apply the map's dimensions to the map view. The dimensions are inherited from the viewport.

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
<a name="tutorial-maplibre-js-add-dependencies"></a>

Add the following dependencies to your application:
+ MapLibre GL JS (v3.x), and its associated CSS.
+ The Amazon Location [JavaScript Authentication helper](loc-sdk-auth.md).

```
<!-- CSS dependencies -->
<link
  href="https://unpkg.com/maplibre-gl@3.x/dist/maplibre-gl.css"
  rel="stylesheet"
/>
<!-- JavaScript dependencies -->
<script src="https://unpkg.com/maplibre-gl@3.x/dist/maplibre-gl.js"></script>
<script src="https://unpkg.com/@aws/amazon-location-authentication-helper.js"></script>
<script>
  // application-specific code
</script>
```

This creates an empty page with the map's container.

## Building the application: Configuration
<a name="tutorial-maplibre-js-configuration"></a>

To configure your application using JavaScript:

1. Enter the names and identifiers of your resources.

   ```
   // Cognito Identity Pool ID
   const identityPoolId = "{{us-east-1:54f2ba88-9390-498d-aaa5-0d97fb7ca3bd}}";
   // Amazon Location Service Map name
   const mapName = "{{ExampleMap}}";
   ```

1. Instantiate a credential provider using the unauthenticated identity pool you created in [Using maps - Step 2, Set up authentication](map-prerequisites.md#using-maps-set-up-authentication). We will put this in a function called `initializeMap`, that will also contain other map initialization code, added in the next step

   ```
   // extract the Region from the Identity Pool ID; this will be used for both Amazon Cognito and Amazon Location
   AWS.config.region = identityPoolId.split(":")[0];

   async function initializeMap() {
     // Create an authentication helper instance using credentials from Cognito
     const authHelper = await amazonLocationAuthHelper.withIdentityPoolId(identityPoolId);

     // ... more here, later
   }
   ```

## Building the application: Map initialization
<a name="tutorial-maplibre-js-request-map-init"></a>

For the map to display after the page is loaded, you must initialize the map. You can adjust the initial map location, add additional controls, and overlay data.

```
async function initializeMap() {
  // Create an authentication helper instance using credentials from Cognito
  const authHelper = await amazonLocationAuthHelper.withIdentityPoolId(identityPoolId);

  // Initialize the map
  const map = new maplibregl.Map({
    container: "map",
    center: [-123.1187, 49.2819], // initial map centerpoint
    zoom: 10, // initial map zoom
    style: `https://maps.geo.${region}.amazonaws.com/maps/v0/maps/${mapName}/style-descriptor`,
    ...authHelper.getMapAuthenticationOptions(), // authentication, using cognito
  });

  map.addControl(new maplibregl.NavigationControl(), "top-left");
}

initializeMap();
```

**Note**
You must provide word mark or text attribution for each data provider that you use, either on your application or your documentation. Attribution strings are included in the style descriptor response under the `sources.esri.attribution`, `sources.here.attribution`, and `sources.grabmaptiles.attribution` keys. MapLibre GL JS will automatically provide attribution. When using Amazon Location resources with [data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html), make sure to read the [service terms and conditions](https://aws.amazon.com/service-terms/).

## Running the application
<a name="tutorial-maplibre-js-writing-js"></a>

You can run this sample application by using it in a local web server, or opening it in a browser.

To use a local web server, you can use npx, because it's installed as part of Node.js. You can use `npx serve` from within the same directory as `index.html`. This serves the application on `localhost:5000`.

**Note**
If the policy you created for your unauthenticated Amazon Cognito role includes a `referer` condition, you might be blocked from testing with `localhost:` URLs. In this case. you can test with a web server that provides a URL that is in your policy.

After completing the tutorial, the final application looks like the following example.

```
<!-- index.html -->
<html>
  <head>
    <link href="https://unpkg.com/maplibre-gl@3.x/dist/maplibre-gl.css" rel="stylesheet" />
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
    <!-- map container -->
    <div id="map" />
    <!-- JavaScript dependencies -->
    <script src="https://unpkg.com/maplibre-gl@3.x/dist/maplibre-gl.js"></script>
    <script src="https://unpkg.com/@aws/amazon-location-authentication-helper.js"></script>
    <script>
      // configuration
      const identityPoolId = "us-east-1:54f2ba88-9390-498d-aaa5-0d97fb7ca3bd"; // Cognito Identity Pool ID
      const mapName = "ExampleMap"; // Amazon Location Service Map Name

      // extract the region from the Identity Pool ID
      const region = identityPoolId.split(":")[0];

      async function initializeMap() {
        // Create an authentication helper instance using credentials from Cognito
        const authHelper = await amazonLocationAuthHelper.withIdentityPoolId(identityPoolId);

        // Initialize the map
        const map = new maplibregl.Map({
          container: "map",
          center: [-123.115898, 49.295868],
          zoom: 10,
          style: `https://maps.geo.${region}.amazonaws.com/maps/v0/maps/${mapName}/style-descriptor`,
          ...authHelper.getMapAuthenticationOptions(),
        });
        map.addControl(new maplibregl.NavigationControl(), "top-left");
      }

      initializeMap();
    </script>
  </body>
</html>
```

Running this application displays a full-screen map using your chosen map style. This sample is available in the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
