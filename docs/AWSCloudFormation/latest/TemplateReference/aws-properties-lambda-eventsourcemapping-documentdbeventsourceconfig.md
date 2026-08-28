---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping DocumentDBEventSourceConfig
<a name="aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig"></a>

 Specific configuration settings for a DocumentDB event source.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig-syntax.json"></a>

```
{
  "[CollectionName](#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-collectionname)" : {{String}},
  "[DatabaseName](#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-databasename)" : {{String}},
  "[FullDocument](#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-fulldocument)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig-syntax.yaml"></a>

```
  [CollectionName](#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-collectionname): {{String}}
  [DatabaseName](#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-databasename): {{String}}
  [FullDocument](#cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-fulldocument): {{String}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-documentdbeventsourceconfig-properties"></a>

`CollectionName`  <a name="cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-collectionname"></a>
 The name of the collection to consume within the database. If you do not specify a collection, Lambda consumes all collections.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `57`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-databasename"></a>
 The name of the database to consume within the DocumentDB cluster.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FullDocument`  <a name="cfn-lambda-eventsourcemapping-documentdbeventsourceconfig-fulldocument"></a>
 Determines what DocumentDB sends to your event stream during document update operations. If set to UpdateLookup, DocumentDB sends a delta describing the changes, along with a copy of the entire document. Otherwise, DocumentDB sends only a partial document that contains the changes.
*Required*: No
*Type*: String
*Allowed values*: `UpdateLookup | Default`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
