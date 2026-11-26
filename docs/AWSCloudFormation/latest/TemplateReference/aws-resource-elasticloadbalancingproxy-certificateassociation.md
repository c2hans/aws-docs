---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingproxy-certificateassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingProxy::CertificateAssociation

Associates an AWS Certificate Manager (ACM) certificate with an Elastic Load Balancing for Envoy proxy so that the proxy can terminate TLS with it.

When the association is `active`, the certificate is available to the proxy. To serve the certificate, you must also reference it by its ARN in a listener in the proxy's configuration file. The proxy supplies the certificate at runtime, so you don't embed the private key in your configuration.

If an earlier association of the same proxy and certificate failed, remove the failed association with the [DisassociateCertificate](https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_DisassociateCertificate.html) operation before you create this resource again. While the failed association exists, CloudFormation reports that the resource already exists.

Associate the certificate before you reference it in the proxy's configuration file. A listener that references a certificate that isn't associated with the proxy doesn't start. If you create a proxy and its certificate association in the same template, don't reference the certificate in the proxy's configuration file at create time. After the association is `active`, update the proxy's `ConfigurationFile` to reference the certificate by its ARN.

If you remove the association outside CloudFormation, for example with the `DisassociateCertificate` operation, drift detection reports the resource as `DELETED`. A stack update doesn't re-create it. To re-create it, remove the resource from your template and update the stack, then add it back and update again.

A proxy can have at most 25 associated certificates. Associations that are `active` or `associate-in-progress` count toward this limit. Creating one more association fails with `ServiceLimitExceeded`.

Changing `CertificateArn` replaces the association. CloudFormation creates the new association before it deletes the old one. To swap certificates, add the new association in one stack update and remove the old one in a later update.

For more information, see [Terminate TLS with an ACM certificate](https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/tls-acm-certificate.html) in the *Elastic Load Balancing for Envoy User Guide*.

## Syntax
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation-syntax.json"></a>

```json
{
  "Type" : "AWS::ElasticLoadBalancingProxy::CertificateAssociation",
  "Properties" : {
      "[CertificateArn](#cfn-elasticloadbalancingproxy-certificateassociation-certificatearn)" : {{String}},
      "[ProxyArn](#cfn-elasticloadbalancingproxy-certificateassociation-proxyarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation-syntax.yaml"></a>

```yaml
Type: AWS::ElasticLoadBalancingProxy::CertificateAssociation
Properties:
  [CertificateArn](#cfn-elasticloadbalancingproxy-certificateassociation-certificatearn): {{String}}
  [ProxyArn](#cfn-elasticloadbalancingproxy-certificateassociation-proxyarn): {{String}}
```

## Properties
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation-properties"></a>

`CertificateArn`  <a name="cfn-elasticloadbalancingproxy-certificateassociation-certificatearn"></a>
The Amazon Resource Name (ARN) of the ACM certificate to associate with the proxy. The certificate must be in the same AWS account and Region as the proxy. If the certificate is in another account, the association fails because the certificate isn't found.
Elastic Load Balancing for Envoy associates the certificate by using your credentials. You need permission to call `acm:CreateCertificateRelation` on the certificate.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9\-]+:acm:[a-z0-9\-]+:[0-9]{12}:certificate/.+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProxyArn`  <a name="cfn-elasticloadbalancingproxy-certificateassociation-proxyarn"></a>
The ARN of the proxy to associate the certificate with. The proxy must be in the same AWS account and Region as the stack.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]+:elasticloadbalancing:[a-z0-9-]+:[0-9]{12}:proxy/[a-zA-Z0-9-]+:[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation-return-values"></a>

### Ref
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the identifier of the certificate association, such as `arn:aws:elasticloadbalancing:us-east-1:123456789012:proxy/my-proxy:0123456789abcdef/certificate/12345678-1234-1234-1234-123456789012`.

CloudFormation uses this identifier only. No Elastic Load Balancing for Envoy API accepts it.

For more information, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The identifier of the certificate association. This value isn't an ARN that Elastic Load Balancing for Envoy issues, and no Elastic Load Balancing for Envoy API accepts it.

`CertificateId`  <a name="CertificateId-fn::getatt"></a>
The ID of the ACM certificate, taken from the certificate ARN.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the association was created.

`ProxyId`  <a name="ProxyId-fn::getatt"></a>
The ID of the proxy, taken from the proxy ARN.

`ProxyName`  <a name="ProxyName-fn::getatt"></a>
The name of the proxy, taken from the proxy ARN.

`Status`  <a name="Status-fn::getatt"></a>
The status of the association. Valid values are the following:
+ `associate-in-progress` – The certificate is being associated with the proxy.
+ `active` – The certificate is associated and available to the proxy.
+ `associate-failed` – The certificate couldn't be associated with the proxy.
+ `disassociate-in-progress` – The certificate is being removed from the proxy.
+ `disassociated` – The certificate isn't associated with the proxy.
After CloudFormation creates the association, the status is `active`. CloudFormation treats an association in `disassociate-in-progress` or `disassociated` as deleted.

## Examples
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation--examples"></a>

### Example - Associate an ACM certificate with a proxy
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation--examples--Example_-_Associate_an_ACM_certificate_with_a_proxy"></a>

The following example creates a proxy and associates an ACM certificate with it. The proxy's configuration file doesn't reference the certificate, because CloudFormation creates the association after the proxy. After you create the stack, update the configuration file to add a TLS listener that references the certificate ARN. For a sample listener, see Terminate TLS with an ACM certificate in the *Elastic Load Balancing for Envoy User Guide*.

#### JSON
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation--examples--Example_-_Associate_an_ACM_certificate_with_a_proxy--json"></a>

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "ProxyRoleArn": {
      "Type": "String",
      "Description": "ARN of the proxy role"
    },
    "SubnetIds": {
      "Type": "List<AWS::EC2::Subnet::Id>",
      "Description": "At least two subnets in different Availability Zones of the same VPC"
    },
    "SecurityGroupId": {
      "Type": "AWS::EC2::SecurityGroup::Id",
      "Description": "Security group for the proxy"
    },
    "CertificateArn": {
      "Type": "String",
      "Description": "ARN of an ACM certificate in the same account and Region"
    }
  },
  "Resources": {
    "Proxy": {
      "Type": "AWS::ElasticLoadBalancingProxy::Proxy",
      "Properties": {
        "Name": "my-proxy",
        "Type": "envoy",
        "ProxyVersion": "1.40",
        "RoleArn": {
          "Ref": "ProxyRoleArn"
        },
        "IpAddressingConfiguration": {
          "Ipv4Addressability": "internal",
          "Ipv6Addressability": "off"
        },
        "Subnets": {
          "Ref": "SubnetIds"
        },
        "SecurityGroups": [
          {
            "Ref": "SecurityGroupId"
          }
        ],
        "ConfigurationFile": {
          "ConfigurationBytes": {
            "Fn::Base64": "admin:\n  address:\n    socket_address:\n      address: 127.0.0.1\n      port_value: 9901\n\nstatic_resources:\n  listeners:\n  - name: listener_0\n    address:\n      socket_address:\n        address: 0.0.0.0\n        port_value: 80\n    filter_chains:\n    - filters:\n      - name: envoy.filters.network.http_connection_manager\n        typed_config:\n          \"@type\": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager\n          stat_prefix: ingress_http\n          route_config:\n            name: local_route\n            virtual_hosts:\n            - name: local_service\n              domains: [\"*\"]\n              routes:\n              - match:\n                  prefix: \"/\"\n                direct_response:\n                  status: 200\n                  body:\n                    inline_string: \"Hello from ELB for Envoy\\n\"\n          http_filters:\n          - name: envoy.filters.http.router\n            typed_config:\n              \"@type\": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router\n"
          }
        },
        "Attributes": [
          {
            "Key": "envoy.log_level",
            "Value": "info"
          }
        ],
        "Tags": [
          {
            "Key": "environment",
            "Value": "test"
          }
        ]
      }
    },
    "CertificateAssociation": {
      "Type": "AWS::ElasticLoadBalancingProxy::CertificateAssociation",
      "Properties": {
        "ProxyArn": {
          "Ref": "Proxy"
        },
        "CertificateArn": {
          "Ref": "CertificateArn"
        }
      }
    }
  },
  "Outputs": {
    "CertificateAssociationStatus": {
      "Value": {
        "Fn::GetAtt": [
          "CertificateAssociation",
          "Status"
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-elasticloadbalancingproxy-certificateassociation--examples--Example_-_Associate_an_ACM_certificate_with_a_proxy--yaml"></a>

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Parameters:
  ProxyRoleArn:
    Type: String
    Description: ARN of the proxy role
  SubnetIds:
    Type: List<AWS::EC2::Subnet::Id>
    Description: At least two subnets in different Availability Zones of the same VPC
  SecurityGroupId:
    Type: AWS::EC2::SecurityGroup::Id
    Description: Security group for the proxy
  CertificateArn:
    Type: String
    Description: ARN of an ACM certificate in the same account and Region
Resources:
  Proxy:
    Type: AWS::ElasticLoadBalancingProxy::Proxy
    Properties:
      Name: my-proxy
      Type: envoy
      ProxyVersion: '1.40'
      RoleArn:
        Ref: ProxyRoleArn
      IpAddressingConfiguration:
        Ipv4Addressability: internal
        Ipv6Addressability: 'off'
      Subnets:
        Ref: SubnetIds
      SecurityGroups:
        - Ref: SecurityGroupId
      ConfigurationFile:
        ConfigurationBytes:
          Fn::Base64: |
            admin:
              address:
                socket_address:
                  address: 127.0.0.1
                  port_value: 9901

            static_resources:
              listeners:
              - name: listener_0
                address:
                  socket_address:
                    address: 0.0.0.0
                    port_value: 80
                filter_chains:
                - filters:
                  - name: envoy.filters.network.http_connection_manager
                    typed_config:
                      "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
                      stat_prefix: ingress_http
                      route_config:
                        name: local_route
                        virtual_hosts:
                        - name: local_service
                          domains: ["*"]
                          routes:
                          - match:
                              prefix: "/"
                            direct_response:
                              status: 200
                              body:
                                inline_string: "Hello from ELB for Envoy\n"
                      http_filters:
                      - name: envoy.filters.http.router
                        typed_config:
                          "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
      Attributes:
        - Key: envoy.log_level
          Value: info
      Tags:
        - Key: environment
          Value: test
  CertificateAssociation:
    Type: AWS::ElasticLoadBalancingProxy::CertificateAssociation
    Properties:
      ProxyArn:
        Ref: Proxy
      CertificateArn:
        Ref: CertificateArn
Outputs:
  CertificateAssociationStatus:
    Value:
      Fn::GetAtt: [CertificateAssociation, Status]
```
