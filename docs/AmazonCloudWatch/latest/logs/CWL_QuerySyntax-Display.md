---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Display.html
---

# **display**
<a name="CWL_QuerySyntax-Display"></a>

 Use `display` to show a specific field or fields in query results.

 The `display` command shows only the fields you specify. If your query contains multiple `display` commands, the query results show only the field or fields that you specified in the final `display` command.

 **Example: Display one field**

 The code snippet shows an example of a query that uses the parse command to extract data from `@message` to create the extracted fields `loggingType` and `loggingMessage`. The query returns all log events where the values for `loggingType` are **ERROR**. `display` shows only the values for `loggingMessage` in the query results.

```
fields @message
| parse @message "[*] *" as loggingType, loggingMessage
| filter loggingType = "ERROR"
| display loggingMessage
```

**Tip**
 Use `display` only once in a query. If you use `display` more than once in a query, the query results show the field specified in the last occurrence of `display` command being used.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
