---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/delete-routing-control.html
---

# Delete a routing control
<a name="delete-routing-control"></a>

The following is an example of a request to delete a routing control. Deleting a routing control doesn't return a response.

```
aws route53-recovery-control-config --region us-west-2 delete-routing-control \
			--routing-control-arn arn:aws:route53-recovery-control::888888888888:controlpanel/zzz123yyy456xxx789zzz123yyy456xxx/routingcontrol/abc123abc123abc
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
