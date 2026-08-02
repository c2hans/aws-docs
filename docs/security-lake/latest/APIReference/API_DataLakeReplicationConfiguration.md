---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeReplicationConfiguration.html
---

# DataLakeReplicationConfiguration
<a name="API_DataLakeReplicationConfiguration"></a>

Provides replication details for objects stored in the Amazon Security Lake data lake.

## Contents
<a name="API_DataLakeReplicationConfiguration_Contents"></a>

 ** regions **   <a name="securitylake-Type-DataLakeReplicationConfiguration-regions"></a>
Specifies one or more centralized rollup Regions. The AWS Region specified in the `region` parameter of the [https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake.html](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake.html) or [https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake.html](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake.html) operations contributes data to the rollup Region or Regions specified in this parameter.
Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. S3 buckets that are configured for object replication can be owned by the same AWS account or by different accounts. You can replicate objects to a single destination bucket or to multiple destination buckets. The destination buckets can be in different Regions or within the same Region as the source bucket.
Type: Array of strings
Pattern: `(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+`
Required: No

 ** roleArn **   <a name="securitylake-Type-DataLakeReplicationConfiguration-roleArn"></a>
Replication settings for the Amazon S3 buckets. This parameter uses the AWS Identity and Access Management (IAM) role you created that is managed by Security Lake, to ensure the replication setting is correct.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## See Also
<a name="API_DataLakeReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DataLakeReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DataLakeReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DataLakeReplicationConfiguration)
