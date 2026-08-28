---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-server-workflowdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Server WorkflowDetails
<a name="aws-properties-transfer-server-workflowdetails"></a>

Container for the `WorkflowDetail` data type. It is used by actions that trigger a workflow to begin execution.

## Syntax
<a name="aws-properties-transfer-server-workflowdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-server-workflowdetails-syntax.json"></a>

```
{
  "[OnPartialUpload](#cfn-transfer-server-workflowdetails-onpartialupload)" : {{[ WorkflowDetail, ... ]}},
  "[OnUpload](#cfn-transfer-server-workflowdetails-onupload)" : {{[ WorkflowDetail, ... ]}}
}
```

### YAML
<a name="aws-properties-transfer-server-workflowdetails-syntax.yaml"></a>

```
  [OnPartialUpload](#cfn-transfer-server-workflowdetails-onpartialupload): {{
    - WorkflowDetail}}
  [OnUpload](#cfn-transfer-server-workflowdetails-onupload): {{
    - WorkflowDetail}}
```

## Properties
<a name="aws-properties-transfer-server-workflowdetails-properties"></a>

`OnPartialUpload`  <a name="cfn-transfer-server-workflowdetails-onpartialupload"></a>
A trigger that starts a workflow if a file is only partially uploaded. You can attach a workflow to a server that executes whenever there is a partial upload.
A *partial upload* occurs when a file is open when the session disconnects.
`OnPartialUpload` can contain a maximum of one `WorkflowDetail` object.
*Required*: No
*Type*: Array of [WorkflowDetail](aws-properties-transfer-server-workflowdetail.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnUpload`  <a name="cfn-transfer-server-workflowdetails-onupload"></a>
A trigger that starts a workflow: the workflow begins to execute after a file is uploaded.
To remove an associated workflow from a server, you can provide an empty `OnUpload` object, as in the following example.
 `aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{"OnUpload":[]}'`
`OnUpload` can contain a maximum of one `WorkflowDetail` object.
*Required*: No
*Type*: Array of [WorkflowDetail](aws-properties-transfer-server-workflowdetail.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
