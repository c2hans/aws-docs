---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-filter-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::Filter Condition
<a name="aws-properties-guardduty-filter-condition"></a>

Specifies the condition to apply to a single field when filtering through GuardDuty findings.

## Syntax
<a name="aws-properties-guardduty-filter-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-guardduty-filter-condition-syntax.json"></a>

```
{
  "[Eq](#cfn-guardduty-filter-condition-eq)" : {{[ String, ... ]}},
  "[Equals](#cfn-guardduty-filter-condition-equals)" : {{[ String, ... ]}},
  "[GreaterThan](#cfn-guardduty-filter-condition-greaterthan)" : {{Integer}},
  "[GreaterThanOrEqual](#cfn-guardduty-filter-condition-greaterthanorequal)" : {{Integer}},
  "[Gt](#cfn-guardduty-filter-condition-gt)" : {{Integer}},
  "[Gte](#cfn-guardduty-filter-condition-gte)" : {{Integer}},
  "[LessThan](#cfn-guardduty-filter-condition-lessthan)" : {{Integer}},
  "[LessThanOrEqual](#cfn-guardduty-filter-condition-lessthanorequal)" : {{Integer}},
  "[Lt](#cfn-guardduty-filter-condition-lt)" : {{Integer}},
  "[Lte](#cfn-guardduty-filter-condition-lte)" : {{Integer}},
  "[Matches](#cfn-guardduty-filter-condition-matches)" : {{[ String, ... ]}},
  "[Neq](#cfn-guardduty-filter-condition-neq)" : {{[ String, ... ]}},
  "[NotEquals](#cfn-guardduty-filter-condition-notequals)" : {{[ String, ... ]}},
  "[NotMatches](#cfn-guardduty-filter-condition-notmatches)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-guardduty-filter-condition-syntax.yaml"></a>

```
  [Eq](#cfn-guardduty-filter-condition-eq): {{
    - String}}
  [Equals](#cfn-guardduty-filter-condition-equals): {{
    - String}}
  [GreaterThan](#cfn-guardduty-filter-condition-greaterthan): {{Integer}}
  [GreaterThanOrEqual](#cfn-guardduty-filter-condition-greaterthanorequal): {{Integer}}
  [Gt](#cfn-guardduty-filter-condition-gt): {{Integer}}
  [Gte](#cfn-guardduty-filter-condition-gte): {{Integer}}
  [LessThan](#cfn-guardduty-filter-condition-lessthan): {{Integer}}
  [LessThanOrEqual](#cfn-guardduty-filter-condition-lessthanorequal): {{Integer}}
  [Lt](#cfn-guardduty-filter-condition-lt): {{Integer}}
  [Lte](#cfn-guardduty-filter-condition-lte): {{Integer}}
  [Matches](#cfn-guardduty-filter-condition-matches): {{
    - String}}
  [Neq](#cfn-guardduty-filter-condition-neq): {{
    - String}}
  [NotEquals](#cfn-guardduty-filter-condition-notequals): {{
    - String}}
  [NotMatches](#cfn-guardduty-filter-condition-notmatches): {{
    - String}}
```

## Properties
<a name="aws-properties-guardduty-filter-condition-properties"></a>

`Eq`  <a name="cfn-guardduty-filter-condition-eq"></a>
Represents the equal condition to apply to a single field when querying for findings.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Equals`  <a name="cfn-guardduty-filter-condition-equals"></a>
Represents an *equal***** condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GreaterThan`  <a name="cfn-guardduty-filter-condition-greaterthan"></a>
Represents a *greater than* condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GreaterThanOrEqual`  <a name="cfn-guardduty-filter-condition-greaterthanorequal"></a>
Represents a *greater than or equal* condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gt`  <a name="cfn-guardduty-filter-condition-gt"></a>
Represents a *greater than* condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gte`  <a name="cfn-guardduty-filter-condition-gte"></a>
Represents the greater than or equal condition to apply to a single field when querying for findings.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LessThan`  <a name="cfn-guardduty-filter-condition-lessthan"></a>
Represents a *less than* condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LessThanOrEqual`  <a name="cfn-guardduty-filter-condition-lessthanorequal"></a>
Represents a *less than or equal* condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lt`  <a name="cfn-guardduty-filter-condition-lt"></a>
Represents the less than condition to apply to a single field when querying for findings.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lte`  <a name="cfn-guardduty-filter-condition-lte"></a>
Represents the less than or equal condition to apply to a single field when querying for findings.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Matches`  <a name="cfn-guardduty-filter-condition-matches"></a>
Represents the *match* condition to be applied to a single field when querying for findings.
 The *matches* condition is available only for create-filter and update-filter APIs.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Neq`  <a name="cfn-guardduty-filter-condition-neq"></a>
Represents the not equal condition to apply to a single field when querying for findings.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotEquals`  <a name="cfn-guardduty-filter-condition-notequals"></a>
Represents a *not equal***** condition to be applied to a single field when querying for findings.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotMatches`  <a name="cfn-guardduty-filter-condition-notmatches"></a>
Represents the *not match* condition to be applied to a single field when querying for findings.
 The *not-matches* condition is available only for create-filter and update-filter APIs.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
