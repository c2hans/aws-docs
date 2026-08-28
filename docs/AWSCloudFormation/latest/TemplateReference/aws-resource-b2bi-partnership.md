---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-b2bi-partnership.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership
<a name="aws-resource-b2bi-partnership"></a>

Creates a partnership between a customer and a trading partner, based on the supplied parameters. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.

## Syntax
<a name="aws-resource-b2bi-partnership-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-b2bi-partnership-syntax.json"></a>

```
{
  "Type" : "AWS::B2BI::Partnership",
  "Properties" : {
      "[Capabilities](#cfn-b2bi-partnership-capabilities)" : {{[ String, ... ]}},
      "[CapabilityOptions](#cfn-b2bi-partnership-capabilityoptions)" : {{CapabilityOptions}},
      "[Email](#cfn-b2bi-partnership-email)" : {{String}},
      "[Name](#cfn-b2bi-partnership-name)" : {{String}},
      "[Phone](#cfn-b2bi-partnership-phone)" : {{String}},
      "[ProfileId](#cfn-b2bi-partnership-profileid)" : {{String}},
      "[Tags](#cfn-b2bi-partnership-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-b2bi-partnership-syntax.yaml"></a>

```
Type: AWS::B2BI::Partnership
Properties:
  [Capabilities](#cfn-b2bi-partnership-capabilities): {{
    - String}}
  [CapabilityOptions](#cfn-b2bi-partnership-capabilityoptions): {{
    CapabilityOptions}}
  [Email](#cfn-b2bi-partnership-email): {{String}}
  [Name](#cfn-b2bi-partnership-name): {{String}}
  [Phone](#cfn-b2bi-partnership-phone): {{String}}
  [ProfileId](#cfn-b2bi-partnership-profileid): {{String}}
  [Tags](#cfn-b2bi-partnership-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-b2bi-partnership-properties"></a>

`Capabilities`  <a name="cfn-b2bi-partnership-capabilities"></a>
Returns one or more capabilities associated with this partnership.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapabilityOptions`  <a name="cfn-b2bi-partnership-capabilityoptions"></a>
Contains the details for an Outbound EDI capability.
*Required*: No
*Type*: [CapabilityOptions](aws-properties-b2bi-partnership-capabilityoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Email`  <a name="cfn-b2bi-partnership-email"></a>
Specifies the email address associated with this trading partner.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\.\-]+@[\w\.\-]+$`
*Minimum*: `5`
*Maximum*: `254`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-b2bi-partnership-name"></a>
Returns the name of the partnership.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `254`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phone`  <a name="cfn-b2bi-partnership-phone"></a>
Specifies the phone number associated with the partnership.
*Required*: No
*Type*: String
*Pattern*: `^\+?([0-9 \t\-()\/]{7,})(?:\s*(?:#|x\.?|ext\.?|extension) \t*(\d+))?$`
*Minimum*: `7`
*Maximum*: `22`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileId`  <a name="cfn-b2bi-partnership-profileid"></a>
Returns the unique, system-generated identifier for the profile connected to this partnership.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-b2bi-partnership-tags"></a>
A key-value pair for a specific partnership. Tags are metadata that you can use to search for and group capabilities for various purposes.
*Required*: No
*Type*: Array of [Tag](aws-properties-b2bi-partnership-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-b2bi-partnership-return-values"></a>

### Ref
<a name="aws-resource-b2bi-partnership-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-b2bi-partnership-return-values-fn--getatt"></a>

####
<a name="aws-resource-b2bi-partnership-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Returns a timestamp for creation date and time of the partnership.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
Returns a timestamp that identifies the most recent date and time that the partnership was modified.

`PartnershipArn`  <a name="PartnershipArn-fn::getatt"></a>
Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.

`PartnershipId`  <a name="PartnershipId-fn::getatt"></a>
Returns the unique, system-generated identifier for a partnership.

`TradingPartnerId`  <a name="TradingPartnerId-fn::getatt"></a>
Returns the unique, system-generated identifier for a trading partner.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
