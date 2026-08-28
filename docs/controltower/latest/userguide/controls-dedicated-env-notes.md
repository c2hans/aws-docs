---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/controls-dedicated-env-notes.html
---

# Important Notes
<a name="controls-dedicated-env-notes"></a>

 Creating an AWS Control Tower environment establishes a trusted relationship with AWS Organizations, enabling drift detection for preventive controls, and tracking of account and OU changes. During setup, AWS Control Tower creates a landing zone configuration that serves as the foundation for your managed controls environment.

 To create your controls-dedicated environment via APIs please see: [Get started with AWS Control Tower using APIs](getting-started-apis.md). Note that the manifest field is now optional with landing zone 4.0.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
