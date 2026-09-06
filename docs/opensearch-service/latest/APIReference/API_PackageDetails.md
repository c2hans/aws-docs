---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PackageDetails.html
---

# PackageDetails
<a name="API_PackageDetails"></a>

Basic information about a package.

## Contents
<a name="API_PackageDetails_Contents"></a>

 ** AllowListedUserList **   <a name="opensearchservice-Type-PackageDetails-AllowListedUserList"></a>
 A list of users who are allowed to view and associate the package. This field is only visible to the owner of a package.
Type: Array of strings
Length Constraints: Minimum length of 6. Maximum length of 12.
Pattern: `^[0-9]{12}$|^GLOBAL$`
Required: No

 ** AvailablePackageConfiguration **   <a name="opensearchservice-Type-PackageDetails-AvailablePackageConfiguration"></a>
This represents the available configuration parameters for the package.
Type: [PackageConfiguration](API_PackageConfiguration.md) object
Required: No

 ** AvailablePackageVersion **   <a name="opensearchservice-Type-PackageDetails-AvailablePackageVersion"></a>
The package version.
Type: String
Required: No

 ** AvailablePluginProperties **   <a name="opensearchservice-Type-PackageDetails-AvailablePluginProperties"></a>
If the package is a `ZIP-PLUGIN` package, additional information about plugin properties.
Type: [PluginProperties](API_PluginProperties.md) object
Required: No

 ** CreatedAt **   <a name="opensearchservice-Type-PackageDetails-CreatedAt"></a>
The timestamp when the package was created.
Type: Timestamp
Required: No

 ** EngineVersion **   <a name="opensearchservice-Type-PackageDetails-EngineVersion"></a>
Version of OpenSearch or Elasticsearch, in the format Elasticsearch\_X.Y or OpenSearch\_X.Y. Defaults to the latest version of OpenSearch.
Type: String
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: No

 ** ErrorDetails **   <a name="opensearchservice-Type-PackageDetails-ErrorDetails"></a>
Additional information if the package is in an error state. Null otherwise.
Type: [ErrorDetails](API_ErrorDetails.md) object
Required: No

 ** LastUpdatedAt **   <a name="opensearchservice-Type-PackageDetails-LastUpdatedAt"></a>
Date and time when the package was last updated.
Type: Timestamp
Required: No

 ** PackageDescription **   <a name="opensearchservice-Type-PackageDetails-PackageDescription"></a>
User-specified description of the package.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** PackageEncryptionOptions **   <a name="opensearchservice-Type-PackageDetails-PackageEncryptionOptions"></a>
Encryption options for a package.
Type: [PackageEncryptionOptions](API_PackageEncryptionOptions.md) object
Required: No

 ** PackageID **   <a name="opensearchservice-Type-PackageDetails-PackageID"></a>
The unique identifier of the package.
Type: String
Pattern: `^([FG][0-9]+)$|^(pkg-[a-f0-9]+)$`
Required: No

 ** PackageName **   <a name="opensearchservice-Type-PackageDetails-PackageName"></a>
The user-specified name of the package.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** PackageOwner **   <a name="opensearchservice-Type-PackageDetails-PackageOwner"></a>
The owner of the package who is allowed to create and update a package and add users to the package scope.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** PackageStatus **   <a name="opensearchservice-Type-PackageDetails-PackageStatus"></a>
The current status of the package. The available options are `AVAILABLE`, `COPYING`, `COPY_FAILED`, `VALIDATNG`, `VALIDATION_FAILED`, `DELETING`, and `DELETE_FAILED`.
Type: String
Valid Values: `COPYING | COPY_FAILED | VALIDATING | VALIDATION_FAILED | AVAILABLE | DELETING | DELETED | DELETE_FAILED`
Required: No

 ** PackageType **   <a name="opensearchservice-Type-PackageDetails-PackageType"></a>
The type of package.
Type: String
Valid Values: `TXT-DICTIONARY | ZIP-PLUGIN | PACKAGE-LICENSE | PACKAGE-CONFIG`
Required: No

 ** PackageVendingOptions **   <a name="opensearchservice-Type-PackageDetails-PackageVendingOptions"></a>
Package Vending Options for a package.
Type: [PackageVendingOptions](API_PackageVendingOptions.md) object
Required: No

## See Also
<a name="API_PackageDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/PackageDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/PackageDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/PackageDetails)
