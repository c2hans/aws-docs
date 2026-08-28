---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-attributetypesselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain AttributeTypesSelector
<a name="aws-properties-customerprofiles-domain-attributetypesselector"></a>

Configures information about the `AttributeTypesSelector` which rule-based identity resolution uses to match profiles.

## Syntax
<a name="aws-properties-customerprofiles-domain-attributetypesselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-attributetypesselector-syntax.json"></a>

```
{
  "[Address](#cfn-customerprofiles-domain-attributetypesselector-address)" : {{[ String, ... ]}},
  "[AttributeMatchingModel](#cfn-customerprofiles-domain-attributetypesselector-attributematchingmodel)" : {{String}},
  "[EmailAddress](#cfn-customerprofiles-domain-attributetypesselector-emailaddress)" : {{[ String, ... ]}},
  "[PhoneNumber](#cfn-customerprofiles-domain-attributetypesselector-phonenumber)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-attributetypesselector-syntax.yaml"></a>

```
  [Address](#cfn-customerprofiles-domain-attributetypesselector-address): {{
    - String}}
  [AttributeMatchingModel](#cfn-customerprofiles-domain-attributetypesselector-attributematchingmodel): {{String}}
  [EmailAddress](#cfn-customerprofiles-domain-attributetypesselector-emailaddress): {{
    - String}}
  [PhoneNumber](#cfn-customerprofiles-domain-attributetypesselector-phonenumber): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-attributetypesselector-properties"></a>

`Address`  <a name="cfn-customerprofiles-domain-attributetypesselector-address"></a>
The `Address` type. You can choose from `Address`, `BusinessAddress`, `MaillingAddress`, and `ShippingAddress`. You only can use the `Address` type in the `MatchingRule`. For example, if you want to match a profile based on `BusinessAddress.City` or `MaillingAddress.City`, you can choose the `BusinessAddress` and the `MaillingAddress` to represent the `Address` type and specify the `Address.City` on the matching rule.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AttributeMatchingModel`  <a name="cfn-customerprofiles-domain-attributetypesselector-attributematchingmodel"></a>
Configures the `AttributeMatchingModel`, you can either choose `ONE_TO_ONE` or `MANY_TO_MANY`.
*Required*: Yes
*Type*: String
*Allowed values*: `ONE_TO_ONE | MANY_TO_MANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailAddress`  <a name="cfn-customerprofiles-domain-attributetypesselector-emailaddress"></a>
The Email type. You can choose from `EmailAddress`, `BusinessEmailAddress` and `PersonalEmailAddress`. You only can use the `EmailAddress` type in the `MatchingRule`. For example, if you want to match profile based on `PersonalEmailAddress` or `BusinessEmailAddress`, you can choose the `PersonalEmailAddress` and the `BusinessEmailAddress` to represent the `EmailAddress` type and only specify the `EmailAddress` on the matching rule.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhoneNumber`  <a name="cfn-customerprofiles-domain-attributetypesselector-phonenumber"></a>
The `PhoneNumber` type. You can choose from `PhoneNumber`, `HomePhoneNumber`, and `MobilePhoneNumber`. You only can use the `PhoneNumber` type in the `MatchingRule`. For example, if you want to match a profile based on `Phone` or `HomePhone`, you can choose the `Phone` and the `HomePhone` to represent the `PhoneNumber` type and only specify the `PhoneNumber` on the matching rule.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `255 | 4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
