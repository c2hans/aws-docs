---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStations.html
---

# ListGroundStations
<a name="API_ListGroundStations"></a>

Returns a list of ground stations.

## Request Syntax
<a name="API_ListGroundStations_RequestSyntax"></a>

```
GET /groundstation?maxResults={{maxResults}}&nextToken={{nextToken}}&satelliteId={{satelliteId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGroundStations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListGroundStations_RequestSyntax) **   <a name="groundstation-ListGroundStations-request-uri-maxResults"></a>
Maximum number of ground stations returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListGroundStations_RequestSyntax) **   <a name="groundstation-ListGroundStations-request-uri-nextToken"></a>
Next token that can be supplied in the next call to get the next page of ground stations.
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

 ** [satelliteId](#API_ListGroundStations_RequestSyntax) **   <a name="groundstation-ListGroundStations-request-uri-satelliteId"></a>
Satellite ID to retrieve on-boarded ground stations.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Request Body
<a name="API_ListGroundStations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGroundStations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "groundStationList": [
      {
         "groundStationId": "string",
         "groundStationName": "string",
         "region": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListGroundStations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [groundStationList](#API_ListGroundStations_ResponseSyntax) **   <a name="groundstation-ListGroundStations-response-groundStationList"></a>
List of ground stations.
Type: Array of [GroundStationData](API_GroundStationData.md) objects

 ** [nextToken](#API_ListGroundStations_ResponseSyntax) **   <a name="groundstation-ListGroundStations-response-nextToken"></a>
Next token that can be supplied in the next call to get the next page of ground stations.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Errors
<a name="API_ListGroundStations_Errors"></a>

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
<a name="API_ListGroundStations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/ListGroundStations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/ListGroundStations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ListGroundStations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/ListGroundStations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ListGroundStations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/ListGroundStations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/ListGroundStations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/ListGroundStations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/ListGroundStations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ListGroundStations)
