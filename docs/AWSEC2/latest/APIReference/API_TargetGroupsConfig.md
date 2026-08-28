---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TargetGroupsConfig.html
---

# TargetGroupsConfig
<a name="API_TargetGroupsConfig"></a>

Describes the target groups to attach to a Spot Fleet. Spot Fleet registers the running Spot Instances with these target groups.

## Contents
<a name="API_TargetGroupsConfig_Contents"></a>

 ** TargetGroups.N **
One or more target groups.
Type: Array of [TargetGroup](API_TargetGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_TargetGroupsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TargetGroupsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TargetGroupsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TargetGroupsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
