---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionExecution.html
---

# ActionExecution
<a name="API_ActionExecution"></a>

Performs an Amazon Q Business plugin action during a non-streaming chat conversation.

## Contents
<a name="API_ActionExecution_Contents"></a>

 ** payload **   <a name="qbusiness-Type-ActionExecution-payload"></a>
A mapping of field names to the field values in input that an end user provides to Amazon Q Business requests to perform their plugin action.
Type: String to [ActionExecutionPayloadField](API_ActionExecutionPayloadField.md) object map
Key Length Constraints: Minimum length of 1.
Required: Yes

 ** payloadFieldNameSeparator **   <a name="qbusiness-Type-ActionExecution-payloadFieldNameSeparator"></a>
A string used to retain information about the hierarchical contexts within an action execution event payload.
Type: String
Length Constraints: Fixed length of 1.
Required: Yes

 ** pluginId **   <a name="qbusiness-Type-ActionExecution-pluginId"></a>
The identifier of the plugin the action is attached to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## See Also
<a name="API_ActionExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ActionExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ActionExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ActionExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
