---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-kafkaclustersasloauthbearerauthentication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator KafkaClusterSaslOAuthBearerAuthentication
<a name="aws-properties-msk-replicator-kafkaclustersasloauthbearerauthentication"></a>

<a name="aws-properties-msk-replicator-kafkaclustersasloauthbearerauthentication-description"></a>The `KafkaClusterSaslOAuthBearerAuthentication` property type specifies Property description not available. for an [AWS::MSK::Replicator](aws-resource-msk-replicator.md).

## Syntax
<a name="aws-properties-msk-replicator-kafkaclustersasloauthbearerauthentication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-kafkaclustersasloauthbearerauthentication-syntax.json"></a>

```
{
  "[ClientCredentials](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-clientcredentials)" : {{KafkaClusterOAuthClientCredentials}},
  "[ClientCredentialsAssertion](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-clientcredentialsassertion)" : {{KafkaClusterOAuthClientCredentialsAssertion}},
  "[IamJwtBearer](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-iamjwtbearer)" : {{KafkaClusterOAuthIamJwtBearer}},
  "[Scope](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-scope)" : {{String}},
  "[TokenEndpointAuthenticationMethod](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-tokenendpointauthenticationmethod)" : {{String}},
  "[TokenEndpointTlsCertificateArn](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-tokenendpointtlscertificatearn)" : {{String}},
  "[TokenEndpointUrl](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-tokenendpointurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-kafkaclustersasloauthbearerauthentication-syntax.yaml"></a>

```
  [ClientCredentials](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-clientcredentials): {{
    KafkaClusterOAuthClientCredentials}}
  [ClientCredentialsAssertion](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-clientcredentialsassertion): {{
    KafkaClusterOAuthClientCredentialsAssertion}}
  [IamJwtBearer](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-iamjwtbearer): {{
    KafkaClusterOAuthIamJwtBearer}}
  [Scope](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-scope): {{String}}
  [TokenEndpointAuthenticationMethod](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-tokenendpointauthenticationmethod): {{String}}
  [TokenEndpointTlsCertificateArn](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-tokenendpointtlscertificatearn): {{String}}
  [TokenEndpointUrl](#cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-tokenendpointurl): {{String}}
```

## Properties
<a name="aws-properties-msk-replicator-kafkaclustersasloauthbearerauthentication-properties"></a>

`ClientCredentials`  <a name="cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-clientcredentials"></a>
Property description not available.
*Required*: No
*Type*: [KafkaClusterOAuthClientCredentials](aws-properties-msk-replicator-kafkaclusteroauthclientcredentials.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientCredentialsAssertion`  <a name="cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-clientcredentialsassertion"></a>
Property description not available.
*Required*: No
*Type*: [KafkaClusterOAuthClientCredentialsAssertion](aws-properties-msk-replicator-kafkaclusteroauthclientcredentialsassertion.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IamJwtBearer`  <a name="cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-iamjwtbearer"></a>
Property description not available.
*Required*: No
*Type*: [KafkaClusterOAuthIamJwtBearer](aws-properties-msk-replicator-kafkaclusteroauthiamjwtbearer.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scope`  <a name="cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-scope"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenEndpointAuthenticationMethod`  <a name="cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-tokenendpointauthenticationmethod"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `POST | BASIC | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenEndpointTlsCertificateArn`  <a name="cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-tokenendpointtlscertificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenEndpointUrl`  <a name="cfn-msk-replicator-kafkaclustersasloauthbearerauthentication-tokenendpointurl"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
