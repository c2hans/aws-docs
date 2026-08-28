---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-applying-policies.html
---

# Applying policies at user journey and service levels
<a name="next-gen-applying-policies"></a>

Policies can be applied at two levels of the application hierarchy:

| Level | How to apply | Who typically owns it |
| --- | --- | --- |
| User journey | Applied on the user journey within the system | Central SRE team |
| Service | Applied directly on the service entity | Service team |

To apply a policy to a user journey, use the following command. All services within that user journey are evaluated against this policy:

```
aws resiliencehubv2 update-user-journey \
  --system-arn "arn:aws:resiliencehub:{{region}}:{{account-id}}:system/{{system-name}}:{{id}}" \
  --user-journey-id "{{user-journey-id}}" \
  --policy-arn "arn:aws:resiliencehub:us-east-1:123456789012:policy/critical-dr:abc123"
```

To apply a policy directly to a service, use the following command:

```
aws resiliencehubv2 update-service \
  --service-arn "arn:aws:resiliencehub:..." \
  --policy-arn "arn:aws:resiliencehub:us-east-1:123456789012:policy/high-performance:def456"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
