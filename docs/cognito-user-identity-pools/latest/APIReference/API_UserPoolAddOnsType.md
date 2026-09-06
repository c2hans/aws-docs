---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolAddOnsType.html
---

# UserPoolAddOnsType
<a name="API_UserPoolAddOnsType"></a>

Contains settings for activation of threat protection, including the operating mode and additional authentication types. To log user security information but take no action, set to `AUDIT`. To configure automatic security responses to potentially unwanted traffic to your user pool, set to `ENFORCED`.

For more information, see [Adding advanced security to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html). To activate this setting, your user pool must be on the [ Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html).

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_UserPoolAddOnsType_Contents"></a>

 ** AdvancedSecurityMode **   <a name="CognitoUserPools-Type-UserPoolAddOnsType-AdvancedSecurityMode"></a>
The operating mode of threat protection for standard authentication types in your user pool, including username-password and secure remote password (SRP) authentication.
Type: String
Valid Values: `OFF | AUDIT | ENFORCED`
Required: Yes

 ** AdvancedSecurityAdditionalFlows **   <a name="CognitoUserPools-Type-UserPoolAddOnsType-AdvancedSecurityAdditionalFlows"></a>
Threat protection configuration options for additional authentication types in your user pool, including custom authentication.
Type: [AdvancedSecurityAdditionalFlowsType](API_AdvancedSecurityAdditionalFlowsType.md) object
Required: No

## See Also
<a name="API_UserPoolAddOnsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserPoolAddOnsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserPoolAddOnsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserPoolAddOnsType)
