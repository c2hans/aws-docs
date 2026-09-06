---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeArchive.html
---

# DescribeArchive
<a name="API_DescribeArchive"></a>

Retrieves details about an archive.

## Request Syntax
<a name="API_DescribeArchive_RequestSyntax"></a>

```
{
   "ArchiveName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeArchive_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArchiveName](#API_DescribeArchive_RequestSyntax) **   <a name="eventbridge-DescribeArchive-request-ArchiveName"></a>
The name of the archive to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DescribeArchive_ResponseSyntax"></a>

```
{
   "ArchiveArn": "string",
   "ArchiveName": "string",
   "CreationTime": number,
   "Description": "string",
   "EventCount": number,
   "EventPattern": "string",
   "EventSourceArn": "string",
   "KmsKeyIdentifier": "string",
   "RetentionDays": number,
   "SizeBytes": number,
   "State": "string",
   "StateReason": "string"
}
```

## Response Elements
<a name="API_DescribeArchive_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArchiveArn](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-ArchiveArn"></a>
The ARN of the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`

 ** [ArchiveName](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-ArchiveName"></a>
The name of the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[\.\-_A-Za-z0-9]+`

 ** [CreationTime](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-CreationTime"></a>
The time at which the archive was created.
Type: Timestamp

 ** [Description](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-Description"></a>
The description of the archive.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

 ** [EventCount](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-EventCount"></a>
The number of events in the archive.
Type: Long

 ** [EventPattern](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-EventPattern"></a>
The event pattern used to filter events sent to the archive.
Type: String
Length Constraints: Maximum length of 4096.

 ** [EventSourceArn](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-EventSourceArn"></a>
The ARN of the event source associated with the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`

 ** [KmsKeyIdentifier](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-KmsKeyIdentifier"></a>
The identifier of the AWS KMS customer managed key for EventBridge to use to encrypt this archive, if one has been specified.
For more information, see [Encrypting archives](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9_\-/:]*$`

 ** [RetentionDays](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-RetentionDays"></a>
The number of days to retain events for in the archive.
Type: Integer
Valid Range: Minimum value of 0.

 ** [SizeBytes](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-SizeBytes"></a>
The size of the archive in bytes.
Type: Long

 ** [State](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-State"></a>
The state of the archive.
Type: String
Valid Values: `ENABLED | DISABLED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`

 ** [StateReason](#API_DescribeArchive_ResponseSyntax) **   <a name="eventbridge-DescribeArchive-response-StateReason"></a>
The reason that the archive is in the state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

## Errors
<a name="API_DescribeArchive_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceAlreadyExistsException **
The resource you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeArchive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DescribeArchive)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DescribeArchive)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DescribeArchive)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DescribeArchive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeArchive)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DescribeArchive)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DescribeArchive)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DescribeArchive)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DescribeArchive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DescribeArchive)
