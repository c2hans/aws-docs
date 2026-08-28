---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-workflow-s3inputfilelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Workflow S3InputFileLocation
<a name="aws-properties-transfer-workflow-s3inputfilelocation"></a>

 Specifies the details for the Amazon S3 location for an input file to a workflow.

## Syntax
<a name="aws-properties-transfer-workflow-s3inputfilelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-workflow-s3inputfilelocation-syntax.json"></a>

```
{
  "[Bucket](#cfn-transfer-workflow-s3inputfilelocation-bucket)" : {{String}},
  "[Key](#cfn-transfer-workflow-s3inputfilelocation-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-workflow-s3inputfilelocation-syntax.yaml"></a>

```
  [Bucket](#cfn-transfer-workflow-s3inputfilelocation-bucket): {{String}}
  [Key](#cfn-transfer-workflow-s3inputfilelocation-key): {{String}}
```

## Properties
<a name="aws-properties-transfer-workflow-s3inputfilelocation-properties"></a>

`Bucket`  <a name="cfn-transfer-workflow-s3inputfilelocation-bucket"></a>
Specifies the S3 bucket for the customer input file.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Key`  <a name="cfn-transfer-workflow-s3inputfilelocation-key"></a>
The name assigned to the file when it was created in Amazon S3. You use the object key to retrieve the object.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
