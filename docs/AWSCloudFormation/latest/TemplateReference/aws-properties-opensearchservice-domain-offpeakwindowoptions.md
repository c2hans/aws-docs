---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-offpeakwindowoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain OffPeakWindowOptions
<a name="aws-properties-opensearchservice-domain-offpeakwindowoptions"></a>

Off-peak window settings for the domain.

## Syntax
<a name="aws-properties-opensearchservice-domain-offpeakwindowoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-offpeakwindowoptions-syntax.json"></a>

```
{
  "[Enabled](#cfn-opensearchservice-domain-offpeakwindowoptions-enabled)" : {{Boolean}},
  "[OffPeakWindow](#cfn-opensearchservice-domain-offpeakwindowoptions-offpeakwindow)" : {{OffPeakWindow}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-offpeakwindowoptions-syntax.yaml"></a>

```
  [Enabled](#cfn-opensearchservice-domain-offpeakwindowoptions-enabled): {{Boolean}}
  [OffPeakWindow](#cfn-opensearchservice-domain-offpeakwindowoptions-offpeakwindow): {{
    OffPeakWindow}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-offpeakwindowoptions-properties"></a>

`Enabled`  <a name="cfn-opensearchservice-domain-offpeakwindowoptions-enabled"></a>
Specifies whether off-peak window settings are enabled for the domain.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OffPeakWindow`  <a name="cfn-opensearchservice-domain-offpeakwindowoptions-offpeakwindow"></a>
Off-peak window settings for the domain.
*Required*: No
*Type*: [OffPeakWindow](aws-properties-opensearchservice-domain-offpeakwindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
