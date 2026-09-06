---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-m2-environment-highavailabilityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::M2::Environment HighAvailabilityConfig
<a name="aws-properties-m2-environment-highavailabilityconfig"></a>

**Important**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Defines the details of a high availability configuration.

## Syntax
<a name="aws-properties-m2-environment-highavailabilityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-m2-environment-highavailabilityconfig-syntax.json"></a>

```
{
  "[DesiredCapacity](#cfn-m2-environment-highavailabilityconfig-desiredcapacity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-m2-environment-highavailabilityconfig-syntax.yaml"></a>

```
  [DesiredCapacity](#cfn-m2-environment-highavailabilityconfig-desiredcapacity): {{Integer}}
```

## Properties
<a name="aws-properties-m2-environment-highavailabilityconfig-properties"></a>

`DesiredCapacity`  <a name="cfn-m2-environment-highavailabilityconfig-desiredcapacity"></a>
The number of instances in a high availability configuration. The minimum possible value is 1 and the maximum is 100.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
