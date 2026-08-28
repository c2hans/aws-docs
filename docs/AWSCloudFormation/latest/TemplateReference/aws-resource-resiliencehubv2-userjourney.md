---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resiliencehubv2-userjourney.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::UserJourney
<a name="aws-resource-resiliencehubv2-userjourney"></a>

Represents a user journey that defines a critical path through a system.

## Syntax
<a name="aws-resource-resiliencehubv2-userjourney-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resiliencehubv2-userjourney-syntax.json"></a>

```
{
  "Type" : "AWS::ResilienceHubV2::UserJourney",
  "Properties" : {
      "[Description](#cfn-resiliencehubv2-userjourney-description)" : {{String}},
      "[Name](#cfn-resiliencehubv2-userjourney-name)" : {{String}},
      "[PolicyArn](#cfn-resiliencehubv2-userjourney-policyarn)" : {{String}},
      "[SystemIdentifier](#cfn-resiliencehubv2-userjourney-systemidentifier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-resiliencehubv2-userjourney-syntax.yaml"></a>

```
Type: AWS::ResilienceHubV2::UserJourney
Properties:
  [Description](#cfn-resiliencehubv2-userjourney-description): {{String}}
  [Name](#cfn-resiliencehubv2-userjourney-name): {{String}}
  [PolicyArn](#cfn-resiliencehubv2-userjourney-policyarn): {{String}}
  [SystemIdentifier](#cfn-resiliencehubv2-userjourney-systemidentifier): {{String}}
```

## Properties
<a name="aws-resource-resiliencehubv2-userjourney-properties"></a>

`Description`  <a name="cfn-resiliencehubv2-userjourney-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-resiliencehubv2-userjourney-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9 _\-]{1,59}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyArn`  <a name="cfn-resiliencehubv2-userjourney-policyarn"></a>
ARN identifier.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SystemIdentifier`  <a name="cfn-resiliencehubv2-userjourney-systemidentifier"></a>
Identifier that accepts either ARN or system ID.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-resiliencehubv2-userjourney-return-values"></a>

### Ref
<a name="aws-resource-resiliencehubv2-userjourney-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-resiliencehubv2-userjourney-return-values-fn--getatt"></a>

####
<a name="aws-resource-resiliencehubv2-userjourney-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the user journey was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the user journey was last updated.

`UserJourneyId`  <a name="UserJourneyId-fn::getatt"></a>
The unique identifier of the user journey.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
