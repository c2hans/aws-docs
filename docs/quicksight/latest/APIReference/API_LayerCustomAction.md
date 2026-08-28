---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LayerCustomAction.html
---

# LayerCustomAction
<a name="API_LayerCustomAction"></a>

A layer custom action.

## Contents
<a name="API_LayerCustomAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ActionOperations **   <a name="QS-Type-LayerCustomAction-ActionOperations"></a>
A list of `LayerCustomActionOperations`.
This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
Type: Array of [LayerCustomActionOperation](API_LayerCustomActionOperation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** CustomActionId **   <a name="QS-Type-LayerCustomAction-CustomActionId"></a>
The ID of the custom action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Name **   <a name="QS-Type-LayerCustomAction-Name"></a>
The name of the custom action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Trigger **   <a name="QS-Type-LayerCustomAction-Trigger"></a>
The trigger of the `LayerCustomAction`.
Valid values are defined as follows:
+  `DATA_POINT_CLICK`: Initiates a custom action by a left pointer click on a data point.
+  `DATA_POINT_MENU`: Initiates a custom action by right pointer click from the menu.
Type: String
Valid Values: `DATA_POINT_CLICK | DATA_POINT_MENU`
Required: Yes

 ** Status **   <a name="QS-Type-LayerCustomAction-Status"></a>
The status of the `LayerCustomAction`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_LayerCustomAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LayerCustomAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LayerCustomAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LayerCustomAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
