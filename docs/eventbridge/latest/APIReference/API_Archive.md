---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Archive.html
---

# Archive
<a name="API_Archive"></a>

An `Archive` object that contains details about an archive.

## Contents
<a name="API_Archive_Contents"></a>

 ** ArchiveName **   <a name="eventbridge-Type-Archive-ArchiveName"></a>
The name of the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** CreationTime **   <a name="eventbridge-Type-Archive-CreationTime"></a>
The time stamp for the time that the archive was created.
Type: Timestamp
Required: No

 ** EventCount **   <a name="eventbridge-Type-Archive-EventCount"></a>
The number of events in the archive.
Type: Long
Required: No

 ** EventSourceArn **   <a name="eventbridge-Type-Archive-EventSourceArn"></a>
The ARN of the event bus associated with the archive. Only events from this event bus are sent to the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`
Required: No

 ** RetentionDays **   <a name="eventbridge-Type-Archive-RetentionDays"></a>
The number of days to retain events in the archive before they are deleted.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** SizeBytes **   <a name="eventbridge-Type-Archive-SizeBytes"></a>
The size of the archive, in bytes.
Type: Long
Required: No

 ** State **   <a name="eventbridge-Type-Archive-State"></a>
The current state of the archive.
Type: String
Valid Values: `ENABLED | DISABLED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`
Required: No

 ** StateReason **   <a name="eventbridge-Type-Archive-StateReason"></a>
A description for the reason that the archive is in the current state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

## See Also
<a name="API_Archive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/Archive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/Archive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/Archive)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
