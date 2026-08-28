---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-certificatemanager-account-expiryeventsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::Account ExpiryEventsConfiguration
<a name="aws-properties-certificatemanager-account-expiryeventsconfiguration"></a>

Object containing expiration events options associated with an AWS account. For more information, see [ExpiryEventsConfiguration](https://docs.aws.amazon.com/acm/latest/APIReference/API_ExpiryEventsConfiguration.html) in the API reference.

## Syntax
<a name="aws-properties-certificatemanager-account-expiryeventsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-certificatemanager-account-expiryeventsconfiguration-syntax.json"></a>

```
{
  "[DaysBeforeExpiry](#cfn-certificatemanager-account-expiryeventsconfiguration-daysbeforeexpiry)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-certificatemanager-account-expiryeventsconfiguration-syntax.yaml"></a>

```
  [DaysBeforeExpiry](#cfn-certificatemanager-account-expiryeventsconfiguration-daysbeforeexpiry): {{Integer}}
```

## Properties
<a name="aws-properties-certificatemanager-account-expiryeventsconfiguration-properties"></a>

`DaysBeforeExpiry`  <a name="cfn-certificatemanager-account-expiryeventsconfiguration-daysbeforeexpiry"></a>
This option specifies the number of days prior to certificate expiration when ACM starts generating `EventBridge` events. ACM sends one event per day per certificate until the certificate expires. By default, accounts receive events starting 45 days before certificate expiration.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `45`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
