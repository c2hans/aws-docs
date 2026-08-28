---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-resilience-testing-iam-ma-create.html
---

# Create the roles and attach them to your test
<a name="next-gen-resilience-testing-iam-ma-create"></a>

In the orchestrator account, create the orchestrator role.

```
aws iam create-role \
  --role-name {{my-orchestrator-role}} \
  --assume-role-policy-document file://orchestrator-trust-policy.json

aws iam put-role-policy \
  --role-name {{my-orchestrator-role}} \
  --policy-name resilience-testing-orchestrator \
  --policy-document file://orchestrator-permissions-policy.json
```

In each target account, create the target role with the permissions policy for your test template.

```
aws iam create-role \
  --role-name {{my-target-role}} \
  --assume-role-policy-document file://target-trust-policy.json

aws iam put-role-policy \
  --role-name {{my-target-role}} \
  --policy-name resilience-testing-target \
  --policy-document file://target-permissions-policy.json
```

Set the orchestrator role as the execution role on your test.

```
aws resiliencehubv2 update-test \
  --test-id {{test-id}} \
  --role-name {{my-orchestrator-role}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
