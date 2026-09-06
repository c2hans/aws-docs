---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_FailedDataSegmentDisassociation.html
---

# FailedDataSegmentDisassociation
<a name="API_FailedDataSegmentDisassociation"></a>

Contains error information for a data segment disassociation that failed.

## Contents
<a name="API_FailedDataSegmentDisassociation_Contents"></a>

 ** endTimestamp **   <a name="iotsitewise-Type-FailedDataSegmentDisassociation-endTimestamp"></a>
The nanosecond-precision end time of the data segment.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** errorCode **   <a name="iotsitewise-Type-FailedDataSegmentDisassociation-errorCode"></a>
The error code for the failed disassociation.
Type: String
Valid Values: `INTERNAL_FAILURE | VALIDATION_ERROR | RESOURCE_NOT_FOUND | LIMIT_EXCEEDED | CONFLICTING_OPERATION`
Required: Yes

 ** errorMessage **   <a name="iotsitewise-Type-FailedDataSegmentDisassociation-errorMessage"></a>
The error message for the failed disassociation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** sourceDatasetId **   <a name="iotsitewise-Type-FailedDataSegmentDisassociation-sourceDatasetId"></a>
The ID of the source dataset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** startTimestamp **   <a name="iotsitewise-Type-FailedDataSegmentDisassociation-startTimestamp"></a>
The nanosecond-precision start time of the data segment.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** timeSeriesId **   <a name="iotsitewise-Type-FailedDataSegmentDisassociation-timeSeriesId"></a>
The ID of the time series.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: Yes

## See Also
<a name="API_FailedDataSegmentDisassociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/FailedDataSegmentDisassociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/FailedDataSegmentDisassociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/FailedDataSegmentDisassociation)
