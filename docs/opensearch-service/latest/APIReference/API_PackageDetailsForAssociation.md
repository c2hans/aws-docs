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
