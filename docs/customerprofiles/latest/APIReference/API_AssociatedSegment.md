---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_AssociatedSegment.html
---

# AssociatedSegment
<a name="API_connect-customer-profiles_AssociatedSegment"></a>

Represents a segment associated with a membership event stream.

## Contents
<a name="API_connect-customer-profiles_AssociatedSegment_Contents"></a>

 ** Message **   <a name="connect-Type-connect-customer-profiles_AssociatedSegment-Message"></a>
An optional message providing context, such as a failure reason.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** SegmentName **   <a name="connect-Type-connect-customer-profiles_AssociatedSegment-SegmentName"></a>
The unique name of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** Status **   <a name="connect-Type-connect-customer-profiles_AssociatedSegment-Status"></a>
The subscription status of the segment. The following are valid values:
+  **STARTING**: The segment is being prepared to publish membership events.
+  **RUNNING**: The segment is actively publishing membership events to the stream.
+  **STOPPED**: The segment has stopped publishing membership events.
+  **FAILED**: The segment failed to publish membership events.
Type: String
Valid Values: `STARTING | RUNNING | STOPPED | FAILED`
Required: No

## See Also
<a name="API_connect-customer-profiles_AssociatedSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AssociatedSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AssociatedSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AssociatedSegment)
