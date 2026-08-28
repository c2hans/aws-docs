---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::AccountAuditConfiguration CertExpirationCheckCustomConfiguration
<a name="aws-properties-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration"></a>

Configuration structure containing settings for the device certificate expiration check.

## Syntax
<a name="aws-properties-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration-syntax.json"></a>

```
{
  "[CertExpirationThresholdInDays](#cfn-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration-certexpirationthresholdindays)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration-syntax.yaml"></a>

```
  [CertExpirationThresholdInDays](#cfn-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration-certexpirationthresholdindays): {{String}}
```

## Properties
<a name="aws-properties-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration-properties"></a>

`CertExpirationThresholdInDays`  <a name="cfn-iot-accountauditconfiguration-certexpirationcheckcustomconfiguration-certexpirationthresholdindays"></a>
The number of days before expiration that defines when a device certificate is considered to be approaching expiration. The check will report a finding if a certificate will expire within this number of days.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
