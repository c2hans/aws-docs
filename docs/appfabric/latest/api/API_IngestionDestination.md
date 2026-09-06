---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_IngestionDestination.html
---

# IngestionDestination
<a name="API_IngestionDestination"></a>

Contains information about an ingestion destination.

## Contents
<a name="API_IngestionDestination_Contents"></a>

 ** arn **   <a name="appfabric-Type-IngestionDestination-arn"></a>
The Amazon Resource Name (ARN) of the ingestion destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** destinationConfiguration **   <a name="appfabric-Type-IngestionDestination-destinationConfiguration"></a>
Contains information about the destination of ingested data.
Type: [DestinationConfiguration](API_DestinationConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** ingestionArn **   <a name="appfabric-Type-IngestionDestination-ingestionArn"></a>
The Amazon Resource Name (ARN) of the ingestion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** processingConfiguration **   <a name="appfabric-Type-IngestionDestination-processingConfiguration"></a>
Contains information about how ingested data is processed.
Type: [ProcessingConfiguration](API_ProcessingConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="appfabric-Type-IngestionDestination-createdAt"></a>
The timestamp of when the ingestion destination was created.
Type: Timestamp
Required: No

 ** status **   <a name="appfabric-Type-IngestionDestination-status"></a>
The state of the ingestion destination.
The following states are possible:
+  `Active`: The ingestion destination is active and is ready to be used.
+  `Failed`: The ingestion destination has failed. If the ingestion destination is in this state, you should verify the ingestion destination configuration and try again.
Type: String
Valid Values: `Active | Failed`
Required: No

 ** statusReason **   <a name="appfabric-Type-IngestionDestination-statusReason"></a>
The reason for the current status of the ingestion destination.
Only present when the `status` of ingestion destination is `Failed`.
Type: String
Required: No

 ** updatedAt **   <a name="appfabric-Type-IngestionDestination-updatedAt"></a>
The timestamp of when the ingestion destination was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_IngestionDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/IngestionDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/IngestionDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/IngestionDestination)
