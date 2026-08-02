---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-auth.html
---

# JavaScript Authentication helper
<a name="loc-sdk-auth"></a>

The Amazon Location JavaScript authentication helper makes it simpler to authenticate when making Amazon Location API calls from your JavaScript application. This authentication helper specifically help you when using [Amazon Cognito](authenticating-using-cognito.md) or [API keys](using-apikeys.md) as your authentication method. This is an open source library that is available on GitHub, here: [https://github.com/aws-geospatial/amazon-location-utilities-auth-helper-js](https://github.com/aws-geospatial/amazon-location-utilities-auth-helper-js).

**Note**
The Amazon Cognito support in the authentication helper does not support the federated identities feature of Amazon Cognito.

**Installation**

You can use the libraries with a local install, if you use a build system like webpack, or by including pre-built JavaScript bundles with `<script>` tags in your html.
+ Use the following command to install the library, using NPM:

  ```
  npm install @aws/amazon-location-utilities-auth-helper
  ```
+ Use the following command in your HTML file to load the script:

  ```
  <script src="https://unpkg.com/@aws/amazon-location-utilities-auth-helper@1.x/dist/amazonLocationAuthHelper.js"></script>
  ```

**Import**

To use a specific function in your JavaScript application, you must import that function. The following code is used to import the function `withIdentityPoolId` into your application.

```
import { withIdentityPoolId } from '@aws/amazon-location-utilities-auth-helper';
```

## Authentication functions
<a name="loc-sdk-auth-functions"></a>

The Amazon Location authentication helpers include the following functions that return an `AuthHelper` object:
+ `async withIdentityPoolId( identityPoolId: string): AuthHelper` – This function returns an AuthHelper object, initialized to work with Amazon Cognito
+ `async withAPIKey( API_KEY: string): AuthHelper` – This function returns an AuthHelper object, initialized to work with API Keys.

The `AuthHelper` object provides the following functions:
+ `AuthHelper.getMapAuthenticationOptions()` – This function of the AuthHelper object returns a JavaScript object with the `transformRequest` that can be used with the map options in MapLibre JS. Only provided when initialized with an identity pool.
+ `AuthHelper.getLocationClientConfig()` – This function of the AuthHelper object returns a JavaScript object with the `credentials` that can be used to initialize a LocationClient.
+ `AuthHelper.getCredentials()` – This function of the AuthHelper object returns the internal credentials from Amazon Cognito. Only provided when initialized with an identity pool.

**Example: Initializing MapLibre map object with Amazon Cognito, using an AuthHelper**

```
import { withIdentityPoolId } from '@aws/amazon-location-utilities-auth-helper';

const authHelper = await withIdentityPoolId("{{identity-pool-id}}"); // use Cognito pool id for credentials

const map = new maplibregl.Map({
    container: "{{map}}", // HTML element ID of map element
    center: [-123.1187, 49.2819], // initial map center point
    zoom: 16, // initial map zoom
    style: https://maps.geo.{{region}}.amazonaws.com/maps/v0/maps/{{mapName}}/style-descriptor', // Defines the appearance of the map
    ...authHelper.getMapAuthenticationOptions(), // Provides credential options required for requests to Amazon Location
});
```

**Example: Initializing MapLibre map object with an API key (`AuthHelper` is not needed in this case)**

```
const map = new maplibregl.Map({
    container: "{{map}}", // HTML element ID of map element
    center: [-123.1187, 49.2819], // initial map center point
    zoom: 16, // initial map zoom
    style: https://maps.geo.{{region}}.amazonaws.com/maps/v0/maps/${{{mapName}}}/style-descriptor?key={{api-key-id}}',
});
```

**Example: Initialize the Location client from the AWS SDK for JS, using Amazon Cognito and AuthHelper**

This example uses AWS SDK for JavaScript v3.

```
import { withIdentityPoolId } from '@aws/amazon-location-utilities-auth-helper';

const authHelper = await withIdentityPoolId("{{identity-pool-id}}"); // use Cognito pool id for credentials

//initialize the Location client:
const client = new LocationClient({
    region: "{{region}}",
    ...authHelper.getLocationClientConfig() // sets up the Location client to use the Cognito pool defined above
});

//call a search function with the location client:
const result = await client.send(new SearchPlaceIndexForPositionCommand({
    IndexName: "{{place-index}}", // Place index resource to use
    Position: [-123.1187, 49.2819], // position to search near
    MaxResults: 10 // number of results to return
});
```

**Example: Initialize the Location client from the AWS SDK for JS, using an API key and AuthHelper**

This example uses AWS SDK for JavaScript v3.

```
import { withAPIKey } from '@aws/amazon-location-utilities-auth-helper';

const authHelper = await withAPIKey("{{api-key-id}}"); // use API Key id for credentials

//initialize the Location client:
const client = new LocationClient({
    region: "{{region}}",
    ...authHelper.getLocationClientConfig() // sets up the Location client to use the API Key defined above
});

//call a search function with the location client:
const result = await client.send(new SearchPlaceIndexForPositionCommand({
    IndexName: "{{place-index}}", // Place index resource to use
    Position: [-123.1187, 49.2819], // position to search near
    MaxResults: 10 // number of results to return
});
```
