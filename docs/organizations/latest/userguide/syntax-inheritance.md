---
source_url: https://docs.aws.amazon.com/organizations/latest/userguide/syntax-inheritance.html
---

# Policy syntax and inheritance for declarative policy types
<a name="syntax-inheritance"></a>

Exactly how policies affect the OUs and accounts that inherit them depends on the type of declarative policy you choose. Declarative policy types include:
+ [EC2 policies](orgs_manage_policies_ec2.md)
+ [Backup policies](orgs_manage_policies_backup.md)
+ [Tag policies](orgs_manage_policies_tag-policies.md)
+ [Chat applications policies](orgs_manage_policies_chatbot.md)
+ [AI services opt-out policies](orgs_manage_policies_ai-opt-out.md)
+ [Security Hub policies](orgs_manage_policies_security_hub.md)
+ [Bedrock policies](orgs_manage_policies_bedrock.md)
+ [Inspector policies](orgs_manage_policies_inspector.md)
+ [Upgrade rollout policies](orgs_manage_policies_upgrade_rollout.md)
+ [S3 policies](orgs_manage_policies_s3.md)
+ [AWS Shield Network Security Director policies](orgs_manage_policies_network_security_director.md)

The syntax for declarative policy types includes *[Inheritance operators](policy-operators.md)*, which enable you to specify with fine granularity what elements from the parent policies are applied and what elements can be overridden or modified when inherited by child OUs and accounts.

The *effective policy* is the set of rules that are inherited from the organization root and OUs along with those directly attached to the account. The effective policy specifies the final set of rules that apply to the account. You can view the effective policy for an account that includes the effect of all of the inheritance operators in the policies applied. For more information, see [Viewing effective declarative policies](orgs_manage_policies_effective.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
