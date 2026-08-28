---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-aclconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup AclConfiguration
<a name="aws-properties-athena-workgroup-aclconfiguration"></a>

Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query results, including data files inserted by Athena as the result of statements like CTAS or INSERT INTO. When Athena stores query results in Amazon S3, the canned ACL is set with the `x-amz-acl` request header. For more information about S3 Object Ownership, see [Object Ownership settings](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html#object-ownership-overview) in the *Amazon S3 User Guide*.

## Syntax
<a name="aws-properties-athena-workgroup-aclconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-aclconfiguration-syntax.json"></a>

```
{
  "[S3AclOption](#cfn-athena-workgroup-aclconfiguration-s3acloption)" : {{String}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-aclconfiguration-syntax.yaml"></a>

```
  [S3AclOption](#cfn-athena-workgroup-aclconfiguration-s3acloption): {{String}}
```

## Properties
<a name="aws-properties-athena-workgroup-aclconfiguration-properties"></a>

`S3AclOption`  <a name="cfn-athena-workgroup-aclconfiguration-s3acloption"></a>
The Amazon S3 canned ACL that Athena should specify when storing query results, including data files inserted by Athena as the result of statements like CTAS or INSERT INTO. Currently the only supported canned ACL is `BUCKET_OWNER_FULL_CONTROL`. If a query runs in a workgroup and the workgroup overrides client-side settings, then the Amazon S3 canned ACL specified in the workgroup's settings is used for all queries that run in the workgroup. For more information about Amazon S3 canned ACLs, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl) in the *Amazon S3 User Guide*.
*Required*: Yes
*Type*: String
*Allowed values*: `BUCKET_OWNER_FULL_CONTROL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
