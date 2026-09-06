---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-oam-link-linkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Oam::Link LinkConfiguration
<a name="aws-properties-oam-link-linkconfiguration"></a>

Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.

## Syntax
<a name="aws-properties-oam-link-linkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-oam-link-linkconfiguration-syntax.json"></a>

```
{
  "[LogGroupConfiguration](#cfn-oam-link-linkconfiguration-loggroupconfiguration)" : {{LinkFilter}},
  "[MetricConfiguration](#cfn-oam-link-linkconfiguration-metricconfiguration)" : {{LinkFilter}}
}
```

### YAML
<a name="aws-properties-oam-link-linkconfiguration-syntax.yaml"></a>

```
  [LogGroupConfiguration](#cfn-oam-link-linkconfiguration-loggroupconfiguration): {{
    LinkFilter}}
  [MetricConfiguration](#cfn-oam-link-linkconfiguration-metricconfiguration): {{
    LinkFilter}}
```

## Properties
<a name="aws-properties-oam-link-linkconfiguration-properties"></a>

`LogGroupConfiguration`  <a name="cfn-oam-link-linkconfiguration-loggroupconfiguration"></a>
Use this structure to filter which log groups are to share log events from this source account to the monitoring account.
*Required*: No
*Type*: [LinkFilter](aws-properties-oam-link-linkfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricConfiguration`  <a name="cfn-oam-link-linkconfiguration-metricconfiguration"></a>
Use this structure to filter which metric namespaces are to be shared from the source account to the monitoring account.
*Required*: No
*Type*: [LinkFilter](aws-properties-oam-link-linkfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
