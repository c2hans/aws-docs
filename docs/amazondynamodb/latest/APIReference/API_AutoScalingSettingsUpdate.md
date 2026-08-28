---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingSettingsUpdate.html
---

# AutoScalingSettingsUpdate
<a name="API_AutoScalingSettingsUpdate"></a>

Represents the auto scaling settings to be modified for a global table or global secondary index.

## Contents
<a name="API_AutoScalingSettingsUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AutoScalingDisabled **   <a name="DDB-Type-AutoScalingSettingsUpdate-AutoScalingDisabled"></a>
Disabled auto scaling for this global table or global secondary index.
Type: Boolean
Required: No

 ** AutoScalingRoleArn **   <a name="DDB-Type-AutoScalingSettingsUpdate-AutoScalingRoleArn"></a>
Role ARN used for configuring auto scaling policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** MaximumUnits **   <a name="DDB-Type-AutoScalingSettingsUpdate-MaximumUnits"></a>
The maximum capacity units that a global table or global secondary index should be scaled up to.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** MinimumUnits **   <a name="DDB-Type-AutoScalingSettingsUpdate-MinimumUnits"></a>
The minimum capacity units that a global table or global secondary index should be scaled down to.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** ScalingPolicyUpdate **   <a name="DDB-Type-AutoScalingSettingsUpdate-ScalingPolicyUpdate"></a>
The scaling policy to apply for scaling target global table or global secondary index capacity units.
Type: [AutoScalingPolicyUpdate](API_AutoScalingPolicyUpdate.md) object
Required: No

## See Also
<a name="API_AutoScalingSettingsUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/AutoScalingSettingsUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/AutoScalingSettingsUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/AutoScalingSettingsUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
