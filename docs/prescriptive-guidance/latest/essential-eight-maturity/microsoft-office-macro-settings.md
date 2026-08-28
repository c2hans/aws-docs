---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/microsoft-office-macro-settings.html
---

# Configure Microsoft Office macro settings
<a name="microsoft-office-macro-settings"></a>

|
|
| Essential Eight control | Implementation guidance | AWS resources | AWS Well-Architected guidance |
| --- |--- |--- |--- |
| Microsoft Office macros are disabled for users that do not have a demonstrated business requirement. | See [Technical example: Configure macro settings](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/small-business-cyber-security/small-business-cloud-security-guide/technical-example-configure-macro-settings) (ACSC website) | Not applicable | Not applicable |
| Only Microsoft Office macros running from within a sandboxed environment, a Trusted Location or that are digitally signed by a trusted publisher are allowed to execute. |
| Only privileged users responsible for validating that Microsoft Office macros are free of malicious code can write to and modify content within Trusted Locations. |
| Microsoft Office macros digitally signed by an untrusted publisher cannot be enabled via the Message Bar or Backstage View. |
| Microsoft Office's list of trusted publishers is validated on an annual or more frequent basis. |
| Microsoft Office macros in files originating from the internet are blocked. |
| Microsoft Office macro antivirus scanning is enabled. |
| Microsoft Office macros are blocked from making Win32 API calls. |
| Microsoft Office macro security settings cannot be changed by users. |
| Allowed and blocked Microsoft Office macro executions are centrally logged and protected from unauthorised modification and deletion, monitored for signs of compromise, and actioned when cyber security events are detected. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
