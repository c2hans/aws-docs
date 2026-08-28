---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-topicrulepayload.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule TopicRulePayload
<a name="aws-properties-iot-topicrule-topicrulepayload"></a>

Describes a rule.

## Syntax
<a name="aws-properties-iot-topicrule-topicrulepayload-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-topicrulepayload-syntax.json"></a>

```
{
  "[Actions](#cfn-iot-topicrule-topicrulepayload-actions)" : {{[ Action, ... ]}},
  "[AwsIotSqlVersion](#cfn-iot-topicrule-topicrulepayload-awsiotsqlversion)" : {{String}},
  "[Description](#cfn-iot-topicrule-topicrulepayload-description)" : {{String}},
  "[ErrorAction](#cfn-iot-topicrule-topicrulepayload-erroraction)" : {{Action}},
  "[RuleDisabled](#cfn-iot-topicrule-topicrulepayload-ruledisabled)" : {{Boolean}},
  "[Sql](#cfn-iot-topicrule-topicrulepayload-sql)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-topicrulepayload-syntax.yaml"></a>

```
  [Actions](#cfn-iot-topicrule-topicrulepayload-actions): {{
    - Action}}
  [AwsIotSqlVersion](#cfn-iot-topicrule-topicrulepayload-awsiotsqlversion): {{String}}
  [Description](#cfn-iot-topicrule-topicrulepayload-description): {{String}}
  [ErrorAction](#cfn-iot-topicrule-topicrulepayload-erroraction): {{
    Action}}
  [RuleDisabled](#cfn-iot-topicrule-topicrulepayload-ruledisabled): {{Boolean}}
  [Sql](#cfn-iot-topicrule-topicrulepayload-sql): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-topicrulepayload-properties"></a>

`Actions`  <a name="cfn-iot-topicrule-topicrulepayload-actions"></a>
The actions associated with the rule.
*Required*: Yes
*Type*: Array of [Action](aws-properties-iot-topicrule-action.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsIotSqlVersion`  <a name="cfn-iot-topicrule-topicrulepayload-awsiotsqlversion"></a>
The version of the SQL rules engine to use when evaluating the rule.
The default value is 2015-10-08.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iot-topicrule-topicrulepayload-description"></a>
The description of the rule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ErrorAction`  <a name="cfn-iot-topicrule-topicrulepayload-erroraction"></a>
The action to take when an error occurs.
*Required*: No
*Type*: [Action](aws-properties-iot-topicrule-action.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleDisabled`  <a name="cfn-iot-topicrule-topicrulepayload-ruledisabled"></a>
Specifies whether the rule is disabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sql`  <a name="cfn-iot-topicrule-topicrulepayload-sql"></a>
The SQL statement used to query the topic. For more information, see [AWS IoT SQL Reference](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html) in the *AWS IoT Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
