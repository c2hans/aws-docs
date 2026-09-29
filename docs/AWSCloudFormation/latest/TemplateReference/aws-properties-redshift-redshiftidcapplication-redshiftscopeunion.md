---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-redshiftidcapplication-redshiftscopeunion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::RedshiftIdcApplication RedshiftScopeUnion
<a name="aws-properties-redshift-redshiftidcapplication-redshiftscopeunion"></a>

A union structure that defines the scope of Amazon Redshift service integrations. Contains configuration for different integration types such as Amazon Redshift.

## Syntax
<a name="aws-properties-redshift-redshiftidcapplication-redshiftscopeunion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-redshiftidcapplication-redshiftscopeunion-syntax.json"></a>

```
{
  "[Connect](#cfn-redshift-redshiftidcapplication-redshiftscopeunion-connect)" : {{Connect}}
}
```

### YAML
<a name="aws-properties-redshift-redshiftidcapplication-redshiftscopeunion-syntax.yaml"></a>

```
  [Connect](#cfn-redshift-redshiftidcapplication-redshiftscopeunion-connect): {{
    Connect}}
```

## Properties
<a name="aws-properties-redshift-redshiftidcapplication-redshiftscopeunion-properties"></a>

`Connect`  <a name="cfn-redshift-redshiftidcapplication-redshiftscopeunion-connect"></a>
The Amazon Redshift connect integration scope configuration. Defines authorization settings for Amazon Redshift connect service integration.
*Required*: No
*Type*: [Connect](aws-properties-redshift-redshiftidcapplication-connect.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
