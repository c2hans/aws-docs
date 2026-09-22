---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Schedule.html
---

# Schedule
<a name="API_Schedule"></a>

A schedule configures when and how often a pipeline will automatically create a new image.

## Contents
<a name="API_Schedule_Contents"></a>

 ** autoDisablePolicy **   <a name="imagebuilder-Type-Schedule-autoDisablePolicy"></a>
The policy that configures when Image Builder should automatically disable a pipeline that is failing.
Type: [AutoDisablePolicy](API_AutoDisablePolicy.md) object
Required: No

 ** pipelineExecutionStartCondition **   <a name="imagebuilder-Type-Schedule-pipelineExecutionStartCondition"></a>
The start condition configures when the pipeline should trigger a new image build, as follows. If no value is set Image Builder defaults to `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`.
+  `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE` (default) – When you use semantic version filters on the base image or components in your image recipe, EC2 Image Builder builds a new image only when there are new versions of the base image or components in your recipe that match the filter.
**Note**
For semantic version syntax, see [CreateComponent](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html).
+  `EXPRESSION_MATCH_ONLY` – This condition builds a new image every time the CRON expression matches the current time.
If the recipe references its base image through an AWS Systems Manager Parameter Store parameter, a change in the parameter's value also counts as an available dependency update.
Type: String
Valid Values: `EXPRESSION_MATCH_ONLY | EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`
Required: No

 ** scheduleExpression **   <a name="imagebuilder-Type-Schedule-scheduleExpression"></a>
The expression determines how often EC2 Image Builder evaluates your `pipelineExecutionStartCondition`. You can specify a cron expression, or a rate expression such as `rate(1 day)`.
For information on how to format a cron expression in Image Builder, see [Use cron expressions in EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-cron.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** timezone **   <a name="imagebuilder-Type-Schedule-timezone"></a>
The timezone that applies to the scheduling expression. Specify a value in [IANA timezone format](https://www.joda.org/joda-time/timezones.html), for example `Etc/UTC` or `America/Los_Angeles`. If not specified, this defaults to UTC.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[a-zA-Z0-9]{2,}(?:\/[a-zA-Z0-9-_+]+)*`
Required: No

## See Also
<a name="API_Schedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/Schedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/Schedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/Schedule)
