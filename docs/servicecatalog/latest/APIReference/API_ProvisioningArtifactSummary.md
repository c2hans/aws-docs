---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisioningArtifactSummary.html
---

# ProvisioningArtifactSummary
<a name="API_ProvisioningArtifactSummary"></a>

Summary information about a provisioning artifact (also known as a version) for a product.

## Contents
<a name="API_ProvisioningArtifactSummary_Contents"></a>

 ** CreatedTime **   <a name="servicecatalog-Type-ProvisioningArtifactSummary-CreatedTime"></a>
The UTC time stamp of the creation time.
Type: Timestamp
Required: No

 ** Description **   <a name="servicecatalog-Type-ProvisioningArtifactSummary-Description"></a>
The description of the provisioning artifact.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** Id **   <a name="servicecatalog-Type-ProvisioningArtifactSummary-Id"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** Name **   <a name="servicecatalog-Type-ProvisioningArtifactSummary-Name"></a>
The name of the provisioning artifact.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** ProvisioningArtifactMetadata **   <a name="servicecatalog-Type-ProvisioningArtifactSummary-ProvisioningArtifactMetadata"></a>
The metadata for the provisioning artifact. This is used with AWS Marketplace products.
Type: String to string map
Map Entries: Maximum number of 100 items.
Required: No

## See Also
<a name="API_ProvisioningArtifactSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactSummary)
