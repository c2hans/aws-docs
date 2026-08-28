---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_FailedServiceActionAssociation.html
---

# FailedServiceActionAssociation
<a name="API_FailedServiceActionAssociation"></a>

An object containing information about the error, along with identifying information about the self-service action and its associations.

## Contents
<a name="API_FailedServiceActionAssociation_Contents"></a>

 ** ErrorCode **   <a name="servicecatalog-Type-FailedServiceActionAssociation-ErrorCode"></a>
The error code. Valid values are listed below.
Type: String
Valid Values: `DUPLICATE_RESOURCE | INTERNAL_FAILURE | LIMIT_EXCEEDED | RESOURCE_NOT_FOUND | THROTTLING | INVALID_PARAMETER`
Required: No

 ** ErrorMessage **   <a name="servicecatalog-Type-FailedServiceActionAssociation-ErrorMessage"></a>
A text description of the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ProductId **   <a name="servicecatalog-Type-FailedServiceActionAssociation-ProductId"></a>
The product identifier. For example, `prod-abcdzk7xy33qa`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ProvisioningArtifactId **   <a name="servicecatalog-Type-FailedServiceActionAssociation-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact. For example, `pa-4abcdjnxjj6ne`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** ServiceActionId **   <a name="servicecatalog-Type-FailedServiceActionAssociation-ServiceActionId"></a>
The self-service action identifier. For example, `act-fs7abcd89wxyz`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

## See Also
<a name="API_FailedServiceActionAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/FailedServiceActionAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/FailedServiceActionAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/FailedServiceActionAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
