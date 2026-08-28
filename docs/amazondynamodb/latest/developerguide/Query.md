---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html
---

# Querying tables in DynamoDB
<a name="Query"></a>

You can use the `Query` API operation in Amazon DynamoDB to find items based on primary key values.

You must provide the name of the partition key attribute and a single value for that attribute. `Query` returns all items with that partition key value. Optionally, you can provide a sort key attribute and use a comparison operator to refine the search results.

For more information on how to use `Query`, such as the request syntax, response parameters, and additional examples, see [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html) in the *Amazon DynamoDB API Reference*.

**Topics**
+ [Key condition expressions for the Query operation in DynamoDB](Query.KeyConditionExpressions.md)
+ [Filter expressions for the Query operation in DynamoDB](Query.FilterExpression.md)
+ [Paginating table query results in DynamoDB](Query.Pagination.md)
+ [Other aspects of working with the Query operation in DynamoDB](Query.Other.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
