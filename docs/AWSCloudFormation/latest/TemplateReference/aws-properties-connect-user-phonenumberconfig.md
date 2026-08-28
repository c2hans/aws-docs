---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-user-phonenumberconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User PhoneNumberConfig
<a name="aws-properties-connect-user-phonenumberconfig"></a>

Configuration settings for phone type and phone number.

## Syntax
<a name="aws-properties-connect-user-phonenumberconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-user-phonenumberconfig-syntax.json"></a>

```
{
  "[Channel](#cfn-connect-user-phonenumberconfig-channel)" : {{String}},
  "[PhoneNumber](#cfn-connect-user-phonenumberconfig-phonenumber)" : {{String}},
  "[PhoneType](#cfn-connect-user-phonenumberconfig-phonetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-user-phonenumberconfig-syntax.yaml"></a>

```
  [Channel](#cfn-connect-user-phonenumberconfig-channel): {{String}}
  [PhoneNumber](#cfn-connect-user-phonenumberconfig-phonenumber): {{String}}
  [PhoneType](#cfn-connect-user-phonenumberconfig-phonetype): {{String}}
```

## Properties
<a name="aws-properties-connect-user-phonenumberconfig-properties"></a>

`Channel`  <a name="cfn-connect-user-phonenumberconfig-channel"></a>
The channel for this phone number configuration. **Only `VOICE` is supported for this data type.**
*Required*: Yes
*Type*: String
*Allowed values*: `VOICE | CHAT | TASK | EMAIL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhoneNumber`  <a name="cfn-connect-user-phonenumberconfig-phonenumber"></a>
The phone number for the user's desk phone.
*Required*: No
*Type*: String
*Pattern*: `\+[1-9]\d{1,14}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhoneType`  <a name="cfn-connect-user-phonenumberconfig-phonetype"></a>
The phone type. Valid values: SOFT\_PHONE, DESK\_PHONE.
*Required*: Yes
*Type*: String
*Allowed values*: `SOFT_PHONE | DESK_PHONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
