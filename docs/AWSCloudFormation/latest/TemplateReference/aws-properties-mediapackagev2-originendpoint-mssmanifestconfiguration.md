---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-mssmanifestconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint MssManifestConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-mssmanifestconfiguration"></a>

<a name="aws-properties-mediapackagev2-originendpoint-mssmanifestconfiguration-description"></a>The `MssManifestConfiguration` property type specifies Property description not available. for an [AWS::MediaPackageV2::OriginEndpoint](aws-resource-mediapackagev2-originendpoint.md).

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-mssmanifestconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-mssmanifestconfiguration-syntax.json"></a>

```
{
  "[FilterConfiguration](#cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-filterconfiguration)" : {{FilterConfiguration}},
  "[ManifestLayout](#cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-manifestlayout)" : {{String}},
  "[ManifestName](#cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-manifestname)" : {{String}},
  "[ManifestWindowSeconds](#cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-manifestwindowseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-mssmanifestconfiguration-syntax.yaml"></a>

```
  [FilterConfiguration](#cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-filterconfiguration): {{
    FilterConfiguration}}
  [ManifestLayout](#cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-manifestlayout): {{String}}
  [ManifestName](#cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-manifestname): {{String}}
  [ManifestWindowSeconds](#cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-manifestwindowseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-mssmanifestconfiguration-properties"></a>

`FilterConfiguration`  <a name="cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-filterconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FilterConfiguration](aws-properties-mediapackagev2-originendpoint-filterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestLayout`  <a name="cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-manifestlayout"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `FULL | COMPACT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestName`  <a name="cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-manifestname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestWindowSeconds`  <a name="cfn-mediapackagev2-originendpoint-mssmanifestconfiguration-manifestwindowseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
