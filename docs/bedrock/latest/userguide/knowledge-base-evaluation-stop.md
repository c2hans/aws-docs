---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-stop.html
---

# Stop a RAG evaluation job in Amazon Bedrock
<a name="knowledge-base-evaluation-stop"></a>

You can stop a Retrieval Augmented Generation (RAG) evaluation job that is currently processing so that you can easily reconfigure your evaluation and chosen metrics, for example.

The following example shows you how to stop a knowledge base evaluation job using the AWS CLI.

*AWS Command Line Interface*

```
aws bedrock stop-evaluation-job \
 --job-identifier "arn:aws:bedrock:<region>:<account-id>:evaluation-job/<job-id>"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
