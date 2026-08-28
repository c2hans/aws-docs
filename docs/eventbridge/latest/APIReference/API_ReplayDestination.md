---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ReplayDestination.html
---

# ReplayDestination
<a name="API_ReplayDestination"></a>

A `ReplayDestination` object that contains details about a replay.

## Contents
<a name="API_ReplayDestination_Contents"></a>

 ** Arn **   <a name="eventbridge-Type-ReplayDestination-Arn"></a>
The ARN of the event bus to replay event to. You can replay events only to the event bus specified to create the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: Yes

 ** FilterArns **   <a name="eventbridge-Type-ReplayDestination-FilterArns"></a>
A list of ARNs for rules to replay events to.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

## See Also
<a name="API_ReplayDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ReplayDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ReplayDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ReplayDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
