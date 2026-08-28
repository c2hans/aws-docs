---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisioningArtifactProperties.html
---

# ProvisioningArtifactProperties
<a name="API_ProvisioningArtifactProperties"></a>

Information about a provisioning artifact (also known as a version) for a product.

## Contents
<a name="API_ProvisioningArtifactProperties_Contents"></a>

 ** Description **   <a name="servicecatalog-Type-ProvisioningArtifactProperties-Description"></a>
The description of the provisioning artifact, including how it differs from the previous provisioning artifact.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** DisableTemplateValidation **   <a name="servicecatalog-Type-ProvisioningArtifactProperties-DisableTemplateValidation"></a>
If set to true, AWS Service Catalog stops validating the specified provisioning artifact even if it is invalid.
 AWS Service Catalog does not support template validation for the `TERRAFORM_OS` product type.
Type: Boolean
Required: No

 ** Info **   <a name="servicecatalog-Type-ProvisioningArtifactProperties-Info"></a>
Specify the template source with one of the following options, but not both. Keys accepted: [ `LoadTemplateFromURL`, `ImportFromPhysicalId` ]
The URL of the AWS CloudFormation template in Amazon S3 or GitHub in JSON format. Specify the URL in JSON format as follows:
 `"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/..."`
 `ImportFromPhysicalId`: The physical id of the resource that contains the template. Currently only supports AWS CloudFormation stack arn. Specify the physical id in JSON format as follows: `ImportFromPhysicalId: “arn:aws:cloudformation:[us-east-1]:[accountId]:stack/[StackName]/[resourceId]`
Type: String to string map
Map Entries: Maximum number of 100 items.
Required: No

 ** Name **   <a name="servicecatalog-Type-ProvisioningArtifactProperties-Name"></a>
The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.
Type: String
Length Constraints: Maximum length of 8192.
Required: No

 ** Type **   <a name="servicecatalog-Type-ProvisioningArtifactProperties-Type"></a>
The type of provisioning artifact.
+  `CLOUD_FORMATION_TEMPLATE` - AWS CloudFormation template
+  `TERRAFORM_OPEN_SOURCE` - Terraform Open Source configuration file
+  `TERRAFORM_CLOUD` - Terraform Cloud configuration file
+  `EXTERNAL` - External configuration file
Type: String
Valid Values: `CLOUD_FORMATION_TEMPLATE | MARKETPLACE_AMI | MARKETPLACE_CAR | TERRAFORM_OPEN_SOURCE | EXTERNAL | TERRAFORM_CLOUD`
Required: No

## See Also
<a name="API_ProvisioningArtifactProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
