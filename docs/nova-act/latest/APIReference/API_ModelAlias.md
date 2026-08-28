---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ModelAlias.html
---

# ModelAlias
<a name="API_ModelAlias"></a>

An alias that provides a stable reference to a model version.

## Contents
<a name="API_ModelAlias_Contents"></a>

 ** aliasName **   <a name="novaact-Type-ModelAlias-aliasName"></a>
The name of the model alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** latestModelId **   <a name="novaact-Type-ModelAlias-latestModelId"></a>
The model ID that this alias currently points to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** resolvedModelId **   <a name="novaact-Type-ModelAlias-resolvedModelId"></a>
The resolved model ID after alias resolution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_ModelAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/nova-act-2025-08-22/ModelAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/nova-act-2025-08-22/ModelAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ModelAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova Act. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova-act` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
