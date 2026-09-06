---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-resourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service ResourceConfiguration
<a name="aws-properties-resiliencehubv2-service-resourceconfiguration"></a>

Resource configuration for an input source. Provide exactly one field.

## Syntax
<a name="aws-properties-resiliencehubv2-service-resourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-resourceconfiguration-syntax.json"></a>

```
{
  "[CfnStackArn](#cfn-resiliencehubv2-service-resourceconfiguration-cfnstackarn)" : {{String}},
  "[DesignFileS3Url](#cfn-resiliencehubv2-service-resourceconfiguration-designfiles3url)" : {{String}},
  "[Eks](#cfn-resiliencehubv2-service-resourceconfiguration-eks)" : {{EksSource}},
  "[ResourceTags](#cfn-resiliencehubv2-service-resourceconfiguration-resourcetags)" : {{[ ResourceTag, ... ]}},
  "[TfStateFileUrl](#cfn-resiliencehubv2-service-resourceconfiguration-tfstatefileurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-resourceconfiguration-syntax.yaml"></a>

```
  [CfnStackArn](#cfn-resiliencehubv2-service-resourceconfiguration-cfnstackarn): {{String}}
  [DesignFileS3Url](#cfn-resiliencehubv2-service-resourceconfiguration-designfiles3url): {{String}}
  [Eks](#cfn-resiliencehubv2-service-resourceconfiguration-eks): {{
    EksSource}}
  [ResourceTags](#cfn-resiliencehubv2-service-resourceconfiguration-resourcetags): {{
    - ResourceTag}}
  [TfStateFileUrl](#cfn-resiliencehubv2-service-resourceconfiguration-tfstatefileurl): {{String}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-resourceconfiguration-properties"></a>

`CfnStackArn`  <a name="cfn-resiliencehubv2-service-resourceconfiguration-cfnstackarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DesignFileS3Url`  <a name="cfn-resiliencehubv2-service-resourceconfiguration-designfiles3url"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Eks`  <a name="cfn-resiliencehubv2-service-resourceconfiguration-eks"></a>
The Amazon EKS configuration for resource discovery.
*Required*: No
*Type*: [EksSource](aws-properties-resiliencehubv2-service-ekssource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTags`  <a name="cfn-resiliencehubv2-service-resourceconfiguration-resourcetags"></a>
The resource tags for tag-based resource discovery.
*Required*: No
*Type*: Array of [ResourceTag](aws-properties-resiliencehubv2-service-resourcetag.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TfStateFileUrl`  <a name="cfn-resiliencehubv2-service-resourceconfiguration-tfstatefileurl"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
