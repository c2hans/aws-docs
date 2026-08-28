---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DestinationDescription.html
---

# DestinationDescription
<a name="API_DestinationDescription"></a>

Describes the destination for a Firehose stream.

## Contents
<a name="API_DestinationDescription_Contents"></a>

 ** DestinationId **   <a name="Firehose-Type-DestinationDescription-DestinationId"></a>
The ID of the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** AmazonOpenSearchServerlessDestinationDescription **   <a name="Firehose-Type-DestinationDescription-AmazonOpenSearchServerlessDestinationDescription"></a>
The destination in the Serverless offering for Amazon OpenSearch Service.
Type: [AmazonOpenSearchServerlessDestinationDescription](API_AmazonOpenSearchServerlessDestinationDescription.md) object
Required: No

 ** AmazonopensearchserviceDestinationDescription **   <a name="Firehose-Type-DestinationDescription-AmazonopensearchserviceDestinationDescription"></a>
The destination in Amazon OpenSearch Service.
Type: [AmazonopensearchserviceDestinationDescription](API_AmazonopensearchserviceDestinationDescription.md) object
Required: No

 ** ElasticsearchDestinationDescription **   <a name="Firehose-Type-DestinationDescription-ElasticsearchDestinationDescription"></a>
The destination in Amazon OpenSearch Service.
Type: [ElasticsearchDestinationDescription](API_ElasticsearchDestinationDescription.md) object
Required: No

 ** ExtendedS3DestinationDescription **   <a name="Firehose-Type-DestinationDescription-ExtendedS3DestinationDescription"></a>
The destination in Amazon S3.
Type: [ExtendedS3DestinationDescription](API_ExtendedS3DestinationDescription.md) object
Required: No

 ** HttpEndpointDestinationDescription **   <a name="Firehose-Type-DestinationDescription-HttpEndpointDestinationDescription"></a>
Describes the specified HTTP endpoint destination.
Type: [HttpEndpointDestinationDescription](API_HttpEndpointDestinationDescription.md) object
Required: No

 ** IcebergDestinationDescription **   <a name="Firehose-Type-DestinationDescription-IcebergDestinationDescription"></a>
 Describes a destination in Apache Iceberg Tables.
Type: [IcebergDestinationDescription](API_IcebergDestinationDescription.md) object
Required: No

 ** RedshiftDestinationDescription **   <a name="Firehose-Type-DestinationDescription-RedshiftDestinationDescription"></a>
The destination in Amazon Redshift.
Type: [RedshiftDestinationDescription](API_RedshiftDestinationDescription.md) object
Required: No

 ** S3DestinationDescription **   <a name="Firehose-Type-DestinationDescription-S3DestinationDescription"></a>
[Deprecated] The destination in Amazon S3.
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: No

 ** SnowflakeDestinationDescription **   <a name="Firehose-Type-DestinationDescription-SnowflakeDestinationDescription"></a>
Optional description for the destination
Type: [SnowflakeDestinationDescription](API_SnowflakeDestinationDescription.md) object
Required: No

 ** SplunkDestinationDescription **   <a name="Firehose-Type-DestinationDescription-SplunkDestinationDescription"></a>
The destination in Splunk.
Type: [SplunkDestinationDescription](API_SplunkDestinationDescription.md) object
Required: No

## See Also
<a name="API_DestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DestinationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
