---
source_url: https://docs.aws.amazon.com/elemental-server/latest/installguide/errors-srvr-ig.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Install Error Messages
<a name="errors-srvr-ig"></a>

During install, you might see the error message `Hardware and license validation failed` at the command line. The table below provides a list of possible problems and causes that might result in this error.

| Possible Problem | Possible Reason |
| --- | --- |
| eth0 is not set up | You didn't specify the address for eth0. Review the prompts in [Step C: Install the AWS Elemental Software](install-srvr-ig-install-sw.md). |
| eme.lic is not valid | If you're installing licenses on several hardware units, you may have installed the wrong eme.lic license on this unit. Review the steps in [Step D: Set-Up Licensing](install-srvr-ig-licensing.md). |
| cable.lic is not valid | If you're installing licenses on several hardware units, you may have installed the wrong cable.lic license on this unit. Review the steps in [Step D: Set-Up Licensing](install-srvr-ig-licensing.md). |
| Products do not match | You might have requested and installed a license for one product (for example, AWS Elemental Server) and then installed a different product (for example, AWS Elemental Live). |
| Card counts do not match | If you changed the CPU or GPU cards on the hardware unit after requesting the license, the license might no longer be valid. Change the cards back or contact your sales representative to discuss your revised licensing requirements. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
