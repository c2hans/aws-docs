---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-server-workflowdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Server WorkflowDetail
<a name="aws-properties-transfer-server-workflowdetail"></a>

Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.

 In addition to a workflow to execute when a file is uploaded completely, `WorkflowDetails` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when a file is open when the session disconnects.

## Syntax
<a name="aws-properties-transfer-server-workflowdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-server-workflowdetail-syntax.json"></a>

```
{
  "[ExecutionRole](#cfn-transfer-server-workflowdetail-executionrole)" : {{String}},
  "[WorkflowId](#cfn-transfer-server-workflowdetail-workflowid)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-server-workflowdetail-syntax.yaml"></a>

```
  [ExecutionRole](#cfn-transfer-server-workflowdetail-executionrole): {{String}}
  [WorkflowId](#cfn-transfer-server-workflowdetail-workflowid): {{String}}
```

## Properties
<a name="aws-properties-transfer-server-workflowdetail-properties"></a>

`ExecutionRole`  <a name="cfn-transfer-server-workflowdetail-executionrole"></a>
Includes the necessary permissions for S3, EFS, and Lambda operations that Transfer can assume, so that all workflow steps can operate on the required resources
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*role/\S+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowId`  <a name="cfn-transfer-server-workflowdetail-workflowid"></a>
A unique identifier for the workflow.
*Required*: Yes
*Type*: String
*Pattern*: `^w-([a-z0-9]{17})$`
*Minimum*: `19`
*Maximum*: `19`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
