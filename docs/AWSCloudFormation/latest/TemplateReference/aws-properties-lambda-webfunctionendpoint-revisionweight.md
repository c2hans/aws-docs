---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionendpoint-revisionweight.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionEndpoint RevisionWeight
<a name="aws-properties-lambda-webfunctionendpoint-revisionweight"></a>

Specifies a revision and its traffic weight for an endpoint. You can assign weights to up to two revisions to split traffic for canary or blue-green deployments.

## Syntax
<a name="aws-properties-lambda-webfunctionendpoint-revisionweight-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionendpoint-revisionweight-syntax.json"></a>

```
{
  "[RevisionId](#cfn-lambda-webfunctionendpoint-revisionweight-revisionid)" : {{String}},
  "[Weight](#cfn-lambda-webfunctionendpoint-revisionweight-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionendpoint-revisionweight-syntax.yaml"></a>

```
  [RevisionId](#cfn-lambda-webfunctionendpoint-revisionweight-revisionid): {{String}}
  [Weight](#cfn-lambda-webfunctionendpoint-revisionweight-weight): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-webfunctionendpoint-revisionweight-properties"></a>

`RevisionId`  <a name="cfn-lambda-webfunctionendpoint-revisionweight-revisionid"></a>
The identifier of the revision.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-lambda-webfunctionendpoint-revisionweight-weight"></a>
The percentage of traffic to route to this revision. Minimum value of 1, maximum value of 100.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
