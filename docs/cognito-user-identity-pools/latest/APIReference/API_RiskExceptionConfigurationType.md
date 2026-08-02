---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RiskExceptionConfigurationType.html
---

# RiskExceptionConfigurationType
<a name="API_RiskExceptionConfigurationType"></a>

Exceptions to the risk evaluation configuration, including always-allow and always-block IP address ranges.

This data type is a request parameter of [SetRiskConfiguration](API_SetRiskConfiguration.md) and a response parameter of [DescribeRiskConfiguration](API_DescribeRiskConfiguration.md).

## Contents
<a name="API_RiskExceptionConfigurationType_Contents"></a>

 ** BlockedIPRangeList **   <a name="CognitoUserPools-Type-RiskExceptionConfigurationType-BlockedIPRangeList"></a>
An always-block IP address list. Overrides the risk decision and always blocks authentication requests. This parameter is displayed and set in CIDR notation.
Type: Array of strings
Array Members: Maximum number of 200 items.
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** SkippedIPRangeList **   <a name="CognitoUserPools-Type-RiskExceptionConfigurationType-SkippedIPRangeList"></a>
An always-allow IP address list. Risk detection isn't performed on the IP addresses in this range list. This parameter is displayed and set in CIDR notation.
Type: Array of strings
Array Members: Maximum number of 200 items.
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_RiskExceptionConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/RiskExceptionConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/RiskExceptionConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/RiskExceptionConfigurationType)
