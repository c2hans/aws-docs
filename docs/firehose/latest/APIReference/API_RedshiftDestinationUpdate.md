---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_RedshiftDestinationUpdate.html
---

# RedshiftDestinationUpdate
<a name="API_RedshiftDestinationUpdate"></a>

Describes an update for a destination in Amazon Redshift.

## Contents
<a name="API_RedshiftDestinationUpdate_Contents"></a>

 ** CloudWatchLoggingOptions **   <a name="Firehose-Type-RedshiftDestinationUpdate-CloudWatchLoggingOptions"></a>
The Amazon CloudWatch logging options for your Firehose stream.
Type: [CloudWatchLoggingOptions](API_CloudWatchLoggingOptions.md) object
Required: No

 ** ClusterJDBCURL **   <a name="Firehose-Type-RedshiftDestinationUpdate-ClusterJDBCURL"></a>
The database connection string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `jdbc:(redshift|postgresql)://((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+(redshift(-serverless)?)\.([a-zA-Z0-9\.\-]+):\d{1,5}/[a-zA-Z0-9_$-]+`
Required: No

 ** CopyCommand **   <a name="Firehose-Type-RedshiftDestinationUpdate-CopyCommand"></a>
The `COPY` command.
Type: [CopyCommand](API_CopyCommand.md) object
Required: No

 ** Password **   <a name="Firehose-Type-RedshiftDestinationUpdate-Password"></a>
The user password.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 512.
Pattern: `.*`
Required: No

 ** ProcessingConfiguration **   <a name="Firehose-Type-RedshiftDestinationUpdate-ProcessingConfiguration"></a>
The data processing configuration.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
Required: No

 ** RetryOptions **   <a name="Firehose-Type-RedshiftDestinationUpdate-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
Type: [RedshiftRetryOptions](API_RedshiftRetryOptions.md) object
Required: No

 ** RoleARN **   <a name="Firehose-Type-RedshiftDestinationUpdate-RoleARN"></a>
The Amazon Resource Name (ARN) of the AWS credentials. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** S3BackupMode **   <a name="Firehose-Type-RedshiftDestinationUpdate-S3BackupMode"></a>
You can update a Firehose stream to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the Firehose stream to disable it.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** S3BackupUpdate **   <a name="Firehose-Type-RedshiftDestinationUpdate-S3BackupUpdate"></a>
The Amazon S3 destination for backup.
Type: [S3DestinationUpdate](API_S3DestinationUpdate.md) object
Required: No

 ** S3Update **   <a name="Firehose-Type-RedshiftDestinationUpdate-S3Update"></a>
The Amazon S3 destination.
The compression formats `SNAPPY` or `ZIP` cannot be specified in `RedshiftDestinationUpdate.S3Update` because the Amazon Redshift `COPY` operation that reads from the S3 bucket doesn't support these compression formats.
Type: [S3DestinationUpdate](API_S3DestinationUpdate.md) object
Required: No

 ** SecretsManagerConfiguration **   <a name="Firehose-Type-RedshiftDestinationUpdate-SecretsManagerConfiguration"></a>
 The configuration that defines how you access secrets for Amazon Redshift.
Type: [SecretsManagerConfiguration](API_SecretsManagerConfiguration.md) object
Required: No

 ** Username **   <a name="Firehose-Type-RedshiftDestinationUpdate-Username"></a>
The name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: No

## See Also
<a name="API_RedshiftDestinationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/RedshiftDestinationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/RedshiftDestinationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/RedshiftDestinationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
