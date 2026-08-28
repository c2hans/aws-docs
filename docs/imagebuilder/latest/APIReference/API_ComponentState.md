---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ComponentState.html
---

# ComponentState
<a name="API_ComponentState"></a>

A group of fields that describe the current status of components.

## Contents
<a name="API_ComponentState_Contents"></a>

 ** reason **   <a name="imagebuilder-Type-ComponentState-reason"></a>
Describes how or why the component changed state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** status **   <a name="imagebuilder-Type-ComponentState-status"></a>
The current state of the component.
Type: String
Valid Values: `DEPRECATED | DISABLED | ACTIVE`
Required: No

## See Also
<a name="API_ComponentState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ComponentState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ComponentState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ComponentState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
