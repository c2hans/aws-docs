---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Ingestion.html
---

# Ingestion
<a name="API_Ingestion"></a>

Information about the SPICE ingestion for a dataset.

## Contents
<a name="API_Ingestion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-Ingestion-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: Yes

 ** CreatedTime **   <a name="QS-Type-Ingestion-CreatedTime"></a>
The time that this ingestion started.
Type: Timestamp
Required: Yes

 ** IngestionStatus **   <a name="QS-Type-Ingestion-IngestionStatus"></a>
Ingestion status.
Type: String
Valid Values: `INITIALIZED | QUEUED | RUNNING | FAILED | COMPLETED | CANCELLED`
Required: Yes

 ** ErrorInfo **   <a name="QS-Type-Ingestion-ErrorInfo"></a>
Error information for this ingestion.
Type: [ErrorInfo](API_ErrorInfo.md) object
Required: No

 ** IngestionId **   <a name="QS-Type-Ingestion-IngestionId"></a>
Ingestion ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** IngestionSizeInBytes **   <a name="QS-Type-Ingestion-IngestionSizeInBytes"></a>
The size of the data ingested, in bytes.
Type: Long
Required: No

 ** IngestionTimeInSeconds **   <a name="QS-Type-Ingestion-IngestionTimeInSeconds"></a>
The time that this ingestion took, measured in seconds.
Type: Long
Required: No

 ** QueueInfo **   <a name="QS-Type-Ingestion-QueueInfo"></a>
Information about a queued dataset SPICE ingestion.
Type: [QueueInfo](API_QueueInfo.md) object
Required: No

 ** RequestSource **   <a name="QS-Type-Ingestion-RequestSource"></a>
Event source for this ingestion.
Type: String
Valid Values: `MANUAL | SCHEDULED`
Required: No

 ** RequestType **   <a name="QS-Type-Ingestion-RequestType"></a>
Type of this ingestion.
Type: String
Valid Values: `INITIAL_INGESTION | EDIT | INCREMENTAL_REFRESH | FULL_REFRESH`
Required: No

 ** RowInfo **   <a name="QS-Type-Ingestion-RowInfo"></a>
Information about rows for a data set SPICE ingestion.
Type: [RowInfo](API_RowInfo.md) object
Required: No

## See Also
<a name="API_Ingestion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Ingestion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Ingestion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Ingestion)
