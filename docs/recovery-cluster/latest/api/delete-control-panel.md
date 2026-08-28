---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/delete-control-panel.html
---

# Delete a control panel
<a name="delete-control-panel"></a>

The following is an example of a request to delete a control panel. Deleting a control panel doesn't return a response.

```
aws route53-recovery-control-config --region us-west-2 delete-control-panel \
			--control-panel-arn arn:aws:route53-recovery-control::012345678901:controlpanel/aaa123bbb456ccc789aaa123bbb456ccc789
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
