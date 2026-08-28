---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-servicesetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::ServiceSetting
<a name="aws-resource-ssm-servicesetting"></a>

The service setting data structure.

`ServiceSetting` is an account-level setting for an AWS service. This setting defines how a user interacts with or uses a service or a feature of a service. For example, if an AWS service charges money to the account based on feature or service usage, then the AWS service team might create a default setting of "false". This means the user can't use this feature unless they change the setting to "true" and intentionally opt in for a paid feature.

Services map a `SettingId` object to a setting value. AWS services teams define the default value for a `SettingId`. You can't create a new `SettingId`, but you can overwrite the default value if you have the `ssm:UpdateServiceSetting` permission for the setting. Use the UpdateServiceSetting API operation to change the default setting. Or, use the ResetServiceSetting to change the value back to the original value defined by the AWS service team.

## Syntax
<a name="aws-resource-ssm-servicesetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-servicesetting-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::ServiceSetting",
  "Properties" : {
      "[SettingId](#cfn-ssm-servicesetting-settingid)" : {{String}},
      "[SettingValue](#cfn-ssm-servicesetting-settingvalue)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ssm-servicesetting-syntax.yaml"></a>

```
Type: AWS::SSM::ServiceSetting
Properties:
  [SettingId](#cfn-ssm-servicesetting-settingid): {{String}}
  [SettingValue](#cfn-ssm-servicesetting-settingvalue): {{String}}
```

## Properties
<a name="aws-resource-ssm-servicesetting-properties"></a>

`SettingId`  <a name="cfn-ssm-servicesetting-settingid"></a>
The ID of the service setting.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SettingValue`  <a name="cfn-ssm-servicesetting-settingvalue"></a>
The value of the service setting.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssm-servicesetting-return-values"></a>

### Ref
<a name="aws-resource-ssm-servicesetting-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssm-servicesetting-return-values-fn--getatt"></a>

####
<a name="aws-resource-ssm-servicesetting-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the service setting.

`LastModifiedDate`  <a name="LastModifiedDate-fn::getatt"></a>
The last time the service setting was modified.

`LastModifiedUser`  <a name="LastModifiedUser-fn::getatt"></a>
The ARN of the last modified user. This field is populated only if the setting value was overwritten.

`Status`  <a name="Status-fn::getatt"></a>
The status of the service setting. The value can be Default, Customized or PendingUpdate.
+ Default: The current setting uses a default value provisioned by the AWS service team.
+ Customized: The current setting use a custom value specified by the customer.
+ PendingUpdate: The current setting uses a default or custom value, but a setting change request is pending approval.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
