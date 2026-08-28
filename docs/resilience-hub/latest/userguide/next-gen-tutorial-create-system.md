---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-tutorial-create-system.html
---

# Create a system
<a name="next-gen-tutorial-create-system"></a>

**Console:**

1. Open the the next generation of Resilience Hub console.

1. Choose **Systems** > **Create system**.

1. Enter a name (for example, `My Application`) and an optional description.

1. Choose **Create**.

**AWS CLI:**

```
aws resiliencehubv2 create-system \
  --name "my-application" \
  --description "My first application in Resilience Hub"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
