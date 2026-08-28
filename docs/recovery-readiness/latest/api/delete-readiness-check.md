---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/delete-readiness-check.html
---

# Delete a readiness check
<a name="delete-readiness-check"></a>

The following is an example of a request to delete a readiness check. Note that there is no response on success when you delete a readiness check.

```
aws route53-recovery-readiness --region us-west-2 delete-readiness-check \
			--readiness-check-name ebs-volume-readiness
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
