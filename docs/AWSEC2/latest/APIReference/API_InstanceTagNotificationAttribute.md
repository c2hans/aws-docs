---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceTagNotificationAttribute.html
---

# InstanceTagNotificationAttribute
<a name="API_InstanceTagNotificationAttribute"></a>

Describes the registered tag keys for the current Region.

## Contents
<a name="API_InstanceTagNotificationAttribute_Contents"></a>

 ** includeAllTagsOfInstance **
Indicates wheter all tag keys in the current Region are registered to appear in scheduled event notifications. `true` indicates that all tag keys in the current Region are registered.
Type: Boolean
Required: No

 ** InstanceTagKeySet.N **
The registered tag keys.
Type: Array of strings
Required: No

## See Also
<a name="API_InstanceTagNotificationAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceTagNotificationAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceTagNotificationAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceTagNotificationAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
