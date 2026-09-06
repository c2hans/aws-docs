---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-domainconfiguration-clientcertificateconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::DomainConfiguration ClientCertificateConfig
<a name="aws-properties-iot-domainconfiguration-clientcertificateconfig"></a>

An object that speciﬁes the client certificate conﬁguration for a domain.

## Syntax
<a name="aws-properties-iot-domainconfiguration-clientcertificateconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-domainconfiguration-clientcertificateconfig-syntax.json"></a>

```
{
  "[ClientCertificateCallbackArn](#cfn-iot-domainconfiguration-clientcertificateconfig-clientcertificatecallbackarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-domainconfiguration-clientcertificateconfig-syntax.yaml"></a>

```
  [ClientCertificateCallbackArn](#cfn-iot-domainconfiguration-clientcertificateconfig-clientcertificatecallbackarn): {{String}}
```

## Properties
<a name="aws-properties-iot-domainconfiguration-clientcertificateconfig-properties"></a>

`ClientCertificateCallbackArn`  <a name="cfn-iot-domainconfiguration-clientcertificateconfig-clientcertificatecallbackarn"></a>
The ARN of the Lambda function that IoT invokes after mutual TLS authentication during the connection.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
