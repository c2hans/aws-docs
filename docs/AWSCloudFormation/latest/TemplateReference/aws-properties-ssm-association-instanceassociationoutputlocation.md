---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-association-instanceassociationoutputlocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::Association InstanceAssociationOutputLocation
<a name="aws-properties-ssm-association-instanceassociationoutputlocation"></a>

`InstanceAssociationOutputLocation` is a property of the [AWS::SSM::Association](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html) resource that specifies an Amazon S3 bucket where you want to store the results of this association request.

For the minimal permissions required to enable Amazon S3 output for an association, see [Creating associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc.html) in the *Systems Manager User Guide*.

## Syntax
<a name="aws-properties-ssm-association-instanceassociationoutputlocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-association-instanceassociationoutputlocation-syntax.json"></a>

```
{
  "[S3Location](#cfn-ssm-association-instanceassociationoutputlocation-s3location)" : {{S3OutputLocation}}
}
```

### YAML
<a name="aws-properties-ssm-association-instanceassociationoutputlocation-syntax.yaml"></a>

```
  [S3Location](#cfn-ssm-association-instanceassociationoutputlocation-s3location): {{
    S3OutputLocation}}
```

## Properties
<a name="aws-properties-ssm-association-instanceassociationoutputlocation-properties"></a>

`S3Location`  <a name="cfn-ssm-association-instanceassociationoutputlocation-s3location"></a>
`S3OutputLocation` is a property of the [InstanceAssociationOutputLocation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html) property that specifies an Amazon S3 bucket where you want to store the results of this request.
*Required*: No
*Type*: [S3OutputLocation](aws-properties-ssm-association-s3outputlocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
