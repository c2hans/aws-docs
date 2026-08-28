---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-domainconfiguration-tlsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::DomainConfiguration TlsConfig
<a name="aws-properties-iot-domainconfiguration-tlsconfig"></a>

An object that specifies the TLS configuration for a domain.

## Syntax
<a name="aws-properties-iot-domainconfiguration-tlsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-domainconfiguration-tlsconfig-syntax.json"></a>

```
{
  "[SecurityPolicy](#cfn-iot-domainconfiguration-tlsconfig-securitypolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-domainconfiguration-tlsconfig-syntax.yaml"></a>

```
  [SecurityPolicy](#cfn-iot-domainconfiguration-tlsconfig-securitypolicy): {{String}}
```

## Properties
<a name="aws-properties-iot-domainconfiguration-tlsconfig-properties"></a>

`SecurityPolicy`  <a name="cfn-iot-domainconfiguration-tlsconfig-securitypolicy"></a>
The security policy for a domain configuration. For more information, see [Security policies ](https://docs.aws.amazon.com/iot/latest/developerguide/transport-security.html#tls-policy-table) in the *AWS IoT Core developer guide*.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
