---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/testing-language-actions-assertion.html
---

# Assertion
<a name="testing-language-actions-assertion"></a>

Validates that a specific attribute or value in the flow matches expected criteria.

## Parameters
<a name="testing-language-actions-assertion-parameters"></a>
+ Identifier: Unique identifier for the action
+ Type: Must be `Assert`
+ Parameters:
  + Namespace: JSON path to the attribute value to check
  + Operator: Comparison operator to use (see [Supported operators](#testing-language-actions-assertion-operators))
  + Operand: Expected value to compare against
+ Transitions
  + NextAction: The unique identifier for the next action

## Supported operators
<a name="testing-language-actions-assertion-operators"></a>
+ Equals: Exact match
+ TextStartsWith: Text begins with the operand
+ TextEndsWith: Text ends with the operand
+ TextContains: Text contains the operand
+ NumberGreaterThan: Numeric value is greater than operand
+ NumberGreaterOrEqualTo: Numeric value is greater than or equal to operand
+ NumberLessThan: Numeric value is less than operand
+ NumberLessOrEqualTo: Numeric value is less than or equal to operand
+ Exists: Checks if the attribute exists (operand not required)

```
{
   "Identifier": "ActionId",
   "Type": "Assert",
   "Parameters": {
       "Namespace": "string", // Data path to fetch.
       "Operator": "string", // Comparison operator.
       "Operand": "string" // Expected value to compare.
   },
   "Transitions": { "NextAction": "string" }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
