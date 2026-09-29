---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-redshiftidcapplication-connect.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::RedshiftIdcApplication Connect
<a name="aws-properties-redshift-redshiftidcapplication-connect"></a>

A structure that defines the Amazon Redshift connect service integration scope.

## Syntax
<a name="aws-properties-redshift-redshiftidcapplication-connect-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-redshiftidcapplication-connect-syntax.json"></a>

```
{
  "[Authorization](#cfn-redshift-redshiftidcapplication-connect-authorization)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-redshiftidcapplication-connect-syntax.yaml"></a>

```
  [Authorization](#cfn-redshift-redshiftidcapplication-connect-authorization): {{String}}
```

## Properties
<a name="aws-properties-redshift-redshiftidcapplication-connect-properties"></a>

`Authorization`  <a name="cfn-redshift-redshiftidcapplication-connect-authorization"></a>
Determines whether the Amazon Redshift connect integration is enabled or disabled for the application.
*Required*: Yes
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
