---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RdsLoginActivity.html
---

# RdsLoginActivity
<a name="API_RdsLoginActivity"></a>

Contains details about login activity on an Amazon RDS database.

## Contents
<a name="API_RdsLoginActivity_Contents"></a>

 ** activityWindow **   <a name="guardduty-Type-RdsLoginActivity-activityWindow"></a>
The time range of the login activity.
Type: [ActivityWindow](API_ActivityWindow.md) object
Required: No

 ** anomalyContext **   <a name="guardduty-Type-RdsLoginActivity-anomalyContext"></a>
An explanation of how the login activity deviates from normal behavior.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** enrichment **   <a name="guardduty-Type-RdsLoginActivity-enrichment"></a>
Additional context about the login activity, such as geolocation information.
Type: [Enrichment](API_Enrichment.md) object
Required: No

 ** loginCount **   <a name="guardduty-Type-RdsLoginActivity-loginCount"></a>
The number of login attempts.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** outcome **   <a name="guardduty-Type-RdsLoginActivity-outcome"></a>
The outcome of the login attempts.
Type: String
Required: No

 ** rate **   <a name="guardduty-Type-RdsLoginActivity-rate"></a>
The rate of the login attempts.
Type: String
Required: No

## See Also
<a name="API_RdsLoginActivity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RdsLoginActivity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RdsLoginActivity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RdsLoginActivity)
