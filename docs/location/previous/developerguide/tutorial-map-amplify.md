---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tutorial-map-amplify.html
---

# Using the Amplify library with Amazon Location Service
<a name="tutorial-map-amplify"></a>

The following tutorial walks you through using AWS Amplify with Amazon Location. Amplify uses MapLibre GL JS to render maps in your JavaScript-based application.

Amplify is a set of open-source client libraries that provide interfaces to different categories of services, including Amplify Geo, which is powered by Amazon Location Service. [ Learn more about the AWS Amplify Geo JavaScript library](https://docs.amplify.aws/lib/geo/getting-started/q/platform/js/).

**Note**
This tutorial assumes that you have already followed the steps in [Using maps - To add a map to your application](map-prerequisites.md#create-map-resource).

## Building the application: Scaffolding
<a name="tutorial-map-amplify-scaffolding"></a>

This tutorial creates a web application that uses JavaScript to build a map on an HTML page.

Begin by creating an HTML page (`index.html`) that includes the map's container:
+ Enter a `div` element with an `id` of `map` to apply the map's dimensions to the map view. The dimensions are inherited from the viewport.

```
<html>
  <head>
    <style>
      body { margin: 0; }
      #map { height: 100vh; } /* 100% of viewport height */
    </style>
  </head>

  <body>
    <!-- map container -->
    <div id="map" />
  </body>
</html>
```

## Building the application: Adding dependencies
<a name="tutorial-map-amplify-add-dependencies"></a>

Add the following dependencies to your application:
+ AWS Amplify map and geo libraries.
+ AWS Amplify core library.
+ AWS Amplify auth library.
+ AWS Amplify stylesheet.

```
<!-- CSS dependencies -->
    <link href="https://cdn.amplify.aws/packages/maplibre-gl/1.15.2/maplibre-gl.css" rel="stylesheet" integrity="sha384-DrPVD9GufrxGb7kWwRv0CywpXTmfvbKOZ5i5pN7urmIThew0zXKTME+gutUgtpeD" crossorigin="anonymous" referrerpolicy="no-referrer"></link>

<!-- JavaScript dependencies -->
    <script src="https://cdn.amplify.aws/packages/maplibre-gl/1.15.2/maplibre-gl.js" integrity="sha384-rwYfkmAOpciZS2bDuwZ/Xa/Gog6jXem8D/whm3wnsZSVFemDDlprcUXHnDDUcrNU" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.amplify.aws/packages/core/4.3.0/aws-amplify-core.min.js" integrity="sha384-7Oh+5w0l7XGyYvSqbKi2Q7SA5K640V5nyW2/LEbevDQEV1HMJqJLA1A00z2hu8fJ" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.amplify.aws/packages/auth/4.3.8/aws-amplify-auth.min.js" integrity="sha384-jfkXCEfYyVmDXYKlgWNwv54xRaZgk14m7sjeb2jLVBtUXCD2p+WU8YZ2mPZ9Xbdw" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.amplify.aws/packages/geo/1.1.0/aws-amplify-geo.min.js" integrity="sha384-TFMTyWuCbiptXTzvOgzJbV8TPUupG1rA1AVrznAhCSpXTIdGw82bGd8RTk5rr3nP" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.amplify.aws/packages/maplibre-gl-js-amplify/1.1.0/maplibre-gl-js-amplify.umd.min.js" integrity="sha384-7/RxWonKW1nM9zCKiwU9x6bkQTjldosg0D1vZYm0Zj+K/vUSnA3sOMhlRRWAtHPi" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>
  // application-specific code
</script>
```

This creates an empty page with the map's container.

## Building the application: Configuration
<a name="tutorial-map-amplify-configuration"></a>

To configure your application using JavaScript:

1. Enter the identifiers of the unauthenticated identity pool that you created in [Using maps - Step 2, Set up authentication](map-prerequisites.md#create-map-resource).

   ```
   // Cognito Identity Pool ID
   const identityPoolId = "{{region}}:{{identityPoolID}}"; // for example: us-east-1:123example-1234-5678
   // extract the Region from the Identity Pool ID
   const region = identityPoolId.split(":")[0];
   ```

1. Configure AWS Amplify to use the resources you've created, including the identity pool and the Map resource (shown here with the default name of `explore.map`).

   ```
   // Configure Amplify
   const { Amplify } = aws_amplify_core;
   const { createMap } = AmplifyMapLibre;

   Amplify.configure({
     Auth: {
       identityPoolId,
       region,
     },
     geo: {
       AmazonLocationService: {
         maps: {
           items: {
             "explore.map": {
               style: "Default style"
             },
           },
           default: "explore.map",
         },
         region,
       },
     }
   });
   ```

## Building the application: Map initialization
<a name="tutorial-map-amplify-request-map-init"></a>

For the map to display after the page is loaded, you must initialize the map. You can adjust the initial map location, add additional controls, and overlay data.

```
async function initializeMap() {
  const map = await createMap(
    {
      container: "map",
      center: [-123.1187, 49.2819],
      zoom: 10,
      hash: true,
    }
  );

  map.addControl(new maplibregl.NavigationControl(), "top-left");
}

initializeMap();
```

**Note**
You must provide word mark or text attribution for each data provider that you use, either on your application or your documentation. Attribution strings are included in the style descriptor response under the `sources.esri.attribution`, `sources.here.attribution`, and `sources.grabmaptiles.attribution` keys. Amplify will automatically provide attribution. When using Amazon Location resources with [data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html), make sure to read the [service terms and conditions](https://aws.amazon.com/service-terms/).

## Running the application
<a name="tutorial-map-amplify-writing-js"></a>

You can run this sample application by using it in a local web server, or opening it in a browser.

To use a local web server, you can use npx, installed as part of Node.js, or any other web server of your choice. To use npx, type `npx serve` from within the same directory as `index.html`. This serves the application on `localhost:5000`.

**Note**
If the policy that you created for your unauthenticated Amazon Cognito role includes a `referer` condition, you might be blocked from testing with `localhost:` URLs. In this case. you can test with a web server that provides a URL that is in your policy.

After completing the tutorial, the final application looks like the following example.

```
<html>
  <head>
    <!-- CSS dependencies -->
    <link href="https://cdn.amplify.aws/packages/maplibre-gl/1.15.2/maplibre-gl.css" rel="stylesheet" integrity="sha384-DrPVD9GufrxGb7kWwRv0CywpXTmfvbKOZ5i5pN7urmIThew0zXKTME+gutUgtpeD" crossorigin="anonymous" referrerpolicy="no-referrer"></link>

    <!-- JavaScript dependencies -->
    <script src="https://cdn.amplify.aws/packages/maplibre-gl/1.15.2/maplibre-gl.js" integrity="sha384-rwYfkmAOpciZS2bDuwZ/Xa/Gog6jXem8D/whm3wnsZSVFemDDlprcUXHnDDUcrNU" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.amplify.aws/packages/core/4.3.0/aws-amplify-core.min.js" integrity="sha384-7Oh+5w0l7XGyYvSqbKi2Q7SA5K640V5nyW2/LEbevDQEV1HMJqJLA1A00z2hu8fJ" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.amplify.aws/packages/auth/4.3.8/aws-amplify-auth.min.js" integrity="sha384-jfkXCEfYyVmDXYKlgWNwv54xRaZgk14m7sjeb2jLVBtUXCD2p+WU8YZ2mPZ9Xbdw" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.amplify.aws/packages/geo/1.1.0/aws-amplify-geo.min.js" integrity="sha384-TFMTyWuCbiptXTzvOgzJbV8TPUupG1rA1AVrznAhCSpXTIdGw82bGd8RTk5rr3nP" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.amplify.aws/packages/maplibre-gl-js-amplify/1.1.0/maplibre-gl-js-amplify.umd.min.js" integrity="sha384-7/RxWonKW1nM9zCKiwU9x6bkQTjldosg0D1vZYm0Zj+K/vUSnA3sOMhlRRWAtHPi" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

    <style>
      body { margin: 0; }
      #map { height: 100vh; }
    </style>
  </head>

  <body>
    <div id="map" />
    <script type="module">
      // Cognito Identity Pool ID
      const identityPoolId = "{{region}}:{{identityPoolId}}"; // for example: us-east-1:123example-1234-5678
      // extract the Region from the Identity Pool ID
      const region = identityPoolId.split(":")[0];

      // Configure Amplify
      const { Amplify } = aws_amplify_core;
      const { createMap } = AmplifyMapLibre;

      Amplify.configure({
        Auth: {
          identityPoolId,
          region,
        },
        geo: {
          AmazonLocationService: {
            maps: {
              items: {
                "explore.map": {
                  style: "Default style"
                },
              },
              default: "explore.map",
            },
            region,
          },
        }
      });

      async function initializeMap() {
        const map = await createMap(
          {
            container: "map",
            center: [-123.1187, 49.2819],
            zoom: 10,
            hash: true,
          }
        );

        map.addControl(new maplibregl.NavigationControl(), "top-left");
      }

      initializeMap();
    </script>
  </body>
</html>
```

Running this application displays a full-screen map using your chosen map style. This sample is also described on the **Embed map** tab of any Map resource page in the [Amazon Location Service console](https://console.aws.amazon.com/location/maps/home).

After you complete this tutorial, go to the [ Display a map](https://docs.amplify.aws/lib/geo/maps/q/platform/js#display-a-map) topic in the AWS Amplify documentation to learn more, including how to display markers on the map.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
