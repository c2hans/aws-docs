---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-geojson.html
---

# GeoJSON conversion helpers
<a name="loc-sdk-geojson"></a>

The Amazon Location GeoJSON conversion helpers provide tools to convert Amazon Location Service data types to and from the industry-standard [GeoJSON](https://geojson.org/) format. GeoJSON is used, for example, with MapLibre to render geographic data on the map. This is an open source library that is available on GitHub, here: [https://github.com/aws-geospatial/amazon-location-utilities-datatypes-js](https://github.com/aws-geospatial/amazon-location-utilities-datatypes-js).

**Installation**

You can use the libraries with a local install, like webpack, or by including pre-built JavaScript bundles with `<script>` tags in your html.
+ Use the following command to install the library, using NPM.

  ```
  npm install @aws/amazon-location-utilities-datatypes
  ```
+ Use the following command in your HTML file to load the script:

  ```
  <script src="https://unpkg.com/@aws/amazon-location-utilities-datatypes@1.x/dist/amazonLocationDataConverter.js"></script>
  ```

**Import**

To use a specific function in your JavaScript application, you must import that function. The following code is used to import the function `placeToFeatureCollection` into your application.

```
import { placeToFeatureCollection } from '@aws/amazon-location-utilities-datatypes';
```

## GeoJSON conversion functions
<a name="loc-sdk-geojson-functions"></a>

The Amazon Location GeoJSON conversion helpers include the following functions:
+ `placeToFeatureCollection(place: GetPlaceResponse | searchPlaceIndexForPositionResponse | searchPlaceIndexForTextResponse, keepNull: boolean): Feature` – This function converts responses from the place search functions to a GeoJSON FeatureCollection with 1 or more Point features.
+ `devicePositionToFeatureCollection(devicePositions: GetDevicePositionResponse | BatchGetDevicePositionResponse | GetDevicePositionHistoryResponse | ListDevicePositionsResponse, keepNull: boolean)` – This function converts responses from the tracker device position functions to a GeoJSON FeatureCollection with 1 or more Point features.
+ `routeToFeatureCollection(legs: CalculateRouteResponse): FeatureCollection` – This function converts responses from the calculate route function to a GeoJSON FeatureCollection with a single MultiStringLine feature. Each leg of the route is represented by a LineString entry in the MultiStringLine.
+ `geofenceToFeatureCollection(geofences: GetGeofenceResponse | PutGeofenceRequest | BatchPutGeofenceRequest | ListGeofencesResponse): FeatureCollection` – This function converts geofence functions request or response to a GeoJSON FeatureCollection with Polygon features. It can convert geofences both in the response and the request, allowing you to show geofences on a map before uploading them with PutGeofence or BatchPutGeofence.

  This function will convert a circle geofence to a feature with an approximated polygon, but will also have "center" and "radius" properties to recreate the circle geofence, if necessary (see the next function).
+ `featureCollectionToGeofences(featureCollection: FeatureCollection): BatchPutGeofenceRequestEntry[]` – This function converts a GeoJSON FeatureCollection with Polygon features to an array of BatchPutGeofenceRequestEntry objects, so the result can be used to create a request to BatchPutGeofence.

  If a Feature in the FeatureCollection has "center" and "radius" properties, it will be converted into a circle geofence request entry, ignoring the geometry of the polygon.

**Example: Convert search results to a point layer in MapLibre**

This example uses AWS SDK for JavaScript v3.

```
import { placeToFeatureCollection } from '@aws/amazon-location-utility-datatypes';

...

let map; // map here is an initialized MapLibre instance

const client = new LocationClient(config);
const input = { {{your_input}} };
const command = new searchPlaceIndexForTextCommand(input);
const response = await client.send(command);

// calling utility function to convert the response to GeoJSON
const featureCollection = placeToFeatureCollection(response);
map.addSource("search-result", featureCollection);
map.addLayer({
    id: "search-result",
    type: "circle",
    source: "search-result",
    paint: {
        "circle-radius": 6,
        "circle-color": "#B42222",
    },
});
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
