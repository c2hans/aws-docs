---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_RedshiftConnectorProfileProperties.html
---

# RedshiftConnectorProfileProperties
<a name="API_RedshiftConnectorProfileProperties"></a>

 The connector-specific profile properties when using Amazon Redshift.

## Contents
<a name="API_RedshiftConnectorProfileProperties_Contents"></a>

 ** bucketName **   <a name="appflow-Type-RedshiftConnectorProfileProperties-bucketName"></a>
 A name for the associated Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `\S+`
Required: Yes

 ** roleArn **   <a name="appflow-Type-RedshiftConnectorProfileProperties-roleArn"></a>
 The Amazon Resource Name (ARN) of IAM role that grants Amazon Redshift read-only access to Amazon S3. For more information, and for the polices that you attach to this role, see [Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3](https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#redshift-access-s3).
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:iam:.*:[0-9]+:.*`
Required: Yes

 ** bucketPrefix **   <a name="appflow-Type-RedshiftConnectorProfileProperties-bucketPrefix"></a>
 The object key for the destination bucket in which Amazon AppFlow places the files.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** clusterIdentifier **   <a name="appflow-Type-RedshiftConnectorProfileProperties-clusterIdentifier"></a>
The unique ID that's assigned to an Amazon Redshift cluster.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** dataApiRoleArn **   <a name="appflow-Type-RedshiftConnectorProfileProperties-dataApiRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that permits Amazon AppFlow to access your Amazon Redshift database through the Data API. For more information, and for the polices that you attach to this role, see [Allow Amazon AppFlow to access Amazon Redshift databases with the Data API](https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#access-redshift).
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:iam:.*:[0-9]+:.*`
Required: No

 ** databaseName **   <a name="appflow-Type-RedshiftConnectorProfileProperties-databaseName"></a>
The name of an Amazon Redshift database.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** databaseUrl **   <a name="appflow-Type-RedshiftConnectorProfileProperties-databaseUrl"></a>
 The JDBC URL of the Amazon Redshift cluster.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** isRedshiftServerless **   <a name="appflow-Type-RedshiftConnectorProfileProperties-isRedshiftServerless"></a>
Indicates whether the connector profile defines a connection to an Amazon Redshift Serverless data warehouse.
Type: Boolean
Required: No

 ** workgroupName **   <a name="appflow-Type-RedshiftConnectorProfileProperties-workgroupName"></a>
The name of an Amazon Redshift workgroup.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

## See Also
<a name="API_RedshiftConnectorProfileProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/RedshiftConnectorProfileProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/RedshiftConnectorProfileProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/RedshiftConnectorProfileProperties)
