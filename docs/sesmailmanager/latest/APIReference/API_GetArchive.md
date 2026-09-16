---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchive.html
---

# GetArchive
<a name="API_GetArchive"></a>

Retrieves the full details and current state of a specified email archive.

## Request Syntax
<a name="API_GetArchive_RequestSyntax"></a>

```
{
   "ArchiveId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetArchive_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchiveId](#API_GetArchive_RequestSyntax) **   <a name="sesmailmanager-GetArchive-request-ArchiveId"></a>
The identifier of the archive to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 66.
Required: Yes

## Response Syntax
<a name="API_GetArchive_ResponseSyntax"></a>

```
{
   "ArchiveArn": "string",
   "ArchiveId": "string",
   "ArchiveName": "string",
   "ArchiveState": "string",
   "CreatedTimestamp": number,
   "KmsKeyArn": "string",
   "LastUpdatedTimestamp": number,
   "Retention": { ... }
}
```

## Response Elements
<a name="API_GetArchive_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArchiveArn](#API_GetArchive_ResponseSyntax) **   <a name="sesmailmanager-GetArchive-response-ArchiveArn"></a>
The Amazon Resource Name (ARN) of the archive.
Type: String

 ** [ArchiveId](#API_GetArchive_ResponseSyntax) **   <a name="sesmailmanager-GetArchive-response-ArchiveId"></a>
The unique identifier of the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 66.

 ** [ArchiveName](#API_GetArchive_ResponseSyntax) **   <a name="sesmailmanager-GetArchive-response-ArchiveName"></a>
The unique name assigned to the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]`

 ** [ArchiveState](#API_GetArchive_ResponseSyntax) **   <a name="sesmailmanager-GetArchive-response-ArchiveState"></a>
The current state of the archive:
+  `ACTIVE` – The archive is ready and available for use.
+  `PENDING_DELETION` – The archive has been marked for deletion and will be permanently deleted in 30 days. No further modifications can be made in this state.
Type: String
Valid Values: `ACTIVE | PENDING_DELETION`

 ** [CreatedTimestamp](#API_GetArchive_ResponseSyntax) **   <a name="sesmailmanager-GetArchive-response-CreatedTimestamp"></a>
The timestamp of when the archive was created.
Type: Timestamp

 ** [KmsKeyArn](#API_GetArchive_ResponseSyntax) **   <a name="sesmailmanager-GetArchive-response-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt the archive.
Type: String
Pattern: `arn:aws(|-cn|-us-gov|-eusc):kms:[a-z0-9-]{1,20}:[0-9]{12}:(key|alias)/.+`

 ** [LastUpdatedTimestamp](#API_GetArchive_ResponseSyntax) **   <a name="sesmailmanager-GetArchive-response-LastUpdatedTimestamp"></a>
The timestamp of when the archive was modified.
Type: Timestamp

 ** [Retention](#API_GetArchive_ResponseSyntax) **   <a name="sesmailmanager-GetArchive-response-Retention"></a>
The retention period for emails in this archive.
Type: [ArchiveRetention](API_ArchiveRetention.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_GetArchive_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetArchive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetArchive)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetArchive)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetArchive)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetArchive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetArchive)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetArchive)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetArchive)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetArchive)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetArchive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetArchive)
