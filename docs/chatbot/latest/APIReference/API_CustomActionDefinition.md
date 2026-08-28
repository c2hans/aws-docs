---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CustomActionDefinition.html
---

# CustomActionDefinition
<a name="API_CustomActionDefinition"></a>

The definition of the command to run when invoked as an alias or as an action button.

## Contents
<a name="API_CustomActionDefinition_Contents"></a>

 ** CommandText **   <a name="qdevinchatapps-Type-CustomActionDefinition-CommandText"></a>
The command string to run which may include variables by prefixing with a dollar sign ($).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\S\s]+`
Required: Yes

## See Also
<a name="API_CustomActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/CustomActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/CustomActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/CustomActionDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
