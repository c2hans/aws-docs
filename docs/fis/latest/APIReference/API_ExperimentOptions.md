---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentOptions.html
---

# ExperimentOptions
<a name="API_ExperimentOptions"></a>

Describes the options for an experiment.

## Contents
<a name="API_ExperimentOptions_Contents"></a>

 ** accountTargeting **   <a name="fis-Type-ExperimentOptions-accountTargeting"></a>
The account targeting setting for an experiment.
Type: String
Valid Values: `single-account | multi-account`
Required: No

 ** actionsMode **   <a name="fis-Type-ExperimentOptions-actionsMode"></a>
The actions mode of the experiment that is set from the StartExperiment API command.
Type: String
Valid Values: `skip-all | run-all`
Required: No

 ** emptyTargetResolutionMode **   <a name="fis-Type-ExperimentOptions-emptyTargetResolutionMode"></a>
The empty target resolution mode for an experiment.
Type: String
Valid Values: `fail | skip`
Required: No

## See Also
<a name="API_ExperimentOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
