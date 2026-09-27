---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PointInTimeConfiguration.html
---

# PointInTimeConfiguration
<a name="API_PointInTimeConfiguration"></a>

Point-in-time configuration for a subscriber. Only applicable when StartingPosition is POINT\_IN\_TIME.

## Contents
<a name="API_PointInTimeConfiguration_Contents"></a>

 ** PointType **   <a name="eventbridgev2-Type-PointInTimeConfiguration-PointType"></a>
Whether to start from the horizon or a specific timestamp.
Type: String
Valid Values: `HORIZON | TIMESTAMP`
Required: Yes

 ** EndPoint **   <a name="eventbridgev2-Type-PointInTimeConfiguration-EndPoint"></a>
Timestamp to stop at. Optional.
Type: Timestamp
Required: No

 ** StartingPoint **   <a name="eventbridgev2-Type-PointInTimeConfiguration-StartingPoint"></a>
Timestamp to start from. Required when PointType is TIMESTAMP.
Type: Timestamp
Required: No

## See Also
<a name="API_PointInTimeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PointInTimeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PointInTimeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PointInTimeConfiguration)
