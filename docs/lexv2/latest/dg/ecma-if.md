---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/ecma-if.html
---

# If statement
<a name="ecma-if"></a>

You can add if statements to perform functions in Amazon Lex V2. This example shows the syntax that can be used in SRGS expressions.

```
if (expressions) {
    statements;
} else {
    statements;
}
```

**Note:** In the preceding example, `expressions` and `statements` must be one of the supported ones from this document.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
