---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-idcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory IDCConfig
<a name="aws-properties-workspaces-directory-idcconfig"></a>

Specifies the configurations of the identity center.

## Syntax
<a name="aws-properties-workspaces-directory-idcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-idcconfig-syntax.json"></a>

```
{
  "[ApplicationArn](#cfn-workspaces-directory-idcconfig-applicationarn)" : {{String}},
  "[InstanceArn](#cfn-workspaces-directory-idcconfig-instancearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-idcconfig-syntax.yaml"></a>

```
  [ApplicationArn](#cfn-workspaces-directory-idcconfig-applicationarn): {{String}}
  [InstanceArn](#cfn-workspaces-directory-idcconfig-instancearn): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-idcconfig-properties"></a>

`ApplicationArn`  <a name="cfn-workspaces-directory-idcconfig-applicationarn"></a>
The Amazon Resource Name (ARN) of the application.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]{0,7}:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-workspaces-directory-idcconfig-instancearn"></a>
The Amazon Resource Name (ARN) of the identity center instance.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]{0,7}:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
