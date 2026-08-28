---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_rule-packages.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Amazon Inspector Classic rules packages and rules
<a name="inspector_rule-packages"></a>

You can use Amazon Inspector Classic to assess your assessment targets (collections of AWS resources) for potential security issues and vulnerabilities. Amazon Inspector Classic compares the behavior and the security configuration of the assessment targets to selected security *rules packages*. In the context of Amazon Inspector Classic, a *rule* is a security check that Amazon Inspector Classic performs during the assessment run.

In Amazon Inspector Classic, rules are grouped into distinct *rules packages* either by category, severity, or pricing. This gives you choices for the kinds of analysis that you can perform. For example, Amazon Inspector Classic offers a large number of rules that you can use to assess your applications. But you might want to include a smaller subset of the available rules to target a specific area of concern or to uncover specific security problems. Companies with large IT departments might want to determine whether their application is exposed to any security threat. Others might want to focus only on issues with the severity level of **High**.
+ [Severity levels for rules in Amazon Inspector Classic](#SeverityLevels)
+ [Rules packages in Amazon Inspector Classic](#InspectorRulePackages)

## Severity levels for rules in Amazon Inspector Classic
<a name="SeverityLevels"></a>

Each Amazon Inspector Classic rule has an assigned severity level. This reduces the need to prioritize one rule over another in your analysis. It can also help you determine your response when a rule highlights a potential problem.

**High**, **Medium**, and **Low** levels all indicate a security issue that can result in compromised information confidentiality, integrity, and availability within your assessment target. The levels are distinguished by how likely the issue is to result in a compromise and how urgent it is to fix the issue.

The **Informational** level simply highlights a security configuration detail of your assessment target.

Here are the recommended ways to respond to issues based on their severity:
+ **High** – High severity issues are extremely urgent. Amazon Inspector Classic recommends that you treat this security issue as an emergency and implement an immediate remediation.
+ **Medium** – Medium severity issues are somewhat urgent. Amazon Inspector Classic recommends that you fix this issue at the next possible opportunity, for example, during your next service update.
+ **Low** – Low severity issues are less urgent. Amazon Inspector Classic recommends that you fix this issue as part of one of your future service updates.
+ **Informational** – These issues are purely informational. Based on your business and organization goals, you can either simply make note of this information or use it to improve the security of your assessment target.

## Rules packages in Amazon Inspector Classic
<a name="InspectorRulePackages"></a>

An Amazon Inspector assessment can use any combination of the following rules packages:

**Network assessments:**
+ [Network Reachability](inspector_network-reachability.md)

**Host assessments:**
+ [Common vulnerabilities and exposures](inspector_cves.md)
+ [Center for Internet Security (CIS) Benchmarks](inspector_cis.md)
+ [Security best practices for Amazon Inspector Classic](inspector_security-best-practices.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
