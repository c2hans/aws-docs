---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataAccessorAuthenticationConfiguration.html
---

# DataAccessorAuthenticationConfiguration
<a name="API_DataAccessorAuthenticationConfiguration"></a>

A union type that contains the specific authentication configuration based on the authentication type selected.

## Contents
<a name="API_DataAccessorAuthenticationConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** idcTrustedTokenIssuerConfiguration **   <a name="qbusiness-Type-DataAccessorAuthenticationConfiguration-idcTrustedTokenIssuerConfiguration"></a>
Configuration for IAM Identity Center Trusted Token Issuer (TTI) authentication used when the authentication type is `AWS_IAM_IDC_TTI`.
Type: [DataAccessorIdcTrustedTokenIssuerConfiguration](API_DataAccessorIdcTrustedTokenIssuerConfiguration.md) object
Required: No

## See Also
<a name="API_DataAccessorAuthenticationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DataAccessorAuthenticationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DataAccessorAuthenticationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DataAccessorAuthenticationConfiguration)
