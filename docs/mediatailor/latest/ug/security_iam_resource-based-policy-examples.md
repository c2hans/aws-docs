---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/security_iam_resource-based-policy-examples.html
---

# Resource-based policy examples for AWS Elemental MediaTailor
<a name="security_iam_resource-based-policy-examples"></a>

To learn how to attach a resource-based policy to a channel, see **[Create a channel using the MediaTailor console](channel-assembly-creating-channels.md)**.

**Topics**
+ [Anonymous access](#security_iam_resource-based-policy-examples-anonymous-access)
+ [Cross-account access](#security_iam_resource-based-policy-examples-cross-account-access)

## Anonymous access
<a name="security_iam_resource-based-policy-examples-anonymous-access"></a>

Consider the following `Allow` policy. With this policy in effect, MediaTailor allows anonymous access to the `mediatailor:GetManifest` action on the channel resource in the policy. This occurs where {{region}} is the AWS Region, {{accountID}} is your AWS account ID, and {{channelName}} is the name of the channel resource.

## Cross-account access
<a name="security_iam_resource-based-policy-examples-cross-account-access"></a>

Consider the following `Allow` policy. With this policy in effect, MediaTailor allows the `mediatailor:GetManifest` action on the channel resource in the policy, across accounts. This occurs where {{region}} is the AWS Region, {{accountID}} is your AWS account ID, and {{channelName}} is the name of the channel resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
