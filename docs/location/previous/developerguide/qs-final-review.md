---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-final-review.html
---

# Review the final Amazon Location application
<a name="qs-final-review"></a>

The final source code for this application is included in this section. You can also find the final project [on GitHub](https://github.com/aws-geospatial/amazon-location-samples-js/tree/main/quick-start-using-api-keys).

You can also find a version of the application that uses Amazon Cognito instead of API keys [on GitHub](https://github.com/aws-geospatial/amazon-location-samples-js/tree/main/quick-start-using-cognito).

------
#### [ Overview ]

Select each tab to view the final source code of the files in this quick start tutorial.

The files are:
+ **quickstart.html** — the framework for your application, including the HTML element holders for the map and search results.
+ **main.css** — the stylesheet for the application.
+ **main.js** — the script for your application that authenticates the user, creates the map, and searches on a `click` event.

------
#### [ quickstart.html ]

The HTML framework for the quick start application.

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Quick start tutorial</title>

    <!-- Styles -->
    <link href="https://unpkg.com/maplibre-gl@3.x/dist/maplibre-gl.css" rel="stylesheet" />
    <link href="main.css" rel="stylesheet" />
  </head>

  <body>
    ...
    <footer>This is a simple Amazon Location Service app. Pan and zoom. Click to see details about entities close to a point.</footer>

    <!-- JavaScript dependencies -->
    <script src="https://unpkg.com/maplibre-gl@3.x/dist/maplibre-gl.js"></script>
    <script src="https://unpkg.com/@aws/amazon-location-client@1.x/dist/amazonLocationClient.js"></script>
    <script src="https://unpkg.com/@aws/amazon-location-utilities-auth-helper@1.x/dist/amazonLocationAuthHelper.js"></script>

    <!-- JavaScript for the app -->
    <script src="main.js"></script>
  </body>
</html>
```

------
#### [ main.css ]

The stylesheet for the quick start application.

```
* {
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
}

body {
  margin: 0;
}

header {
  background: #000000;
  padding: 0.5rem;
}

h1 {
  margin: 0;
  text-align: center;
  font-size: 1.5rem;
  color: #ffffff;
}

main {
  display: flex;
  min-height: calc(100vh - 94px);
}

#map {
  flex: 1;
}

aside {
  overflow-y: auto;
  flex: 0 0 30%;
  max-height: calc(100vh - 94px);
  box-shadow: 0 1px 1px 0 #001c244d, 1px 1px 1px 0 #001c2426, -1px 1px 1px 0 #001c2426;
  background: #f9f9f9;
  padding: 1rem;
}

h2 {
  margin: 0;
}

pre {
  white-space: pre-wrap;
  font-family: monospace;
  color: #16191f;
}

footer {
  background: #000000;
  padding: 1rem;
  color: #ffffff;
}
```

------
#### [ main.js ]

The code for the quick start application. The text in {{red}} should be replaced with the appropriate Amazon Location object names.

```
// Amazon Location Service resource names:
const mapName = "{{explore.map}}";
const placesName = "{{explore.place}}";
const region = "{{your_region}}";
const apiKey = "{{v1.public.a1b2c3d4...}}

// Initialize a map
async function initializeMap() {
  // Initialize the map
  const mlglMap = new maplibregl.Map({
    container: "map", // HTML element ID of map element
    center: [-77.03674, 38.891602], // Initial map centerpoint
    zoom: 16, // Initial map zoom
    style: `https://maps.geo.${region}.amazonaws.com/maps/v0/maps/${mapName}/style-descriptor?key=${apiKey}`, // Defines the appearance of the map and authenticates using an API key
  });

  // Add navigation control to the top left of the map
  mlglMap.addControl(new maplibregl.NavigationControl(), "top-left");

  return mlglMap;
}

async function main() {
  // Create an authentication helper instance using an API key
  const authHelper = await amazonLocationAuthHelper.withAPIKey(apiKey);

  // Initialize map and Amazon Location SDK client
  const map = await initializeMap();
  const client = new amazonLocationClient.LocationClient({
    region,
    ...authHelper.getLocationClientConfig(), // Provides configuration required to make requests to Amazon Location
  });

  // Variable to hold marker that will be rendered on click
  let marker;

  // On mouse click, display marker and get results:
  map.on("click", async function (e) {
    // Remove any existing marker
    if (marker) {
      marker.remove();
    }

    // Render a marker on clicked point
    marker = new maplibregl.Marker().setLngLat([e.lngLat.lng, e.lngLat.lat]).addTo(map);

    // Set up parameters for search call
    let params = {
      IndexName: placesName,
      Position: [e.lngLat.lng, e.lngLat.lat],
      Language: "en",
      MaxResults: "5",
    };

    // Set up command to search for results around clicked point
    const searchCommand = new amazonLocationClient.SearchPlaceIndexForPositionCommand(params);

    try {
      // Make request to search for results around clicked point
      const data = await client.send(searchCommand);

      // Write JSON response data to HTML
      document.querySelector("#response").textContent = JSON.stringify(data, undefined, 2);

      // Display place label in an alert box
      alert(data.Results[0].Place.Label);
    } catch (error) {
      // Write JSON response error to HTML
      document.querySelector("#response").textContent = JSON.stringify(error, undefined, 2);

      // Display error in an alert box
      alert("There was an error searching.");
    }
  });
}

main();
```

------

## What's next
<a name="qs-whats-next"></a>

You have completed the quick start tutorial, and should have an idea of how Amazon Location Service is used to build applications. To get more out of Amazon Location, you can check out the following resources:
+ Dive deeper into the [concepts of Amazon Location Service](how-it-works.md)
+ Get more information about [how to use Amazon Location features and functionality](using-amazon-location.md)
+ See how to expand on this sample and build more complex applications by looking at [code examples using Amazon Location](samples.md)
