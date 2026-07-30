---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-scraper-source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Scraper Source
<a name="aws-properties-aps-scraper-source"></a>

The source of collected metrics for a scraper.

## Syntax
<a name="aws-properties-aps-scraper-source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-scraper-source-syntax.json"></a>

```
{
  "[EksConfiguration](#cfn-aps-scraper-source-eksconfiguration)" : {{EksConfiguration}},
  "[VpcConfiguration](#cfn-aps-scraper-source-vpcconfiguration)" : {{VpcConfiguration}}
}
```

### YAML
<a name="aws-properties-aps-scraper-source-syntax.yaml"></a>

```
  [EksConfiguration](#cfn-aps-scraper-source-eksconfiguration): {{
    EksConfiguration}}
  [VpcConfiguration](#cfn-aps-scraper-source-vpcconfiguration): {{
    VpcConfiguration}}
```

## Properties
<a name="aws-properties-aps-scraper-source-properties"></a>

`EksConfiguration`  <a name="cfn-aps-scraper-source-eksconfiguration"></a>
The Amazon EKS cluster from which a scraper collects metrics.
*Required*: No
*Type*: [EksConfiguration](aws-properties-aps-scraper-eksconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfiguration`  <a name="cfn-aps-scraper-source-vpcconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [VpcConfiguration](aws-properties-aps-scraper-vpcconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
