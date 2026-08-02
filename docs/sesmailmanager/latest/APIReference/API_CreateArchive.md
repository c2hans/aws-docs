---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateArchive.html
---

# CreateArchive
<a name="API_CreateArchive"></a>

Creates a new email archive resource for storing and retaining emails.

## Request Syntax
<a name="API_CreateArchive_RequestSyntax"></a>

```
{
   "ArchiveName": "{{string}}",
   "ClientToken": "{{string}}",
   "KmsKeyArn": "{{string}}",
   "Retention": { ... },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateArchive_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchiveName](#API_CreateArchive_RequestSyntax) **   <a name="sesmailmanager-CreateArchive-request-ArchiveName"></a>
A unique name for the new archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]`
Required: Yes

 ** [ClientToken](#API_CreateArchive_RequestSyntax) **   <a name="sesmailmanager-CreateArchive-request-ClientToken"></a>
A unique token Amazon SES uses to recognize retries of this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [KmsKeyArn](#API_CreateArchive_RequestSyntax) **   <a name="sesmailmanager-CreateArchive-request-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key for encrypting emails in the archive.
Type: String
Pattern: `arn:aws(|-cn|-us-gov|-eusc):kms:[a-z0-9-]{1,20}:[0-9]{12}:(key|alias)/.+`
Required: No

 ** [Retention](#API_CreateArchive_RequestSyntax) **   <a name="sesmailmanager-CreateArchive-request-Retention"></a>
The period for retaining emails in the archive before automatic deletion.
Type: [ArchiveRetention](API_ArchiveRetention.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Tags](#API_CreateArchive_RequestSyntax) **   <a name="sesmailmanager-CreateArchive-request-Tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateArchive_ResponseSyntax"></a>

```
{
   "ArchiveId": "string"
}
```

## Response Elements
<a name="API_CreateArchive_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArchiveId](#API_CreateArchive_ResponseSyntax) **   <a name="sesmailmanager-CreateArchive-response-ArchiveId"></a>
The unique identifier for the newly created archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 66.

## Errors
<a name="API_CreateArchive_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Occurs when an operation exceeds a predefined service quota or limit.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateArchive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/CreateArchive)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/CreateArchive)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/CreateArchive)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/CreateArchive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/CreateArchive)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/CreateArchive)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/CreateArchive)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/CreateArchive)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/CreateArchive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/CreateArchive)
