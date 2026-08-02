---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ContinuousExportDescription.html
---

# ContinuousExportDescription
<a name="API_ContinuousExportDescription"></a>

A list of continuous export descriptions.

## Contents
<a name="API_ContinuousExportDescription_Contents"></a>

 ** dataSource **   <a name="DiscServ-Type-ContinuousExportDescription-dataSource"></a>
The type of data collector used to gather this data (currently only offered for AGENT).
Type: String
Valid Values: `AGENT`
Required: No

 ** exportId **   <a name="DiscServ-Type-ContinuousExportDescription-exportId"></a>
The unique ID assigned to this export.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: No

 ** s3Bucket **   <a name="DiscServ-Type-ContinuousExportDescription-s3Bucket"></a>
The name of the s3 bucket where the export data parquet files are stored.
Type: String
Required: No

 ** schemaStorageConfig **   <a name="DiscServ-Type-ContinuousExportDescription-schemaStorageConfig"></a>
An object which describes how the data is stored.
+  `databaseName` - the name of the Glue database used to store the schema.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 252.
Value Length Constraints: Maximum length of 10000.
Value Pattern: `[\s\S]*`
Required: No

 ** startTime **   <a name="DiscServ-Type-ContinuousExportDescription-startTime"></a>
The timestamp representing when the continuous export was started.
Type: Timestamp
Required: No

 ** status **   <a name="DiscServ-Type-ContinuousExportDescription-status"></a>
Describes the status of the export. Can be one of the following values:
+ START\_IN\_PROGRESS - setting up resources to start continuous export.
+ START\_FAILED - an error occurred setting up continuous export. To recover, call start-continuous-export again.
+ ACTIVE - data is being exported to the customer bucket.
+ ERROR - an error occurred during export. To fix the issue, call stop-continuous-export and start-continuous-export.
+ STOP\_IN\_PROGRESS - stopping the export.
+ STOP\_FAILED - an error occurred stopping the export. To recover, call stop-continuous-export again.
+ INACTIVE - the continuous export has been stopped. Data is no longer being exported to the customer bucket.
Type: String
Valid Values: `START_IN_PROGRESS | START_FAILED | ACTIVE | ERROR | STOP_IN_PROGRESS | STOP_FAILED | INACTIVE`
Required: No

 ** statusDetail **   <a name="DiscServ-Type-ContinuousExportDescription-statusDetail"></a>
Contains information about any errors that have occurred. This data type can have the following values:
+ ACCESS\_DENIED - You don’t have permission to start Data Exploration in Amazon Athena. Contact your AWS administrator for help. For more information, see [Setting Up AWS Application Discovery Service](http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html) in the Application Discovery Service User Guide.
+ DELIVERY\_STREAM\_LIMIT\_FAILURE - You reached the limit for Amazon Kinesis Data Firehose delivery streams. Reduce the number of streams or request a limit increase and try again. For more information, see [Kinesis Data Streams Limits](http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html) in the Amazon Kinesis Data Streams Developer Guide.
+ FIREHOSE\_ROLE\_MISSING - The Data Exploration feature is in an error state because your user is missing the AWSApplicationDiscoveryServiceFirehose role. Turn on Data Exploration in Amazon Athena and try again. For more information, see [Creating the AWSApplicationDiscoveryServiceFirehose Role](https://docs.aws.amazon.com/application-discovery/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-create-firehose-role) in the Application Discovery Service User Guide.
+ FIREHOSE\_STREAM\_DOES\_NOT\_EXIST - The Data Exploration feature is in an error state because your user is missing one or more of the Kinesis data delivery streams.
+ INTERNAL\_FAILURE - The Data Exploration feature is in an error state because of an internal failure. Try again later. If this problem persists, contact AWS Support.
+ LAKE\_FORMATION\_ACCESS\_DENIED - You don't have sufficient lake formation permissions to start continuous export. For more information, see [ Upgrading AWS Glue Data Permissions to the AWS Lake Formation Model ](http://docs.aws.amazon.com/lake-formation/latest/dg/upgrade-glue-lake-formation.html) in the AWS *Lake Formation Developer Guide*.

  You can use one of the following two ways to resolve this issue.

  1. If you don’t want to use the Lake Formation permission model, you can change the default Data Catalog settings to use only AWS Identity and Access Management (IAM) access control for new databases. For more information, see [Change Data Catalog Settings](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html#setup-change-cat-settings) in the *Lake Formation Developer Guide*.

  1. You can give the service-linked IAM roles AWSServiceRoleForApplicationDiscoveryServiceContinuousExport and AWSApplicationDiscoveryServiceFirehose the required Lake Formation permissions. For more information, see [ Granting Database Permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-database-permissions.html) in the *Lake Formation Developer Guide*.

     1. AWSServiceRoleForApplicationDiscoveryServiceContinuousExport - Grant database creator permissions, which gives the role database creation ability and implicit permissions for any created tables. For more information, see [ Implicit Lake Formation Permissions ](https://docs.aws.amazon.com/lake-formation/latest/dg/implicit-permissions.html) in the *Lake Formation Developer Guide*.

     1. AWSApplicationDiscoveryServiceFirehose - Grant describe permissions for all tables in the database.
+ S3\_BUCKET\_LIMIT\_FAILURE - You reached the limit for Amazon S3 buckets. Reduce the number of S3 buckets or request a limit increase and try again. For more information, see [Bucket Restrictions and Limitations](http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) in the Amazon Simple Storage Service Developer Guide.
+ S3\_NOT\_SIGNED\_UP - Your account is not signed up for the Amazon S3 service. You must sign up before you can use Amazon S3. You can sign up at the following URL: [https://aws.amazon.com/s3](https://aws.amazon.com/s3).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** stopTime **   <a name="DiscServ-Type-ContinuousExportDescription-stopTime"></a>
The timestamp that represents when this continuous export was stopped.
Type: Timestamp
Required: No

## See Also
<a name="API_ContinuousExportDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/ContinuousExportDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/ContinuousExportDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/ContinuousExportDescription)
