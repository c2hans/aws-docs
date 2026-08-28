---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-tenant-resourceassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::Tenant ResourceAssociation
<a name="aws-properties-ses-tenant-resourceassociation"></a>

The resource to associate with the tenant.

## Syntax
<a name="aws-properties-ses-tenant-resourceassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-tenant-resourceassociation-syntax.json"></a>

```
{
  "[ResourceArn](#cfn-ses-tenant-resourceassociation-resourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-tenant-resourceassociation-syntax.yaml"></a>

```
  [ResourceArn](#cfn-ses-tenant-resourceassociation-resourcearn): {{String}}
```

## Properties
<a name="aws-properties-ses-tenant-resourceassociation-properties"></a>

`ResourceArn`  <a name="cfn-ses-tenant-resourceassociation-resourcearn"></a>
The Amazon Resource Name (ARN) of the resource associated with the tenant.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
