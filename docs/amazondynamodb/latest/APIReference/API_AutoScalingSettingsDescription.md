---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingSettingsDescription.html
---

# AutoScalingSettingsDescription
<a name="API_AutoScalingSettingsDescription"></a>

Represents the auto scaling settings for a global table or global secondary index.

## Contents
<a name="API_AutoScalingSettingsDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AutoScalingDisabled **   <a name="DDB-Type-AutoScalingSettingsDescription-AutoScalingDisabled"></a>
Disabled auto scaling for this global table or global secondary index.
Type: Boolean
Required: No

 ** AutoScalingRoleArn **   <a name="DDB-Type-AutoScalingSettingsDescription-AutoScalingRoleArn"></a>
Role ARN used for configuring the auto scaling policy.
Type: String
Required: No

 ** MaximumUnits **   <a name="DDB-Type-AutoScalingSettingsDescription-MaximumUnits"></a>
The maximum capacity units that a global table or global secondary index should be scaled up to.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** MinimumUnits **   <a name="DDB-Type-AutoScalingSettingsDescription-MinimumUnits"></a>
The minimum capacity units that a global table or global secondary index should be scaled down to.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** ScalingPolicies **   <a name="DDB-Type-AutoScalingSettingsDescription-ScalingPolicies"></a>
Information about the scaling policies.
Type: Array of [AutoScalingPolicyDescription](API_AutoScalingPolicyDescription.md) objects
Required: No

## See Also
<a name="API_AutoScalingSettingsDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/AutoScalingSettingsDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/AutoScalingSettingsDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/AutoScalingSettingsDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
