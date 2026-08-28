---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-forceendpointerrorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint ForceEndpointErrorConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-forceendpointerrorconfiguration"></a>

The failover settings for the endpoint.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-forceendpointerrorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-forceendpointerrorconfiguration-syntax.json"></a>

```
{
  "[EndpointErrorConditions](#cfn-mediapackagev2-originendpoint-forceendpointerrorconfiguration-endpointerrorconditions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-forceendpointerrorconfiguration-syntax.yaml"></a>

```
  [EndpointErrorConditions](#cfn-mediapackagev2-originendpoint-forceendpointerrorconfiguration-endpointerrorconditions): {{
    - String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-forceendpointerrorconfiguration-properties"></a>

`EndpointErrorConditions`  <a name="cfn-mediapackagev2-originendpoint-forceendpointerrorconfiguration-endpointerrorconditions"></a>
The failover conditions for the endpoint. The options are:
+ `STALE_MANIFEST` - The manifest stalled and there are no new segments or parts.
+ `INCOMPLETE_MANIFEST` - There is a gap in the manifest.
+ `MISSING_DRM_KEY` - Key rotation is enabled but we're unable to fetch the key for the current key period.
+ `SLATE_INPUT` - The segments which contain slate content are considered to be missing content.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
