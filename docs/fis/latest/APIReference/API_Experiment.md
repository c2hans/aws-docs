---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_Experiment.html
---

# Experiment
<a name="API_Experiment"></a>

Describes an experiment.

## Contents
<a name="API_Experiment_Contents"></a>

 ** actions **   <a name="fis-Type-Experiment-actions"></a>
The actions for the experiment.
Type: String to [ExperimentAction](API_ExperimentAction.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: No

 ** arn **   <a name="fis-Type-Experiment-arn"></a>
The Amazon Resource Name (ARN) of the experiment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** creationTime **   <a name="fis-Type-Experiment-creationTime"></a>
The time that the experiment was created.
Type: Timestamp
Required: No

 ** endTime **   <a name="fis-Type-Experiment-endTime"></a>
The time that the experiment ended.
Type: Timestamp
Required: No

 ** experimentOptions **   <a name="fis-Type-Experiment-experimentOptions"></a>
The experiment options for the experiment.
Type: [ExperimentOptions](API_ExperimentOptions.md) object
Required: No

 ** experimentReport **   <a name="fis-Type-Experiment-experimentReport"></a>
The experiment report for the experiment.
Type: [ExperimentReport](API_ExperimentReport.md) object
Required: No

 ** experimentReportConfiguration **   <a name="fis-Type-Experiment-experimentReportConfiguration"></a>
The experiment report configuration for the experiment.
Type: [ExperimentReportConfiguration](API_ExperimentReportConfiguration.md) object
Required: No

 ** experimentTemplateId **   <a name="fis-Type-Experiment-experimentTemplateId"></a>
The ID of the experiment template.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** id **   <a name="fis-Type-Experiment-id"></a>
The ID of the experiment.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** logConfiguration **   <a name="fis-Type-Experiment-logConfiguration"></a>
The configuration for experiment logging.
Type: [ExperimentLogConfiguration](API_ExperimentLogConfiguration.md) object
Required: No

 ** roleArn **   <a name="fis-Type-Experiment-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that grants the AWS FIS service permission to perform service actions on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** startTime **   <a name="fis-Type-Experiment-startTime"></a>
The time that the experiment started.
Type: Timestamp
Required: No

 ** state **   <a name="fis-Type-Experiment-state"></a>
The state of the experiment.
Type: [ExperimentState](API_ExperimentState.md) object
Required: No

 ** stopConditions **   <a name="fis-Type-Experiment-stopConditions"></a>
The stop conditions for the experiment.
Type: Array of [ExperimentStopCondition](API_ExperimentStopCondition.md) objects
Required: No

 ** tags **   <a name="fis-Type-Experiment-tags"></a>
The tags for the experiment.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

 ** targetAccountConfigurationsCount **   <a name="fis-Type-Experiment-targetAccountConfigurationsCount"></a>
The count of target account configurations for the experiment.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** targets **   <a name="fis-Type-Experiment-targets"></a>
The targets for the experiment.
Type: String to [ExperimentTarget](API_ExperimentTarget.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: No

## See Also
<a name="API_Experiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/Experiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/Experiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/Experiment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
