---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RDSDataSpec.html
---

# RDSDataSpec
<a name="API_RDSDataSpec"></a>

The data specification of an Amazon Relational Database Service (Amazon RDS) `DataSource`.

## Contents
<a name="API_RDSDataSpec_Contents"></a>

 ** DatabaseCredentials **   <a name="amazonml-Type-RDSDataSpec-DatabaseCredentials"></a>
The AWS Identity and Access Management (IAM) credentials that are used connect to the Amazon RDS database.
Type: [RDSDatabaseCredentials](API_RDSDatabaseCredentials.md) object
Required: Yes

 ** DatabaseInformation **   <a name="amazonml-Type-RDSDataSpec-DatabaseInformation"></a>
Describes the `DatabaseName` and `InstanceIdentifier` of an Amazon RDS database.
Type: [RDSDatabase](API_RDSDatabase.md) object
Required: Yes

 ** ResourceRole **   <a name="amazonml-Type-RDSDataSpec-ResourceRole"></a>
The role (DataPipelineDefaultResourceRole) assumed by an Amazon Elastic Compute Cloud (Amazon EC2) instance to carry out the copy operation from Amazon RDS to an Amazon S3 task. For more information, see [Role templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** S3StagingLocation **   <a name="amazonml-Type-RDSDataSpec-S3StagingLocation"></a>
The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using `SelectSqlQuery` is stored in this location.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: Yes

 ** SecurityGroupIds **   <a name="amazonml-Type-RDSDataSpec-SecurityGroupIds"></a>
The security group IDs to be used to access a VPC-based RDS DB instance. Ensure that there are appropriate ingress rules set up to allow access to the RDS DB instance. This attribute is used by Data Pipeline to carry out the copy operation from Amazon RDS to an Amazon S3 task.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** SelectSqlQuery **   <a name="amazonml-Type-RDSDataSpec-SelectSqlQuery"></a>
The query that is used to retrieve the observation data for the `DataSource`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16777216.
Required: Yes

 ** ServiceRole **   <a name="amazonml-Type-RDSDataSpec-ServiceRole"></a>
The role (DataPipelineDefaultRole) assumed by AWS Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see [Role templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** SubnetId **   <a name="amazonml-Type-RDSDataSpec-SubnetId"></a>
The subnet ID to be used to access a VPC-based RDS DB instance. This attribute is used by Data Pipeline to carry out the copy task from Amazon RDS to Amazon S3.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** DataRearrangement **   <a name="amazonml-Type-RDSDataSpec-DataRearrangement"></a>
A JSON string that represents the splitting and rearrangement processing to be applied to a `DataSource`. If the `DataRearrangement` parameter is not provided, all of the input data is used to create the `Datasource`.
There are multiple parameters that control what data is used to create a datasource:
+  ** `percentBegin` **

  Use `percentBegin` to indicate the beginning of the range of the data used to create the Datasource. If you do not include `percentBegin` and `percentEnd`, Amazon ML includes all of the data when creating the datasource.
+  ** `percentEnd` **

  Use `percentEnd` to indicate the end of the range of the data used to create the Datasource. If you do not include `percentBegin` and `percentEnd`, Amazon ML includes all of the data when creating the datasource.
+  ** `complement` **

  The `complement` parameter instructs Amazon ML to use the data that is not included in the range of `percentBegin` to `percentEnd` to create a datasource. The `complement` parameter is useful if you need to create complementary datasources for training and evaluation. To create a complementary datasource, use the same values for `percentBegin` and `percentEnd`, along with the `complement` parameter.

  For example, the following two datasources do not share any data, and can be used to train and evaluate a model. The first datasource has 25 percent of the data, and the second one has 75 percent of the data.

  Datasource for evaluation: `{"splitting":{"percentBegin":0, "percentEnd":25}}`

  Datasource for training: `{"splitting":{"percentBegin":0, "percentEnd":25, "complement":"true"}}`
+  ** `strategy` **

  To change how Amazon ML splits the data for a datasource, use the `strategy` parameter.

  The default value for the `strategy` parameter is `sequential`, meaning that Amazon ML takes all of the data records between the `percentBegin` and `percentEnd` parameters for the datasource, in the order that the records appear in the input data.

  The following two `DataRearrangement` lines are examples of sequentially ordered training and evaluation datasources:

  Datasource for evaluation: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential"}}`

  Datasource for training: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential", "complement":"true"}}`

  To randomly split the input data into the proportions indicated by the percentBegin and percentEnd parameters, set the `strategy` parameter to `random` and provide a string that is used as the seed value for the random data splitting (for example, you can use the S3 path to your data as the random seed string). If you choose the random split strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then selects the rows that have an assigned number between `percentBegin` and `percentEnd`. Pseudo-random numbers are assigned using both the input seed string value and the byte offset as a seed, so changing the data results in a different split. Any existing ordering is preserved. The random splitting strategy ensures that variables in the training and evaluation data are distributed similarly. It is useful in the cases where the input data may have an implicit sort order, which would otherwise result in training and evaluation datasources containing non-similar data records.

  The following two `DataRearrangement` lines are examples of non-sequentially ordered training and evaluation datasources:

  Datasource for evaluation: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "strategyParams": {"randomSeed":"RANDOMSEED"}}}`

  Datasource for training: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "strategyParams": {"randomSeed":"RANDOMSEED"}, "complement":"true"}}`
Type: String
Required: No

 ** DataSchema **   <a name="amazonml-Type-RDSDataSpec-DataSchema"></a>
A JSON string that represents the schema for an Amazon RDS `DataSource`. The `DataSchema` defines the structure of the observation data in the data file(s) referenced in the `DataSource`.
A `DataSchema` is not required if you specify a `DataSchemaUri`
Define your `DataSchema` as a series of key-value pairs. `attributes` and `excludedAttributeNames` have an array of key-value pairs for their value. Use the following format to define your `DataSchema`.
{ "version": "1.0",
"recordAnnotationFieldName": "F1",
"recordWeightFieldName": "F2",
"targetAttributeName": "F3",
"dataFormat": "CSV",
"dataFileContainsHeader": true,
"attributes": [
{ "attributeName": "F1", "attributeType": "TEXT" }, { "attributeName": "F2", "attributeType": "NUMERIC" }, { "attributeName": "F3", "attributeType": "CATEGORICAL" }, { "attributeName": "F4", "attributeType": "NUMERIC" }, { "attributeName": "F5", "attributeType": "CATEGORICAL" }, { "attributeName": "F6", "attributeType": "TEXT" }, { "attributeName": "F7", "attributeType": "WEIGHTED\_INT\_SEQUENCE" }, { "attributeName": "F8", "attributeType": "WEIGHTED\_STRING\_SEQUENCE" } ],
"excludedAttributeNames": [ "F6" ] }
Type: String
Length Constraints: Maximum length of 131071.
Required: No

 ** DataSchemaUri **   <a name="amazonml-Type-RDSDataSpec-DataSchemaUri"></a>
The Amazon S3 location of the `DataSchema`.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: No

## See Also
<a name="API_RDSDataSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/RDSDataSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/RDSDataSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/RDSDataSpec)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
