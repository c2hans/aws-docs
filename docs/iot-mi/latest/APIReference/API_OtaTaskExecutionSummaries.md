---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_OtaTaskExecutionSummaries.html
---

# OtaTaskExecutionSummaries
<a name="API_OtaTaskExecutionSummaries"></a>

Structure representing one execution summary.

## Contents
<a name="API_OtaTaskExecutionSummaries_Contents"></a>

 ** ManagedThingId **   <a name="managedintegrations-Type-OtaTaskExecutionSummaries-ManagedThingId"></a>
The id of a managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: No

 ** TaskExecutionSummary **   <a name="managedintegrations-Type-OtaTaskExecutionSummaries-TaskExecutionSummary"></a>
Structure representing one over-the-air (OTA) task execution summary
Type: [OtaTaskExecutionSummary](API_OtaTaskExecutionSummary.md) object
Required: No

## See Also
<a name="API_OtaTaskExecutionSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/OtaTaskExecutionSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/OtaTaskExecutionSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/OtaTaskExecutionSummaries)
