---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-activedirectoryconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory ActiveDirectoryConfig
<a name="aws-properties-workspaces-directory-activedirectoryconfig"></a>

Information about the Active Directory config.

## Syntax
<a name="aws-properties-workspaces-directory-activedirectoryconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-activedirectoryconfig-syntax.json"></a>

```
{
  "[DomainName](#cfn-workspaces-directory-activedirectoryconfig-domainname)" : {{String}},
  "[ServiceAccountSecretArn](#cfn-workspaces-directory-activedirectoryconfig-serviceaccountsecretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-activedirectoryconfig-syntax.yaml"></a>

```
  [DomainName](#cfn-workspaces-directory-activedirectoryconfig-domainname): {{String}}
  [ServiceAccountSecretArn](#cfn-workspaces-directory-activedirectoryconfig-serviceaccountsecretarn): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-activedirectoryconfig-properties"></a>

`DomainName`  <a name="cfn-workspaces-directory-activedirectoryconfig-domainname"></a>
The name of the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9]+[.-])+([a-zA-Z0-9])+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceAccountSecretArn`  <a name="cfn-workspaces-directory-activedirectoryconfig-serviceaccountsecretarn"></a>
Indicates the secret ARN on the service account.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z-]{0,7}:secretsmanager:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:secret:[A-Za-z0-9][A-za-z0-9_/.-]{8,519}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
