---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration IdentityCenterConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration"></a>

<a name="aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration-description"></a>The `IdentityCenterConfiguration` property type specifies Property description not available. for an [AWS::EMRContainers::SecurityConfiguration](aws-resource-emrcontainers-securityconfiguration.md).

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration-syntax.json"></a>

```
{
  "[EnableIdentityCenter](#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-enableidentitycenter)" : {{Boolean}},
  "[IdentityCenterApplicationAssignmentRequired](#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterapplicationassignmentrequired)" : {{Boolean}},
  "[IdentityCenterInstanceARN](#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterinstancearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration-syntax.yaml"></a>

```
  [EnableIdentityCenter](#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-enableidentitycenter): {{Boolean}}
  [IdentityCenterApplicationAssignmentRequired](#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterapplicationassignmentrequired): {{Boolean}}
  [IdentityCenterInstanceARN](#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterinstancearn): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration-properties"></a>

`EnableIdentityCenter`  <a name="cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-enableidentitycenter"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityCenterApplicationAssignmentRequired`  <a name="cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterapplicationassignmentrequired"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityCenterInstanceARN`  <a name="cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterinstancearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
