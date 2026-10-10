---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityagent-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::Integration
<a name="aws-resource-securityagent-integration"></a>

Creates a new integration with a third-party provider, such as GitHub, for code review and remediation.

## Syntax
<a name="aws-resource-securityagent-integration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityagent-integration-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityAgent::Integration",
  "Properties" : {
      "[DisplayName](#cfn-securityagent-integration-displayname)" : {{String}},
      "[KmsKeyId](#cfn-securityagent-integration-kmskeyid)" : {{String}},
      "[PrivateConnectionName](#cfn-securityagent-integration-privateconnectionname)" : {{String}},
      "[Provider](#cfn-securityagent-integration-provider)" : {{String}},
      "[ProviderInput](#cfn-securityagent-integration-providerinput)" : {{ProviderInput}},
      "[Tags](#cfn-securityagent-integration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-securityagent-integration-syntax.yaml"></a>

```
Type: AWS::SecurityAgent::Integration
Properties:
  [DisplayName](#cfn-securityagent-integration-displayname): {{String}}
  [KmsKeyId](#cfn-securityagent-integration-kmskeyid): {{String}}
  [PrivateConnectionName](#cfn-securityagent-integration-privateconnectionname): {{String}}
  [Provider](#cfn-securityagent-integration-provider): {{String}}
  [ProviderInput](#cfn-securityagent-integration-providerinput): {{
    ProviderInput}}
  [Tags](#cfn-securityagent-integration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-securityagent-integration-properties"></a>

`DisplayName`  <a name="cfn-securityagent-integration-displayname"></a>
The display name of the integration.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-securityagent-integration-kmskeyid"></a>
Identifier of a KMS key. Can be a key ID, key ARN, alias name, or alias ARN.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivateConnectionName`  <a name="cfn-securityagent-integration-privateconnectionname"></a>
The name of the private connection used to reach the integration's self-hosted instance over private networking, if one is configured.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Provider`  <a name="cfn-securityagent-integration-provider"></a>
The integration provider.
*Required*: Yes
*Type*: String
*Allowed values*: `GITHUB | GITLAB | BITBUCKET | CONFLUENCE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProviderInput`  <a name="cfn-securityagent-integration-providerinput"></a>
The provider-specific input for creating an integration. This is a union type that contains provider-specific configuration.
*Required*: No
*Type*: [ProviderInput](aws-properties-securityagent-integration-providerinput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-securityagent-integration-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-securityagent-integration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityagent-integration-return-values"></a>

### Ref
<a name="aws-resource-securityagent-integration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-securityagent-integration-return-values-fn--getatt"></a>

####
<a name="aws-resource-securityagent-integration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`InstallationId`  <a name="InstallationId-fn::getatt"></a>
The installation identifier from the integration provider.

`IntegrationId`  <a name="IntegrationId-fn::getatt"></a>
The unique identifier of the integration.

`ProviderType`  <a name="ProviderType-fn::getatt"></a>
The type of the integration provider.

`TargetUrl`  <a name="TargetUrl-fn::getatt"></a>
The HTTPS URL of the customer self-hosted instance, such as a GitHub Enterprise Server or self-managed GitLab instance. This value is absent for SaaS integrations.
