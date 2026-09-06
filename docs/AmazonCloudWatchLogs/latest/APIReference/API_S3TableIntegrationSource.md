---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_S3TableIntegrationSource.html
---

# S3TableIntegrationSource
<a name="API_S3TableIntegrationSource"></a>

Represents a data source association with an S3 Table Integration, including its status and metadata.

## Contents
<a name="API_S3TableIntegrationSource_Contents"></a>

 ** createdTimeStamp **   <a name="CWL-Type-S3TableIntegrationSource-createdTimeStamp"></a>
The timestamp when the data source association was created.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** dataSource **   <a name="CWL-Type-S3TableIntegrationSource-dataSource"></a>
The data source associated with the S3 Table Integration.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** identifier **   <a name="CWL-Type-S3TableIntegrationSource-identifier"></a>
The unique identifier for this data source association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** parentSourceIdentifier **   <a name="CWL-Type-S3TableIntegrationSource-parentSourceIdentifier"></a>
The identifier of the parent data source for this association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** status **   <a name="CWL-Type-S3TableIntegrationSource-status"></a>
The current status of the data source association.
Type: String
Valid Values: `ACTIVE | UNHEALTHY | FAILED | DATA_SOURCE_DELETE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="CWL-Type-S3TableIntegrationSource-statusReason"></a>
Additional information about the status of the data source association.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_S3TableIntegrationSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/S3TableIntegrationSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/S3TableIntegrationSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/S3TableIntegrationSource)
