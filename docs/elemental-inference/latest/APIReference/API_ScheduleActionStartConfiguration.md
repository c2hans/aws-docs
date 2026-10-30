---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ScheduleActionStartConfiguration.html
---

# ScheduleActionStartConfiguration
<a name="API_ScheduleActionStartConfiguration"></a>

Holds the typed start settings that determine when a schedule action runs. Currently, only fixed mode is supported.

## Contents
<a name="API_ScheduleActionStartConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fixedModeScheduleActionStartSettings **   <a name="elementalinference-Type-ScheduleActionStartConfiguration-fixedModeScheduleActionStartSettings"></a>
The start settings type for an action that runs once, at a fixed time.
Type: [FixedModeScheduleActionStartSettings](API_FixedModeScheduleActionStartSettings.md) object
Required: No

## See Also
<a name="API_ScheduleActionStartConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ScheduleActionStartConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ScheduleActionStartConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ScheduleActionStartConfiguration)
