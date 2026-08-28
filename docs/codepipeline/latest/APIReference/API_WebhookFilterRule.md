---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html
---

# WebhookFilterRule
<a name="API_WebhookFilterRule"></a>

The event criteria that specify when a webhook notification is sent to your URL.

## Contents
<a name="API_WebhookFilterRule_Contents"></a>

 ** jsonPath **   <a name="CodePipeline-Type-WebhookFilterRule-jsonPath"></a>
A JsonPath expression that is applied to the body/payload of the webhook. The value selected by the JsonPath expression must match the value specified in the `MatchEquals` field. Otherwise, the request is ignored. For more information, see [Java JsonPath implementation](https://github.com/json-path/JsonPath) in GitHub.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

 ** matchEquals **   <a name="CodePipeline-Type-WebhookFilterRule-matchEquals"></a>
The value selected by the `JsonPath` expression must match what is supplied in the `MatchEquals` field. Otherwise, the request is ignored. Properties from the target action configuration can be included as placeholders in this value by surrounding the action configuration key with curly brackets. For example, if the value supplied here is "refs/heads/{Branch}" and the target action has an action configuration property called "Branch" with a value of "main", the `MatchEquals` value is evaluated as "refs/heads/main". For a list of action configuration properties for built-in action types, see [Pipeline Structure Reference Action Requirements](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

## See Also
<a name="API_WebhookFilterRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/WebhookFilterRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/WebhookFilterRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/WebhookFilterRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
