---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateStopConditionInput.html
---

# CreateExperimentTemplateStopConditionInput
<a name="API_CreateExperimentTemplateStopConditionInput"></a>

Specifies a stop condition for an experiment template.

## Contents
<a name="API_CreateExperimentTemplateStopConditionInput_Contents"></a>

 ** source **   <a name="fis-Type-CreateExperimentTemplateStopConditionInput-source"></a>
The source for the stop condition. Specify `aws:cloudwatch:alarm` if the stop condition is defined by a CloudWatch alarm. Specify `none` if there is no stop condition.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: Yes

 ** value **   <a name="fis-Type-CreateExperimentTemplateStopConditionInput-value"></a>
The Amazon Resource Name (ARN) of the CloudWatch alarm. This is required if the source is a CloudWatch alarm.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\s\S]+`
Required: No

## See Also
<a name="API_CreateExperimentTemplateStopConditionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/CreateExperimentTemplateStopConditionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/CreateExperimentTemplateStopConditionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/CreateExperimentTemplateStopConditionInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
