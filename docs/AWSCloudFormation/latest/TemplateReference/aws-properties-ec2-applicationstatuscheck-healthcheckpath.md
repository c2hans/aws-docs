---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-applicationstatuscheck-healthcheckpath.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ApplicationStatusCheck HealthCheckPath
<a name="aws-properties-ec2-applicationstatuscheck-healthcheckpath"></a>

<a name="aws-properties-ec2-applicationstatuscheck-healthcheckpath-description"></a>The `HealthCheckPath` property type specifies Property description not available. for an [AWS::EC2::ApplicationStatusCheck](aws-resource-ec2-applicationstatuscheck.md).

## Syntax
<a name="aws-properties-ec2-applicationstatuscheck-healthcheckpath-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-applicationstatuscheck-healthcheckpath-syntax.json"></a>

```
{
  "[Destinations](#cfn-ec2-applicationstatuscheck-healthcheckpath-destinations)" : {{[ HealthCheckPathDestination, ... ]}},
  "[Source](#cfn-ec2-applicationstatuscheck-healthcheckpath-source)" : {{HealthCheckPathSource}}
}
```

### YAML
<a name="aws-properties-ec2-applicationstatuscheck-healthcheckpath-syntax.yaml"></a>

```
  [Destinations](#cfn-ec2-applicationstatuscheck-healthcheckpath-destinations): {{
    - HealthCheckPathDestination}}
  [Source](#cfn-ec2-applicationstatuscheck-healthcheckpath-source): {{
    HealthCheckPathSource}}
```

## Properties
<a name="aws-properties-ec2-applicationstatuscheck-healthcheckpath-properties"></a>

`Destinations`  <a name="cfn-ec2-applicationstatuscheck-healthcheckpath-destinations"></a>
Property description not available.
*Required*: No
*Type*: Array of [HealthCheckPathDestination](aws-properties-ec2-applicationstatuscheck-healthcheckpathdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-ec2-applicationstatuscheck-healthcheckpath-source"></a>
Property description not available.
*Required*: No
*Type*: [HealthCheckPathSource](aws-properties-ec2-applicationstatuscheck-healthcheckpathsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
