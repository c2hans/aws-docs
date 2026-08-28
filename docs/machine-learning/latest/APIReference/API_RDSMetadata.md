---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RDSMetadata.html
---

# RDSMetadata
<a name="API_RDSMetadata"></a>

The datasource details that are specific to Amazon RDS.

## Contents
<a name="API_RDSMetadata_Contents"></a>

 ** Database **   <a name="amazonml-Type-RDSMetadata-Database"></a>
The database details required to connect to an Amazon RDS.
Type: [RDSDatabase](API_RDSDatabase.md) object
Required: No

 ** DatabaseUserName **   <a name="amazonml-Type-RDSMetadata-DatabaseUserName"></a>
The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an `RDSSelectSqlQuery` query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** DataPipelineId **   <a name="amazonml-Type-RDSMetadata-DataPipelineId"></a>
The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS to Amazon S3. You can use the ID to find details about the instance in the Data Pipeline console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ResourceRole **   <a name="amazonml-Type-RDSMetadata-ResourceRole"></a>
The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry out the copy task from Amazon RDS to Amazon S3. For more information, see [Role templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** SelectSqlQuery **   <a name="amazonml-Type-RDSMetadata-SelectSqlQuery"></a>
The SQL query that is supplied during [CreateDataSourceFromRDS](API_CreateDataSourceFromRDS.md). Returns only if `Verbose` is true in `GetDataSourceInput`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16777216.
Required: No

 ** ServiceRole **   <a name="amazonml-Type-RDSMetadata-ServiceRole"></a>
The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see [Role templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_RDSMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/RDSMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/RDSMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/RDSMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
