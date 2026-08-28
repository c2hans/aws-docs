---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_RecordDetail.html
---

# RecordDetail
<a name="API_RecordDetail"></a>

Information about a request operation.

## Contents
<a name="API_RecordDetail_Contents"></a>

 ** CreatedTime **   <a name="servicecatalog-Type-RecordDetail-CreatedTime"></a>
The UTC time stamp of the creation time.
Type: Timestamp
Required: No

 ** LaunchRoleArn **   <a name="servicecatalog-Type-RecordDetail-LaunchRoleArn"></a>
The ARN of the launch role associated with the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:[a-z0-9-\.]{1,63}:iam::[a-z0-9-\.]{0,63}:role\/.{0,1023}`
Required: No

 ** PathId **   <a name="servicecatalog-Type-RecordDetail-PathId"></a>
The path identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProductId **   <a name="servicecatalog-Type-RecordDetail-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisionedProductId **   <a name="servicecatalog-Type-RecordDetail-ProvisionedProductId"></a>
The identifier of the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisionedProductName **   <a name="servicecatalog-Type-RecordDetail-ProvisionedProductName"></a>
The user-friendly name of the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`
Required: No

 ** ProvisionedProductType **   <a name="servicecatalog-Type-RecordDetail-ProvisionedProductType"></a>
The type of provisioned product. The supported values are `CFN_STACK`, `CFN_STACKSET`, `TERRAFORM_OPEN_SOURCE`, `TERRAFORM_CLOUD`, and `EXTERNAL`.
Type: String
Required: No

 ** ProvisioningArtifactId **   <a name="servicecatalog-Type-RecordDetail-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** RecordErrors **   <a name="servicecatalog-Type-RecordDetail-RecordErrors"></a>
The errors that occurred.
Type: Array of [RecordError](API_RecordError.md) objects
Required: No

 ** RecordId **   <a name="servicecatalog-Type-RecordDetail-RecordId"></a>
The identifier of the record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** RecordTags **   <a name="servicecatalog-Type-RecordDetail-RecordTags"></a>
One or more tags.
Type: Array of [RecordTag](API_RecordTag.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** RecordType **   <a name="servicecatalog-Type-RecordDetail-RecordType"></a>
The record type.
+  `PROVISION_PRODUCT`
+  `UPDATE_PROVISIONED_PRODUCT`
+  `TERMINATE_PROVISIONED_PRODUCT`
Type: String
Required: No

 ** Status **   <a name="servicecatalog-Type-RecordDetail-Status"></a>
The status of the provisioned product.
+  `CREATED` - The request was created but the operation has not started.
+  `IN_PROGRESS` - The requested operation is in progress.
+  `IN_PROGRESS_IN_ERROR` - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.
+  `SUCCEEDED` - The requested operation has successfully completed.
+  `FAILED` - The requested operation has unsuccessfully completed. Investigate using the error messages returned.
Type: String
Valid Values: `CREATED | IN_PROGRESS | IN_PROGRESS_IN_ERROR | SUCCEEDED | FAILED`
Required: No

 ** UpdatedTime **   <a name="servicecatalog-Type-RecordDetail-UpdatedTime"></a>
The time when the record was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_RecordDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/RecordDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/RecordDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/RecordDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
