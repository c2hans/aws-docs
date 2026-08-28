---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DataProvider.html
---

# DataProvider
<a name="API_DataProvider"></a>

Provides information that defines a data provider.

## Contents
<a name="API_DataProvider_Contents"></a>

 ** DataProviderArn **   <a name="DMS-Type-DataProvider-DataProviderArn"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the data provider.
Type: String
Required: No

 ** DataProviderCreationTime **   <a name="DMS-Type-DataProvider-DataProviderCreationTime"></a>
The time the data provider was created.
Type: Timestamp
Required: No

 ** DataProviderName **   <a name="DMS-Type-DataProvider-DataProviderName"></a>
The name of the data provider.
Type: String
Required: No

 ** Description **   <a name="DMS-Type-DataProvider-Description"></a>
A description of the data provider. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.
Type: String
Required: No

 ** Engine **   <a name="DMS-Type-DataProvider-Engine"></a>
The type of database engine for the data provider.
Valid values: `aurora`, `aurora-postgresql`, `db2`, `db2-zos`, `docdb`, `mariadb`, `mongodb`, `mysql`, `oracle`, `postgres`, `redshift`, `sqlserver`, and `sybase`. A value of `aurora` represents Amazon Aurora MySQL-Compatible Edition.
Type: String
Required: No

 ** Settings **   <a name="DMS-Type-DataProvider-Settings"></a>
The settings in JSON format for a data provider.
Type: [DataProviderSettings](API_DataProviderSettings.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Virtual **   <a name="DMS-Type-DataProvider-Virtual"></a>
Indicates whether the data provider is virtual.
Type: Boolean
Required: No

## See Also
<a name="API_DataProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DataProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DataProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DataProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
