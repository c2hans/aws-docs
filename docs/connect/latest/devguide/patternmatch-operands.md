---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/patternmatch-operands.html
---

# PatternMatch Operands
<a name="patternmatch-operands"></a>

Each operand is an array of Pattern match objects.

## PatternMatch Object
<a name="patternmatch-object"></a>

**Type**
+ Description: The type of the pattern match object.
+ Type: String
+ Valid values: `PLAIN` \| `LIST` \| `PROXIMITY` \| `NUMERICAL`
+ Required: Yes

**Value**
+ Description: Depending on the type, value type varies.
  + If type is `PLAIN`, Value is a string.
  + If type is `LIST`, Value is an array of `PLAIN` PatternMatch object.
  + If type is `PROXIMITY`, Value is an object for format.

    ```
    {
      "Distance": number,
      "IsWithin": boolean
    }
    ```
  + If type is `NUMERICAL`, Value is an object for format.

    ```
    {
      "Decimal": boolean
    }
    ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
