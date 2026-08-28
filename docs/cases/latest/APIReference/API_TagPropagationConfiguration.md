---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_TagPropagationConfiguration.html
---

# TagPropagationConfiguration
<a name="API_connect-cases_TagPropagationConfiguration"></a>

Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.

## Contents
<a name="API_connect-cases_TagPropagationConfiguration_Contents"></a>

 ** resourceType **   <a name="connect-Type-connect-cases_TagPropagationConfiguration-resourceType"></a>
Supported resource types for tag propagation. Determines which resources will receive automatically propagated tags.
Type: String
Valid Values: `Cases`
Required: Yes

 ** tagMap **   <a name="connect-Type-connect-cases_TagPropagationConfiguration-tagMap"></a>
The tags that will be applied to the created resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?![aA][wW][sS]:)[a-zA-Z0-9 _.:/=+\-@]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([a-zA-Z0-9 _.:/=+\-@]*)`
Required: Yes

## See Also
<a name="API_connect-cases_TagPropagationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/TagPropagationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/TagPropagationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/TagPropagationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
