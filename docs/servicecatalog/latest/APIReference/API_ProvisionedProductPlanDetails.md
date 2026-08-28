---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisionedProductPlanDetails.html
---

# ProvisionedProductPlanDetails
<a name="API_ProvisionedProductPlanDetails"></a>

Information about a plan.

## Contents
<a name="API_ProvisionedProductPlanDetails_Contents"></a>

 ** CreatedTime **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-CreatedTime"></a>
The UTC time stamp of the creation time.
Type: Timestamp
Required: No

 ** NotificationArns **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-NotificationArns"></a>
Passed to AWS CloudFormation. The SNS topic ARNs to which to publish stack-related events.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** PathId **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-PathId"></a>
The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use [ListLaunchPaths](API_ListLaunchPaths.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** PlanId **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-PlanId"></a>
The plan identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** PlanName **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-PlanName"></a>
The name of the plan.
Type: String
Required: No

 ** PlanType **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-PlanType"></a>
The plan type.
Type: String
Valid Values: `CLOUDFORMATION`
Required: No

 ** ProductId **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisioningArtifactId **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisioningParameters **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-ProvisioningParameters"></a>
Parameters specified by the administrator that are required for provisioning the product.
Type: Array of [UpdateProvisioningParameter](API_UpdateProvisioningParameter.md) objects
Required: No

 ** ProvisionProductId **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-ProvisionProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisionProductName **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-ProvisionProductName"></a>
The user-friendly name of the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`
Required: No

 ** Status **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-Status"></a>
The status.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_SUCCESS | CREATE_FAILED | EXECUTE_IN_PROGRESS | EXECUTE_SUCCESS | EXECUTE_FAILED`
Required: No

 ** StatusMessage **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-StatusMessage"></a>
The status message.
Type: String
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** Tags **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-Tags"></a>
One or more tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** UpdatedTime **   <a name="servicecatalog-Type-ProvisionedProductPlanDetails-UpdatedTime"></a>
The UTC time stamp when the plan was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ProvisionedProductPlanDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisionedProductPlanDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisionedProductPlanDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisionedProductPlanDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
