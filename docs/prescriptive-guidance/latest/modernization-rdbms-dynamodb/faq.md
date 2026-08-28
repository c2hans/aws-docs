---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about using DynamoDB.

**Q. What is the maximum table size that I can create in DynamoDB?**

A. There is no limit on the table size or number of columns that you can create.

 **Q. How many tables can I create per account?**

A. You can create up to 2500 tables for each AWS Region per account. If you want to create more tables, you can request a service quota increase at [https://aws.amazon.com/support](https://aws.amazon.com/support).

**Q. How many global secondary indexes can I create on a DynamoDB table?**

A. There is initial quota of 20 global secondary indexes per table. If you want to create more indexes, you can request a service quota increase at [https://aws.amazon.com/support](https://aws.amazon.com/support).

**Q. How many items can I add or modify per transaction?**

A. You can add or modify up to 100 items (or 4 MB of data) per transaction. If you want to write more than 100 records to a table, you can use batched write operations.

For a full list of quotas, see [Quotas in Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the DynamoDB documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
