---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amplify-webhook.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Webhook
<a name="aws-resource-amplify-webhook"></a>

Describes a webhook that connects repository events to an Amplify app.

## Syntax
<a name="aws-resource-amplify-webhook-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amplify-webhook-syntax.json"></a>

```
{
  "Type" : "AWS::Amplify::Webhook",
  "Properties" : {
      "[AppId](#cfn-amplify-webhook-appid)" : {{String}},
      "[BranchName](#cfn-amplify-webhook-branchname)" : {{String}},
      "[Description](#cfn-amplify-webhook-description)" : {{String}},
      "[Tags](#cfn-amplify-webhook-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-amplify-webhook-syntax.yaml"></a>

```
Type: AWS::Amplify::Webhook
Properties:
  [AppId](#cfn-amplify-webhook-appid): {{String}}
  [BranchName](#cfn-amplify-webhook-branchname): {{String}}
  [Description](#cfn-amplify-webhook-description): {{String}}
  [Tags](#cfn-amplify-webhook-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-amplify-webhook-properties"></a>

`AppId`  <a name="cfn-amplify-webhook-appid"></a>
The unique ID of an Amplify app.
*Required*: No
*Type*: String
*Pattern*: `^d[a-z0-9]+$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BranchName`  <a name="cfn-amplify-webhook-branchname"></a>
The name for a branch that is part of an Amplify app.
*Required*: Yes
*Type*: String
*Pattern*: `^(?s).+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-amplify-webhook-description"></a>
The description for a webhook.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-amplify-webhook-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-amplify-webhook-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-amplify-webhook-return-values"></a>

### Ref
<a name="aws-resource-amplify-webhook-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-amplify-webhook-return-values-fn--getatt"></a>

####
<a name="aws-resource-amplify-webhook-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`WebhookId`  <a name="WebhookId-fn::getatt"></a>
The ID of the webhook.

`WebhookUrl`  <a name="WebhookUrl-fn::getatt"></a>
The URL of the webhook.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
