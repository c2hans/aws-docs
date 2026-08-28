---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateArchive.html
---

# UpdateArchive
<a name="API_UpdateArchive"></a>

Updates the specified archive.

## Request Syntax
<a name="API_UpdateArchive_RequestSyntax"></a>

```
{
   "ArchiveName": "{{string}}",
   "Description": "{{string}}",
   "EventPattern": "{{string}}",
   "KmsKeyIdentifier": "{{string}}",
   "RetentionDays": {{number}}
}
```

## Request Parameters
<a name="API_UpdateArchive_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchiveName](#API_UpdateArchive_RequestSyntax) **   <a name="eventbridge-UpdateArchive-request-ArchiveName"></a>
The name of the archive to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

 ** [Description](#API_UpdateArchive_RequestSyntax) **   <a name="eventbridge-UpdateArchive-request-Description"></a>
The description for the archive.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** [EventPattern](#API_UpdateArchive_RequestSyntax) **   <a name="eventbridge-UpdateArchive-request-EventPattern"></a>
The event pattern to use to filter events sent to the archive.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [KmsKeyIdentifier](#API_UpdateArchive_RequestSyntax) **   <a name="eventbridge-UpdateArchive-request-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt this archive. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.
If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt the archive.
For more information, see [Identify and view keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html) in the * AWS Key Management Service Developer Guide*.
If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well.
For more information, see [Encrypting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9_\-/:]*$`
Required: No

 ** [RetentionDays](#API_UpdateArchive_RequestSyntax) **   <a name="eventbridge-UpdateArchive-request-RetentionDays"></a>
The number of days to retain events in the archive.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_UpdateArchive_ResponseSyntax"></a>

```
{
   "ArchiveArn": "string",
   "CreationTime": number,
   "State": "string",
   "StateReason": "string"
}
```

## Response Elements
<a name="API_UpdateArchive_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArchiveArn](#API_UpdateArchive_ResponseSyntax) **   <a name="eventbridge-UpdateArchive-response-ArchiveArn"></a>
The ARN of the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`

 ** [CreationTime](#API_UpdateArchive_ResponseSyntax) **   <a name="eventbridge-UpdateArchive-response-CreationTime"></a>
The time at which the archive was updated.
Type: Timestamp

 ** [State](#API_UpdateArchive_ResponseSyntax) **   <a name="eventbridge-UpdateArchive-response-State"></a>
The state of the archive.
Type: String
Valid Values: `ENABLED | DISABLED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`

 ** [StateReason](#API_UpdateArchive_ResponseSyntax) **   <a name="eventbridge-UpdateArchive-response-StateReason"></a>
The reason that the archive is in the current state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

## Errors
<a name="API_UpdateArchive_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** InvalidEventPatternException **
The event pattern is not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The request failed because it attempted to create resource beyond the allowed service quota.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateArchive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/UpdateArchive)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/UpdateArchive)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/UpdateArchive)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/UpdateArchive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/UpdateArchive)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/UpdateArchive)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/UpdateArchive)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/UpdateArchive)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/UpdateArchive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/UpdateArchive)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
