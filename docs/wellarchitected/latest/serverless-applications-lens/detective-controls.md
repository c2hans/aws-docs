---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/detective-controls.html
---

# Detective controls
<a name="detective-controls"></a>

Log management is an important part of a well-architected design for reasons ranging from security and forensics to regulatory or legal requirements.

 It is equally important that you track vulnerabilities in application dependencies because attackers can exploit known vulnerabilities found in dependencies regardless of which programming language is used.

 For application dependency vulnerability scans, there are several commercial and open-source solutions, such as OWASP Dependency Check, that can integrate within your CI/CD pipeline. It’s important to include all your dependencies, including AWS SDKs, as part of your version control software repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
