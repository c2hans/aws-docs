---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-notifications-organizationalunitassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Notifications::OrganizationalUnitAssociation
<a name="aws-resource-notifications-organizationalunitassociation"></a>

<a name="aws-resource-notifications-organizationalunitassociation-description"></a>The `AWS::Notifications::OrganizationalUnitAssociation` resource Property description not available. for Notifications.

## Syntax
<a name="aws-resource-notifications-organizationalunitassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-notifications-organizationalunitassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Notifications::OrganizationalUnitAssociation",
  "Properties" : {
      "[NotificationConfigurationArn](#cfn-notifications-organizationalunitassociation-notificationconfigurationarn)" : {{String}},
      "[OrganizationalUnitId](#cfn-notifications-organizationalunitassociation-organizationalunitid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-notifications-organizationalunitassociation-syntax.yaml"></a>

```
Type: AWS::Notifications::OrganizationalUnitAssociation
Properties:
  [NotificationConfigurationArn](#cfn-notifications-organizationalunitassociation-notificationconfigurationarn): {{String}}
  [OrganizationalUnitId](#cfn-notifications-organizationalunitassociation-organizationalunitid): {{String}}
```

## Properties
<a name="aws-resource-notifications-organizationalunitassociation-properties"></a>

`NotificationConfigurationArn`  <a name="cfn-notifications-organizationalunitassociation-notificationconfigurationarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OrganizationalUnitId`  <a name="cfn-notifications-organizationalunitassociation-organizationalunitid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(r-[0-9a-z]{4,32})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-notifications-organizationalunitassociation-return-values"></a>

### Ref
<a name="aws-resource-notifications-organizationalunitassociation-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
