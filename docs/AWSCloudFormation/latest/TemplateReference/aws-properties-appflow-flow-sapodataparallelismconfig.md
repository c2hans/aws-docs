---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-sapodataparallelismconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow SAPODataParallelismConfig
<a name="aws-properties-appflow-flow-sapodataparallelismconfig"></a>

Sets the number of *concurrent processes* that transfer OData records from your SAP instance. A concurrent process is query that retrieves a batch of records as part of a flow run. Amazon AppFlow can run multiple concurrent processes in parallel to transfer data faster.

## Syntax
<a name="aws-properties-appflow-flow-sapodataparallelismconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-sapodataparallelismconfig-syntax.json"></a>

```
{
  "[maxParallelism](#cfn-appflow-flow-sapodataparallelismconfig-maxparallelism)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appflow-flow-sapodataparallelismconfig-syntax.yaml"></a>

```
  [maxParallelism](#cfn-appflow-flow-sapodataparallelismconfig-maxparallelism): {{Integer}}
```

## Properties
<a name="aws-properties-appflow-flow-sapodataparallelismconfig-properties"></a>

`maxParallelism`  <a name="cfn-appflow-flow-sapodataparallelismconfig-maxparallelism"></a>
The maximum number of processes that Amazon AppFlow runs at the same time when it retrieves your data from your SAP application.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
