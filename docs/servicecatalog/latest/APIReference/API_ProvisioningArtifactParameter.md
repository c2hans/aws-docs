---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisioningArtifactParameter.html
---

# ProvisioningArtifactParameter
<a name="API_ProvisioningArtifactParameter"></a>

Information about a parameter used to provision a product.

## Contents
<a name="API_ProvisioningArtifactParameter_Contents"></a>

 ** DefaultValue **   <a name="servicecatalog-Type-ProvisioningArtifactParameter-DefaultValue"></a>
The default value.
Type: String
Required: No

 ** Description **   <a name="servicecatalog-Type-ProvisioningArtifactParameter-Description"></a>
The description of the parameter.
Type: String
Required: No

 ** IsNoEcho **   <a name="servicecatalog-Type-ProvisioningArtifactParameter-IsNoEcho"></a>
If this value is true, the value for this parameter is obfuscated from view when the parameter is retrieved. This parameter is used to hide sensitive information.
Type: Boolean
Required: No

 ** ParameterConstraints **   <a name="servicecatalog-Type-ProvisioningArtifactParameter-ParameterConstraints"></a>
Constraints that the administrator has put on a parameter.
Type: [ParameterConstraints](API_ParameterConstraints.md) object
Required: No

 ** ParameterKey **   <a name="servicecatalog-Type-ProvisioningArtifactParameter-ParameterKey"></a>
The parameter key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** ParameterType **   <a name="servicecatalog-Type-ProvisioningArtifactParameter-ParameterType"></a>
The parameter type.
Type: String
Required: No

## See Also
<a name="API_ProvisioningArtifactParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactParameter)
