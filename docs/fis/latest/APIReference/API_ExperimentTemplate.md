---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplate.html
---

# ExperimentTemplate
<a name="API_ExperimentTemplate"></a>

Describes an experiment template.

## Contents
<a name="API_ExperimentTemplate_Contents"></a>

 ** actions **   <a name="fis-Type-ExperimentTemplate-actions"></a>
The actions for the experiment.
Type: String to [ExperimentTemplateAction](API_ExperimentTemplateAction.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: No

 ** arn **   <a name="fis-Type-ExperimentTemplate-arn"></a>
The Amazon Resource Name (ARN) of the experiment template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** creationTime **   <a name="fis-Type-ExperimentTemplate-creationTime"></a>
The time the experiment template was created.
Type: Timestamp
Required: No

 ** description **   <a name="fis-Type-ExperimentTemplate-description"></a>
The description for the experiment template.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** experimentOptions **   <a name="fis-Type-ExperimentTemplate-experimentOptions"></a>
The experiment options for an experiment template.
Type: [ExperimentTemplateExperimentOptions](API_ExperimentTemplateExperimentOptions.md) object
Required: No

 ** experimentReportConfiguration **   <a name="fis-Type-ExperimentTemplate-experimentReportConfiguration"></a>
Describes the report configuration for the experiment template.
Type: [ExperimentTemplateReportConfiguration](API_ExperimentTemplateReportConfiguration.md) object
Required: No

 ** id **   <a name="fis-Type-ExperimentTemplate-id"></a>
The ID of the experiment template.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** lastUpdateTime **   <a name="fis-Type-ExperimentTemplate-lastUpdateTime"></a>
The time the experiment template was last updated.
Type: Timestamp
Required: No

 ** logConfiguration **   <a name="fis-Type-ExperimentTemplate-logConfiguration"></a>
The configuration for experiment logging.
Type: [ExperimentTemplateLogConfiguration](API_ExperimentTemplateLogConfiguration.md) object
Required: No

 ** roleArn **   <a name="fis-Type-ExperimentTemplate-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** stopConditions **   <a name="fis-Type-ExperimentTemplate-stopConditions"></a>
The stop conditions for the experiment.
Type: Array of [ExperimentTemplateStopCondition](API_ExperimentTemplateStopCondition.md) objects
Required: No

 ** tags **   <a name="fis-Type-ExperimentTemplate-tags"></a>
The tags for the experiment template.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

 ** targetAccountConfigurationsCount **   <a name="fis-Type-ExperimentTemplate-targetAccountConfigurationsCount"></a>
The count of target account configurations for the experiment template.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** targets **   <a name="fis-Type-ExperimentTemplate-targets"></a>
The targets for the experiment.
Type: String to [ExperimentTemplateTarget](API_ExperimentTemplateTarget.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTemplate)
