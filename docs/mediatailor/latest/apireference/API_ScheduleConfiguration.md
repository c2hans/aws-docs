---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ScheduleConfiguration.html
---

# ScheduleConfiguration
<a name="API_ScheduleConfiguration"></a>

Schedule configuration parameters. A channel must be stopped before changes can be made to the schedule.

## Contents
<a name="API_ScheduleConfiguration_Contents"></a>

 ** Transition **   <a name="mediatailor-Type-ScheduleConfiguration-Transition"></a>
Program transition configurations.
Type: [Transition](API_Transition.md) object
Required: Yes

 ** ClipRange **   <a name="mediatailor-Type-ScheduleConfiguration-ClipRange"></a>
Program clip range configuration.
Type: [ClipRange](API_ClipRange.md) object
Required: No

## See Also
<a name="API_ScheduleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ScheduleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ScheduleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ScheduleConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
