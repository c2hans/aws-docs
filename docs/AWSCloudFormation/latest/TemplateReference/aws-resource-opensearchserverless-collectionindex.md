---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchserverless-collectionindex.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::CollectionIndex
<a name="aws-resource-opensearchserverless-collectionindex"></a>

<a name="aws-resource-opensearchserverless-collectionindex-description"></a>The `AWS::OpenSearchServerless::CollectionIndex` resource Property description not available. for OpenSearchServerless.

## Syntax
<a name="aws-resource-opensearchserverless-collectionindex-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-opensearchserverless-collectionindex-syntax.json"></a>

```
{
  "Type" : "AWS::OpenSearchServerless::CollectionIndex",
  "Properties" : {
      "[Id](#cfn-opensearchserverless-collectionindex-id)" : {{String}},
      "[IndexName](#cfn-opensearchserverless-collectionindex-indexname)" : {{String}},
      "[IndexSchema](#cfn-opensearchserverless-collectionindex-indexschema)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-opensearchserverless-collectionindex-syntax.yaml"></a>

```
Type: AWS::OpenSearchServerless::CollectionIndex
Properties:
  [Id](#cfn-opensearchserverless-collectionindex-id): {{String}}
  [IndexName](#cfn-opensearchserverless-collectionindex-indexname): {{String}}
  [IndexSchema](#cfn-opensearchserverless-collectionindex-indexschema): {{String}}
```

## Properties
<a name="aws-resource-opensearchserverless-collectionindex-properties"></a>

`Id`  <a name="cfn-opensearchserverless-collectionindex-id"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]{3,40}$`
*Minimum*: `3`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IndexName`  <a name="cfn-opensearchserverless-collectionindex-indexname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?![_-])[a-z][a-z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IndexSchema`  <a name="cfn-opensearchserverless-collectionindex-indexschema"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+`
*Minimum*: `1`
*Maximum*: `2480`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-opensearchserverless-collectionindex-return-values"></a>

### Ref
<a name="aws-resource-opensearchserverless-collectionindex-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
