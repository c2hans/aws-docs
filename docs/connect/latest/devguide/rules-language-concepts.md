---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/rules-language-concepts.html
---

# Concepts
<a name="rules-language-concepts"></a>

The following terms are used in the Rules Function language.

**Operator**
A function that is used to evaluate Operands. The very top Operator has to be either AND or OR.

**Operands**
An array of objects that Operator is evaluating on. The length the array and the type of each object depends on the Operator defined on the same level.

**ComparisonValue**
A JSON path string that specifies the value field the rule is comparing.

**FilterClause**
An object that defines additional criteria that the rule is evaluating against. Depending on **ComparisonValue**, the value of this field varies.

**Negate**
A Boolean value that indicates if negation should be applied to the operator.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
