---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration IdentityCenterConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration"></a>

Contains the IAM Identity Center settings for a security configuration, including instance ARN, application assignment requirements, and application ARN.

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
Specifies whether Identity Center is enabled for the security configuration.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityCenterApplicationAssignmentRequired`  <a name="cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterapplicationassignmentrequired"></a>
Specifies whether user assignment is required for the Identity Center application.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityCenterInstanceARN`  <a name="cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterinstancearn"></a>
The Amazon Resource Name (ARN) of the Identity Center instance.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
