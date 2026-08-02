---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListEphemerides.html
---

# ListEphemerides
<a name="API_ListEphemerides"></a>

List your existing ephemerides.

## Request Syntax
<a name="API_ListEphemerides_RequestSyntax"></a>

```
POST /ephemerides?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "endTime": {{number}},
   "ephemerisType": "{{string}}",
   "satelliteId": "{{string}}",
   "startTime": {{number}},
   "statusList": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListEphemerides_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListEphemerides_RequestSyntax) **   <a name="groundstation-ListEphemerides-request-uri-maxResults"></a>
Maximum number of ephemerides to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListEphemerides_RequestSyntax) **   <a name="groundstation-ListEphemerides-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Request Body
<a name="API_ListEphemerides_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [endTime](#API_ListEphemerides_RequestSyntax) **   <a name="groundstation-ListEphemerides-request-endTime"></a>
The end time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.
Type: Timestamp
Required: Yes

 ** [ephemerisType](#API_ListEphemerides_RequestSyntax) **   <a name="groundstation-ListEphemerides-request-ephemerisType"></a>
Filter ephemerides by type. If not specified, all ephemeris types will be returned.
Type: String
Valid Values: `TLE | OEM | AZ_EL | SERVICE_MANAGED`
Required: No

 ** [satelliteId](#API_ListEphemerides_RequestSyntax) **   <a name="groundstation-ListEphemerides-request-satelliteId"></a>
The AWS Ground Station satellite ID to list ephemeris for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [startTime](#API_ListEphemerides_RequestSyntax) **   <a name="groundstation-ListEphemerides-request-startTime"></a>
The start time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.
Type: Timestamp
Required: Yes

 ** [statusList](#API_ListEphemerides_RequestSyntax) **   <a name="groundstation-ListEphemerides-request-statusList"></a>
The list of ephemeris status to return.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Valid Values: `VALIDATING | INVALID | ERROR | ENABLED | DISABLED | EXPIRED`
Required: No

## Response Syntax
<a name="API_ListEphemerides_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ephemerides": [
      {
         "creationTime": number,
         "enabled": boolean,
         "ephemerisId": "string",
         "ephemerisType": "string",
         "name": "string",
         "priority": number,
         "sourceS3Object": {
            "bucket": "string",
            "key": "string",
            "version": "string"
         },
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEphemerides_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ephemerides](#API_ListEphemerides_ResponseSyntax) **   <a name="groundstation-ListEphemerides-response-ephemerides"></a>
List of ephemerides.
Type: Array of [EphemerisItem](API_EphemerisItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.

 ** [nextToken](#API_ListEphemerides_ResponseSyntax) **   <a name="groundstation-ListEphemerides-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

## Errors
<a name="API_ListEphemerides_Errors"></a>

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
<a name="API_ListEphemerides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/ListEphemerides)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/ListEphemerides)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ListEphemerides)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/ListEphemerides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ListEphemerides)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/ListEphemerides)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/ListEphemerides)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/ListEphemerides)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/ListEphemerides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ListEphemerides)
