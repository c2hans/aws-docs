---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector-arns-resources.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# ARNs for Amazon Inspector Classic resources
<a name="inspector-arns-resources"></a>

In Amazon Inspector Classic, the primary resources are resource groups, assessment targets, assessment templates, assessment runs, and findings. These resources have unique Amazon Resource Names (ARNs) associated with them, as shown in the following table.

| Resource Type | ARN Format  |
| --- | --- |
| Resource group | `arn:aws:inspector:{{region}}:{{account-id}}:resourcegroup/{{ID}}` |
| Assessment target | `arn:aws:inspector:{{region}}:{{account-id}}:target/{{ID}} ` |
| Assessment template | `arn:aws:inspector:{{region}}:{{account-id}}:target/{{ID}}:template:{{ID}}` |
| Assessment run | `arn:aws:inspector:{{region}}:{{account-id}}:target/{{ID}}/template/{{ID}}/run/{{ID}}` |
| Finding | `arn:aws:inspector:{{region}}:{{account-id}}:target/{{ID}}/template/{{ID}}/run/{{ID}}/finding/{{ID}}` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
