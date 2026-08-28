---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-tenant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::Tenant
<a name="aws-resource-ses-tenant"></a>

Create a tenant.

*Tenants* are logical containers that group related SES resources together. Each tenant can have its own set of resources like email identities, configuration sets, and templates, along with reputation metrics and sending status. This helps isolate and manage email sending for different customers or business units within your Amazon SES API v2 account.

You can optionally specify `SuppressionAttributes` to configure tenant-level suppression at creation time. When tenant-level suppression is enabled, Amazon SES maintains a separate suppression list for the tenant instead of using the account-level suppression list.

## Syntax
<a name="aws-resource-ses-tenant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-tenant-syntax.json"></a>

```
{
  "Type" : "AWS::SES::Tenant",
  "Properties" : {
      "[ResourceAssociations](#cfn-ses-tenant-resourceassociations)" : {{[ ResourceAssociation, ... ]}},
      "[Tags](#cfn-ses-tenant-tags)" : {{[ Tag, ... ]}},
      "[TenantName](#cfn-ses-tenant-tenantname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ses-tenant-syntax.yaml"></a>

```
Type: AWS::SES::Tenant
Properties:
  [ResourceAssociations](#cfn-ses-tenant-resourceassociations): {{
    - ResourceAssociation}}
  [Tags](#cfn-ses-tenant-tags): {{
    - Tag}}
  [TenantName](#cfn-ses-tenant-tenantname): {{String}}
```

## Properties
<a name="aws-resource-ses-tenant-properties"></a>

`ResourceAssociations`  <a name="cfn-ses-tenant-resourceassociations"></a>
The list of resources to associate with the tenant.
*Required*: No
*Type*: Array of [ResourceAssociation](aws-properties-ses-tenant-resourceassociation.md)
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ses-tenant-tags"></a>
An array of objects that define the tags (keys and values) associated with the tenant.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-tenant-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantName`  <a name="cfn-ses-tenant-tenantname"></a>
The name of a tenant. The name can contain up to 64 alphanumeric characters, including letters, numbers, hyphens (-) and underscores (\_) only.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ses-tenant-return-values"></a>

### Ref
<a name="aws-resource-ses-tenant-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the resource name.

### Fn::GetAtt
<a name="aws-resource-ses-tenant-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-tenant-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the ARN of the tenant.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
