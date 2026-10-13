---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-tenant-tenantsuppressionattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::Tenant TenantSuppressionAttributes
<a name="aws-properties-ses-tenant-tenantsuppressionattributes"></a>

An object that contains the suppression list preferences for a tenant.

## Syntax
<a name="aws-properties-ses-tenant-tenantsuppressionattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-tenant-tenantsuppressionattributes-syntax.json"></a>

```
{
  "[SuppressedReasons](#cfn-ses-tenant-tenantsuppressionattributes-suppressedreasons)" : {{[ String, ... ]}},
  "[SuppressionScope](#cfn-ses-tenant-tenantsuppressionattributes-suppressionscope)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-tenant-tenantsuppressionattributes-syntax.yaml"></a>

```
  [SuppressedReasons](#cfn-ses-tenant-tenantsuppressionattributes-suppressedreasons): {{
    - String}}
  [SuppressionScope](#cfn-ses-tenant-tenantsuppressionattributes-suppressionscope): {{String}}
```

## Properties
<a name="aws-properties-ses-tenant-tenantsuppressionattributes-properties"></a>

`SuppressedReasons`  <a name="cfn-ses-tenant-tenantsuppressionattributes-suppressedreasons"></a>
A list that contains the reasons that email addresses are automatically added to the suppression list for the tenant. This list can contain any or all of the following:
+ `COMPLAINT` – Amazon SES adds an email address to the suppression list when a message sent to that address results in a complaint.
+ `BOUNCE` – Amazon SES adds an email address to the suppression list when a message sent to that address results in a hard bounce.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `BOUNCE | COMPLAINT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuppressionScope`  <a name="cfn-ses-tenant-tenantsuppressionattributes-suppressionscope"></a>
The suppression scope for the tenant. Can be one of the following:
+ `TENANT` – The tenant uses its own suppression list.
+ `ACCOUNT` – The tenant uses the account-level suppression list.
If you don't specify a suppression scope, the tenant defaults to `ACCOUNT` scope and uses the account-level suppression list.
*Required*: Yes
*Type*: String
*Allowed values*: `ACCOUNT | TENANT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
