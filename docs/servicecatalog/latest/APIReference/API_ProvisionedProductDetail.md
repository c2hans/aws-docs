---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisionedProductDetail.html
---

# ProvisionedProductDetail
<a name="API_ProvisionedProductDetail"></a>

Information about a provisioned product.

## Contents
<a name="API_ProvisionedProductDetail_Contents"></a>

 ** Arn **   <a name="servicecatalog-Type-ProvisionedProductDetail-Arn"></a>
The ARN of the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}|arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** CreatedTime **   <a name="servicecatalog-Type-ProvisionedProductDetail-CreatedTime"></a>
The UTC time stamp of the creation time.
Type: Timestamp
Required: No

 ** Id **   <a name="servicecatalog-Type-ProvisionedProductDetail-Id"></a>
The identifier of the provisioned product.
Type: String
Required: No

 ** IdempotencyToken **   <a name="servicecatalog-Type-ProvisionedProductDetail-IdempotencyToken"></a>
A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** LastProvisioningRecordId **   <a name="servicecatalog-Type-ProvisionedProductDetail-LastProvisioningRecordId"></a>
The record identifier of the last request performed on this provisioned product of the following types:
+  ProvisionProduct
+  UpdateProvisionedProduct
+  ExecuteProvisionedProductPlan
+  TerminateProvisionedProduct
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** LastRecordId **   <a name="servicecatalog-Type-ProvisionedProductDetail-LastRecordId"></a>
The record identifier of the last request performed on this provisioned product.
Type: String
Required: No

 ** LastSuccessfulProvisioningRecordId **   <a name="servicecatalog-Type-ProvisionedProductDetail-LastSuccessfulProvisioningRecordId"></a>
The record identifier of the last successful request performed on this provisioned product of the following types:
+  ProvisionProduct
+  UpdateProvisionedProduct
+  ExecuteProvisionedProductPlan
+  TerminateProvisionedProduct
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** LaunchRoleArn **   <a name="servicecatalog-Type-ProvisionedProductDetail-LaunchRoleArn"></a>
The ARN of the launch role associated with the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:[a-z0-9-\.]{1,63}:iam::[a-z0-9-\.]{0,63}:role\/.{0,1023}`
Required: No

 ** Name **   <a name="servicecatalog-Type-ProvisionedProductDetail-Name"></a>
The user-friendly name of the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}|arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** ProductId **   <a name="servicecatalog-Type-ProvisionedProductDetail-ProductId"></a>
The product identifier. For example, `prod-abcdzk7xy33qa`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisioningArtifactId **   <a name="servicecatalog-Type-ProvisionedProductDetail-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact. For example, `pa-4abcdjnxjj6ne`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** Status **   <a name="servicecatalog-Type-ProvisionedProductDetail-Status"></a>
The current status of the provisioned product.
+  `AVAILABLE` - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
+  `UNDER_CHANGE` - Transitive state. Operations performed might not have valid results. Wait for an `AVAILABLE` status before performing operations.
+  `TAINTED` - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
+  `ERROR` - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, AWS CloudFormation received a parameter value that was not valid and could not launch the stack.
+  `PLAN_IN_PROGRESS` - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an `AVAILABLE` status before performing operations.
Type: String
Valid Values: `AVAILABLE | UNDER_CHANGE | TAINTED | ERROR | PLAN_IN_PROGRESS`
Required: No

 ** StatusMessage **   <a name="servicecatalog-Type-ProvisionedProductDetail-StatusMessage"></a>
The current status message of the provisioned product.
Type: String
Required: No

 ** Type **   <a name="servicecatalog-Type-ProvisionedProductDetail-Type"></a>
The type of provisioned product. The supported values are `CFN_STACK`, `CFN_STACKSET`, `TERRAFORM_OPEN_SOURCE`, `TERRAFORM_CLOUD`, and `EXTERNAL`.
Type: String
Required: No

## See Also
<a name="API_ProvisionedProductDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisionedProductDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisionedProductDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisionedProductDetail)
