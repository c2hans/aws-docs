---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containerfleet-connectionportrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet ConnectionPortRange
<a name="aws-properties-gamelift-containerfleet-connectionportrange"></a>

The set of port numbers to open on each instance in a container fleet. Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.

The port range must not overlap with the Amazon GameLift Servers reserved port range `4092-4191`. This range is reserved for internal Amazon GameLift Servers services.

## Syntax
<a name="aws-properties-gamelift-containerfleet-connectionportrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containerfleet-connectionportrange-syntax.json"></a>

```
{
  "[FromPort](#cfn-gamelift-containerfleet-connectionportrange-fromport)" : {{Integer}},
  "[ToPort](#cfn-gamelift-containerfleet-connectionportrange-toport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-gamelift-containerfleet-connectionportrange-syntax.yaml"></a>

```
  [FromPort](#cfn-gamelift-containerfleet-connectionportrange-fromport): {{Integer}}
  [ToPort](#cfn-gamelift-containerfleet-connectionportrange-toport): {{Integer}}
```

## Properties
<a name="aws-properties-gamelift-containerfleet-connectionportrange-properties"></a>

`FromPort`  <a name="cfn-gamelift-containerfleet-connectionportrange-fromport"></a>
Starting value for the port range.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToPort`  <a name="cfn-gamelift-containerfleet-connectionportrange-toport"></a>
Ending value for the port. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort`.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `60000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
