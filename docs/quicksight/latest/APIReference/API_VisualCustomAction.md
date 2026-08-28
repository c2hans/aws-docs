---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VisualCustomAction.html
---

# VisualCustomAction
<a name="API_VisualCustomAction"></a>

A custom action defined on a visual.

## Contents
<a name="API_VisualCustomAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ActionOperations **   <a name="QS-Type-VisualCustomAction-ActionOperations"></a>
A list of `VisualCustomActionOperations`.
This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
Type: Array of [VisualCustomActionOperation](API_VisualCustomActionOperation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** CustomActionId **   <a name="QS-Type-VisualCustomAction-CustomActionId"></a>
The ID of the `VisualCustomAction`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Name **   <a name="QS-Type-VisualCustomAction-Name"></a>
The name of the `VisualCustomAction`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Trigger **   <a name="QS-Type-VisualCustomAction-Trigger"></a>
The trigger of the `VisualCustomAction`.
Valid values are defined as follows:
+  `DATA_POINT_CLICK`: Initiates a custom action by a left pointer click on a data point.
+  `DATA_POINT_MENU`: Initiates a custom action by right pointer click from the menu.
Type: String
Valid Values: `DATA_POINT_CLICK | DATA_POINT_MENU`
Required: Yes

 ** Status **   <a name="QS-Type-VisualCustomAction-Status"></a>
The status of the `VisualCustomAction`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_VisualCustomAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/VisualCustomAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/VisualCustomAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/VisualCustomAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
