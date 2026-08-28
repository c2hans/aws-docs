---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RedshiftDataSpec.html
---

# RedshiftDataSpec
<a name="API_RedshiftDataSpec"></a>

Describes the data specification of an Amazon Redshift `DataSource`.

## Contents
<a name="API_RedshiftDataSpec_Contents"></a>

 ** DatabaseCredentials **   <a name="amazonml-Type-RedshiftDataSpec-DatabaseCredentials"></a>
Describes AWS Identity and Access Management (IAM) credentials that are used connect to the Amazon Redshift database.
Type: [RedshiftDatabaseCredentials](API_RedshiftDatabaseCredentials.md) object
Required: Yes

 ** DatabaseInformation **   <a name="amazonml-Type-RedshiftDataSpec-DatabaseInformation"></a>
Describes the `DatabaseName` and `ClusterIdentifier` for an Amazon Redshift `DataSource`.
Type: [RedshiftDatabase](API_RedshiftDatabase.md) object
Required: Yes

 ** S3StagingLocation **   <a name="amazonml-Type-RedshiftDataSpec-S3StagingLocation"></a>
Describes an Amazon S3 location to store the result set of the `SelectSqlQuery` query.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: Yes

 ** SelectSqlQuery **   <a name="amazonml-Type-RedshiftDataSpec-SelectSqlQuery"></a>
Describes the SQL Query to execute on an Amazon Redshift database for an Amazon Redshift `DataSource`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16777216.
Required: Yes

 ** DataRearrangement **   <a name="amazonml-Type-RedshiftDataSpec-DataRearrangement"></a>
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

 ** DataSchema **   <a name="amazonml-Type-RedshiftDataSpec-DataSchema"></a>
A JSON string that represents the schema for an Amazon Redshift `DataSource`. The `DataSchema` defines the structure of the observation data in the data file(s) referenced in the `DataSource`.
A `DataSchema` is not required if you specify a `DataSchemaUri`.
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

 ** DataSchemaUri **   <a name="amazonml-Type-RedshiftDataSpec-DataSchemaUri"></a>
Describes the schema location for an Amazon Redshift `DataSource`.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: No

## See Also
<a name="API_RedshiftDataSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/RedshiftDataSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/RedshiftDataSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/RedshiftDataSpec)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
