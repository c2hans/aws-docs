---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-delete.html
---

# Delete a RAG evaluation job in Amazon Bedrock
<a name="knowledge-base-evaluation-delete"></a>

You can delete a RAG evaluation job that you no longer want to use.

You cannot delete a knowledge base evaluation job with a status that is currently in progress of being created. You can, however, [stop the creation of a knowledge base evaluation job](knowledge-base-evaluation-stop.md).

If you delete a knowledge base evaluation job, it doesn’t automatically delete your Amazon S3 bucket that stores your prompts dataset and the bucket or directory that stores the results of the evaluation. Your IAM role for the evaluation job is also not automatically deleted.

The following example shows you how to delete a knowledge base evaluation job using the AWS CLI.

*AWS Command Line Interface*

```
aws bedrock batch-delete-evaluation-job \
 --job-identifiers '["arn:aws:bedrock:<region>:<account-id>:evaluation-job/<job-id>"]'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
