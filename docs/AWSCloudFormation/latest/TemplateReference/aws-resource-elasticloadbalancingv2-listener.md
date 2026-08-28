---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::Listener
<a name="aws-resource-elasticloadbalancingv2-listener"></a>

Specifies a listener for an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.

## Syntax
<a name="aws-resource-elasticloadbalancingv2-listener-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticloadbalancingv2-listener-syntax.json"></a>

```
{
  "Type" : "AWS::ElasticLoadBalancingV2::Listener",
  "Properties" : {
      "[AlpnPolicy](#cfn-elasticloadbalancingv2-listener-alpnpolicy)" : {{[ String, ... ]}},
      "[Certificates](#cfn-elasticloadbalancingv2-listener-certificates)" : {{[ Certificate, ... ]}},
      "[DefaultActions](#cfn-elasticloadbalancingv2-listener-defaultactions)" : {{[ Action, ... ]}},
      "[ListenerAttributes](#cfn-elasticloadbalancingv2-listener-listenerattributes)" : {{[ ListenerAttribute, ... ]}},
      "[LoadBalancerArn](#cfn-elasticloadbalancingv2-listener-loadbalancerarn)" : {{String}},
      "[MutualAuthentication](#cfn-elasticloadbalancingv2-listener-mutualauthentication)" : {{MutualAuthentication}},
      "[Port](#cfn-elasticloadbalancingv2-listener-port)" : {{Integer}},
      "[Protocol](#cfn-elasticloadbalancingv2-listener-protocol)" : {{String}},
      "[SslPolicy](#cfn-elasticloadbalancingv2-listener-sslpolicy)" : {{String}},
      "[Tags](#cfn-elasticloadbalancingv2-listener-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticloadbalancingv2-listener-syntax.yaml"></a>

```
Type: AWS::ElasticLoadBalancingV2::Listener
Properties:
  [AlpnPolicy](#cfn-elasticloadbalancingv2-listener-alpnpolicy): {{
    - String}}
  [Certificates](#cfn-elasticloadbalancingv2-listener-certificates): {{
    - Certificate}}
  [DefaultActions](#cfn-elasticloadbalancingv2-listener-defaultactions): {{
    - Action}}
  [ListenerAttributes](#cfn-elasticloadbalancingv2-listener-listenerattributes): {{
    - ListenerAttribute}}
  [LoadBalancerArn](#cfn-elasticloadbalancingv2-listener-loadbalancerarn): {{String}}
  [MutualAuthentication](#cfn-elasticloadbalancingv2-listener-mutualauthentication): {{
    MutualAuthentication}}
  [Port](#cfn-elasticloadbalancingv2-listener-port): {{Integer}}
  [Protocol](#cfn-elasticloadbalancingv2-listener-protocol): {{String}}
  [SslPolicy](#cfn-elasticloadbalancingv2-listener-sslpolicy): {{String}}
  [Tags](#cfn-elasticloadbalancingv2-listener-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-elasticloadbalancingv2-listener-properties"></a>

`AlpnPolicy`  <a name="cfn-elasticloadbalancingv2-listener-alpnpolicy"></a>
[TLS listener] The name of the Application-Layer Protocol Negotiation (ALPN) policy.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Certificates`  <a name="cfn-elasticloadbalancingv2-listener-certificates"></a>
The default SSL server certificate for a secure listener. You must provide exactly one certificate if the listener protocol is HTTPS or TLS.
For an HTTPS listener, update requires some interruptions. For a TLS listener, update requires no interruption.
To create a certificate list for a secure listener, use [AWS::ElasticLoadBalancingV2::ListenerCertificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenercertificate.html).
*Required*: Conditional
*Type*: Array of [Certificate](aws-properties-elasticloadbalancingv2-listener-certificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultActions`  <a name="cfn-elasticloadbalancingv2-listener-defaultactions"></a>
The actions for the default rule. You cannot define a condition for a default rule.
To create additional rules for an Application Load Balancer, use [AWS::ElasticLoadBalancingV2::ListenerRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html).
*Required*: Yes
*Type*: Array of [Action](aws-properties-elasticloadbalancingv2-listener-action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListenerAttributes`  <a name="cfn-elasticloadbalancingv2-listener-listenerattributes"></a>
The listener attributes. Attributes that you do not modify retain their current values.
*Required*: No
*Type*: Array of [ListenerAttribute](aws-properties-elasticloadbalancingv2-listener-listenerattribute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadBalancerArn`  <a name="cfn-elasticloadbalancingv2-listener-loadbalancerarn"></a>
The Amazon Resource Name (ARN) of the load balancer.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MutualAuthentication`  <a name="cfn-elasticloadbalancingv2-listener-mutualauthentication"></a>
The mutual authentication configuration information.
*Required*: No
*Type*: [MutualAuthentication](aws-properties-elasticloadbalancingv2-listener-mutualauthentication.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-elasticloadbalancingv2-listener-port"></a>
The port on which the load balancer is listening. You can't specify a port for a Gateway Load Balancer.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-elasticloadbalancingv2-listener-protocol"></a>
The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, TCP\_UDP, QUIC, and TCP\_QUIC. You can’t specify the UDP, TCP\_UDP, QUIC, or TCP\_QUIC protocol if dual-stack mode is enabled. You can't specify a protocol for a Gateway Load Balancer.
*Required*: No
*Type*: String
*Allowed values*: `HTTP | HTTPS | TCP | TLS | UDP | TCP_UDP | GENEVE | QUIC | TCP_QUIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslPolicy`  <a name="cfn-elasticloadbalancingv2-listener-sslpolicy"></a>
[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported. For more information, see [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html) in the *Application Load Balancers Guide* and [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html) in the *Network Load Balancers Guide*.
[HTTPS listeners] Updating the security policy can result in interruptions if the load balancer is handling a high volume of traffic. To decrease the possibility of an interruption if your load balancer is handling a high volume of traffic, create an additional load balancer or request an LCU reservation.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-elasticloadbalancingv2-listener-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticloadbalancingv2-listener-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticloadbalancingv2-listener-return-values"></a>

### Ref
<a name="aws-resource-elasticloadbalancingv2-listener-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the listener.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticloadbalancingv2-listener-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticloadbalancingv2-listener-return-values-fn--getatt-fn--getatt"></a>

`ListenerArn`  <a name="ListenerArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the listener.

## Examples
<a name="aws-resource-elasticloadbalancingv2-listener--examples"></a>

After you create your load balancer using [AWS::ElasticLoadBalancingV2::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html), you can add a listener.

**Topics**
+ [Create an HTTP listener](#aws-resource-elasticloadbalancingv2-listener--examples--Create_an_HTTP_listener)
+ [Create an HTTPS listener](#aws-resource-elasticloadbalancingv2-listener--examples--Create_an_HTTPS_listener)
+ [Create a TCP listener](#aws-resource-elasticloadbalancingv2-listener--examples--Create_a_TCP_listener)
+ [Create a TLS listener](#aws-resource-elasticloadbalancingv2-listener--examples--Create_a_TLS_listener)
+ [Create a UDP listener](#aws-resource-elasticloadbalancingv2-listener--examples--Create_a_UDP_listener)
+ [Create a QUIC listener](#aws-resource-elasticloadbalancingv2-listener--examples--Create_a_QUIC_listener)

### Create an HTTP listener
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_an_HTTP_listener"></a>

The following example creates an HTTP listener with a default action that redirects HTTP requests on port 80 to HTTPS requests on port 443, retaining the original host name, path, and query string.

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_an_HTTP_listener--yaml"></a>

```
myHTTPlistener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: HTTP
    Port: 80
    DefaultActions:
      - Type: redirect
        RedirectConfig:
          Protocol: HTTPS
          Port: 443
          Host: "#{host}"
          Path: "/#{path}"
          Query: "#{query}"
          StatusCode: "HTTP_301"
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_an_HTTP_listener--json"></a>

```
{
    "myHTTPlistener": {
        "Type": "AWS::ElasticLoadBalancingV2::Listener",
        "Properties": {
            "DefaultActions": [
                {
                    "Type": "redirect",
                    "RedirectConfig": {
                        "Protocol": "HTTPS",
                        "Port": 443,
                        "Host": "#{host}",
                        "Path": "/#{path}",
                        "Query": "#{query}",
                        "StatusCode": "HTTP_301"
                    }
                }
            ],
            "LoadBalancerArn": {
                "Ref": "myLoadBalancer"
            },
            "Port": 80,
            "Protocol": "HTTP"
        }
    }
}
```

### Create an HTTPS listener
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_an_HTTPS_listener"></a>

The following example creates an HTTPS listener with a default action that forwards traffic to the specified target group. When you create a secure listener, you must specify a security policy and a certificate. You can create the target group using [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html).

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_an_HTTPS_listener--yaml"></a>

```
myHTTPSListener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: HTTPS
    Port: 443
    SslPolicy: "ELBSecurityPolicy-TLS13-1-2-2021-06"
    Certificates:
      - CertificateArn: "arn:aws:acm:us-west-2:123456789012:certificate/88ca7932-756c-46f1-a70d-03fa7EXAMPLE"
    DefaultActions:
      - Type: forward
        TargetGroupArn: !Ref myTargetGroup
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_an_HTTPS_listener--json"></a>

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
            "SslPolicy": "ELBSecurityPolicy-TLS13-1-2-2021-06",
            "Certificates": [
                {
                    "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/88ca7932-756c-46f1-a70d-03fa7EXAMPLE"
                }
            ],
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": {
                        "Ref": "myTargetGroup"
                    }
                }
            ]
        }
    }
}
```

### Create a TCP listener
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_TCP_listener"></a>

The following example creates a TCP listener with a default action that forwards traffic to the specified target group. You can create the target group using [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html).

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_TCP_listener--yaml"></a>

```
myTCPListener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: TCP
    Port: 80
    DefaultActions:
      - Type: forward
        TargetGroupArn: !Ref myTargetGroup
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_TCP_listener--json"></a>

```
{
    "myTCPListener": {
        "Type": "AWS::ElasticLoadBalancingV2::Listener",
        "Properties": {
            "LoadBalancerArn": {
                "Ref": "myLoadBalancer"
            },
            "Protocol": "TCP",
            "Port": 80,
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": {
                        "Ref": "myTargetGroup"
                    }
                }
            ]
        }
    }
}
```

### Create a TLS listener
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_TLS_listener"></a>

The following example creates a TLS listener with a default action that forwards traffic to the specified target group. When you create a secure listener, you must specify a security policy and a certificate. You can create the target group using [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html).

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_TLS_listener--yaml"></a>

```
myTLSListener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: TLS
    Port: 443
    SslPolicy: "ELBSecurityPolicy-TLS13-1-2-2021-06"
    Certificates:
      - CertificateArn: "arn:aws:acm:us-west-2:123456789012:certificate/88ca7932-756c-46f1-a70d-03fa7EXAMPLE"
    DefaultActions:
      - Type: forward
        TargetGroupArn: !Ref myTargetGroup
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_TLS_listener--json"></a>

```
{
    "myTLSListener": {
        "Type": "AWS::ElasticLoadBalancingV2::Listener",
        "Properties": {
            "LoadBalancerArn": {
                "Ref": "myLoadBalancer"
            },
            "Protocol": "TLS",
            "Port": 443,
            "SslPolicy": "ELBSecurityPolicy-TLS13-1-2-2021-06",
            "Certificates": [
                {
                    "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/88ca7932-756c-46f1-a70d-03fa7EXAMPLE"
                }
            ],
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": {
                        "Ref": "myTargetGroup"
                    }
                }
            ]
        }
    }
}
```

### Create a UDP listener
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_UDP_listener"></a>

The following example creates a UDP listener with a default action that forwards traffic to the specified target group. You can create the target group using [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html).

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_UDP_listener--yaml"></a>

```
myUDPListener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: UDP
    Port: 53
    DefaultActions:
      - Type: forward
        TargetGroupArn: !Ref myTargetGroup
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_UDP_listener--json"></a>

```
{
    "myUDPListener": {
        "Type": "AWS::ElasticLoadBalancingV2::Listener",
        "Properties": {
            "LoadBalancerArn": {
                "Ref": "myLoadBalancer"
            },
            "Protocol": "UDP",
            "Port": 53,
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": {
                        "Ref": "myTargetGroup"
                    }
                }
            ]
        }
    }
}
```

### Create a QUIC listener
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_QUIC_listener"></a>

The following example creates a QUIC listener with a default action that forwards traffic to the specified target group. You can create the target group using [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html).

#### YAML
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_QUIC_listener--yaml"></a>

```
myQUICListener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: QUIC
    Port: 443
    DefaultActions:
      - Type: forward
        TargetGroupArn: !Ref myTargetGroup
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-listener--examples--Create_a_QUIC_listener--json"></a>

```
{
    "myUDPListener": {
        "Type": "AWS::ElasticLoadBalancingV2::Listener",
        "Properties": {
            "LoadBalancerArn": {
                "Ref": "myLoadBalancer"
            },
            "Protocol": "QUIC",
            "Port": 443,
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": {
                        "Ref": "myTargetGroup"
                    }
                }
            ]
        }
    }
}
```

## See also
<a name="aws-resource-elasticloadbalancingv2-listener--seealso"></a>
+ [CreateListener](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateListener.html) in the *Elastic Load Balancing API Reference (version 2015-12-01)*
+ [Listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html) in the *User Guide for Application Load Balancers*
+ [Listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html) in the *User Guide for Network Load Balancers*
+ [Listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-listeners.html) in the *User Guide for Gateway Load Balancers*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
