---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisionedProductPlanSummary.html
---

# ProvisionedProductPlanSummary
<a name="API_ProvisionedProductPlanSummary"></a>

Summary information about a plan.

## Contents
<a name="API_ProvisionedProductPlanSummary_Contents"></a>

 ** PlanId **   <a name="servicecatalog-Type-ProvisionedProductPlanSummary-PlanId"></a>
The plan identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** PlanName **   <a name="servicecatalog-Type-ProvisionedProductPlanSummary-PlanName"></a>
The name of the plan.
Type: String
Required: No

 ** PlanType **   <a name="servicecatalog-Type-ProvisionedProductPlanSummary-PlanType"></a>
The plan type.
Type: String
Valid Values: `CLOUDFORMATION`
Required: No

 ** ProvisioningArtifactId **   <a name="servicecatalog-Type-ProvisionedProductPlanSummary-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisionProductId **   <a name="servicecatalog-Type-ProvisionedProductPlanSummary-ProvisionProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisionProductName **   <a name="servicecatalog-Type-ProvisionedProductPlanSummary-ProvisionProductName"></a>
The user-friendly name of the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`
Required: No

## See Also
<a name="API_ProvisionedProductPlanSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisionedProductPlanSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisionedProductPlanSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisionedProductPlanSummary)
