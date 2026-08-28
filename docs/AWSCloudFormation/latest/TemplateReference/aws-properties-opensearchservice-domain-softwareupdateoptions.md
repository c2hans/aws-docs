---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-softwareupdateoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain SoftwareUpdateOptions
<a name="aws-properties-opensearchservice-domain-softwareupdateoptions"></a>

Options for configuring service software updates for a domain.

## Syntax
<a name="aws-properties-opensearchservice-domain-softwareupdateoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-softwareupdateoptions-syntax.json"></a>

```
{
  "[AutoSoftwareUpdateEnabled](#cfn-opensearchservice-domain-softwareupdateoptions-autosoftwareupdateenabled)" : {{Boolean}},
  "[UseLatestServiceSoftwareForBlueGreen](#cfn-opensearchservice-domain-softwareupdateoptions-uselatestservicesoftwareforbluegreen)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-softwareupdateoptions-syntax.yaml"></a>

```
  [AutoSoftwareUpdateEnabled](#cfn-opensearchservice-domain-softwareupdateoptions-autosoftwareupdateenabled): {{Boolean}}
  [UseLatestServiceSoftwareForBlueGreen](#cfn-opensearchservice-domain-softwareupdateoptions-uselatestservicesoftwareforbluegreen): {{Boolean}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-softwareupdateoptions-properties"></a>

`AutoSoftwareUpdateEnabled`  <a name="cfn-opensearchservice-domain-softwareupdateoptions-autosoftwareupdateenabled"></a>
Specifies whether automatic service software updates are enabled for the domain.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseLatestServiceSoftwareForBlueGreen`  <a name="cfn-opensearchservice-domain-softwareupdateoptions-uselatestservicesoftwareforbluegreen"></a>
Whether the domain should use the latest service software version during a blue/green deployment. If enabled, the domain will automatically use the latest available service software when a blue/green deployment is triggered.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
