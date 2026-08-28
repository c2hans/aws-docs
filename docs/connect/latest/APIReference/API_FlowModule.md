---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_FlowModule.html
---

# FlowModule
<a name="API_FlowModule"></a>

 A list of Flow Modules an AI Agent can invoke as a tool

## Contents
<a name="API_FlowModule_Contents"></a>

 ** FlowModuleId **   <a name="connect-Type-FlowModule-FlowModuleId"></a>
 If of Flow Modules invocable as tool
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Type **   <a name="connect-Type-FlowModule-Type"></a>
 Only Type we support is MCP.
Type: String
Valid Values: `MCP`
Required: No

## See Also
<a name="API_FlowModule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/FlowModule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/FlowModule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/FlowModule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
