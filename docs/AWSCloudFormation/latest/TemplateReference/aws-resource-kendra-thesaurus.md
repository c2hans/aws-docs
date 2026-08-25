---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kendra-thesaurus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::Thesaurus
<a name="aws-resource-kendra-thesaurus"></a>

**Note**
Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

Creates a thesaurus for an index. The thesaurus contains a list of synonyms in Solr format.

For an example of adding a thesaurus file to an index, see [Adding custom synonyms to an index](https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms-adding-thesaurus-file.html).

## Syntax
<a name="aws-resource-kendra-thesaurus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kendra-thesaurus-syntax.json"></a>

```
{
  "Type" : "AWS::Kendra::Thesaurus",
  "Properties" : {
      "[Description](#cfn-kendra-thesaurus-description)" : {{String}},
      "[IndexId](#cfn-kendra-thesaurus-indexid)" : {{String}},
      "[Name](#cfn-kendra-thesaurus-name)" : {{String}},
      "[RoleArn](#cfn-kendra-thesaurus-rolearn)" : {{String}},
      "[SourceS3Path](#cfn-kendra-thesaurus-sources3path)" : {{S3Path}},
      "[Tags](#cfn-kendra-thesaurus-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kendra-thesaurus-syntax.yaml"></a>

```
Type: AWS::Kendra::Thesaurus
Properties:
  [Description](#cfn-kendra-thesaurus-description): {{String}}
  [IndexId](#cfn-kendra-thesaurus-indexid): {{String}}
  [Name](#cfn-kendra-thesaurus-name): {{String}}
  [RoleArn](#cfn-kendra-thesaurus-rolearn): {{String}}
  [SourceS3Path](#cfn-kendra-thesaurus-sources3path): {{
    S3Path}}
  [Tags](#cfn-kendra-thesaurus-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kendra-thesaurus-properties"></a>

`Description`  <a name="cfn-kendra-thesaurus-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^\P{C}*$`
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexId`  <a name="cfn-kendra-thesaurus-indexid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]*$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-kendra-thesaurus-name"></a>
The name of the thesaurus.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-kendra-thesaurus-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceS3Path`  <a name="cfn-kendra-thesaurus-sources3path"></a>
Information required to find a specific file in an Amazon S3 bucket.
*Required*: Yes
*Type*: [S3Path](aws-properties-kendra-thesaurus-s3path.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-kendra-thesaurus-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-kendra-thesaurus-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kendra-thesaurus-return-values"></a>

### Ref
<a name="aws-resource-kendra-thesaurus-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-kendra-thesaurus-return-values-fn--getatt"></a>

####
<a name="aws-resource-kendra-thesaurus-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the thesaurus.
