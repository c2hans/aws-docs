---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/user-application-hardening.html
---

# User application hardening
<a name="user-application-hardening"></a>

|
|
| Essential Eight control | Implementation guidance | AWS resources | AWS Well-Architected guidance |
| --- |--- |--- |--- |
| Web browsers do not process Java from the internet. | See [Technical example: User application hardening](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-user-application-hardening) (ACSC website) | Not applicable | Not applicable |
| Web browsers do not process web advertisements from the internet. |
| Internet Explorer 11 is disabled or removed. |
| Microsoft Office is blocked from creating child processes. |
| Microsoft Office is blocked from creating executable content. |
| Microsoft Office is blocked from injecting code into other processes. |
| Microsoft Office is configured to prevent activation of OLE packages. |
| PDF software is blocked from creating child processes. |
| ACSC or vendor hardening guidance for web browsers, Microsoft Office and PDF software is implemented. |
| Web browser, Microsoft Office and PDF software security settings cannot be changed by users. |
| .NET Framework 3.5 (includes .NET 2.0 and 3.0) is disabled or removed. |
| Windows PowerShell 2.0 is disabled or removed. |
| PowerShell is configured to use Constrained Language Mode. |
| Blocked PowerShell script executions are centrally logged and protected from unauthorised modification and deletion, monitored for signs of compromise, and actioned when cyber security events are detected. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
