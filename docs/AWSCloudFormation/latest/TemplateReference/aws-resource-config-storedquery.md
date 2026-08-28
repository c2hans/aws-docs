---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-storedquery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::StoredQuery
<a name="aws-resource-config-storedquery"></a>

Provides the details of a stored query.

## Syntax
<a name="aws-resource-config-storedquery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-config-storedquery-syntax.json"></a>

```
{
  "Type" : "AWS::Config::StoredQuery",
  "Properties" : {
      "[QueryDescription](#cfn-config-storedquery-querydescription)" : {{String}},
      "[QueryExpression](#cfn-config-storedquery-queryexpression)" : {{String}},
      "[QueryName](#cfn-config-storedquery-queryname)" : {{String}},
      "[Tags](#cfn-config-storedquery-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-config-storedquery-syntax.yaml"></a>

```
Type: AWS::Config::StoredQuery
Properties:
  [QueryDescription](#cfn-config-storedquery-querydescription): {{String}}
  [QueryExpression](#cfn-config-storedquery-queryexpression): {{String}}
  [QueryName](#cfn-config-storedquery-queryname): {{String}}
  [Tags](#cfn-config-storedquery-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-config-storedquery-properties"></a>

`QueryDescription`  <a name="cfn-config-storedquery-querydescription"></a>
A unique description for the query.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryExpression`  <a name="cfn-config-storedquery-queryexpression"></a>
The expression of the query. For example, `SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.`
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryName`  <a name="cfn-config-storedquery-queryname"></a>
The name of the query.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-config-storedquery-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-config-storedquery-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-config-storedquery-return-values"></a>

### Ref
<a name="aws-resource-config-storedquery-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-config-storedquery-return-values-fn--getatt"></a>

####
<a name="aws-resource-config-storedquery-return-values-fn--getatt-fn--getatt"></a>

`QueryArn`  <a name="QueryArn-fn::getatt"></a>
Amazon Resource Name (ARN) of the query. For example, arn:partition:service:region:account-id:resource-type/resource-name/resource-id.

`QueryId`  <a name="QueryId-fn::getatt"></a>
The ID of the query.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
