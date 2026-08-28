---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/API_SolutionUpdateConfig.html
---

# SolutionUpdateConfig
<a name="API_SolutionUpdateConfig"></a>

The configuration details of the solution update.

## Contents
<a name="API_SolutionUpdateConfig_Contents"></a>

 ** autoTrainingConfig **   <a name="personalize-Type-SolutionUpdateConfig-autoTrainingConfig"></a>
The automatic training configuration to use when `performAutoTraining` is true.
Type: [AutoTrainingConfig](API_AutoTrainingConfig.md) object
Required: No

 ** eventsConfig **   <a name="personalize-Type-SolutionUpdateConfig-eventsConfig"></a>
Describes the configuration of an event, which includes a list of event parameters. You can specify up to 10 event parameters. Events are used in solution creation.
Type: [EventsConfig](API_EventsConfig.md) object
Required: No

## See Also
<a name="API_SolutionUpdateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/SolutionUpdateConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/SolutionUpdateConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/SolutionUpdateConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
