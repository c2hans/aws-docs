---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetSatellite.html
---

# GetSatellite
<a name="API_GetSatellite"></a>

Returns a satellite.

## Request Syntax
<a name="API_GetSatellite_RequestSyntax"></a>

```
GET /satellite/{{satelliteId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSatellite_RequestParameters"></a>

The request uses the following URI parameters.

 ** [satelliteId](#API_GetSatellite_RequestSyntax) **   <a name="groundstation-GetSatellite-request-uri-satelliteId"></a>
UUID of a satellite.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_GetSatellite_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSatellite_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "currentEphemeris": {
      "ephemerisId": "string",
      "epoch": number,
      "name": "string",
      "source": "string"
   },
   "groundStations": [ "string" ],
   "noradSatelliteID": number,
   "satelliteArn": "string",
   "satelliteId": "string"
}
```

## Response Elements
<a name="API_GetSatellite_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [currentEphemeris](#API_GetSatellite_ResponseSyntax) **   <a name="groundstation-GetSatellite-response-currentEphemeris"></a>
The current ephemeris being used to compute the trajectory of the satellite.
Type: [EphemerisMetaData](API_EphemerisMetaData.md) object

 ** [groundStations](#API_GetSatellite_ResponseSyntax) **   <a name="groundstation-GetSatellite-response-groundStations"></a>
A list of ground stations to which the satellite is on-boarded.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`

 ** [noradSatelliteID](#API_GetSatellite_ResponseSyntax) **   <a name="groundstation-GetSatellite-response-noradSatelliteID"></a>
NORAD satellite ID number.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 339999.

 ** [satelliteArn](#API_GetSatellite_ResponseSyntax) **   <a name="groundstation-GetSatellite-response-satelliteArn"></a>
ARN of a satellite.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 132.
Pattern: `arn:aws:groundstation:([-a-z0-9]{1,50})?:[0-9]{12}:satellite/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [satelliteId](#API_GetSatellite_ResponseSyntax) **   <a name="groundstation-GetSatellite-response-satelliteId"></a>
UUID of a satellite.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_GetSatellite_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_GetSatellite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/GetSatellite)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/GetSatellite)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/GetSatellite)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/GetSatellite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/GetSatellite)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/GetSatellite)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/GetSatellite)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/GetSatellite)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/GetSatellite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/GetSatellite)
