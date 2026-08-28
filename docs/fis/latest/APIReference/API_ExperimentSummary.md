---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentSummary.html
---

# ExperimentSummary
<a name="API_ExperimentSummary"></a>

Provides a summary of an experiment.

## Contents
<a name="API_ExperimentSummary_Contents"></a>

 ** arn **   <a name="fis-Type-ExperimentSummary-arn"></a>
The Amazon Resource Name (ARN) of the experiment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** creationTime **   <a name="fis-Type-ExperimentSummary-creationTime"></a>
The time that the experiment was created.
Type: Timestamp
Required: No

 ** experimentOptions **   <a name="fis-Type-ExperimentSummary-experimentOptions"></a>
The experiment options for the experiment.
Type: [ExperimentOptions](API_ExperimentOptions.md) object
Required: No

 ** experimentTemplateId **   <a name="fis-Type-ExperimentSummary-experimentTemplateId"></a>
The ID of the experiment template.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** id **   <a name="fis-Type-ExperimentSummary-id"></a>
The ID of the experiment.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

 ** state **   <a name="fis-Type-ExperimentSummary-state"></a>
The state of the experiment.
Type: [ExperimentState](API_ExperimentState.md) object
Required: No

 ** tags **   <a name="fis-Type-ExperimentSummary-tags"></a>
The tags for the experiment.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_ExperimentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
