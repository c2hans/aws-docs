---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_LifecycleEvent.html
---

# LifecycleEvent
<a name="API_LifecycleEvent"></a>

A lifecycle event for an AWS service version, such as end-of-support or end-of-life.

## Contents
<a name="API_LifecycleEvent_Contents"></a>

 ** date **   <a name="AWSHealth-Type-LifecycleEvent-date"></a>
The date of the lifecycle event.
Type: Timestamp
Required: No

 ** description **   <a name="AWSHealth-Type-LifecycleEvent-description"></a>
A description of the lifecycle event.
Type: String
Required: No

 ** impactRisks **   <a name="AWSHealth-Type-LifecycleEvent-impactRisks"></a>
The potential impact risks associated with this lifecycle event.
Type: Array of strings
Required: No

 ** lifecycleEventType **   <a name="AWSHealth-Type-LifecycleEvent-lifecycleEventType"></a>
The type of lifecycle event (for example, end-of-support, end-of-life).
Type: String
Required: No

 ** regions **   <a name="AWSHealth-Type-LifecycleEvent-regions"></a>
The AWS Regions affected by this lifecycle event.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `[^:/]{2,25}`
Required: No

## See Also
<a name="API_LifecycleEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/LifecycleEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/LifecycleEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/LifecycleEvent)
