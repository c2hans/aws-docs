---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_EventStreamSummary.html
---

# EventStreamSummary
<a name="API_connect-customer-profiles_EventStreamSummary"></a>

An instance of EventStream in a list of EventStreams.

## Contents
<a name="API_connect-customer-profiles_EventStreamSummary_Contents"></a>

 ** DomainName **   <a name="connect-Type-connect-customer-profiles_EventStreamSummary-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** EventStreamArn **   <a name="connect-Type-connect-customer-profiles_EventStreamSummary-EventStreamArn"></a>
A unique identifier for the event stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** EventStreamName **   <a name="connect-Type-connect-customer-profiles_EventStreamSummary-EventStreamName"></a>
The name of the event stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** State **   <a name="connect-Type-connect-customer-profiles_EventStreamSummary-State"></a>
The operational state of destination stream for export.
Type: String
Valid Values: `RUNNING | STOPPED`
Required: Yes

 ** DestinationSummary **   <a name="connect-Type-connect-customer-profiles_EventStreamSummary-DestinationSummary"></a>
Summary information about the Kinesis data stream.
Type: [DestinationSummary](API_connect-customer-profiles_DestinationSummary.md) object
Required: No

 ** StoppedSince **   <a name="connect-Type-connect-customer-profiles_EventStreamSummary-StoppedSince"></a>
The timestamp when the `State` changed to `STOPPED`.
Type: Timestamp
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_EventStreamSummary-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-customer-profiles_EventStreamSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/EventStreamSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/EventStreamSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/EventStreamSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
