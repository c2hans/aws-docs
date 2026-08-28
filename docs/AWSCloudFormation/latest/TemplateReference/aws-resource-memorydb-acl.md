---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-memorydb-acl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::ACL
<a name="aws-resource-memorydb-acl"></a>

Specifies an Access Control List. For more information, see [Authenticating users with Access Contol Lists (ACLs)](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html).

## Syntax
<a name="aws-resource-memorydb-acl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-memorydb-acl-syntax.json"></a>

```
{
  "Type" : "AWS::MemoryDB::ACL",
  "Properties" : {
      "[ACLName](#cfn-memorydb-acl-aclname)" : {{String}},
      "[Tags](#cfn-memorydb-acl-tags)" : {{[ Tag, ... ]}},
      "[UserNames](#cfn-memorydb-acl-usernames)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-memorydb-acl-syntax.yaml"></a>

```
Type: AWS::MemoryDB::ACL
Properties:
  [ACLName](#cfn-memorydb-acl-aclname): {{String}}
  [Tags](#cfn-memorydb-acl-tags): {{
    - Tag}}
  [UserNames](#cfn-memorydb-acl-usernames): {{
    - String}}
```

## Properties
<a name="aws-resource-memorydb-acl-properties"></a>

`ACLName`  <a name="cfn-memorydb-acl-aclname"></a>
The name of the Access Control List. This value is stored as a lowercase string.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z][a-z0-9\\-]*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-memorydb-acl-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-memorydb-acl-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserNames`  <a name="cfn-memorydb-acl-usernames"></a>
The list of users that belong to the Access Control List.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-memorydb-acl-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-memorydb-acl-return-values-fn--getatt"></a>

####
<a name="aws-resource-memorydb-acl-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the ARN of the Access Control List, such as `arn:aws:memorydb:us-east-1:123456789012:acl/my-acl`

`Status`  <a name="Status-fn::getatt"></a>
Indicates ACL status.
*Valid values*: `creating` \| `active` \| `modifying` \| `deleting`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
