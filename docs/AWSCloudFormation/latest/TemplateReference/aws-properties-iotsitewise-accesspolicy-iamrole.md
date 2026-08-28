---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-accesspolicy-iamrole.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AccessPolicy IamRole
<a name="aws-properties-iotsitewise-accesspolicy-iamrole"></a>

Contains information about an AWS Identity and Access Management role. For more information, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *IAM User Guide*.

## Syntax
<a name="aws-properties-iotsitewise-accesspolicy-iamrole-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-accesspolicy-iamrole-syntax.json"></a>

```
{
  "[arn](#cfn-iotsitewise-accesspolicy-iamrole-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-accesspolicy-iamrole-syntax.yaml"></a>

```
  [arn](#cfn-iotsitewise-accesspolicy-iamrole-arn): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-accesspolicy-iamrole-properties"></a>

`arn`  <a name="cfn-iotsitewise-accesspolicy-iamrole-arn"></a>
The ARN of the IAM role. For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
