---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.CustomPassword.html
---

# Creating custom functions to verify passwords
<a name="Appendix.Oracle.CommonDBATasks.CustomPassword"></a>

You can create a custom password verification function in the following ways:
+ To use standard verification logic, and to store your function in the `SYS` schema, use the `create_verify_function` procedure.
+ To use custom verification logic, or to avoid storing your function in the `SYS` schema, use the `create_passthrough_verify_fcn` procedure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
