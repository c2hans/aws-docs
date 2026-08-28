---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Node.html
---

# Node
<a name="API_Node"></a>

Details about an individual managed node.

## Contents
<a name="API_Node_Contents"></a>

 ** CaptureTime **   <a name="systemsmanager-Type-Node-CaptureTime"></a>
The UTC timestamp for when the managed node data was last captured.
Type: Timestamp
Required: No

 ** Id **   <a name="systemsmanager-Type-Node-Id"></a>
The ID of the managed node.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** NodeType **   <a name="systemsmanager-Type-Node-NodeType"></a>
Information about the type of node.
Type: [NodeType](API_NodeType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Owner **   <a name="systemsmanager-Type-Node-Owner"></a>
Information about the ownership of the managed node.
Type: [NodeOwnerInfo](API_NodeOwnerInfo.md) object
Required: No

 ** Region **   <a name="systemsmanager-Type-Node-Region"></a>
The AWS Region that a managed node was created in or assigned to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_Node_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Node)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Node)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Node)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
