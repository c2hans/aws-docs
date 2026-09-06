---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetFindingDetails.html
---

# BatchGetFindingDetails
<a name="API_BatchGetFindingDetails"></a>

Gets vulnerability details for findings.

## Request Syntax
<a name="API_BatchGetFindingDetails_RequestSyntax"></a>

```
POST /findings/details/batch/get HTTP/1.1
Content-type: application/json

{
   "findingArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetFindingDetails_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetFindingDetails_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [findingArns](#API_BatchGetFindingDetails_RequestSyntax) **   <a name="inspector2-BatchGetFindingDetails-request-findingArns"></a>
A list of finding ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:finding/[a-f0-9]{32}`
Required: Yes

## Response Syntax
<a name="API_BatchGetFindingDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "findingArn": "string"
      }
   ],
   "findingDetails": [
      {
         "cisaData": {
            "action": "string",
            "dateAdded": number,
            "dateDue": number
         },
         "cwes": [ "string" ],
         "epssScore": number,
         "evidences": [
            {
               "evidenceDetail": "string",
               "evidenceRule": "string",
               "severity": "string"
            }
         ],
         "exploitObserved": {
            "firstSeen": number,
            "lastSeen": number
         },
         "findingArn": "string",
         "referenceUrls": [ "string" ],
         "riskScore": number,
         "tools": [ "string" ],
         "ttps": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetFindingDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetFindingDetails_ResponseSyntax) **   <a name="inspector2-BatchGetFindingDetails-response-errors"></a>
Error information for findings that details could not be returned for.
Type: Array of [FindingDetailsError](API_FindingDetailsError.md) objects

 ** [findingDetails](#API_BatchGetFindingDetails_ResponseSyntax) **   <a name="inspector2-BatchGetFindingDetails-response-findingDetails"></a>
A finding's vulnerability details.
Type: Array of [FindingDetail](API_FindingDetail.md) objects
Array Members: Minimum number of 0 items.

## Errors
<a name="API_BatchGetFindingDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetFindingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/BatchGetFindingDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/BatchGetFindingDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/BatchGetFindingDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/BatchGetFindingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/BatchGetFindingDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/BatchGetFindingDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/BatchGetFindingDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/BatchGetFindingDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/BatchGetFindingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/BatchGetFindingDetails)
