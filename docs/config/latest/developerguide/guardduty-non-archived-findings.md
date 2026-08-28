---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/guardduty-non-archived-findings.html
---

# guardduty-non-archived-findings
<a name="guardduty-non-archived-findings"></a>

Checks if Amazon GuardDuty has findings that are non-archived. The rule is NON\_COMPLIANT if GuardDuty has non-archived low/medium/high severity findings older than the specified number in the daysLowSev/daysMediumSev/`daysHighSev` parameter.

**Identifier:** GUARDDUTY\_NON\_ARCHIVED\_FINDINGS

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

daysLowSev (Optional)Type: intDefault: 30
The number of days Amazon GuardDuty low severity findings are allowed to stay non archived. The default is 30 days.

daysMediumSev (Optional)Type: intDefault: 7
The number of days Amazon GuardDuty medium severity findings are allowed to stay non archived. The default is 7 days.

daysHighSev (Optional)Type: intDefault: 1
The number of days Amazon GuardDuty high severity findings are allowed to stay non archived. The default is 1 day.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d905c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
