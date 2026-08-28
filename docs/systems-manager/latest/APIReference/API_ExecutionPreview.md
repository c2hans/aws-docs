---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ExecutionPreview.html
---

# ExecutionPreview
<a name="API_ExecutionPreview"></a>

Information about the changes that would be made if an execution were run.

## Contents
<a name="API_ExecutionPreview_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Automation **   <a name="systemsmanager-Type-ExecutionPreview-Automation"></a>
Information about the changes that would be made if an Automation workflow were run.
Type: [AutomationExecutionPreview](API_AutomationExecutionPreview.md) object
Required: No

## See Also
<a name="API_ExecutionPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ExecutionPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ExecutionPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ExecutionPreview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
