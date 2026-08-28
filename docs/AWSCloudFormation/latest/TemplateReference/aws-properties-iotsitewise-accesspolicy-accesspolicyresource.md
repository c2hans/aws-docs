---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AccessPolicy AccessPolicyResource
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyresource"></a>

The AWS IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.

## Syntax
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyresource-syntax.json"></a>

```
{
  "[Portal](#cfn-iotsitewise-accesspolicy-accesspolicyresource-portal)" : {{Portal}},
  "[Project](#cfn-iotsitewise-accesspolicy-accesspolicyresource-project)" : {{Project}}
}
```

### YAML
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyresource-syntax.yaml"></a>

```
  [Portal](#cfn-iotsitewise-accesspolicy-accesspolicyresource-portal): {{
    Portal}}
  [Project](#cfn-iotsitewise-accesspolicy-accesspolicyresource-project): {{
    Project}}
```

## Properties
<a name="aws-properties-iotsitewise-accesspolicy-accesspolicyresource-properties"></a>

`Portal`  <a name="cfn-iotsitewise-accesspolicy-accesspolicyresource-portal"></a>
Identifies an AWS IoT SiteWise Monitor portal.
*Required*: No
*Type*: [Portal](aws-properties-iotsitewise-accesspolicy-portal.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Project`  <a name="cfn-iotsitewise-accesspolicy-accesspolicyresource-project"></a>
Identifies a specific AWS IoT SiteWise Monitor project.
*Required*: No
*Type*: [Project](aws-properties-iotsitewise-accesspolicy-project.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
