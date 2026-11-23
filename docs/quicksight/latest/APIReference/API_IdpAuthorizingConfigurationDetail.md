---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IdpAuthorizingConfigurationDetail.html
---

# IdpAuthorizingConfigurationDetail

The details of the identity provider configuration.

## Contents
<a name="API_IdpAuthorizingConfigurationDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ExternalIdpConfidentialAuthCode **   <a name="QS-Type-IdpAuthorizingConfigurationDetail-ExternalIdpConfidentialAuthCode"></a>
The configuration for an external IdP with a confidential client.
Type: [ExternalIdpConfidentialAuthCodeAuthorizingConfig](API_ExternalIdpConfidentialAuthCodeAuthorizingConfig.md) object
Required: No

 ** ExternalIdpPublicAuthCode **   <a name="QS-Type-IdpAuthorizingConfigurationDetail-ExternalIdpPublicAuthCode"></a>
The configuration for an external IdP with a public client.
Type: [ExternalIdpPublicAuthCodeAuthorizingConfig](API_ExternalIdpPublicAuthCodeAuthorizingConfig.md) object
Required: No

## See Also
<a name="API_IdpAuthorizingConfigurationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/IdpAuthorizingConfigurationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/IdpAuthorizingConfigurationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/IdpAuthorizingConfigurationDetail)
