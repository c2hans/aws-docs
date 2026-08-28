---
source_url: https://docs.aws.amazon.com/elemental-statmux/latest/installguide/errors-sm-ig.html
---

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Install Error Messages
<a name="errors-sm-ig"></a>

During install, you might see the error message `Hardware and license validation failed` at the command line. The table below provides a list of possible problems and causes that might result in this error.

| Possible Problem | Possible Reason |
| --- | --- |
| eth0 is not set up | You didn't specify the address for eth0. Review the prompts in [Step C: Install the AWS Elemental Software](install-sm-ig-install-sw.md). |
| Products do not match | You might have requested and installed a license for one product (for example, AWS Elemental Statmux) and then installed a different product (for example, AWS Elemental Live). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Statmux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-statmux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
