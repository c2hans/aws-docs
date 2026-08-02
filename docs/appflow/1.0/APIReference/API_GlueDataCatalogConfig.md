---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_GlueDataCatalogConfig.html
---

# GlueDataCatalogConfig
<a name="API_GlueDataCatalogConfig"></a>

Specifies the configuration that Amazon AppFlow uses when it catalogs your data with the AWS Glue Data Catalog. When Amazon AppFlow catalogs your data, it stores metadata in Data Catalog tables. This metadata represents the data that's transferred by the flow that you configure with these settings.

**Note**
You can configure a flow with these settings only when the flow destination is Amazon S3.

## Contents
<a name="API_GlueDataCatalogConfig_Contents"></a>

 ** databaseName **   <a name="appflow-Type-GlueDataCatalogConfig-databaseName"></a>
The name of the Data Catalog database that stores the metadata tables that Amazon AppFlow creates in your AWS account. These tables contain metadata for the data that's transferred by the flow that you configure with this parameter.
When you configure a new flow with this parameter, you must specify an existing database.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** roleArn **   <a name="appflow-Type-GlueDataCatalogConfig-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that grants Amazon AppFlow the permissions it needs to create Data Catalog tables, databases, and partitions.
For an example IAM policy that has the required permissions, see [Identity-based policy examples for Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_id-based-policy-examples.html).
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:iam:.*:[0-9]+:.*`
Required: Yes

 ** tablePrefix **   <a name="appflow-Type-GlueDataCatalogConfig-tablePrefix"></a>
A naming prefix for each Data Catalog table that Amazon AppFlow creates for the flow that you configure with this setting. Amazon AppFlow adds the prefix to the beginning of the each table name.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## See Also
<a name="API_GlueDataCatalogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/GlueDataCatalogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/GlueDataCatalogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/GlueDataCatalogConfig)
