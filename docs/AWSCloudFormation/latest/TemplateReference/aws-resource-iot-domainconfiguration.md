---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-domainconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::DomainConfiguration
<a name="aws-resource-iot-domainconfiguration"></a>

Specifies a domain configuration.

## Syntax
<a name="aws-resource-iot-domainconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-domainconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::DomainConfiguration",
  "Properties" : {
      "[ApplicationProtocol](#cfn-iot-domainconfiguration-applicationprotocol)" : {{String}},
      "[AuthenticationType](#cfn-iot-domainconfiguration-authenticationtype)" : {{String}},
      "[AuthorizerConfig](#cfn-iot-domainconfiguration-authorizerconfig)" : {{AuthorizerConfig}},
      "[ClientCertificateConfig](#cfn-iot-domainconfiguration-clientcertificateconfig)" : {{ClientCertificateConfig}},
      "[DomainConfigurationName](#cfn-iot-domainconfiguration-domainconfigurationname)" : {{String}},
      "[DomainConfigurationStatus](#cfn-iot-domainconfiguration-domainconfigurationstatus)" : {{String}},
      "[DomainName](#cfn-iot-domainconfiguration-domainname)" : {{String}},
      "[ServerCertificateArns](#cfn-iot-domainconfiguration-servercertificatearns)" : {{[ String, ... ]}},
      "[ServerCertificateConfig](#cfn-iot-domainconfiguration-servercertificateconfig)" : {{ServerCertificateConfig}},
      "[ServiceType](#cfn-iot-domainconfiguration-servicetype)" : {{String}},
      "[Tags](#cfn-iot-domainconfiguration-tags)" : {{[ Tag, ... ]}},
      "[TlsConfig](#cfn-iot-domainconfiguration-tlsconfig)" : {{TlsConfig}},
      "[ValidationCertificateArn](#cfn-iot-domainconfiguration-validationcertificatearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iot-domainconfiguration-syntax.yaml"></a>

```
Type: AWS::IoT::DomainConfiguration
Properties:
  [ApplicationProtocol](#cfn-iot-domainconfiguration-applicationprotocol): {{String}}
  [AuthenticationType](#cfn-iot-domainconfiguration-authenticationtype): {{String}}
  [AuthorizerConfig](#cfn-iot-domainconfiguration-authorizerconfig): {{
    AuthorizerConfig}}
  [ClientCertificateConfig](#cfn-iot-domainconfiguration-clientcertificateconfig): {{
    ClientCertificateConfig}}
  [DomainConfigurationName](#cfn-iot-domainconfiguration-domainconfigurationname): {{String}}
  [DomainConfigurationStatus](#cfn-iot-domainconfiguration-domainconfigurationstatus): {{String}}
  [DomainName](#cfn-iot-domainconfiguration-domainname): {{String}}
  [ServerCertificateArns](#cfn-iot-domainconfiguration-servercertificatearns): {{
    - String}}
  [ServerCertificateConfig](#cfn-iot-domainconfiguration-servercertificateconfig): {{
    ServerCertificateConfig}}
  [ServiceType](#cfn-iot-domainconfiguration-servicetype): {{String}}
  [Tags](#cfn-iot-domainconfiguration-tags): {{
    - Tag}}
  [TlsConfig](#cfn-iot-domainconfiguration-tlsconfig): {{
    TlsConfig}}
  [ValidationCertificateArn](#cfn-iot-domainconfiguration-validationcertificatearn): {{String}}
```

## Properties
<a name="aws-resource-iot-domainconfiguration-properties"></a>

`ApplicationProtocol`  <a name="cfn-iot-domainconfiguration-applicationprotocol"></a>
An enumerated string that speciﬁes the application-layer protocol.
*Required*: No
*Type*: String
*Allowed values*: `SECURE_MQTT | MQTT_WSS | HTTPS | DEFAULT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthenticationType`  <a name="cfn-iot-domainconfiguration-authenticationtype"></a>
An enumerated string that speciﬁes the authentication type.
*Required*: No
*Type*: String
*Allowed values*: `AWS_X509 | CUSTOM_AUTH | AWS_SIGV4 | CUSTOM_AUTH_X509 | DEFAULT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizerConfig`  <a name="cfn-iot-domainconfiguration-authorizerconfig"></a>
An object that specifies the authorization service for a domain.
*Required*: No
*Type*: [AuthorizerConfig](aws-properties-iot-domainconfiguration-authorizerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientCertificateConfig`  <a name="cfn-iot-domainconfiguration-clientcertificateconfig"></a>
An object that speciﬁes the client certificate conﬁguration for a domain.
*Required*: No
*Type*: [ClientCertificateConfig](aws-properties-iot-domainconfiguration-clientcertificateconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainConfigurationName`  <a name="cfn-iot-domainconfiguration-domainconfigurationname"></a>
The name of the domain configuration. This value must be unique to a region.
*Required*: No
*Type*: String
*Pattern*: `^[\w.-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainConfigurationStatus`  <a name="cfn-iot-domainconfiguration-domainconfigurationstatus"></a>
The status to which the domain configuration should be updated.
Valid values: `ENABLED` \| `DISABLED`
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-iot-domainconfiguration-domainname"></a>
The name of the domain.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerCertificateArns`  <a name="cfn-iot-domainconfiguration-servercertificatearns"></a>
The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake. Currently you can specify only one certificate ARN. This value is not required for AWS-managed domains.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `2048 | 1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerCertificateConfig`  <a name="cfn-iot-domainconfiguration-servercertificateconfig"></a>
The server certificate configuration.
For more information, see [Configurable endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable.html) from the AWS IoT Core Developer Guide.
*Required*: No
*Type*: [ServerCertificateConfig](aws-properties-iot-domainconfiguration-servercertificateconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceType`  <a name="cfn-iot-domainconfiguration-servicetype"></a>
The type of service delivered by the endpoint.
AWS IoT Core currently supports only the `DATA` service type.
*Required*: No
*Type*: String
*Allowed values*: `DATA | CREDENTIAL_PROVIDER | JOBS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iot-domainconfiguration-tags"></a>
Metadata which can be used to manage the domain configuration.
For URI Request parameters use format: ...key1=value1&key2=value2...
For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."
For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-domainconfiguration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TlsConfig`  <a name="cfn-iot-domainconfiguration-tlsconfig"></a>
An object that specifies the TLS configuration for a domain.
*Required*: No
*Type*: [TlsConfig](aws-properties-iot-domainconfiguration-tlsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidationCertificateArn`  <a name="cfn-iot-domainconfiguration-validationcertificatearn"></a>
The certificate used to validate the server certificate and prove domain name ownership. This certificate must be signed by a public certificate authority. This value is not required for AWS-managed domains.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\d{1}:\d{12}:certificate/[a-zA-Z0-9/-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iot-domainconfiguration-return-values"></a>

### Ref
<a name="aws-resource-iot-domainconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the domain configuration name. For example:

 `{ "Ref": "MyDomainConfiguration" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iot-domainconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iot-domainconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the domain configuration.

`DomainType`  <a name="DomainType-fn::getatt"></a>
The type of service delivered by the domain.

`ServerCertificates`  <a name="ServerCertificates-fn::getatt"></a>
The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake. Currently you can specify only one certificate ARN. This value is not required for AWS-managed domains.
