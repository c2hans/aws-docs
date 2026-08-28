---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/dev-maplibre.html
---

# Use MapLibre tools and libraries with Amazon Location
<a name="dev-maplibre"></a>

One of the important tools for creating interactive applications with Amazon Location is MapLibre. [MapLibre](https://maplibre.org/) is primarily a rendering engine for displaying maps in a web or mobile application. However, it also includes support for plug-ins, and provides functionality for working with other aspects of Amazon Location. The following describes tools that you can use, based on the area of location that you want to work with.

**Note**
To use any aspect of Amazon Location, install the [AWS SDK for the language that you want to use](dev-by-language.md).
+ **Maps**

  To display maps in your application, you need a map rendering engine that will use the data provided by Amazon Location, and draw to the screen. Map rendering engines also provide functionality to pan and zoom the map, or to add markers or pushpins and other annotations to the map.

  Amazon Location Service recommends rendering maps using the [MapLibre](https://github.com/maplibre/maplibre-gl-js) rendering engine. MapLibre GL JS is an engine for displaying maps in JavaScript, while MapLibre Native provides maps for either iOS or Android.

  MapLibre also has a plug-in ecosystem to extend the core functionality. For more information, visit [https://maplibre.org/maplibre-gl-js/docs/plugins/](https://maplibre.org/maplibre-gl-js/docs/plugins/).
+ **Places search**

  To make creating a search user interface simpler, you can use the [MapLibre geocoder](https://github.com/maplibre/maplibre-gl-geocoder) for web (Android applications can use the [Android Places plug-in](https://github.com/maplibre/maplibre-plugins-android/tree/master/plugin-places)).

  Use the [Amazon Location for Maplibre geocoder library](https://github.com/aws-geospatial/amazon-location-for-maplibre-gl-geocoder?tab=readme-ov-file) to simplify the process of using Amazon Location with `amazon-location-for-maplibre-gl-geocoder` in JavaScript Applications.
+ **Routes**

  To display routes on the map, use [MapLibre directions](https://github.com/maplibre/maplibre-gl-directions).
+ **Geofences and Trackers**

  MapLibre doesn't have any specific rendering or tools for geofences and tracking, but you can use the rendering functionality and [plug-ins](https://maplibre.org/maplibre-gl-js/docs/plugins/) to show the geofences and tracked devices on the map.

  The devices being tracked can use [MQTT](tracking-using-mqtt.md) or manually send updates to Amazon Location Service. Geofence events can be responded to using [AWS Lambda](https://docs.aws.amazon.com/lambda/).

Many open source libraries are available to provide additional functionality for Amazon Location Service, for example [Turf](https://github.com/Turfjs/turf) which provide spatial analysis functionality.

Many libraries use the open standard [GeoJSON](https://geojson.org/) formatted data. Amazon Location Service provides a library to support using GeoJSON in JavaScript applications. For more information, see the next section, [How to use Amazon Location SDK and libraries](dev-location-libraries.md).

## Amazon Location MapLibre Geocoder Plugin
<a name="dev-maplibre-grocoder"></a>

The Amazon Location MapLibre geocoder plugin is designed to make it easier for you to incorporate Amazon Location functionality into your JavaScript applications, when working with map rendering and geocoding using the [maplibre-gl-geocoder](https://github.com/maplibre/maplibre-gl-geocoder) library.

Installation
You can install Amazon Location MapLibre geocoder plugin from NPM for usage with modules, with this command:

```
npm install @aws/amazon-location-for-maplibre-gl-geocoder
```
You can import into an HTML file for usage directly in the browser, with a script:

```
<script src="https://www.unpkg.com/@aws/amazon-location-for-maplibre-gl-geocoder@1">/script<
```

Usage with Module
This code sets up a Maplibre GL JavaScript map with Amazon Location geocoding capabilities. It uses authentication via Amazon Cognito Identity Pool to access Amazon Location resources. The map is rendered with a specified style and center coordinates, and allows to search for places on the map.

```
// Import MapLibre GL JS
import maplibregl from "maplibre-gl";
// Import from the AWS JavaScript SDK V3
import { LocationClient } from "@aws-sdk/client-location";
// Import the utility functions
import { withIdentityPoolId } from "@aws/amazon-location-utilities-auth-helper";
// Import the AmazonLocationWithMaplibreGeocoder
import { buildAmazonLocationMaplibreGeocoder, AmazonLocationMaplibreGeocoder } from "@aws/amazon-location-for-maplibre-gl-geocoder"

const identityPoolId = "{{Identity Pool ID}}";
const mapName = "{{Map Name}}";
const region = "{{Region}}"; // region containing the Amazon Location resource
const placeIndex = "{{PlaceIndexName}}" // Name of your places resource in your AWS Account.

// Create an authentication helper instance using credentials from Amazon Cognito
const authHelper = await withIdentityPoolId("{{Identity Pool ID}}");

const client = new LocationClient({
  region: "{{Region}}", // Region containing Amazon Location resources
  ...authHelper.getLocationClientConfig(), // Configures the client to use credentials obtained via Amazon Cognito
});

// Render the map
const map = new maplibregl.Map({
    container: "map",
    center: [-123.115898, 49.295868],
    zoom: 10,
    style: `https://maps.geo.${region}.amazonaws.com/maps/v0/maps/${mapName}/style-descriptor`,
    ...authHelper.getMapAuthenticationOptions(),
});

// Gets an instance of the AmazonLocationMaplibreGeocoder Object.
const amazonLocationMaplibreGeocoder = buildAmazonLocationMaplibreGeocoder(client, placeIndex, {enableAll: true});

// Now we can add the Geocoder to the map.
map.addControl(amazonLocationMaplibreGeocoder.getPlacesGeocoder());
```

Usage with a browser
This example uses the Amazon Location Client to make a request that authenticates using Amazon Cognito.
Some of these example use the Amazon Location Client. The Amazon Location Client is based on the [AWS SDK for JavaScript V3](https://github.com/aws/aws-sdk-js-v3) and allows for making calls to Amazon Location through a script referenced in an HTML file.
Include the following in an HTML file:

```
< Import the Amazon Location With Maplibre Geocoder>
<script src="https://www.unpkg.com/@aws/amazon-location-with-maplibre-geocoder@1"></script>
<Import the Amazon Location Client>
<script src="https://www.unpkg.com/@aws/amazon-location-client@1"></script>
<!Import the utility library>
<script src="https://www.unpkg.com/@aws/amazon-location-utilities-auth-helper@1"></script>
```
Include the following in a JavaScript file:

```
const identityPoolId = "{{Identity Pool ID}}";
const mapName = "{{Map Name}}";
const region = "{{Region}}"; // region containing Amazon Location resource

// Create an authentication helper instance using credentials from Amazon Cognito
const authHelper = await amazonLocationAuthHelper.withIdentityPoolId(identityPoolId);

// Render the map
const map = new maplibregl.Map({
  container: "map",
  center: [-123.115898, 49.295868],
  zoom: 10,
  style: `https://maps.geo.${region}.amazonaws.com/maps/v0/maps/${mapName}/style-descriptor`,
  ...authHelper.getMapAuthenticationOptions(),
});

// Initialize the AmazonLocationMaplibreGeocoder object
const amazonLocationMaplibreGeocoderObject = amazonLocationMaplibreGeocoder.buildAmazonLocationMaplibreGeocoder(client, placesName, {enableAll: true});

// Use the AmazonLocationWithMaplibreGeocoder object to add a geocoder to the map.
map.addControl(amazonLocationMaplibreGeocoderObject.getPlacesGeocoder());
```

Listed below are the functions, and commands used in the Amazon Location MapLibre geocoder plugin:
+ **`buildAmazonLocationMaplibreGeocoder`**

  This class creates an instance of the `AmazonLocationMaplibreGeocder` which is the entry point to the other all other calls:

  ```
  const amazonLocationMaplibreGeocoder = buildAmazonLocationMaplibreGeocoder(client, placesIndex, {enableAll: true});
  ```
+ **`getPlacesGeocoder`**

  Returns a ready to use IControl object that can be added directly to a map.

  ```
  const geocoder = getPlacesGeocoder();

  // Initialize map
  let map = await initializeMap();

  // Add the geocoder to the map.
  map.addControl(geocoder);
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
