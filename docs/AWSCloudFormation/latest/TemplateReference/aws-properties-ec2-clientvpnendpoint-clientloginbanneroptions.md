---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint ClientLoginBannerOptions
<a name="aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions"></a>

Options for enabling a customizable text banner that will be displayed on AWS provided clients when a VPN session is established.

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions-syntax.json"></a>

```
{
  "[BannerText](#cfn-ec2-clientvpnendpoint-clientloginbanneroptions-bannertext)" : {{String}},
  "[Enabled](#cfn-ec2-clientvpnendpoint-clientloginbanneroptions-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions-syntax.yaml"></a>

```
  [BannerText](#cfn-ec2-clientvpnendpoint-clientloginbanneroptions-bannertext): {{String}}
  [Enabled](#cfn-ec2-clientvpnendpoint-clientloginbanneroptions-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions-properties"></a>

`BannerText`  <a name="cfn-ec2-clientvpnendpoint-clientloginbanneroptions-bannertext"></a>
Customizable text that will be displayed in a banner on AWS provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-ec2-clientvpnendpoint-clientloginbanneroptions-enabled"></a>
Enable or disable a customizable text banner that will be displayed on AWS provided clients when a VPN session is established.
Valid values: `true | false`
Default value: `false`
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
