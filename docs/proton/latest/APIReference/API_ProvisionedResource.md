---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ProvisionedResource.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ProvisionedResource
<a name="API_ProvisionedResource"></a>

Detail data for a provisioned resource.

## Contents
<a name="API_ProvisionedResource_Contents"></a>

 ** identifier **   <a name="proton-Type-ProvisionedResource-identifier"></a>
The provisioned resource identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** name **   <a name="proton-Type-ProvisionedResource-name"></a>
The provisioned resource name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** provisioningEngine **   <a name="proton-Type-ProvisionedResource-provisioningEngine"></a>
The resource provisioning engine. At this time, `CLOUDFORMATION` can be used for AWS-managed provisioning, and `TERRAFORM` can be used for self-managed provisioning.
For more information, see [Self-managed provisioning](https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self) in the * AWS Proton User Guide*.
Type: String
Valid Values: `CLOUDFORMATION | TERRAFORM`
Required: No

## See Also
<a name="API_ProvisionedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ProvisionedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ProvisionedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ProvisionedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
