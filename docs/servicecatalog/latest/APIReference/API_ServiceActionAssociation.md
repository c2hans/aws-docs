---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ServiceActionAssociation.html
---

# ServiceActionAssociation
<a name="API_ServiceActionAssociation"></a>

A self-service action association consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.

## Contents
<a name="API_ServiceActionAssociation_Contents"></a>

 ** ProductId **   <a name="servicecatalog-Type-ServiceActionAssociation-ProductId"></a>
The product identifier. For example, `prod-abcdzk7xy33qa`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** ProvisioningArtifactId **   <a name="servicecatalog-Type-ServiceActionAssociation-ProvisioningArtifactId"></a>
The identifier of the provisioning artifact. For example, `pa-4abcdjnxjj6ne`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** ServiceActionId **   <a name="servicecatalog-Type-ServiceActionAssociation-ServiceActionId"></a>
The self-service action identifier. For example, `act-fs7abcd89wxyz`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## See Also
<a name="API_ServiceActionAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ServiceActionAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ServiceActionAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ServiceActionAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
