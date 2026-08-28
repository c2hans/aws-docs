---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-associatedsystem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service AssociatedSystem
<a name="aws-properties-resiliencehubv2-service-associatedsystem"></a>

Represents a system associated with a service.

## Syntax
<a name="aws-properties-resiliencehubv2-service-associatedsystem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-associatedsystem-syntax.json"></a>

```
{
  "[SystemArn](#cfn-resiliencehubv2-service-associatedsystem-systemarn)" : {{String}},
  "[UserJourneyIds](#cfn-resiliencehubv2-service-associatedsystem-userjourneyids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-associatedsystem-syntax.yaml"></a>

```
  [SystemArn](#cfn-resiliencehubv2-service-associatedsystem-systemarn): {{String}}
  [UserJourneyIds](#cfn-resiliencehubv2-service-associatedsystem-userjourneyids): {{
    - String}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-associatedsystem-properties"></a>

`SystemArn`  <a name="cfn-resiliencehubv2-service-associatedsystem-systemarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserJourneyIds`  <a name="cfn-resiliencehubv2-service-associatedsystem-userjourneyids"></a>
The list of user journey identifiers that associate this system with the service.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
