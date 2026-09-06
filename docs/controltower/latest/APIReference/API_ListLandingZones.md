---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZones.html
---

# ListLandingZones
<a name="API_ListLandingZones"></a>

Returns the landing zone ARN for the landing zone deployed in your managed account. This API also creates an ARN for existing accounts that do not yet have a landing zone ARN.

Returns one landing zone ARN.

## Request Syntax
<a name="API_ListLandingZones_RequestSyntax"></a>

```
POST /list-landingzones HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListLandingZones_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLandingZones_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListLandingZones_RequestSyntax) **   <a name="controltower-ListLandingZones-request-maxResults"></a>
The maximum number of returned landing zone ARNs, which is one.
Type: Integer
Valid Range: Fixed value of 1.
Required: No

 ** [nextToken](#API_ListLandingZones_RequestSyntax) **   <a name="controltower-ListLandingZones-request-nextToken"></a>
The token to continue the list from a previous API call with the same parameters.
Type: String
Required: No

## Response Syntax
<a name="API_ListLandingZones_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "landingZones": [
      {
         "arn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLandingZones_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [landingZones](#API_ListLandingZones_ResponseSyntax) **   <a name="controltower-ListLandingZones-response-landingZones"></a>
The ARN of the landing zone.
Type: Array of [LandingZoneSummary](API_LandingZoneSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [nextToken](#API_ListLandingZones_ResponseSyntax) **   <a name="controltower-ListLandingZones-response-nextToken"></a>
Retrieves the next page of results. If the string is empty, the response is the end of the results.
Type: String

## Errors
<a name="API_ListLandingZones_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListLandingZones_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/ListLandingZones)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/ListLandingZones)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ListLandingZones)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/ListLandingZones)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ListLandingZones)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/ListLandingZones)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/ListLandingZones)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/ListLandingZones)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListLandingZones)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ListLandingZones)
