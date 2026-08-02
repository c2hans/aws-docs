---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule
<a name="aws-resource-connect-rule"></a>

Creates a rule for the specified Connect Customer instance.

## Syntax
<a name="aws-resource-connect-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-rule-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::Rule",
  "Properties" : {
      "[Actions](#cfn-connect-rule-actions)" : {{Actions}},
      "[Function](#cfn-connect-rule-function)" : {{String}},
      "[InstanceArn](#cfn-connect-rule-instancearn)" : {{String}},
      "[Name](#cfn-connect-rule-name)" : {{String}},
      "[PublishStatus](#cfn-connect-rule-publishstatus)" : {{String}},
      "[Tags](#cfn-connect-rule-tags)" : {{[ Tag, ... ]}},
      "[TriggerEventSource](#cfn-connect-rule-triggereventsource)" : {{RuleTriggerEventSource}}
    }
}
```

### YAML
<a name="aws-resource-connect-rule-syntax.yaml"></a>

```
Type: AWS::Connect::Rule
Properties:
  [Actions](#cfn-connect-rule-actions): {{
    Actions}}
  [Function](#cfn-connect-rule-function): {{String}}
  [InstanceArn](#cfn-connect-rule-instancearn): {{String}}
  [Name](#cfn-connect-rule-name): {{String}}
  [PublishStatus](#cfn-connect-rule-publishstatus): {{String}}
  [Tags](#cfn-connect-rule-tags): {{
    - Tag}}
  [TriggerEventSource](#cfn-connect-rule-triggereventsource): {{
    RuleTriggerEventSource}}
```

## Properties
<a name="aws-resource-connect-rule-properties"></a>

`Actions`  <a name="cfn-connect-rule-actions"></a>
 A list of actions to be run when the rule is triggered.
*Required*: Yes
*Type*: [Actions](aws-properties-connect-rule-actions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Function`  <a name="cfn-connect-rule-function"></a>
The conditions of the rule.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-rule-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-connect-rule-name"></a>
The name of the rule.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,200}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublishStatus`  <a name="cfn-connect-rule-publishstatus"></a>
 The publish status of the rule.
*Allowed values*: `DRAFT` \| `PUBLISHED`
*Required*: Yes
*Type*: String
*Allowed values*: `DRAFT | PUBLISHED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-rule-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-rule-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TriggerEventSource`  <a name="cfn-connect-rule-triggereventsource"></a>
The event source to trigger the rule.
*Required*: Yes
*Type*: [RuleTriggerEventSource](aws-properties-connect-rule-ruletriggereventsource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-connect-rule-return-values"></a>

### Ref
<a name="aws-resource-connect-rule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the quick rule name. For example:

 `{ "Ref": "myRuleName" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-rule-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-rule-return-values-fn--getatt-fn--getatt"></a>

`RuleArn`  <a name="RuleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the rule.

## Examples
<a name="aws-resource-connect-rule--examples"></a>

### Specify a rule resource
<a name="aws-resource-connect-rule--examples--Specify_a_rule_resource"></a>

The following example specifies a rule resource for an Connect Customer instance.

#### JSON
<a name="aws-resource-connect-rule--examples--Specify_a_rule_resource--json"></a>

```
{
    "Name": "ExampleRule",
    "InstanceArn": "arn:aws:connect:region-name:aws-account-id:instance/instance-arn",
    "TriggerEventSource": {
        "EventSourceName": "OnPostCallAnalysisAvailable"
    },
    "Function": "Example function using Amazon Connect Rules Function Language.",
    "Actions": {
        "AssignContactCategoryActions": [{}],
        "EventBridgeActions": [
            {
                "Name": "Name of the event bridge action"
            }
        ],
        "SendNotificationActions": [
            {
                "DeliveryMethod": "EMAIL",
                "Subject": "Email subject",
                "Content": "Email content",
                "ContentType": "PLAIN_TEXT",
                "Recipient": {
                    "UserArns": ["arn:aws:connect:region-name:aws-account-id:instance/instance-arn/agent/user-arn"]
                }
            }
        ],
        "TaskActions": [
            {
              "Name": "Name of the task action",
              "ContactFlowArn": "arn:aws:connect:region-name:aws-account-id:instance/instance-arn/contact-flow/contact-flow-arn",
              "References": {
                "reference1": {
                  "Type": "URL",
                  "Value": "URL of the reference"
                }
              },
              "Description": "Task description"
            }
          ]
    },
    "PublishStatus": "DRAFT"
}
```
