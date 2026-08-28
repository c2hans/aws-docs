---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_CloudWatchDestination.html
---

# CloudWatchDestination
<a name="API_CloudWatchDestination"></a>

Contains information associated with an Amazon CloudWatch event destination to which email sending events are published.

Event destinations, such as Amazon CloudWatch, are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html).

## Contents
<a name="API_CloudWatchDestination_Contents"></a>

 ** DimensionConfigurations.member.N **
A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.
Type: Array of [CloudWatchDimensionConfiguration](API_CloudWatchDimensionConfiguration.md) objects
Required: Yes

## See Also
<a name="API_CloudWatchDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/CloudWatchDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/CloudWatchDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/CloudWatchDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
