---
source_url: https://docs.aws.amazon.com/devicefarm/latest/testgrid/techref-limits.html
---

# Quotas in Device Farm desktop browser testing
<a name="techref-limits"></a>

Exceeding the following limits will result in session creation failure:
+ You may have up to 50 sessions in an `active` state at any time.
+ You may create up to 5 sessions per second.
+ You may call `createTestGridUrl` up to 10 times a second.
+ No `POST` payload may be greater than 30MB.

If you have too many open sessions or create them too fast, session creation will fail. If you require more than 50 concurrent sessions, open a technical support case with your use case. For more information about increasing your service quota, see [AWS Service Quotas](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
