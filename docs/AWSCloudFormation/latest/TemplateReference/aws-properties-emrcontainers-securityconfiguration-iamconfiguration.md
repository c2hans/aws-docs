---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-iamconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration IAMConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration"></a>

Contains the IAM settings for a security configuration, including the system role used for authentication.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration-syntax.json"></a>

```
{
  "[SystemRole](#cfn-emrcontainers-securityconfiguration-iamconfiguration-systemrole)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration-syntax.yaml"></a>

```
  [SystemRole](#cfn-emrcontainers-securityconfiguration-iamconfiguration-systemrole): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-iamconfiguration-properties"></a>

`SystemRole`  <a name="cfn-emrcontainers-securityconfiguration-iamconfiguration-systemrole"></a>
The Amazon Resource Name (ARN) of the system role used by the security configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):iam::\d{12}:role/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
