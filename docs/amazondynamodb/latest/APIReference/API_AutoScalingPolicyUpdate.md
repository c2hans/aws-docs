---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingPolicyUpdate.html
---

# AutoScalingPolicyUpdate
<a name="API_AutoScalingPolicyUpdate"></a>

Represents the auto scaling policy to be modified.

## Contents
<a name="API_AutoScalingPolicyUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TargetTrackingScalingPolicyConfiguration **   <a name="DDB-Type-AutoScalingPolicyUpdate-TargetTrackingScalingPolicyConfiguration"></a>
Represents a target tracking scaling policy configuration.
Type: [AutoScalingTargetTrackingScalingPolicyConfigurationUpdate](API_AutoScalingTargetTrackingScalingPolicyConfigurationUpdate.md) object
Required: Yes

 ** PolicyName **   <a name="DDB-Type-AutoScalingPolicyUpdate-PolicyName"></a>
The name of the scaling policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\p{Print}+`
Required: No

## See Also
<a name="API_AutoScalingPolicyUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/AutoScalingPolicyUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/AutoScalingPolicyUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/AutoScalingPolicyUpdate)
