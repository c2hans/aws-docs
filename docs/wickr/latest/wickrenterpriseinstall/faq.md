---
source_url: https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/faq.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# FAQ
<a name="faq"></a>

Q: My deployment fails with the following error in helm stderr:

`Error: UPGRADE FAILED: cannot patch "enterprise-init" with kind Job: Job.batch "enterprise-init" is invalid: spec.template: Invalid value: core.`

A: This can happen when Debug Logging is enabled. Please disable debug logging, delete the problematic jobs, and try again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
