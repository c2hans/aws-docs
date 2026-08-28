---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emrcontainers-securityconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration
<a name="aws-resource-emrcontainers-securityconfiguration"></a>

Creates a security configuration. Security configurations in Amazon EMR on EKS are templates for different security setups. You can use security configurations to configure the AWS Lake Formation integration setup. You can also create a security configuration to re-use a security setup each time you create a virtual cluster.

## Syntax
<a name="aws-resource-emrcontainers-securityconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emrcontainers-securityconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::EMRContainers::SecurityConfiguration",
  "Properties" : {
      "[ContainerProvider](#cfn-emrcontainers-securityconfiguration-containerprovider)" : {{ContainerProvider}},
      "[Name](#cfn-emrcontainers-securityconfiguration-name)" : {{String}},
      "[SecurityConfigurationData](#cfn-emrcontainers-securityconfiguration-securityconfigurationdata)" : {{SecurityConfigurationData}},
      "[Tags](#cfn-emrcontainers-securityconfiguration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-emrcontainers-securityconfiguration-syntax.yaml"></a>

```
Type: AWS::EMRContainers::SecurityConfiguration
Properties:
  [ContainerProvider](#cfn-emrcontainers-securityconfiguration-containerprovider): {{
    ContainerProvider}}
  [Name](#cfn-emrcontainers-securityconfiguration-name): {{String}}
  [SecurityConfigurationData](#cfn-emrcontainers-securityconfiguration-securityconfigurationdata): {{
    SecurityConfigurationData}}
  [Tags](#cfn-emrcontainers-securityconfiguration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-emrcontainers-securityconfiguration-properties"></a>

`ContainerProvider`  <a name="cfn-emrcontainers-securityconfiguration-containerprovider"></a>
The information about the container provider.
*Required*: No
*Type*: [ContainerProvider](aws-properties-emrcontainers-securityconfiguration-containerprovider.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-emrcontainers-securityconfiguration-name"></a>
The name of the security configuration.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityConfigurationData`  <a name="cfn-emrcontainers-securityconfiguration-securityconfigurationdata"></a>
Security configuration inputs for the request.
*Required*: Yes
*Type*: [SecurityConfigurationData](aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-emrcontainers-securityconfiguration-tags"></a>
The tags to assign to the security configuration.
*Required*: No
*Type*: Array of [Tag](aws-properties-emrcontainers-securityconfiguration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-emrcontainers-securityconfiguration-return-values"></a>

### Ref
<a name="aws-resource-emrcontainers-securityconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-emrcontainers-securityconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-emrcontainers-securityconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN (Amazon Resource Name) of the security configuration.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the security configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
