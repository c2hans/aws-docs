---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SchemaConfiguration.html
---

# SchemaConfiguration
<a name="API_SchemaConfiguration"></a>

Specifies the schema to which you want Firehose to configure your data before it writes it to Amazon S3. This parameter is required if `Enabled` is set to true.

## Contents
<a name="API_SchemaConfiguration_Contents"></a>

 ** CatalogId **   <a name="Firehose-Type-SchemaConfiguration-CatalogId"></a>
The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: No

 ** DatabaseName **   <a name="Firehose-Type-SchemaConfiguration-DatabaseName"></a>
Specifies the name of the AWS Glue database that contains the schema for the output data.
If the `SchemaConfiguration` request parameter is used as part of invoking the `CreateDeliveryStream` API, then the `DatabaseName` property is required and its value must be specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: No

 ** Region **   <a name="Firehose-Type-SchemaConfiguration-Region"></a>
If you don't specify an AWS Region, the default is the current Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: No

 ** RoleARN **   <a name="Firehose-Type-SchemaConfiguration-RoleARN"></a>
The role that Firehose can use to access AWS Glue. This role must be in the same account you use for Firehose. Cross-account roles aren't allowed.
If the `SchemaConfiguration` request parameter is used as part of invoking the `CreateDeliveryStream` API, then the `RoleARN` property is required and its value must be specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: No

 ** TableName **   <a name="Firehose-Type-SchemaConfiguration-TableName"></a>
Specifies the AWS Glue table that contains the column information that constitutes your data schema.
If the `SchemaConfiguration` request parameter is used as part of invoking the `CreateDeliveryStream` API, then the `TableName` property is required and its value must be specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: No

 ** VersionId **   <a name="Firehose-Type-SchemaConfiguration-VersionId"></a>
Specifies the table version for the output data schema. If you don't specify this version ID, or if you set it to `LATEST`, Firehose uses the most recent version. This means that any updates to the table are automatically picked up.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: No

## See Also
<a name="API_SchemaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SchemaConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SchemaConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SchemaConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
