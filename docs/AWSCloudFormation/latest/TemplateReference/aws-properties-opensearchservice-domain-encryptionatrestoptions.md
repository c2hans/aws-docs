---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-encryptionatrestoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain EncryptionAtRestOptions
<a name="aws-properties-opensearchservice-domain-encryptionatrestoptions"></a>

Whether the domain should encrypt data at rest, and if so, the AWS Key Management Service key to use.

## Syntax
<a name="aws-properties-opensearchservice-domain-encryptionatrestoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-encryptionatrestoptions-syntax.json"></a>

```
{
  "[Enabled](#cfn-opensearchservice-domain-encryptionatrestoptions-enabled)" : {{Boolean}},
  "[KmsKeyId](#cfn-opensearchservice-domain-encryptionatrestoptions-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-encryptionatrestoptions-syntax.yaml"></a>

```
  [Enabled](#cfn-opensearchservice-domain-encryptionatrestoptions-enabled): {{Boolean}}
  [KmsKeyId](#cfn-opensearchservice-domain-encryptionatrestoptions-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-encryptionatrestoptions-properties"></a>

`Enabled`  <a name="cfn-opensearchservice-domain-encryptionatrestoptions-enabled"></a>
Specify `true` to enable encryption at rest. Required if you enable fine-grained access control in [AdvancedSecurityOptionsInput](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html).
If no encryption at rest options were initially specified in the template, updating this property by adding it causes no interruption. However, if you change this property after it's already been set within a template, the domain is deleted and recreated in order to modify the property.
*Required*: Conditional
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`KmsKeyId`  <a name="cfn-opensearchservice-domain-encryptionatrestoptions-kmskeyid"></a>
The KMS key ID. Takes the form `1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a`. Required if you enable encryption at rest.
You can also use `keyAlias` as a value.
If no encryption at rest options were initially specified in the template, updating this property by adding it causes no interruption. However, if you change this property after it's already been set within a template, the domain is deleted and recreated in order to modify the property.
*Required*: Conditional
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also
<a name="aws-properties-opensearchservice-domain-encryptionatrestoptions--seealso"></a>
+ [CreateDomain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configuration-api.html#configuration-api-actions-createdomain) in the *Amazon OpenSearch Service Developer Guide*.
