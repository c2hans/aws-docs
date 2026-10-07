---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-certificatebasedauthproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory CertificateBasedAuthProperties
<a name="aws-properties-workspaces-directory-certificatebasedauthproperties"></a>

Describes the properties of the certificate-based authentication you want to use with your WorkSpaces.

## Syntax
<a name="aws-properties-workspaces-directory-certificatebasedauthproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-certificatebasedauthproperties-syntax.json"></a>

```
{
  "[CertificateAuthorityArn](#cfn-workspaces-directory-certificatebasedauthproperties-certificateauthorityarn)" : {{String}},
  "[Status](#cfn-workspaces-directory-certificatebasedauthproperties-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-certificatebasedauthproperties-syntax.yaml"></a>

```
  [CertificateAuthorityArn](#cfn-workspaces-directory-certificatebasedauthproperties-certificateauthorityarn): {{String}}
  [Status](#cfn-workspaces-directory-certificatebasedauthproperties-status): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-certificatebasedauthproperties-properties"></a>

`CertificateAuthorityArn`  <a name="cfn-workspaces-directory-certificatebasedauthproperties-certificateauthorityarn"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager Private CA resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w+=/,.@-]+:[\w+=/,.@-]+:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*$`
*Minimum*: `5`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-workspaces-directory-certificatebasedauthproperties-status"></a>
The status of the certificate-based authentication properties.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
