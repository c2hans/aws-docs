---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/shield-limits.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS Shield Advanced quotas
<a name="shield-limits"></a>

AWS Shield Advanced has default quotas on the number of entities per Region. You can [request an increase](https://console.aws.amazon.com/servicequotas/home/services/shield/quotas) in these quotas.

| Resource | Default quota |
| --- | --- |
| Maximum number of protected resources for each resource type that AWS Shield Advanced offers protection for, per account.  | 1,000 |
| Maximum number of protection groups, per account.  | 100 |
| Maximum number of individual protected resources that you can specifically include in a protection group. In the API, this applies to the `Members` that you specify when you set the protection group `Pattern` to `ARBITRARY`. In the console, this applies to the resources that you select for the protection grouping **Choose from protected resources**. | 1,000 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
