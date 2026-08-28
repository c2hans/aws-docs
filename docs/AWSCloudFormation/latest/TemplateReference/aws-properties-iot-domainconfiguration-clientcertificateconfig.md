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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
