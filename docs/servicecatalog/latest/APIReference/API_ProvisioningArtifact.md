---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisioningArtifact.html
---

# ProvisioningArtifact
<a name="API_ProvisioningArtifact"></a>

Information about a provisioning artifact. A provisioning artifact is also known as a product version.

## Contents
<a name="API_ProvisioningArtifact_Contents"></a>

 ** CreatedTime **   <a name="servicecatalog-Type-ProvisioningArtifact-CreatedTime"></a>
The UTC time stamp of the creation time.
Type: Timestamp
Required: No

 ** Description **   <a name="servicecatalog-Type-ProvisioningArtifact-Description"></a>
The description of the provisioning artifact.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** Guidance **   <a name="servicecatalog-Type-ProvisioningArtifact-Guidance"></a>
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.
Type: String
Valid Values: `DEFAULT | DEPRECATED`
Required: No

 ** Id **   <a name="servicecatalog-Type-ProvisioningArtifact-Id"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** Name **   <a name="servicecatalog-Type-ProvisioningArtifact-Name"></a>
The name of the provisioning artifact.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

## See Also
<a name="API_ProvisioningArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifact)
