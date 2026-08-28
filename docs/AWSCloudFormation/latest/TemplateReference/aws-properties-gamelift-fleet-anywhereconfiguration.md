---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-fleet-anywhereconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Fleet AnywhereConfiguration
<a name="aws-properties-gamelift-fleet-anywhereconfiguration"></a>

Amazon GameLift Servers configuration options for your Anywhere fleets.

## Syntax
<a name="aws-properties-gamelift-fleet-anywhereconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-fleet-anywhereconfiguration-syntax.json"></a>

```
{
  "[Cost](#cfn-gamelift-fleet-anywhereconfiguration-cost)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-fleet-anywhereconfiguration-syntax.yaml"></a>

```
  [Cost](#cfn-gamelift-fleet-anywhereconfiguration-cost): {{String}}
```

## Properties
<a name="aws-properties-gamelift-fleet-anywhereconfiguration-properties"></a>

`Cost`  <a name="cfn-gamelift-fleet-anywhereconfiguration-cost"></a>
The cost to run your fleet per hour. Amazon GameLift Servers uses the provided cost of your fleet to balance usage in queues. For more information about queues, see [Setting up queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html) in the *Amazon GameLift Servers Developer Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{1,5}(?:\.\d{1,5})?$`
*Minimum*: `1`
*Maximum*: `11`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-gamelift-fleet-anywhereconfiguration--seealso"></a>
+ [ Create GameLift resources using Amazon CloudFront](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Developer Guide*
+ [ Create an Amazon GameLift Anywhere fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-anywhere.html) in the *Amazon GameLift Developer Guide*
+ [LocationModel](https://docs.aws.amazon.com/gamelift/latest/apireference/API_LocationModel.html) in the *Amazon GameLift API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
