---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-migration-step1.html
---

# Identify the application to migrate
<a name="next-gen-migration-step1"></a>

Use the AWS Resilience Hub v1 API to find the application ARN you want to migrate.

```
# List your v1 applications
aws resiliencehub list-apps
```

Note the ARN of the application you want to migrate. You use this ARN in the next step.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
