---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-multiregionendpoint-details.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MultiRegionEndpoint Details
<a name="aws-properties-ses-multiregionendpoint-details"></a>

An object that contains configuration details of multi-region endpoint (global-endpoint).

## Syntax
<a name="aws-properties-ses-multiregionendpoint-details-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-multiregionendpoint-details-syntax.json"></a>

```
{
  "[RouteDetails](#cfn-ses-multiregionendpoint-details-routedetails)" : {{[ RouteDetailsItems, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-multiregionendpoint-details-syntax.yaml"></a>

```
  [RouteDetails](#cfn-ses-multiregionendpoint-details-routedetails): {{
    - RouteDetailsItems}}
```

## Properties
<a name="aws-properties-ses-multiregionendpoint-details-properties"></a>

`RouteDetails`  <a name="cfn-ses-multiregionendpoint-details-routedetails"></a>
A list of route configuration details. Must contain exactly one route configuration.
*Required*: Yes
*Type*: Array of [RouteDetailsItems](aws-properties-ses-multiregionendpoint-routedetailsitems.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
