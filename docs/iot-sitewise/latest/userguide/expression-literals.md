---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-literals.html
---

# Use literals in formula expressions
<a name="expression-literals"></a>

AWS IoT SiteWise supports the use of literals in expressions and formulas. Literals are fixed values that represent a specific data type. In AWS IoT SiteWise, you can define number and string literals in formula expressions. Literals can be used in various contexts, including data transformations, alarm conditions, and visualization calculations.

+ <a name="number-literal-definition"></a>**Numbers**

  Use numbers and scientific notation to define integers and doubles. You can use [E notation](https://en.wikipedia.org/wiki/Scientific_notation#E_notation) to express numbers with scientific notation.

  Examples: `1`, `2.0`, `.9`, `-23.1`, `7.89e3`, `3.4E-5`
+ <a name="string-literal-definition"></a>**Strings**

  Use the `'` (quote) and `"` (double quote) characters to define strings. The quote type for the start and end must match. To escape a quote that matches the one that you use to declare a string, include that quote character twice. This is the only escape character in AWS IoT SiteWise strings.

  Examples: `'active'`, `"inactive"`, `'{"temp": 52}'`, `"{""temp"": ""high""}"`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
