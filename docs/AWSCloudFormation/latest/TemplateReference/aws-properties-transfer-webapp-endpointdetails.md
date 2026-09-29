---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-webapp-endpointdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::WebApp EndpointDetails
<a name="aws-properties-transfer-webapp-endpointdetails"></a>

Contains the endpoint configuration for a web app, including VPC settings when the endpoint is hosted within a VPC.

## Syntax
<a name="aws-properties-transfer-webapp-endpointdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-webapp-endpointdetails-syntax.json"></a>

```
{
  "[Vpc](#cfn-transfer-webapp-endpointdetails-vpc)" : {{Vpc}}
}
```

### YAML
<a name="aws-properties-transfer-webapp-endpointdetails-syntax.yaml"></a>

```
  [Vpc](#cfn-transfer-webapp-endpointdetails-vpc): {{
    Vpc}}
```

## Properties
<a name="aws-properties-transfer-webapp-endpointdetails-properties"></a>

`Vpc`  <a name="cfn-transfer-webapp-endpointdetails-vpc"></a>
The VPC configuration for hosting the web app endpoint within a VPC.
*Required*: No
*Type*: [Vpc](aws-properties-transfer-webapp-vpc.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
