---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-server-identityproviderdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Server IdentityProviderDetails
<a name="aws-properties-transfer-server-identityproviderdetails"></a>

Required when `IdentityProviderType` is set to `AWS_DIRECTORY_SERVICE`, `AWS_LAMBDA` or `API_GATEWAY`. Accepts an array containing all of the information required to use a directory in `AWS_DIRECTORY_SERVICE` or invoke a customer-supplied authentication API, including the API Gateway URL. Cannot be specified when `IdentityProviderType` is set to `SERVICE_MANAGED`.

## Syntax
<a name="aws-properties-transfer-server-identityproviderdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-server-identityproviderdetails-syntax.json"></a>

```
{
  "[DirectoryId](#cfn-transfer-server-identityproviderdetails-directoryid)" : {{String}},
  "[Function](#cfn-transfer-server-identityproviderdetails-function)" : {{String}},
  "[InvocationRole](#cfn-transfer-server-identityproviderdetails-invocationrole)" : {{String}},
  "[SftpAuthenticationMethods](#cfn-transfer-server-identityproviderdetails-sftpauthenticationmethods)" : {{String}},
  "[Url](#cfn-transfer-server-identityproviderdetails-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-server-identityproviderdetails-syntax.yaml"></a>

```
  [DirectoryId](#cfn-transfer-server-identityproviderdetails-directoryid): {{String}}
  [Function](#cfn-transfer-server-identityproviderdetails-function): {{String}}
  [InvocationRole](#cfn-transfer-server-identityproviderdetails-invocationrole): {{String}}
  [SftpAuthenticationMethods](#cfn-transfer-server-identityproviderdetails-sftpauthenticationmethods): {{String}}
  [Url](#cfn-transfer-server-identityproviderdetails-url): {{String}}
```

## Properties
<a name="aws-properties-transfer-server-identityproviderdetails-properties"></a>

`DirectoryId`  <a name="cfn-transfer-server-identityproviderdetails-directoryid"></a>
The identifier of the AWS Directory Service directory that you want to use as your identity provider.
*Required*: No
*Type*: String
*Pattern*: `^d-[0-9a-f]{10}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Function`  <a name="cfn-transfer-server-identityproviderdetails-function"></a>
The ARN for a Lambda function to use for the Identity provider.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z-]+:lambda:.*$`
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationRole`  <a name="cfn-transfer-server-identityproviderdetails-invocationrole"></a>
This parameter is only applicable if your `IdentityProviderType` is `API_GATEWAY`. Provides the type of `InvocationRole` used to authenticate the user account.
*Required*: No
*Type*: String
*Pattern*: `^arn:.*role/\S+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SftpAuthenticationMethods`  <a name="cfn-transfer-server-identityproviderdetails-sftpauthenticationmethods"></a>
For SFTP-enabled servers, and for custom identity providers *only*, you can specify whether to authenticate using a password, SSH key pair, or both.
+ `PASSWORD` - users must provide their password to connect.
+ `PUBLIC_KEY` - users must provide their private key to connect.
+ `PUBLIC_KEY_OR_PASSWORD` - users can authenticate with either their password or their key. This is the default value.
+ `PUBLIC_KEY_AND_PASSWORD` - users must provide both their private key and their password to connect. The server checks the key first, and then if the key is valid, the system prompts for a password. If the private key provided does not match the public key that is stored, authentication fails.
*Required*: No
*Type*: String
*Allowed values*: `PASSWORD | PUBLIC_KEY | PUBLIC_KEY_OR_PASSWORD | PUBLIC_KEY_AND_PASSWORD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-transfer-server-identityproviderdetails-url"></a>
Provides the location of the service endpoint used to authenticate users.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
