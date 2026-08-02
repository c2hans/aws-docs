---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listener-mutualauthentication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::Listener MutualAuthentication
<a name="aws-properties-elasticloadbalancingv2-listener-mutualauthentication"></a>

The mutual authentication configuration information.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listener-mutualauthentication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listener-mutualauthentication-syntax.json"></a>

```
{
  "[AdvertiseTrustStoreCaNames](#cfn-elasticloadbalancingv2-listener-mutualauthentication-advertisetruststorecanames)" : {{String}},
  "[IgnoreClientCertificateExpiry](#cfn-elasticloadbalancingv2-listener-mutualauthentication-ignoreclientcertificateexpiry)" : {{Boolean}},
  "[Mode](#cfn-elasticloadbalancingv2-listener-mutualauthentication-mode)" : {{String}},
  "[TrustStoreArn](#cfn-elasticloadbalancingv2-listener-mutualauthentication-truststorearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listener-mutualauthentication-syntax.yaml"></a>

```
  [AdvertiseTrustStoreCaNames](#cfn-elasticloadbalancingv2-listener-mutualauthentication-advertisetruststorecanames): {{String}}
  [IgnoreClientCertificateExpiry](#cfn-elasticloadbalancingv2-listener-mutualauthentication-ignoreclientcertificateexpiry): {{Boolean}}
  [Mode](#cfn-elasticloadbalancingv2-listener-mutualauthentication-mode): {{String}}
  [TrustStoreArn](#cfn-elasticloadbalancingv2-listener-mutualauthentication-truststorearn): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listener-mutualauthentication-properties"></a>

`AdvertiseTrustStoreCaNames`  <a name="cfn-elasticloadbalancingv2-listener-mutualauthentication-advertisetruststorecanames"></a>
Indicates whether trust store CA certificate names are advertised.
*Required*: No
*Type*: String
*Allowed values*: `on | off`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IgnoreClientCertificateExpiry`  <a name="cfn-elasticloadbalancingv2-listener-mutualauthentication-ignoreclientcertificateexpiry"></a>
Indicates whether expired client certificates are ignored.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-elasticloadbalancingv2-listener-mutualauthentication-mode"></a>
The client certificate handling method. Options are `off`, `passthrough` or `verify`. The default value on initial resource creation is `off`. After mutual authentication is turned on, you must explicitly set the `Mode` to `off` to turn it off; removing the property from your template will not turn it off.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrustStoreArn`  <a name="cfn-elasticloadbalancingv2-listener-mutualauthentication-truststorearn"></a>
The Amazon Resource Name (ARN) of the trust store.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-listener-mutualauthentication--examples"></a>

###
<a name="aws-properties-elasticloadbalancingv2-listener-mutualauthentication--examples--"></a>

The following example configures mutual TLS verify mode.

#### YAML
<a name="aws-properties-elasticloadbalancingv2-listener-mutualauthentication--examples----yaml"></a>

```
myHTTPSListener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: HTTPS
    Port: 443
    DefaultActions:
      - Type: forward
        TargetGroupArn: !Ref myTargetGroup
    SslPolicy: "ELBSecurityPolicy-TLS13-1-2-2021-06"
    Certificates:
      - CertificateArn: "arn:aws:acm:us-west-2:123456789012:certificate/88ca7932-756c-46f1-a70d-03fa7EXAMPLE"
    MutualAuthentication:
      - Mode: verify
        TrustStoreArn: !Ref myTrustStore
```

#### JSON
<a name="aws-properties-elasticloadbalancingv2-listener-mutualauthentication--examples----json"></a>

```
{
    "myHTTPSListener": {
        "Type": "AWS::ElasticLoadBalancingV2::Listener",
        "Properties": {
            "LoadBalancerArn": {
                "Ref": "myLoadBalancer"
            },
            "Protocol": "HTTPS",
            "Port": 443,
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": {
                        "Ref": "myTargetGroup"
                    }
                }
            ],
            "SslPolicy": "ELBSecurityPolicy-TLS13-1-2-2021-06",
            "Certificates": [
                {
                    "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/88ca7932-756c-46f1-a70d-03fa7EXAMPLE"
                }
            ],
            "MutualAuthentication": [
                {
                    "Mode": "verify",
                    "TrustStoreArn": {
                        "Ref": "myTrustStore"
                    }
                }
            ]
        }
    }
}
```
