---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DomainPackageDetails.html
---

# DomainPackageDetails
<a name="API_DomainPackageDetails"></a>

Information about a package that is associated with a domain. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html).

## Contents
<a name="API_DomainPackageDetails_Contents"></a>

 ** AssociationConfiguration **   <a name="opensearchservice-Type-DomainPackageDetails-AssociationConfiguration"></a>
The configuration for associating a package with an Amazon OpenSearch Service domain.
Type: [PackageAssociationConfiguration](API_PackageAssociationConfiguration.md) object
Required: No

 ** DomainName **   <a name="opensearchservice-Type-DomainPackageDetails-DomainName"></a>
Name of the domain that the package is associated with.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** DomainPackageStatus **   <a name="opensearchservice-Type-DomainPackageDetails-DomainPackageStatus"></a>
State of the association.
Type: String
Valid Values: `ASSOCIATING | ASSOCIATION_FAILED | ACTIVE | DISSOCIATING | DISSOCIATION_FAILED`
Required: No

 ** ErrorDetails **   <a name="opensearchservice-Type-DomainPackageDetails-ErrorDetails"></a>
Additional information if the package is in an error state. Null otherwise.
Type: [ErrorDetails](API_ErrorDetails.md) object
Required: No

 ** LastUpdated **   <a name="opensearchservice-Type-DomainPackageDetails-LastUpdated"></a>
Timestamp of the most recent update to the package association status.
Type: Timestamp
Required: No

 ** PackageID **   <a name="opensearchservice-Type-DomainPackageDetails-PackageID"></a>
Internal ID of the package.
Type: String
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: No

 ** PackageName **   <a name="opensearchservice-Type-DomainPackageDetails-PackageName"></a>
User-specified name of the package.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** PackageType **   <a name="opensearchservice-Type-DomainPackageDetails-PackageType"></a>
The type of package.
Type: String
Valid Values: `TXT-DICTIONARY | ZIP-PLUGIN | PACKAGE-LICENSE | PACKAGE-CONFIG`
Required: No

 ** PackageVersion **   <a name="opensearchservice-Type-DomainPackageDetails-PackageVersion"></a>
The current version of the package.
Type: String
Required: No

 ** PrerequisitePackageIDList **   <a name="opensearchservice-Type-DomainPackageDetails-PrerequisitePackageIDList"></a>
A list of package IDs that must be associated with the domain before or with the package can be associated.
Type: Array of strings
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: No

 ** ReferencePath **   <a name="opensearchservice-Type-DomainPackageDetails-ReferencePath"></a>
The relative path of the package on the OpenSearch Service cluster nodes. This is `synonym_path` when the package is for synonym files.
Type: String
Required: No

## See Also
<a name="API_DomainPackageDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DomainPackageDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DomainPackageDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DomainPackageDetails)
