---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_RedshiftDestinationDescription.html
---

# RedshiftDestinationDescription
<a name="API_RedshiftDestinationDescription"></a>

Describes a destination in Amazon Redshift.

## Contents
<a name="API_RedshiftDestinationDescription_Contents"></a>

 ** ClusterJDBCURL **   <a name="Firehose-Type-RedshiftDestinationDescription-ClusterJDBCURL"></a>
The database connection string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `jdbc:(redshift|postgresql)://((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+(redshift(-serverless)?)\.([a-zA-Z0-9\.\-]+):\d{1,5}/[a-zA-Z0-9_$-]+`
Required: Yes

 ** CopyCommand **   <a name="Firehose-Type-RedshiftDestinationDescription-CopyCommand"></a>
The `COPY` command.
Type: [CopyCommand](API_CopyCommand.md) object
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-RedshiftDestinationDescription-RoleARN"></a>
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** S3DestinationDescription **   <a name="Firehose-Type-RedshiftDestinationDescription-S3DestinationDescription"></a>
The Amazon S3 destination.
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: Yes

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-RedshiftDestinationDescription-CloudWatchLoggingOptions"></a>
The Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-RedshiftDestinationDescription-ProcessingConfiguration"></a>
The data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-RedshiftDestinationDescription-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
Type: [RedshiftRetryOptions](API_RedshiftRetryOptions.md) object
Required: No

 ** S3BackupDescription **   <a name="Firehose-Type-RedshiftDestinationDescription-S3BackupDescription"></a>
The configuration for backup in Amazon S3.
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-RedshiftDestinationDescription-S3BackupMode"></a>
The Amazon S3 backup mode.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** SecretsManagerConfiguration **   <a name="Firehose-Type-RedshiftDestinationDescription-SecretsManagerConfiguration"></a>
 The configuration that defines how you access secrets for Amazon Redshift.
Type: [SecretsManagerConfiguration](API_SecretsManagerConfiguration.md) object
Required: No

 ** Username **   <a name="Firehose-Type-RedshiftDestinationDescription-Username"></a>
The name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: No

## See Also
<a name="API_RedshiftDestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/RedshiftDestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/RedshiftDestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/RedshiftDestinationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
