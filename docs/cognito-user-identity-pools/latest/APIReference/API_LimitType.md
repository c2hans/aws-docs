---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_LimitType.html
---

# LimitType
<a name="API_LimitType"></a>

The limit definition and current limit values for a provisioned limit.

A response element of [GetProvisionedLimit](API_GetProvisionedLimit.md) and [UpdateProvisionedLimit](API_UpdateProvisionedLimit.md).

## Contents
<a name="API_LimitType_Contents"></a>

 ** FreeLimitValue **   <a name="CognitoUserPools-Type-LimitType-FreeLimitValue"></a>
The default (free) limit value, in requests per second (RPS). This is the rate included at no additional cost.
Type: Integer
Required: Yes

 ** LimitDefinition **   <a name="CognitoUserPools-Type-LimitType-LimitDefinition"></a>
The definition that identifies this limit, including the class and attributes.
Type: [LimitDefinitionType](API_LimitDefinitionType.md) object
Required: Yes

 ** ProvisionedLimitValue **   <a name="CognitoUserPools-Type-LimitType-ProvisionedLimitValue"></a>
The provisioned limit value, in requests per second (RPS). This is the rate that Amazon Cognito currently enforces for your account.
Type: Integer
Required: Yes

## See Also
<a name="API_LimitType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/LimitType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/LimitType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/LimitType)
