---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-systemsmanagersap-application-componentinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SystemsManagerSAP::Application ComponentInfo
<a name="aws-properties-systemsmanagersap-application-componentinfo"></a>

This is information about the component of your SAP application, such as Web Dispatcher.

## Syntax
<a name="aws-properties-systemsmanagersap-application-componentinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-systemsmanagersap-application-componentinfo-syntax.json"></a>

```
{
  "[ComponentType](#cfn-systemsmanagersap-application-componentinfo-componenttype)" : {{String}},
  "[Ec2InstanceId](#cfn-systemsmanagersap-application-componentinfo-ec2instanceid)" : {{String}},
  "[Sid](#cfn-systemsmanagersap-application-componentinfo-sid)" : {{String}}
}
```

### YAML
<a name="aws-properties-systemsmanagersap-application-componentinfo-syntax.yaml"></a>

```
  [ComponentType](#cfn-systemsmanagersap-application-componentinfo-componenttype): {{String}}
  [Ec2InstanceId](#cfn-systemsmanagersap-application-componentinfo-ec2instanceid): {{String}}
  [Sid](#cfn-systemsmanagersap-application-componentinfo-sid): {{String}}
```

## Properties
<a name="aws-properties-systemsmanagersap-application-componentinfo-properties"></a>

`ComponentType`  <a name="cfn-systemsmanagersap-application-componentinfo-componenttype"></a>
This string is the type of the component.
Accepted value is `WD`.
*Required*: No
*Type*: String
*Allowed values*: `HANA | HANA_NODE | ABAP | ASCS | DIALOG | WEBDISP | WD | ERS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ec2InstanceId`  <a name="cfn-systemsmanagersap-application-componentinfo-ec2instanceid"></a>
This is the Amazon EC2 instance on which your SAP component is running.
Accepted values are alphanumeric.
*Required*: No
*Type*: String
*Pattern*: `^i-[\w\d]{8}$|^i-[\w\d]{17}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Sid`  <a name="cfn-systemsmanagersap-application-componentinfo-sid"></a>
This string is the SAP System ID of the component.
Accepted values are alphanumeric.
*Required*: No
*Type*: String
*Pattern*: `[A-Z][A-Z0-9]{2}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
