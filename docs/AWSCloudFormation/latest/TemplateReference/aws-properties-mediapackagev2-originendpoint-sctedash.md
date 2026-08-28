---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-sctedash.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint ScteDash
<a name="aws-properties-mediapackagev2-originendpoint-sctedash"></a>

The SCTE configuration.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-sctedash-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-sctedash-syntax.json"></a>

```
{
  "[AdMarkerDash](#cfn-mediapackagev2-originendpoint-sctedash-admarkerdash)" : {{String}},
  "[ScteInManifests](#cfn-mediapackagev2-originendpoint-sctedash-scteinmanifests)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-sctedash-syntax.yaml"></a>

```
  [AdMarkerDash](#cfn-mediapackagev2-originendpoint-sctedash-admarkerdash): {{String}}
  [ScteInManifests](#cfn-mediapackagev2-originendpoint-sctedash-scteinmanifests): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-sctedash-properties"></a>

`AdMarkerDash`  <a name="cfn-mediapackagev2-originendpoint-sctedash-admarkerdash"></a>
Choose how ad markers are included in the packaged content. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output.
Value description:
+ `Binary` - The SCTE-35 marker is expressed as a hex-string (Base64 string) rather than full XML.
+ `XML` - The SCTE marker is expressed fully in XML.
*Required*: No
*Type*: String
*Allowed values*: `BINARY | XML`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScteInManifests`  <a name="cfn-mediapackagev2-originendpoint-sctedash-scteinmanifests"></a>
Controls which SCTE-35 events appear in DASH manifests. `ALL` includes all non-implicit SCTE-35 events. `MATCHES_FILTER` includes only events whose type matches the configured `ScteFilter`.
If you don't specify a value, the default is `ALL`.
*Required*: No
*Type*: String
*Allowed values*: `ALL | MATCHES_FILTER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
