---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listener-listenerattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::Listener ListenerAttribute
<a name="aws-properties-elasticloadbalancingv2-listener-listenerattribute"></a>

Information about a listener attribute.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listener-listenerattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listener-listenerattribute-syntax.json"></a>

```
{
  "[Key](#cfn-elasticloadbalancingv2-listener-listenerattribute-key)" : {{String}},
  "[Value](#cfn-elasticloadbalancingv2-listener-listenerattribute-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listener-listenerattribute-syntax.yaml"></a>

```
  [Key](#cfn-elasticloadbalancingv2-listener-listenerattribute-key): {{String}}
  [Value](#cfn-elasticloadbalancingv2-listener-listenerattribute-value): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listener-listenerattribute-properties"></a>

`Key`  <a name="cfn-elasticloadbalancingv2-listener-listenerattribute-key"></a>
The name of the attribute.
The following attribute is supported by Network Load Balancers, and Gateway Load Balancers.
+ `tcp.idle_timeout.seconds` - The tcp idle timeout value, in seconds. The valid range is 60-6000 seconds. The default is 350 seconds.
The following attributes are only supported by Application Load Balancers.
+ `routing.http.request.x_amzn_mtls_clientcert_serial_number.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Serial-Number** HTTP request header.
+ `routing.http.request.x_amzn_mtls_clientcert_issuer.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Issuer** HTTP request header.
+ `routing.http.request.x_amzn_mtls_clientcert_subject.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Subject** HTTP request header.
+ `routing.http.request.x_amzn_mtls_clientcert_validity.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Validity** HTTP request header.
+ `routing.http.request.x_amzn_mtls_clientcert_leaf.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert-Leaf** HTTP request header.
+ `routing.http.request.x_amzn_mtls_clientcert.header_name` - Enables you to modify the header name of the **X-Amzn-Mtls-Clientcert** HTTP request header.
+ `routing.http.request.x_amzn_tls_version.header_name` - Enables you to modify the header name of the **X-Amzn-Tls-Version** HTTP request header.
+ `routing.http.request.x_amzn_tls_cipher_suite.header_name` - Enables you to modify the header name of the **X-Amzn-Tls-Cipher-Suite** HTTP request header.
+ `routing.http.response.server.enabled` - Enables you to allow or remove the HTTP response server header.
+ `routing.http.response.strict_transport_security.header_value` - Informs browsers that the site should only be accessed using HTTPS, and that any future attempts to access it using HTTP should automatically be converted to HTTPS.
+ `routing.http.response.access_control_allow_origin.header_value` - Specifies which origins are allowed to access the server.
+ `routing.http.response.access_control_allow_methods.header_value` - Returns which HTTP methods are allowed when accessing the server from a different origin.
+ `routing.http.response.access_control_allow_headers.header_value` - Specifies which headers can be used during the request.
+ `routing.http.response.access_control_allow_credentials.header_value` - Indicates whether the browser should include credentials such as cookies or authentication when making requests.
+ `routing.http.response.access_control_expose_headers.header_value` - Returns which headers the browser can expose to the requesting client.
+ `routing.http.response.access_control_max_age.header_value` - Specifies how long the results of a preflight request can be cached, in seconds.
+ `routing.http.response.content_security_policy.header_value` - Specifies restrictions enforced by the browser to help minimize the risk of certain types of security threats.
+ `routing.http.response.x_content_type_options.header_value` - Indicates whether the MIME types advertised in the **Content-Type** headers should be followed and not be changed.
+ `routing.http.response.x_frame_options.header_value` - Indicates whether the browser is allowed to render a page in a **frame**, **iframe**, **embed** or **object**.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9._]+$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-elasticloadbalancingv2-listener-listenerattribute-value"></a>
The value of the attribute.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-listener-listenerattribute--examples"></a>

###
<a name="aws-properties-elasticloadbalancingv2-listener-listenerattribute--examples--"></a>

The following example defines a TCP listener, specifying the `tcp.idle_timeout.seconds` attribute.

#### YAML
<a name="aws-properties-elasticloadbalancingv2-listener-listenerattribute--examples----yaml"></a>

```
myTCPListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TCP
      Port: 80
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
      ListenerAttributes:
        - Key: tcp.idle_timeout.seconds
          Value: 500
```

#### JSON
<a name="aws-properties-elasticloadbalancingv2-listener-listenerattribute--examples----json"></a>

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
            ],
            "ListenerAttributes": [
                {
                    "Key": "tcp.idle_timeout.seconds",
                    "Value": 500
                }
            ]
        }
    }
}
```
