---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenercertificate-certificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerCertificate Certificate
<a name="aws-properties-elasticloadbalancingv2-listenercertificate-certificate"></a>

Specifies an SSL server certificate for the certificate list of a secure listener.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenercertificate-certificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenercertificate-certificate-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-elasticloadbalancingv2-listenercertificate-certificate-certificatearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenercertificate-certificate-syntax.yaml"></a>

```
  [CertificateArn](#cfn-elasticloadbalancingv2-listenercertificate-certificate-certificatearn): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenercertificate-certificate-properties"></a>

`CertificateArn`  <a name="cfn-elasticloadbalancingv2-listenercertificate-certificate-certificatearn"></a>
The Amazon Resource Name (ARN) of the certificate.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
