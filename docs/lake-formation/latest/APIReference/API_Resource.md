---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

A structure for the resource.

## Contents
<a name="API_Resource_Contents"></a>

 ** Catalog **   <a name="lakeformation-Type-Resource-Catalog"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: [CatalogResource](API_CatalogResource.md) object
Required: No

 ** Database **   <a name="lakeformation-Type-Resource-Database"></a>
The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.
Type: [DatabaseResource](API_DatabaseResource.md) object
Required: No

 ** DataCellsFilter **   <a name="lakeformation-Type-Resource-DataCellsFilter"></a>
A data cell filter.
Type: [DataCellsFilterResource](API_DataCellsFilterResource.md) object
Required: No

 ** DataLocation **   <a name="lakeformation-Type-Resource-DataLocation"></a>
The location of an Amazon S3 path where permissions are granted or revoked.
Type: [DataLocationResource](API_DataLocationResource.md) object
Required: No

 ** LFTag **   <a name="lakeformation-Type-Resource-LFTag"></a>
The LF-Tag key and values attached to a resource.
Type: [LFTagKeyResource](API_LFTagKeyResource.md) object
Required: No

 ** LFTagExpression **   <a name="lakeformation-Type-Resource-LFTagExpression"></a>
LF-Tag expression resource. A logical expression composed of one or more LF-Tag key:value pairs.
Type: [LFTagExpressionResource](API_LFTagExpressionResource.md) object
Required: No

 ** LFTagPolicy **   <a name="lakeformation-Type-Resource-LFTagPolicy"></a>
A list of LF-tag conditions or saved LF-Tag expressions that define a resource's LF-tag policy.
Type: [LFTagPolicyResource](API_LFTagPolicyResource.md) object
Required: No

 ** Table **   <a name="lakeformation-Type-Resource-Table"></a>
The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
Type: [TableResource](API_TableResource.md) object
Required: No

 ** TableWithColumns **   <a name="lakeformation-Type-Resource-TableWithColumns"></a>
The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.
Type: [TableWithColumnsResource](API_TableWithColumnsResource.md) object
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
