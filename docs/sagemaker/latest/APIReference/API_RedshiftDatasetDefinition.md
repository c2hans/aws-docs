---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RedshiftDatasetDefinition.html
---

# RedshiftDatasetDefinition
<a name="API_RedshiftDatasetDefinition"></a>

Configuration for Redshift Dataset Definition input.

## Contents
<a name="API_RedshiftDatasetDefinition_Contents"></a>

 ** ClusterId **   <a name="sagemaker-Type-RedshiftDatasetDefinition-ClusterId"></a>
The Redshift cluster Identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `.*`
Required: Yes

 ** ClusterRoleArn **   <a name="sagemaker-Type-RedshiftDatasetDefinition-ClusterRoleArn"></a>
The IAM role attached to your Redshift cluster that Amazon SageMaker uses to generate datasets.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** Database **   <a name="sagemaker-Type-RedshiftDatasetDefinition-Database"></a>
The name of the Redshift database used in Redshift query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: Yes

 ** DbUser **   <a name="sagemaker-Type-RedshiftDatasetDefinition-DbUser"></a>
The database user name used in Redshift query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*`
Required: Yes

 ** OutputFormat **   <a name="sagemaker-Type-RedshiftDatasetDefinition-OutputFormat"></a>
The data storage format for Redshift query results.
Type: String
Valid Values: `PARQUET | CSV`
Required: Yes

 ** OutputS3Uri **   <a name="sagemaker-Type-RedshiftDatasetDefinition-OutputS3Uri"></a>
The location in Amazon S3 where the Redshift query results are stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** QueryString **   <a name="sagemaker-Type-RedshiftDatasetDefinition-QueryString"></a>
The SQL query statements to be executed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\s\S]+`
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-RedshiftDatasetDefinition-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data from a Redshift execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** OutputCompression **   <a name="sagemaker-Type-RedshiftDatasetDefinition-OutputCompression"></a>
The compression used for Redshift query results.
Type: String
Valid Values: `None | GZIP | BZIP2 | ZSTD | SNAPPY`
Required: No

## See Also
<a name="API_RedshiftDatasetDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RedshiftDatasetDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RedshiftDatasetDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RedshiftDatasetDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
