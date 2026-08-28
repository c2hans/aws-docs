---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenercertificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerCertificate
<a name="aws-resource-elasticloadbalancingv2-listenercertificate"></a>

Specifies an SSL server certificate to add to the certificate list for an HTTPS or TLS listener.

## Syntax
<a name="aws-resource-elasticloadbalancingv2-listenercertificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticloadbalancingv2-listenercertificate-syntax.json"></a>

```
{
  "Type" : "AWS::ElasticLoadBalancingV2::ListenerCertificate",
  "Properties" : {
      "[Certificates](#cfn-elasticloadbalancingv2-listenercertificate-certificates)" : {{[ Certificate, ... ]}},
      "[ListenerArn](#cfn-elasticloadbalancingv2-listenercertificate-listenerarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-elasticloadbalancingv2-listenercertificate-syntax.yaml"></a>

```
Type: AWS::ElasticLoadBalancingV2::ListenerCertificate
Properties:
  [Certificates](#cfn-elasticloadbalancingv2-listenercertificate-certificates): {{
    - Certificate}}
  [ListenerArn](#cfn-elasticloadbalancingv2-listenercertificate-listenerarn): {{String}}
```

## Properties
<a name="aws-resource-elasticloadbalancingv2-listenercertificate-properties"></a>

`Certificates`  <a name="cfn-elasticloadbalancingv2-listenercertificate-certificates"></a>
The certificate. You can specify one certificate per resource.
*Required*: Yes
*Type*: Array of [Certificate](aws-properties-elasticloadbalancingv2-listenercertificate-certificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListenerArn`  <a name="cfn-elasticloadbalancingv2-listenercertificate-listenerarn"></a>
The Amazon Resource Name (ARN) of the listener.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-resource-elasticloadbalancingv2-listenercertificate--examples"></a>

###
<a name="aws-resource-elasticloadbalancingv2-listenercertificate--examples--"></a>

The following example creates a certificate list.

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listenercertificate--examples----yaml"></a>

```
myCertificateList:
  Type: 'AWS::ElasticLoadBalancingV2::ListenerCertificate'
  Properties:
    ListenerArn: !Ref myTLSListener
    Certificates:
      - CertificateArn: "arn:aws:acm:us-west-2:123456789012:certificate/11111111-1234-46f1-abcd-11117EXAMPLE"
      - CertificateArn: "arn:aws:acm:us-west-2:123456789012:certificate/22222222-4567-57f2-cdef-22227EXAMPLE"
      - CertificateArn: "arn:aws:acm:us-west-2:123456789012:certificate/33333333-5678-68f3-a123-33337EXAMPLE"
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listenercertificate--examples----json"></a>

```
{
    "myCertificateList": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerCertificate",
        "Properties": {
            "ListenerArn": {
                "Ref": "myTLSListener"
            },
            "Certificates": [
                {
                    "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/11111111-1234-46f1-abcd-11117EXAMPLE"
                },
                {
                    "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/22222222-4567-57f2-cdef-22227EXAMPLE"
                },
                {
                    "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/33333333-5678-68f3-a123-33337EXAMPLE"
                }
            ]
        }
    }
}
```

## See also
<a name="aws-resource-elasticloadbalancingv2-listenercertificate--seealso"></a>
+ [AddListenerCertificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddListenerCertificates.html) in the *Elastic Load Balancing API Reference (version 2015-12-01)*
+ [SSL Certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/https-listener-certificates.html) in the *User Guide for Application Load Balancers*
+ [Server certificates](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/tls-listener-certificates.html) in the *User Guide for Network Load Balancers*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
