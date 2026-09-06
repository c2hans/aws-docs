---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_ActivitySummary.html
---

# ActivitySummary
<a name="API_freetier_ActivitySummary"></a>

 The summary of activities.

## Contents
<a name="API_freetier_ActivitySummary_Contents"></a>

 ** activityId **   <a name="awscostmanagement-Type-freetier_ActivitySummary-activityId"></a>
 A unique identifier that identifies the activity.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** reward **   <a name="awscostmanagement-Type-freetier_ActivitySummary-reward"></a>
 The reward for the activity.
Type: [ActivityReward](API_freetier_ActivityReward.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** status **   <a name="awscostmanagement-Type-freetier_ActivitySummary-status"></a>
 The current status of the activity.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | EXPIRING`
Required: Yes

 ** title **   <a name="awscostmanagement-Type-freetier_ActivitySummary-title"></a>
 The title of the activity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_freetier_ActivitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/freetier-2023-09-07/ActivitySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/freetier-2023-09-07/ActivitySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/freetier-2023-09-07/ActivitySummary)
