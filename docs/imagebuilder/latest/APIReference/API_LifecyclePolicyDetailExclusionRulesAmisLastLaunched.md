---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicyDetailExclusionRulesAmisLastLaunched.html
---

# LifecyclePolicyDetailExclusionRulesAmisLastLaunched
<a name="API_LifecyclePolicyDetailExclusionRulesAmisLastLaunched"></a>

Defines criteria to exclude AMIs from lifecycle actions based on the last time they were used to launch an instance.

## Contents
<a name="API_LifecyclePolicyDetailExclusionRulesAmisLastLaunched_Contents"></a>

 ** unit **   <a name="imagebuilder-Type-LifecyclePolicyDetailExclusionRulesAmisLastLaunched-unit"></a>
Defines the unit of time that the lifecycle policy uses to calculate elapsed time since the last instance launched from the AMI. For example: days, weeks, months, or years.
Type: String
Valid Values: `DAYS | WEEKS | MONTHS | YEARS`
Required: Yes

 ** value **   <a name="imagebuilder-Type-LifecyclePolicyDetailExclusionRulesAmisLastLaunched-value"></a>
The integer number of units for the time period. For example `6` (months).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 365.
Required: Yes

## See Also
<a name="API_LifecyclePolicyDetailExclusionRulesAmisLastLaunched_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecyclePolicyDetailExclusionRulesAmisLastLaunched)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecyclePolicyDetailExclusionRulesAmisLastLaunched)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecyclePolicyDetailExclusionRulesAmisLastLaunched)
