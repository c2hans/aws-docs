---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListSatellites.html
---

# ListSatellites
<a name="API_ListSatellites"></a>

Returns a list of satellites.

## Request Syntax
<a name="API_ListSatellites_RequestSyntax"></a>

```
GET /satellite?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSatellites_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSatellites_RequestSyntax) **   <a name="groundstation-ListSatellites-request-uri-maxResults"></a>
Maximum number of satellites returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSatellites_RequestSyntax) **   <a name="groundstation-ListSatellites-request-uri-nextToken"></a>
Next token that can be supplied in the next call to get the next page of satellites.
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Request Body
<a name="API_ListSatellites_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSatellites_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "satellites": [
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
   ]
}
```

## Response Elements
<a name="API_ListSatellites_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSatellites_ResponseSyntax) **   <a name="groundstation-ListSatellites-response-nextToken"></a>
Next token that can be supplied in the next call to get the next page of satellites.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

 ** [satellites](#API_ListSatellites_ResponseSyntax) **   <a name="groundstation-ListSatellites-response-satellites"></a>
List of satellites.
Type: Array of [SatelliteListItem](API_SatelliteListItem.md) objects

## Errors
<a name="API_ListSatellites_Errors"></a>

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
<a name="API_ListSatellites_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/ListSatellites)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/ListSatellites)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ListSatellites)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/ListSatellites)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ListSatellites)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/ListSatellites)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/ListSatellites)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/ListSatellites)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/ListSatellites)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ListSatellites)
