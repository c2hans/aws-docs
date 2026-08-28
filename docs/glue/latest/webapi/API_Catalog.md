---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Catalog.html
---

# Catalog
<a name="API_Catalog"></a>

The catalog object represents a logical grouping of databases in the AWS Glue Data Catalog or a federated source. You can now create a Redshift-federated catalog or a catalog containing resource links to Redshift databases in another account or region.

## Contents
<a name="API_Catalog_Contents"></a>

 ** Name **   <a name="Glue-Type-Catalog-Name"></a>
The name of the catalog. Cannot be the same as the account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^(?!(.*[.\/\\]|aws:)).*$`
Required: Yes

 ** AllowFullTableExternalDataAccess **   <a name="Glue-Type-Catalog-AllowFullTableExternalDataAccess"></a>
 Allows third-party engines to access data in Amazon S3 locations that are registered with Lake Formation.
Type: String
Valid Values: `True | False`
Required: No

 ** CatalogId **   <a name="Glue-Type-Catalog-CatalogId"></a>
The ID of the catalog. To grant access to the default catalog, this field should not be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** CatalogProperties **   <a name="Glue-Type-Catalog-CatalogProperties"></a>
A `CatalogProperties` object that specifies data lake access properties and other custom properties.
Type: [CatalogPropertiesOutput](API_CatalogPropertiesOutput.md) object
Required: No

 ** CreateDatabaseDefaultPermissions **   <a name="Glue-Type-Catalog-CreateDatabaseDefaultPermissions"></a>
An array of `PrincipalPermissions` objects. Creates a set of default permissions on the database(s) for principals. Used by AWS Lake Formation. Not used in the normal course of AWS Glue operations.
Type: Array of [PrincipalPermissions](API_PrincipalPermissions.md) objects
Required: No

 ** CreateTableDefaultPermissions **   <a name="Glue-Type-Catalog-CreateTableDefaultPermissions"></a>
An array of `PrincipalPermissions` objects. Creates a set of default permissions on the table(s) for principals. Used by AWS Lake Formation. Not used in the normal course of AWS Glue operations.
Type: Array of [PrincipalPermissions](API_PrincipalPermissions.md) objects
Required: No

 ** CreateTime **   <a name="Glue-Type-Catalog-CreateTime"></a>
The time at which the catalog was created.
Type: Timestamp
Required: No

 ** Description **   <a name="Glue-Type-Catalog-Description"></a>
Description string, not more than 2048 bytes long, matching the URI address multi-line string pattern. A description of the catalog.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** FederatedCatalog **   <a name="Glue-Type-Catalog-FederatedCatalog"></a>
A `FederatedCatalog` object that points to an entity outside the AWS Glue Data Catalog.
Type: [FederatedCatalog](API_FederatedCatalog.md) object
Required: No

 ** Parameters **   <a name="Glue-Type-Catalog-Parameters"></a>
 A map array of key-value pairs that define parameters and properties of the catalog.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** ResourceArn **   <a name="Glue-Type-Catalog-ResourceArn"></a>
The Amazon Resource Name (ARN) assigned to the catalog resource.
Type: String
Required: No

 ** TargetRedshiftCatalog **   <a name="Glue-Type-Catalog-TargetRedshiftCatalog"></a>
A `TargetRedshiftCatalog` object that describes a target catalog for database resource linking.
Type: [TargetRedshiftCatalog](API_TargetRedshiftCatalog.md) object
Required: No

 ** UpdateTime **   <a name="Glue-Type-Catalog-UpdateTime"></a>
The time at which the catalog was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Catalog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Catalog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Catalog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Catalog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
