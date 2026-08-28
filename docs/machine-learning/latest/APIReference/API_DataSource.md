---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DataSource.html
---

# DataSource
<a name="API_DataSource"></a>

 Represents the output of the `GetDataSource` operation.

 The content consists of the detailed metadata and data file information and the current status of the `DataSource`.

## Contents
<a name="API_DataSource_Contents"></a>

 ** ComputeStatistics **   <a name="amazonml-Type-DataSource-ComputeStatistics"></a>
 The parameter is `true` if statistics need to be generated from the observation data.
Type: Boolean
Required: No

 ** ComputeTime **   <a name="amazonml-Type-DataSource-ComputeTime"></a>
Long integer type that is a 64-bit signed number.
Type: Long
Required: No

 ** CreatedAt **   <a name="amazonml-Type-DataSource-CreatedAt"></a>
The time that the `DataSource` was created. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** CreatedByIamUser **   <a name="amazonml-Type-DataSource-CreatedByIamUser"></a>
The AWS user account from which the `DataSource` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
Type: String
Pattern: `arn:aws:iam::[0-9]+:((user/.+)|(root))`
Required: No

 ** DataLocationS3 **   <a name="amazonml-Type-DataSource-DataLocationS3"></a>
The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is used by a `DataSource`.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `s3://([^/]+)(/.*)?`
Required: No

 ** DataRearrangement **   <a name="amazonml-Type-DataSource-DataRearrangement"></a>
A JSON string that represents the splitting and rearrangement requirement used when this `DataSource` was created.
Type: String
Required: No

 ** DataSizeInBytes **   <a name="amazonml-Type-DataSource-DataSizeInBytes"></a>
The total number of observations contained in the data files that the `DataSource` references.
Type: Long
Required: No

 ** DataSourceId **   <a name="amazonml-Type-DataSource-DataSourceId"></a>
The ID that is assigned to the `DataSource` during creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** FinishedAt **   <a name="amazonml-Type-DataSource-FinishedAt"></a>
A timestamp represented in epoch time.
Type: Timestamp
Required: No

 ** LastUpdatedAt **   <a name="amazonml-Type-DataSource-LastUpdatedAt"></a>
The time of the most recent edit to the `BatchPrediction`. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** Message **   <a name="amazonml-Type-DataSource-Message"></a>
A description of the most recent details about creating the `DataSource`.
Type: String
Length Constraints: Maximum length of 10240.
Required: No

 ** Name **   <a name="amazonml-Type-DataSource-Name"></a>
A user-supplied name or description of the `DataSource`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `.*\S.*|^$`
Required: No

 ** NumberOfFiles **   <a name="amazonml-Type-DataSource-NumberOfFiles"></a>
The number of data files referenced by the `DataSource`.
Type: Long
Required: No

 ** RDSMetadata **   <a name="amazonml-Type-DataSource-RDSMetadata"></a>
The datasource details that are specific to Amazon RDS.
Type: [RDSMetadata](API_RDSMetadata.md) object
Required: No

 ** RedshiftMetadata **   <a name="amazonml-Type-DataSource-RedshiftMetadata"></a>
Describes the `DataSource` details specific to Amazon Redshift.
Type: [RedshiftMetadata](API_RedshiftMetadata.md) object
Required: No

 ** RoleARN **   <a name="amazonml-Type-DataSource-RoleARN"></a>
The Amazon Resource Name (ARN) of an [AWS IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts), such as the following: arn:aws:iam::account:role/rolename.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 110.
Required: No

 ** StartedAt **   <a name="amazonml-Type-DataSource-StartedAt"></a>
A timestamp represented in epoch time.
Type: Timestamp
Required: No

 ** Status **   <a name="amazonml-Type-DataSource-Status"></a>
The current status of the `DataSource`. This element can have one of the following values:
+ PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a `DataSource`.
+ INPROGRESS - The creation process is underway.
+ FAILED - The request to create a `DataSource` did not run to completion. It is not usable.
+ COMPLETED - The creation process completed successfully.
+ DELETED - The `DataSource` is marked as deleted. It is not usable.
Type: String
Valid Values: `PENDING | INPROGRESS | FAILED | COMPLETED | DELETED`
Required: No

## See Also
<a name="API_DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/DataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MachineLearning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
