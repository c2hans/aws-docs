---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogInput.html
---

# CatalogInput
<a name="API_CatalogInput"></a>

A structure that describes catalog properties.

## Contents
<a name="API_CatalogInput_Contents"></a>

 ** AllowFullTableExternalDataAccess **   <a name="Glue-Type-CatalogInput-AllowFullTableExternalDataAccess"></a>
 Allows third-party engines to access data in Amazon S3 locations that are registered with Lake Formation.
Type: String
Valid Values: `True | False`
Required: No

 ** CatalogProperties **   <a name="Glue-Type-CatalogInput-CatalogProperties"></a>
A `CatalogProperties` object that specifies data lake access properties and other custom properties.
Type: [CatalogProperties](API_CatalogProperties.md) object
Required: No

 ** CreateDatabaseDefaultPermissions **   <a name="Glue-Type-CatalogInput-CreateDatabaseDefaultPermissions"></a>
An array of `PrincipalPermissions` objects. Creates a set of default permissions on the database(s) for principals. Used by AWS Lake Formation. Typically should be explicitly set as an empty list.
Type: Array of [PrincipalPermissions](API_PrincipalPermissions.md) objects
Required: No

 ** CreateTableDefaultPermissions **   <a name="Glue-Type-CatalogInput-CreateTableDefaultPermissions"></a>
An array of `PrincipalPermissions` objects. Creates a set of default permissions on the table(s) for principals. Used by AWS Lake Formation. Typically should be explicitly set as an empty list.
Type: Array of [PrincipalPermissions](API_PrincipalPermissions.md) objects
Required: No

 ** Description **   <a name="Glue-Type-CatalogInput-Description"></a>
Description string, not more than 2048 bytes long, matching the URI address multi-line string pattern. A description of the catalog.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** FederatedCatalog **   <a name="Glue-Type-CatalogInput-FederatedCatalog"></a>
A `FederatedCatalog` object. A `FederatedCatalog` structure that references an entity outside the AWS Glue Data Catalog, for example a Redshift database.
Type: [FederatedCatalog](API_FederatedCatalog.md) object
Required: No

 ** Parameters **   <a name="Glue-Type-CatalogInput-Parameters"></a>
A map array of key-value pairs that define the parameters and properties of the catalog.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** TargetRedshiftCatalog **   <a name="Glue-Type-CatalogInput-TargetRedshiftCatalog"></a>
A `TargetRedshiftCatalog` object that describes a target catalog for resource linking.
Type: [TargetRedshiftCatalog](API_TargetRedshiftCatalog.md) object
Required: No

## See Also
<a name="API_CatalogInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogInput)
