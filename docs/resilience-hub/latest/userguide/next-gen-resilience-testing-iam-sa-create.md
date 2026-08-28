---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-resilience-testing-iam-sa-create.html
---

# Create the role and attach it to your test
<a name="next-gen-resilience-testing-iam-sa-create"></a>

Save the trust policy as `trust-policy.json` and the permissions policy as `permissions-policy.json`, then create the role with the AWS CLI.

```
aws iam create-role \
  --role-name {{my-resilience-testing-role}} \
  --assume-role-policy-document file://trust-policy.json

aws iam put-role-policy \
  --role-name {{my-resilience-testing-role}} \
  --policy-name resilience-testing \
  --policy-document file://permissions-policy.json
```

Set the role on your test so that Resilience Hub uses it for test runs.

```
aws resiliencehubv2 update-test \
  --test-id {{test-id}} \
  --role-name {{my-resilience-testing-role}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
