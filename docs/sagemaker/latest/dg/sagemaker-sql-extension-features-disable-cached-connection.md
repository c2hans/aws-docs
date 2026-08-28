---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-sql-extension-features-disable-cached-connection.html
---

# Disable cached connections
<a name="sagemaker-sql-extension-features-disable-cached-connection"></a>

To disable connection caching, run the following command:

```
%sm_sql_manage --set-connection-reuse False
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
