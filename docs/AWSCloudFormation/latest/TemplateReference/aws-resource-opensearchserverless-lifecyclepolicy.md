---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchserverless-lifecyclepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::LifecyclePolicy
<a name="aws-resource-opensearchserverless-lifecyclepolicy"></a>

Creates a lifecyle policy to be applied to OpenSearch Serverless indexes. Lifecycle policies define the number of days or hours to retain the data on an OpenSearch Serverless index. For more information, see [Creating data lifecycle policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-create).

## Syntax
<a name="aws-resource-opensearchserverless-lifecyclepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-opensearchserverless-lifecyclepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::OpenSearchServerless::LifecyclePolicy",
  "Properties" : {
      "[Description](#cfn-opensearchserverless-lifecyclepolicy-description)" : {{String}},
      "[Name](#cfn-opensearchserverless-lifecyclepolicy-name)" : {{String}},
      "[Policy](#cfn-opensearchserverless-lifecyclepolicy-policy)" : {{String}},
      "[Type](#cfn-opensearchserverless-lifecyclepolicy-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-opensearchserverless-lifecyclepolicy-syntax.yaml"></a>

```
Type: AWS::OpenSearchServerless::LifecyclePolicy
Properties:
  [Description](#cfn-opensearchserverless-lifecyclepolicy-description): {{String}}
  [Name](#cfn-opensearchserverless-lifecyclepolicy-name): {{String}}
  [Policy](#cfn-opensearchserverless-lifecyclepolicy-policy): {{String}}
  [Type](#cfn-opensearchserverless-lifecyclepolicy-type): {{String}}
```

## Properties
<a name="aws-resource-opensearchserverless-lifecyclepolicy-properties"></a>

`Description`  <a name="cfn-opensearchserverless-lifecyclepolicy-description"></a>
The description of the lifecycle policy.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-opensearchserverless-lifecyclepolicy-name"></a>
The name of the lifecycle policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-opensearchserverless-lifecyclepolicy-policy"></a>
The JSON policy document without any whitespaces.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]+`
*Minimum*: `1`
*Maximum*: `20480`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-opensearchserverless-lifecyclepolicy-type"></a>
The type of lifecycle policy.
*Required*: Yes
*Type*: String
*Allowed values*: `retention`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-opensearchserverless-lifecyclepolicy-return-values"></a>

### Ref
<a name="aws-resource-opensearchserverless-lifecyclepolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the type and name of the lifecycle policy. For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-opensearchserverless-lifecyclepolicy--examples"></a>

### Create a lifecycle policy that sets a minimum rollover period for all indexes in a collection
<a name="aws-resource-opensearchserverless-lifecyclepolicy--examples--Create_a_lifecycle_policy_that_sets_a_minimum_rollover_period_for_all_indexes_in_a_collection"></a>

The following example specifies an OpenSearch Serverless lifecycle policy that sets a minimum rollover period for all indexes within `my-collection`.

#### JSON
<a name="aws-resource-opensearchserverless-lifecyclepolicy--examples--Create_a_lifecycle_policy_that_sets_a_minimum_rollover_period_for_all_indexes_in_a_collection--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "OpenSearch Serverless lifecycle policy template",
  "Resources": {
    "TestLifecyclePolicy": {
      "Type": "AWS::OpenSearchServerless::LifecyclePolicy",
      "Properties": {
        "Name": "test-lifecycle-policy",
        "Type": "retention",
        "Description": "Lifecycle policy for all indexes in my-collection",
        "Policy": {\"Rules\": [{\"Resource\": [\"index/my-collection/*\"],\"ResourceType\": \"index\",\"MinIndexRetention\": \"2d\"}}
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-opensearchserverless-lifecyclepolicy--examples--Create_a_lifecycle_policy_that_sets_a_minimum_rollover_period_for_all_indexes_in_a_collection--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09T00:00:00.000Z
Description: OpenSearch Serverless lifecycle policy template
Resources:
  TestLifecyclePolicy:
    Type: 'AWS::OpenSearchServerless::LifecyclePolicy'
    Properties:
      Name: test-lifecycle-policy
      Type: retention
      Description: Lifecycle policy for all indexes in my-collection
      Policy: {"Rules": [{"Resource": ["index/my-collection/*"],"ResourceType": "index","MinIndexRetention": "2d"}]}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
