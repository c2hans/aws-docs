---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-applicationlogs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link ApplicationLogs
<a name="aws-properties-rtbfabric-link-applicationlogs"></a>

Describes the configuration of a link application log.

## Syntax
<a name="aws-properties-rtbfabric-link-applicationlogs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-applicationlogs-syntax.json"></a>

```
{
  "[LinkApplicationLogSampling](#cfn-rtbfabric-link-applicationlogs-linkapplicationlogsampling)" : {{LinkApplicationLogSampling}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-applicationlogs-syntax.yaml"></a>

```
  [LinkApplicationLogSampling](#cfn-rtbfabric-link-applicationlogs-linkapplicationlogsampling): {{
    LinkApplicationLogSampling}}
```

## Properties
<a name="aws-properties-rtbfabric-link-applicationlogs-properties"></a>

`LinkApplicationLogSampling`  <a name="cfn-rtbfabric-link-applicationlogs-linkapplicationlogsampling"></a>
Describes a link application log sample.
*Required*: Yes
*Type*: [LinkApplicationLogSampling](aws-properties-rtbfabric-link-linkapplicationlogsampling.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
