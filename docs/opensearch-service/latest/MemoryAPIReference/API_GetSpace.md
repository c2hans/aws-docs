---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetSpace.html
---

# GetSpace
<a name="API_GetSpace"></a>

Returns a space's configuration and status.

## Request Syntax
<a name="API_GetSpace_RequestSyntax"></a>

```
{
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSpace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [spaceId](#API_GetSpace_RequestSyntax) **   <a name="opensearchmemory-GetSpace-request-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_GetSpace_ResponseSyntax"></a>

```
{
   "arn": "string",
   "createdAt": number,
   "encryptionConfiguration": {
      "kmsKeyArn": "string"
   },
   "eventExpiryDays": number,
   "extractionModelId": "string",
   "memoryExpiryDays": number,
   "memoryStrategies": [
      {
         "configuration": {
            "consolidationEnabled": boolean,
            "extractEveryNMessages": number,
            "extractEveryNTokens": number,
            "extractionPrompt": "string",
            "extractionSeedRecentN": number,
            "extractionSeedTopK": number,
            "idleTimeoutSeconds": number
         },
         "description": "string",
         "name": "string",
         "type": "string"
      }
   ],
   "name": "string",
   "spaceId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_GetSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-arn"></a>
The Amazon Resource Name (ARN) of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws:osm:[a-z0-9-]+:[0-9]{12}:space/sp-[a-f0-9]{12}`

 ** [createdAt](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-createdAt"></a>
When the space was created.
Type: Timestamp

 ** [encryptionConfiguration](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-encryptionConfiguration"></a>
The AWS KMS key the space was created with. Absent when the space uses an AWS owned key.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [eventExpiryDays](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-eventExpiryDays"></a>
How many days the space keeps each event. Absent when it was never set, in which case the default of 90 days applies.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 365.

 ** [extractionModelId](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-extractionModelId"></a>
The model that extracts and consolidates memories for the space. Absent when it was never set. The service default then applies, which is currently `anthropic.claude-haiku-5-5`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._:-]*`

 ** [memoryExpiryDays](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-memoryExpiryDays"></a>
How many days the space keeps each memory. 0 means memories never expire. Absent when it was never set, in which case memories never expire.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3650.

 ** [memoryStrategies](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-memoryStrategies"></a>
The space's memory strategies, including the names the service generated for strategies created without one. Empty for a space that has no memory strategies.
Type: Array of [MemoryStrategy](API_MemoryStrategy.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [name](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-name"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9 _-]*`

 ** [spaceId](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`

 ** [status](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-status"></a>
The status of the space.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | DELETED | FAILED`

 ** [statusReason](#API_GetSpace_ResponseSyntax) **   <a name="opensearchmemory-GetSpace-response-statusReason"></a>
Details about why the space is `FAILED`. Read it only when `status` is `FAILED`: it can still hold the reason for an earlier failure.
Type: String

## Errors
<a name="API_GetSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.
 ** message **
A message that describes which access the request is missing.
HTTP Status Code: 403

 ** InternalServerException **
The service couldn't process the request because of an internal error. Retry the request.
 ** message **
A message that describes the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist. Check the IDs in the request.
 ** message **
A message that describes which resource wasn't found.
 ** resourceId **
The ID of the resource that wasn't found.
 ** resourceType **
The type of the resource that wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The service throttled the request. Retry the request with exponential backoff.
 ** message **
A message that describes the throttling.
 ** retryAfterSeconds **
The number of seconds to wait before you retry the request.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. The `reason`, `message`, and `fieldList` members describe the problem. Fix the request, and then try again.
 ** fieldList **
The fields that failed validation, if any.
 ** message **
A message that describes why the request failed validation, such as the field, key, or limit involved.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/GetSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/GetSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/GetSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/GetSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/GetSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/GetSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/GetSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/GetSpace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/GetSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/GetSpace)
