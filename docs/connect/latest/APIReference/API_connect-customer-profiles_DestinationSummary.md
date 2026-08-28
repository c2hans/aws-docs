---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_DestinationSummary.html
---

# DestinationSummary
<a name="API_connect-customer-profiles_DestinationSummary"></a>

Summary information about the Kinesis data stream

## Contents
<a name="API_connect-customer-profiles_DestinationSummary_Contents"></a>

 ** Status **   <a name="connect-Type-connect-customer-profiles_DestinationSummary-Status"></a>
The status of enabling the Kinesis stream as a destination for export.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: Yes

 ** Uri **   <a name="connect-Type-connect-customer-profiles_DestinationSummary-Uri"></a>
The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** UnhealthySince **   <a name="connect-Type-connect-customer-profiles_DestinationSummary-UnhealthySince"></a>
The timestamp when the status last changed to `UNHEALHY`.
Type: Timestamp
Required: No

## See Also
<a name="API_connect-customer-profiles_DestinationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DestinationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DestinationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DestinationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
