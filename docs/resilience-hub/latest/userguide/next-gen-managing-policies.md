---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-managing-policies.html
---

# Managing and updating policies
<a name="next-gen-managing-policies"></a>

You can list, update, and delete resilience policies from the the next generation of Resilience Hub console or AWS CLI.

To list all policies in your account:

```
aws resiliencehubv2 list-policies
```

To update a policy:

```
aws resiliencehubv2 update-policy \
  --policy-arn "arn:aws:resiliencehub:..." \
  --availability-slo '{"target": 99.99}'
```

Changes to a policy take effect on the next failure mode assessment for all services using that policy.

You cannot delete a policy that is currently applied to services or user journeys. Remove all associations first.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
