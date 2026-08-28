---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_EventSubscription.html
---

# EventSubscription
<a name="API_EventSubscription"></a>

Indicates an event you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports notifications only for **Drift detected** and **Scheduled assessment failure** events.

## Contents
<a name="API_EventSubscription_Contents"></a>

 ** eventType **   <a name="resiliencehub-Type-EventSubscription-eventType"></a>
The type of event you would like to subscribe and get notification for. Currently, AWS Resilience Hub supports notifications only for **Drift detected** (`DriftDetected`) and **Scheduled assessment failure** (`ScheduledAssessmentFailure`) events.
Type: String
Valid Values: `ScheduledAssessmentFailure | DriftDetected`
Required: Yes

 ** name **   <a name="resiliencehub-Type-EventSubscription-name"></a>
Unique name to identify an event subscription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** snsTopicArn **   <a name="resiliencehub-Type-EventSubscription-snsTopicArn"></a>
Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic. The format for this ARN is: `arn:partition:sns:region:account:topic-name`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

## See Also
<a name="API_EventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/EventSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/EventSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/EventSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
