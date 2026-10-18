---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectionRuleRuntimeMonitoringDetails.html
---

# DetectionRuleRuntimeMonitoringDetails
<a name="API_DetectionRuleRuntimeMonitoringDetails"></a>

Contains Runtime Monitoring-specific details for a custom detection rule.

## Contents
<a name="API_DetectionRuleRuntimeMonitoringDetails_Contents"></a>

 ** platforms **   <a name="guardduty-Type-DetectionRuleRuntimeMonitoringDetails-platforms"></a>
The platforms on which the rule can run. The presence of a platform member indicates that the rule is supported on that platform; the absence of a member indicates that the rule cannot run on that platform at any agent version.
Type: [DetectionRuleRuntimePlatforms](API_DetectionRuleRuntimePlatforms.md) object
Required: No

## See Also
<a name="API_DetectionRuleRuntimeMonitoringDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectionRuleRuntimeMonitoringDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectionRuleRuntimeMonitoringDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectionRuleRuntimeMonitoringDetails)
