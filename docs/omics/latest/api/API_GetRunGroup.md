---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetRunGroup.html
---

# GetRunGroup
<a name="API_GetRunGroup"></a>

Gets information about a run group and returns its metadata.

## Request Syntax
<a name="API_GetRunGroup_RequestSyntax"></a>

```
GET /runGroup/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRunGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetRunGroup_RequestSyntax) **   <a name="omics-GetRunGroup-request-uri-id"></a>
The group's ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetRunGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRunGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationTime": "string",
   "id": "string",
   "maxCpus": number,
   "maxDuration": number,
   "maxGpus": number,
   "maxRuns": number,
   "name": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetRunGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetRunGroup_ResponseSyntax) **   <a name="omics-GetRunGroup-response-arn"></a>
The group's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [creationTime](#API_GetRunGroup_ResponseSyntax) **   <a name="omics-GetRunGroup-response-creationTime"></a>
When the group was created.
Type: Timestamp

 ** [id](#API_GetRunGroup_ResponseSyntax) **   <a name="omics-GetRunGroup-response-id"></a>
The group's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [maxCpus](#API_GetRunGroup_ResponseSyntax) **   <a name="omics-GetRunGroup-response-maxCpus"></a>
The group's maximum number of CPUs to use.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [maxDuration](#API_GetRunGroup_ResponseSyntax) **   <a name="omics-GetRunGroup-response-maxDuration"></a>
The group's maximum run time in minutes.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [maxGpus](#API_GetRunGroup_ResponseSyntax) **   <a name="omics-GetRunGroup-response-maxGpus"></a>
The maximum GPUs that can be used by a run group.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [maxRuns](#API_GetRunGroup_ResponseSyntax) **   <a name="omics-GetRunGroup-response-maxRuns"></a>
The maximum number of concurrent runs for the group.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [name](#API_GetRunGroup_ResponseSyntax) **   <a name="omics-GetRunGroup-response-name"></a>
The group's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [tags](#API_GetRunGroup_ResponseSyntax) **   <a name="omics-GetRunGroup-response-tags"></a>
The group's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetRunGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetRunGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetRunGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetRunGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetRunGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetRunGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetRunGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetRunGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetRunGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetRunGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetRunGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetRunGroup)
