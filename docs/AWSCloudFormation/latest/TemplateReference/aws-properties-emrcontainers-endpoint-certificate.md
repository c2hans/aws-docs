---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-endpoint-certificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::Endpoint Certificate
<a name="aws-properties-emrcontainers-endpoint-certificate"></a>

The entity representing certificate data generated for managed endpoint.

## Syntax
<a name="aws-properties-emrcontainers-endpoint-certificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-endpoint-certificate-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-emrcontainers-endpoint-certificate-certificatearn)" : {{String}},
  "[CertificateData](#cfn-emrcontainers-endpoint-certificate-certificatedata)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-endpoint-certificate-syntax.yaml"></a>

```
  [CertificateArn](#cfn-emrcontainers-endpoint-certificate-certificatearn): {{String}}
  [CertificateData](#cfn-emrcontainers-endpoint-certificate-certificatedata): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-endpoint-certificate-properties"></a>

`CertificateArn`  <a name="cfn-emrcontainers-endpoint-certificate-certificatearn"></a>
The ARN of the certificate generated for managed endpoint.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):acm:.+:(\d{12}):certificate/.+$`
*Minimum*: `44`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateData`  <a name="cfn-emrcontainers-endpoint-certificate-certificatedata"></a>
The base64 encoded PEM certificate data generated for managed endpoint.
*Required*: No
*Type*: String
*Pattern*: `^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
