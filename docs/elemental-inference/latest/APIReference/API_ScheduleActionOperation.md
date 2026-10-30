---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ScheduleActionOperation.html
---

# ScheduleActionOperation
<a name="API_ScheduleActionOperation"></a>

Holds one typed configuration change that a schedule action makes to a feed. Each operation must contain exactly one property.

## Contents
<a name="API_ScheduleActionOperation_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** removeClippingDataSourceConfiguration **   <a name="elementalinference-Type-ScheduleActionOperation-removeClippingDataSourceConfiguration"></a>
The operation type that removes the game from an event clipping output.
Type: [RemoveClippingDataSourceConfiguration](API_RemoveClippingDataSourceConfiguration.md) object
Required: No

 ** updateClippingDataSourceConfiguration **   <a name="elementalinference-Type-ScheduleActionOperation-updateClippingDataSourceConfiguration"></a>
The operation type that attaches a game to an event clipping output.
Type: [UpdateClippingDataSourceConfiguration](API_UpdateClippingDataSourceConfiguration.md) object
Required: No

 ** updateOutputStatus **   <a name="elementalinference-Type-ScheduleActionOperation-updateOutputStatus"></a>
The operation type that enables or disables an output.
Type: [UpdateOutputStatus](API_UpdateOutputStatus.md) object
Required: No

## See Also
<a name="API_ScheduleActionOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ScheduleActionOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ScheduleActionOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ScheduleActionOperation)
