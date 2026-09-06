---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnecttlsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ServiceConnectTlsConfiguration
<a name="aws-properties-ecs-service-serviceconnecttlsconfiguration"></a>

The key that encrypts and decrypts your resources for Service Connect TLS.

## Syntax
<a name="aws-properties-ecs-service-serviceconnecttlsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-serviceconnecttlsconfiguration-syntax.json"></a>

```
{
  "[IssuerCertificateAuthority](#cfn-ecs-service-serviceconnecttlsconfiguration-issuercertificateauthority)" : {{ServiceConnectTlsCertificateAuthority}},
  "[KmsKey](#cfn-ecs-service-serviceconnecttlsconfiguration-kmskey)" : {{String}},
  "[RoleArn](#cfn-ecs-service-serviceconnecttlsconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-serviceconnecttlsconfiguration-syntax.yaml"></a>

```
  [IssuerCertificateAuthority](#cfn-ecs-service-serviceconnecttlsconfiguration-issuercertificateauthority): {{
    ServiceConnectTlsCertificateAuthority}}
  [KmsKey](#cfn-ecs-service-serviceconnecttlsconfiguration-kmskey): {{String}}
  [RoleArn](#cfn-ecs-service-serviceconnecttlsconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-serviceconnecttlsconfiguration-properties"></a>

`IssuerCertificateAuthority`  <a name="cfn-ecs-service-serviceconnecttlsconfiguration-issuercertificateauthority"></a>
The signer certificate authority.
*Required*: Yes
*Type*: [ServiceConnectTlsCertificateAuthority](aws-properties-ecs-service-serviceconnecttlscertificateauthority.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKey`  <a name="cfn-ecs-service-serviceconnecttlsconfiguration-kmskey"></a>
The AWS Key Management Service key.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ecs-service-serviceconnecttlsconfiguration-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that's associated with the Service Connect TLS.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
