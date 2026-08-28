---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint DirectoryServiceAuthenticationRequest
<a name="aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest"></a>

Describes the Active Directory to be used for client authentication.

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest-syntax.json"></a>

```
{
  "[DirectoryId](#cfn-ec2-clientvpnendpoint-directoryserviceauthenticationrequest-directoryid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest-syntax.yaml"></a>

```
  [DirectoryId](#cfn-ec2-clientvpnendpoint-directoryserviceauthenticationrequest-directoryid): {{String}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest-properties"></a>

`DirectoryId`  <a name="cfn-ec2-clientvpnendpoint-directoryserviceauthenticationrequest-directoryid"></a>
The ID of the Active Directory to be used for authentication.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
