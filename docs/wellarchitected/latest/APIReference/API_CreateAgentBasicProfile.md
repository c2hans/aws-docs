---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentBasicProfile.html
---

# CreateAgentBasicProfile
<a name="API_CreateAgentBasicProfile"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Creates a Basic profile for the calling account. No configuration input is required because the account and region are inferred from the caller. The profile uses the reserved name `basic`. This operation is idempotent. Calling it twice returns the same ARN. Each account can have at most one Basic profile.

## Request Syntax
<a name="API_CreateAgentBasicProfile_RequestSyntax"></a>

```
POST /api/v1/agent-basic-profile HTTP/1.1
Content-type: application/json

{
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAgentBasicProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAgentBasicProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_CreateAgentBasicProfile_RequestSyntax) **   <a name="wellarchitected-CreateAgentBasicProfile-request-tags"></a>
Tags to apply to the Basic profile at creation time.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateAgentBasicProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "createdBy": "string",
   "lastModifiedAt": "string",
   "lastModifiedBy": "string"
}
```

## Response Elements
<a name="API_CreateAgentBasicProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateAgentBasicProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentBasicProfile-response-arn"></a>
The Amazon Resource Name (ARN) of the created Basic profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`

 ** [createdAt](#API_CreateAgentBasicProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentBasicProfile-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [createdBy](#API_CreateAgentBasicProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentBasicProfile-response-createdBy"></a>
The identifier of the user or system that created this resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [lastModifiedAt](#API_CreateAgentBasicProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentBasicProfile-response-lastModifiedAt"></a>
The timestamp when the resource was last modified.
Type: Timestamp

 ** [lastModifiedBy](#API_CreateAgentBasicProfile_ResponseSyntax) **   <a name="wellarchitected-CreateAgentBasicProfile-response-lastModifiedBy"></a>
The identifier of the user or system that last modified this resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_CreateAgentBasicProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateAgentBasicProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateAgentBasicProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateAgentBasicProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateAgentBasicProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateAgentBasicProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateAgentBasicProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateAgentBasicProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateAgentBasicProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateAgentBasicProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateAgentBasicProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateAgentBasicProfile)
