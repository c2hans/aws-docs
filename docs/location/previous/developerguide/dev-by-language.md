---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/dev-by-language.html
---

# SDKs by language
<a name="dev-by-language"></a>

The following tables provide information about AWS SDKs and MapLibre versions for languages and frameworks, by application type: web, mobile, or backend application.

**SDK Versions**
We recommend that you use the most recent build of the AWS SDK, and any other SDKs, that you use in your projects, and to keep the SDKs up to date. The AWS SDK provides you with the latest features and functionality, and also security updates. To find the latest build of the AWS SDK for JavaScript, for example, see the [browser installation ](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html#In_the_Browser) topic in the *AWS SDK for JavaScript* documentation.

------
#### [ Web frontend ]

The following AWS SDKs and MapLibre versions are available for web frontend application development.

<table>
<thead>
  <tr><th>Language / Framework</th><th>AWS SDK</th><th>Rendering Framework</th></tr>
</thead>
<tbody>
  <tr><td colspan="3">**Fully supported**</td></tr>
  <tr><td>JavaScript</td><td>[https://aws.amazon.com/sdk-for-javascript/](https://aws.amazon.com/sdk-for-javascript/)</td><td>[https://github.com/maplibre/maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js)</td></tr>
  <tr><td>ReactJS</td><td>[https://aws.amazon.com/sdk-for-javascript/](https://aws.amazon.com/sdk-for-javascript/)</td><td>[https://github.com/maplibre/maplibre-react-native](https://github.com/maplibre/maplibre-react-native)</td></tr>
  <tr><td>TypeScript</td><td>[https://aws.amazon.com/sdk-for-javascript/](https://aws.amazon.com/sdk-for-javascript/)</td><td>[https://github.com/maplibre/maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js)</td></tr>
  <tr><td colspan="3">**Partially supported**</td></tr>
  <tr><td>Flutter</td><td>[https://docs.amplify.aws/start/q/integration/flutter/](https://docs.amplify.aws/start/q/integration/flutter/)<br />Flutter is not yet fully supported by AWS, but limited support is offered via Amplify.</td><td>[https://github.com/maplibre/flutter-maplibre-gl](https://github.com/maplibre/flutter-maplibre-gl)<br />The MapLibre Flutter library is considered experimental.</td></tr>
  <tr><td>Node.js</td><td>[https://aws.amazon.com/sdk-for-javascript/](https://aws.amazon.com/sdk-for-javascript/)</td><td> There is no MapLibre support for Node.js.</td></tr>
  <tr><td>PHP</td><td>[https://aws.amazon.com/sdk-for-php/](https://aws.amazon.com/sdk-for-php/)</td><td> There is no MapLibre support for PHP.</td></tr>
</tbody>
</table>

------
#### [ Mobile frontend ]

The following AWS SDKs and MapLibre versions are available for mobile frontend application development.

<table>
<thead>
  <tr><th>Language / Framework</th><th>AWS SDK</th><th>Rendering Framework</th></tr>
</thead>
<tbody>
  <tr><td colspan="3">**Fully supported**</td></tr>
  <tr><td>Java</td><td>[https://aws.amazon.com/sdk-for-java/](https://aws.amazon.com/sdk-for-java/)</td><td>[https://github.com/maplibre/maplibre-native](https://github.com/maplibre/maplibre-native)</td></tr>
  <tr><td>Kotlin</td><td>[https://aws.amazon.com/sdk-for-kotlin/](https://aws.amazon.com/sdk-for-kotlin/) <br />Amazon Location Service Mobile Authentication SDK for Android: [https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-android](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-android)<br />Amazon Location Service Mobile Tracking SDK for Android: [https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-android](https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-android)</td><td>[https://github.com/maplibre/maplibre-native](https://github.com/maplibre/maplibre-native)<br />Requires custom bindings, as MapLibre is Java-based.</td></tr>
  <tr><td>ObjectiveC</td><td>[https://github.com/aws-amplify/aws-sdk-ios](https://github.com/aws-amplify/aws-sdk-ios)</td><td>[https://github.com/maplibre/maplibre-native](https://github.com/maplibre/maplibre-native)</td></tr>
  <tr><td>ReactNative</td><td>[https://aws.amazon.com/sdk-for-javascript/](https://aws.amazon.com/sdk-for-javascript/)</td><td>[https://github.com/maplibre/maplibre-react-native](https://github.com/maplibre/maplibre-react-native)</td></tr>
  <tr><td>Swift</td><td>[https://aws.amazon.com/sdk-for-swift/](https://aws.amazon.com/sdk-for-swift/)<br />Amazon Location Service Mobile Authentication SDK for iOS: [https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios)<br />Amazon Location Service Mobile Tracking SDK for iOS: [https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios](https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios)</td><td>[https://github.com/maplibre/maplibre-native](https://github.com/maplibre/maplibre-native)</td></tr>
  <tr><td colspan="3">**Partially supported**</td></tr>
  <tr><td>Flutter</td><td>[https://docs.amplify.aws/start/q/integration/flutter/](https://docs.amplify.aws/start/q/integration/flutter/)<br />Flutter is not yet fully supported by AWS, but limited support is offered via Amplify.</td><td>[https://github.com/maplibre/flutter-maplibre-gl](https://github.com/maplibre/flutter-maplibre-gl)<br />The MapLibre Flutter library is considered experimental.</td></tr>
</tbody>
</table>

------
#### [ Backend application ]

The following AWS SDKs are available for backend application development. MapLibre is not listed here, because map rendering is not typically needed for backend applications.

| Language | AWS SDK |
| --- | --- |
| .NET | [https://aws.amazon.com/sdk-for-net/](https://aws.amazon.com/sdk-for-net/) |
| C\+\+ | [https://aws.amazon.com/sdk-for-cpp/](https://aws.amazon.com/sdk-for-cpp/) |
| Go | [https://aws.amazon.com/sdk-for-go/](https://aws.amazon.com/sdk-for-go/) |
| Java | [https://aws.amazon.com/sdk-for-java/](https://aws.amazon.com/sdk-for-java/) |
| JavaScript | [https://aws.amazon.com/sdk-for-javascript/](https://aws.amazon.com/sdk-for-javascript/) |
| Node.js | [https://aws.amazon.com/sdk-for-javascript/](https://aws.amazon.com/sdk-for-javascript/) |
| TypeScript | [https://aws.amazon.com/sdk-for-javascript/](https://aws.amazon.com/sdk-for-javascript/) |
| Kotlin | [https://aws.amazon.com/sdk-for-kotlin/](https://aws.amazon.com/sdk-for-kotlin/) |
| PHP | [https://aws.amazon.com/sdk-for-php/](https://aws.amazon.com/sdk-for-php/) |
| Python | [https://aws.amazon.com/sdk-for-python/](https://aws.amazon.com/sdk-for-python/) |
| Ruby | [https://aws.amazon.com/sdk-for-ruby/](https://aws.amazon.com/sdk-for-ruby/) |
| Rust | [https://aws.amazon.com/sdk-for-rust/](https://aws.amazon.com/sdk-for-rust/)<br />The AWS SDK for Rust is in developer preview. |

------
