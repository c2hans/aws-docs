---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunSourceEventDetail.html
---

# TestRunSourceEventDetail
<a name="API_TestRunSourceEventDetail"></a>

The payload of a test run source event. Exactly one member is set.

## Contents
<a name="API_TestRunSourceEventDetail_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** alarmStateChange **   <a name="ngresiliencehub-Type-TestRunSourceEventDetail-alarmStateChange"></a>
A CloudWatch alarm state change.
Type: [AlarmStateChangeDetail](API_AlarmStateChangeDetail.md) object
Required: No

 ** error **   <a name="ngresiliencehub-Type-TestRunSourceEventDetail-error"></a>
An error that prevented event collection from the source.
Type: [TestRunSourceEventError](API_TestRunSourceEventError.md) object
Required: No

## See Also
<a name="API_TestRunSourceEventDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunSourceEventDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunSourceEventDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunSourceEventDetail)
