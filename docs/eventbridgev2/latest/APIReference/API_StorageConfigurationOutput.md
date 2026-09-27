---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_StorageConfigurationOutput.html
---

# StorageConfigurationOutput
<a name="API_StorageConfigurationOutput"></a>

Event storage configuration of an event bus, as returned on reads.

## Contents
<a name="API_StorageConfigurationOutput_Contents"></a>

 ** RetentionPeriodInDays **   <a name="eventbridgev2-Type-StorageConfigurationOutput-RetentionPeriodInDays"></a>
Number of days events are retained on the event bus.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 365.
Required: No

 ** RetentionWindowStartTime **   <a name="eventbridgev2-Type-StorageConfigurationOutput-RetentionWindowStartTime"></a>
The earliest point in time from which stored events are available. Events older than this have expired from retention.
Type: Timestamp
Required: No

## See Also
<a name="API_StorageConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/StorageConfigurationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/StorageConfigurationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/StorageConfigurationOutput)
