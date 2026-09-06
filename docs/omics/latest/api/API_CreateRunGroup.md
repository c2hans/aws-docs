---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateRunGroup.html
---

# CreateRunGroup
<a name="API_CreateRunGroup"></a>

Creates a run group to limit the compute resources for the runs that are added to the group. Returns an ARN, ID, and tags for the run group.

## Request Syntax
<a name="API_CreateRunGroup_RequestSyntax"></a>

```
POST /runGroup HTTP/1.1
Content-type: application/json

{
   "maxCpus": {{number}},
   "maxDuration": {{number}},
   "maxGpus": {{number}},
   "maxRuns": {{number}},
   "name": "{{string}}",
   "requestId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRunGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRunGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxCpus](#API_CreateRunGroup_RequestSyntax) **   <a name="omics-CreateRunGroup-request-maxCpus"></a>
The maximum number of CPUs that can run concurrently across all active runs in the run group.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** [maxDuration](#API_CreateRunGroup_RequestSyntax) **   <a name="omics-CreateRunGroup-request-maxDuration"></a>
The maximum time for each run (in minutes). If a run exceeds the maximum run time, the run fails automatically.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** [maxGpus](#API_CreateRunGroup_RequestSyntax) **   <a name="omics-CreateRunGroup-request-maxGpus"></a>
The maximum number of GPUs that can run concurrently across all active runs in the run group.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** [maxRuns](#API_CreateRunGroup_RequestSyntax) **   <a name="omics-CreateRunGroup-request-maxRuns"></a>
The maximum number of runs that can be running at the same time.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** [name](#API_CreateRunGroup_RequestSyntax) **   <a name="omics-CreateRunGroup-request-name"></a>
A name for the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [requestId](#API_CreateRunGroup_RequestSyntax) **   <a name="omics-CreateRunGroup-request-requestId"></a>
To ensure that requests don't run multiple times, specify a unique ID for each request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [tags](#API_CreateRunGroup_RequestSyntax) **   <a name="omics-CreateRunGroup-request-tags"></a>
Tags for the group.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateRunGroup_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateRunGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateRunGroup_ResponseSyntax) **   <a name="omics-CreateRunGroup-response-arn"></a>
The group's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [id](#API_CreateRunGroup_ResponseSyntax) **   <a name="omics-CreateRunGroup-response-id"></a>
The group's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [tags](#API_CreateRunGroup_ResponseSyntax) **   <a name="omics-CreateRunGroup-response-tags"></a>
Tags for the run group.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateRunGroup_Errors"></a>

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
<a name="API_CreateRunGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateRunGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateRunGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateRunGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateRunGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateRunGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateRunGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateRunGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateRunGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateRunGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateRunGroup)
