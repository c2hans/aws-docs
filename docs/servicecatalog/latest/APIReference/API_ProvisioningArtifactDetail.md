---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisioningArtifactDetail.html
---

# ProvisioningArtifactDetail
<a name="API_ProvisioningArtifactDetail"></a>

Information about a provisioning artifact (also known as a version) for a product.

## Contents
<a name="API_ProvisioningArtifactDetail_Contents"></a>

 ** Active **   <a name="servicecatalog-Type-ProvisioningArtifactDetail-Active"></a>
Indicates whether the product version is active.
Type: Boolean
Required: No

 ** CreatedTime **   <a name="servicecatalog-Type-ProvisioningArtifactDetail-CreatedTime"></a>
The UTC time stamp of the creation time.
Type: Timestamp
Required: No

 ** Description **   <a name="servicecatalog-Type-ProvisioningArtifactDetail-Description"></a>
The description of the provisioning artifact.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** Guidance **   <a name="servicecatalog-Type-ProvisioningArtifactDetail-Guidance"></a>
Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.
Type: String
Valid Values: `DEFAULT | DEPRECATED`
Required: No

 ** Id **   <a name="servicecatalog-Type-ProvisioningArtifactDetail-Id"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** Name **   <a name="servicecatalog-Type-ProvisioningArtifactDetail-Name"></a>
The name of the provisioning artifact.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** SourceRevision **   <a name="servicecatalog-Type-ProvisioningArtifactDetail-SourceRevision"></a>
Specifies the revision of the external artifact that was used to automatically sync the AWS Service Catalog product and create the provisioning artifact. AWS Service Catalog includes this response parameter as a high level field to the existing `ProvisioningArtifactDetail` type, which is returned as part of the response for `CreateProduct`, `UpdateProduct`, `DescribeProductAsAdmin`, `DescribeProvisioningArtifact`, `ListProvisioningArtifact`, and `UpdateProvisioningArticat` APIs.
This field only exists for Repo-Synced products.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Type **   <a name="servicecatalog-Type-ProvisioningArtifactDetail-Type"></a>
The type of provisioning artifact.
+  `CLOUD_FORMATION_TEMPLATE` - AWS CloudFormation template
+  `TERRAFORM_OPEN_SOURCE` - Terraform Open Source configuration file
+  `TERRAFORM_CLOUD` - Terraform Cloud configuration file
+  `EXTERNAL` - External configuration file
Type: String
Valid Values: `CLOUD_FORMATION_TEMPLATE | MARKETPLACE_AMI | MARKETPLACE_CAR | TERRAFORM_OPEN_SOURCE | EXTERNAL | TERRAFORM_CLOUD`
Required: No

## See Also
<a name="API_ProvisioningArtifactDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
