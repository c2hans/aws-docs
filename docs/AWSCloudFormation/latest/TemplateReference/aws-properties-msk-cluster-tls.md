---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-tls.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster Tls
<a name="aws-properties-msk-cluster-tls"></a>

Details for client authentication using TLS.

## Syntax
<a name="aws-properties-msk-cluster-tls-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-tls-syntax.json"></a>

```
{
  "[CertificateAuthorityArnList](#cfn-msk-cluster-tls-certificateauthorityarnlist)" : {{[ String, ... ]}},
  "[Enabled](#cfn-msk-cluster-tls-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-msk-cluster-tls-syntax.yaml"></a>

```
  [CertificateAuthorityArnList](#cfn-msk-cluster-tls-certificateauthorityarnlist): {{
    - String}}
  [Enabled](#cfn-msk-cluster-tls-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-msk-cluster-tls-properties"></a>

`CertificateAuthorityArnList`  <a name="cfn-msk-cluster-tls-certificateauthorityarnlist"></a>
List of AWS Private CA ARNs.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-msk-cluster-tls-enabled"></a>
TLS authentication is enabled or not.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
