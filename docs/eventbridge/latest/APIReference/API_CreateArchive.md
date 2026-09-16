---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateArchive.html
---

# CreateArchive
<a name="API_CreateArchive"></a>

Creates an archive of events with the specified settings. When you create an archive, incoming events might not immediately start being sent to the archive. Allow a short period of time for changes to take effect. If you do not specify a pattern to filter events sent to the archive, all events are sent to the archive except replayed events. Replayed events are not sent to an archive.

**Important**
If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well.
For more information, see [Encrypting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html) in the *Amazon EventBridge User Guide*.

## Request Syntax
<a name="API_CreateArchive_RequestSyntax"></a>

```
{
   "ArchiveName": "{{string}}",
   "Description": "{{string}}",
   "EventPattern": "{{string}}",
   "EventSourceArn": "{{string}}",
   "KmsKeyIdentifier": "{{string}}",
   "RetentionDays": {{number}}
}
```

## Request Parameters
<a name="API_CreateArchive_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchiveName](#API_CreateArchive_RequestSyntax) **   <a name="eventbridge-CreateArchive-request-ArchiveName"></a>
The name for the archive to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

 ** [Description](#API_CreateArchive_RequestSyntax) **   <a name="eventbridge-CreateArchive-request-Description"></a>
A description for the archive.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** [EventPattern](#API_CreateArchive_RequestSyntax) **   <a name="eventbridge-CreateArchive-request-EventPattern"></a>
An event pattern to use to filter events sent to the archive.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [EventSourceArn](#API_CreateArchive_RequestSyntax) **   <a name="eventbridge-CreateArchive-request-EventSourceArn"></a>
The ARN of the event bus that sends events to the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`
Required: Yes

 ** [KmsKeyIdentifier](#API_CreateArchive_RequestSyntax) **   <a name="eventbridge-CreateArchive-request-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt this archive. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.
If you do not specify a customer managed key identifier, EventBridge uses an AWS owned key to encrypt the archive.
For more information, see [Identify and view keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html) in the * AWS Key Management Service Developer Guide*.
If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well.
For more information, see [Encrypting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9_\-/:]*$`
Required: No

 ** [RetentionDays](#API_CreateArchive_RequestSyntax) **   <a name="eventbridge-CreateArchive-request-RetentionDays"></a>
The number of days to retain events for. Default value is 0. If set to 0, events are retained indefinitely
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_CreateArchive_ResponseSyntax"></a>

```
{
   "ArchiveArn": "string",
   "CreationTime": number,
   "State": "string",
   "StateReason": "string"
}
```

## Response Elements
<a name="API_CreateArchive_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArchiveArn](#API_CreateArchive_ResponseSyntax) **   <a name="eventbridge-CreateArchive-response-ArchiveArn"></a>
The ARN of the archive that was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`

 ** [CreationTime](#API_CreateArchive_ResponseSyntax) **   <a name="eventbridge-CreateArchive-response-CreationTime"></a>
The time at which the archive was created.
Type: Timestamp

 ** [State](#API_CreateArchive_ResponseSyntax) **   <a name="eventbridge-CreateArchive-response-State"></a>
The state of the archive that was created.
Type: String
Valid Values: `ENABLED | DISABLED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`

 ** [StateReason](#API_CreateArchive_ResponseSyntax) **   <a name="eventbridge-CreateArchive-response-StateReason"></a>
The reason that the archive is in the state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

## Errors
<a name="API_CreateArchive_Errors"></a>

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

 ** ResourceAlreadyExistsException **
The resource you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_CreateArchive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/CreateArchive)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/CreateArchive)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreateArchive)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/CreateArchive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreateArchive)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/CreateArchive)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/CreateArchive)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/CreateArchive)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/CreateArchive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreateArchive)
