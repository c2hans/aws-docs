---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-multiregionendpoint-routedetailsitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MultiRegionEndpoint RouteDetailsItems
<a name="aws-properties-ses-multiregionendpoint-routedetailsitems"></a>

An object that contains route configuration. Includes secondary region name.

## Syntax
<a name="aws-properties-ses-multiregionendpoint-routedetailsitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-multiregionendpoint-routedetailsitems-syntax.json"></a>

```
{
  "[Region](#cfn-ses-multiregionendpoint-routedetailsitems-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-multiregionendpoint-routedetailsitems-syntax.yaml"></a>

```
  [Region](#cfn-ses-multiregionendpoint-routedetailsitems-region): {{String}}
```

## Properties
<a name="aws-properties-ses-multiregionendpoint-routedetailsitems-properties"></a>

`Region`  <a name="cfn-ses-multiregionendpoint-routedetailsitems-region"></a>
The name of an AWS-Region to be a secondary region for the multi-region endpoint (global-endpoint).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
