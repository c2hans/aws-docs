---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PackageDetailsForAssociation.html
---

# PackageDetailsForAssociation
<a name="API_PackageDetailsForAssociation"></a>

 Details of a package that is associated with a domain.

## Contents
<a name="API_PackageDetailsForAssociation_Contents"></a>

 ** PackageID **   <a name="opensearchservice-Type-PackageDetailsForAssociation-PackageID"></a>
Internal ID of the package that you want to associate with a domain.
Type: String
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: Yes

 ** AssociationConfiguration **   <a name="opensearchservice-Type-PackageDetailsForAssociation-AssociationConfiguration"></a>
The configuration parameters for associating the package with a domain.
Type: [PackageAssociationConfiguration](API_PackageAssociationConfiguration.md) object
Required: No

 ** PrerequisitePackageIDList **   <a name="opensearchservice-Type-PackageDetailsForAssociation-PrerequisitePackageIDList"></a>
List of package IDs that must be linked to the domain before or simultaneously with the package association.
Type: Array of strings
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: No

## See Also
<a name="API_PackageDetailsForAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/PackageDetailsForAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/PackageDetailsForAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/PackageDetailsForAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
