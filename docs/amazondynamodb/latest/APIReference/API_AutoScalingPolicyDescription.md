---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AutoScalingPolicyDescription.html
---

# AutoScalingPolicyDescription
<a name="API_AutoScalingPolicyDescription"></a>

Represents the properties of the scaling policy.

## Contents
<a name="API_AutoScalingPolicyDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PolicyName **   <a name="DDB-Type-AutoScalingPolicyDescription-PolicyName"></a>
The name of the scaling policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\p{Print}+`
Required: No

 ** TargetTrackingScalingPolicyConfiguration **   <a name="DDB-Type-AutoScalingPolicyDescription-TargetTrackingScalingPolicyConfiguration"></a>
Represents a target tracking scaling policy configuration.
Type: [AutoScalingTargetTrackingScalingPolicyConfigurationDescription](API_AutoScalingTargetTrackingScalingPolicyConfigurationDescription.md) object
Required: No

## See Also
<a name="API_AutoScalingPolicyDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/AutoScalingPolicyDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/AutoScalingPolicyDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/AutoScalingPolicyDescription)
