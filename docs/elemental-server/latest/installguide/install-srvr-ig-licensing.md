---
source_url: https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-licensing.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Step D: Set-Up Licensing
<a name="install-srvr-ig-licensing"></a>

At this point, the software is installed but it is not yet enabled. To begin using the software, install a valid license file on each node.

To do so, follow the detailed steps described in the following table.

| Step | Where to Perform Step | Start Step With | Finish Step With |
| --- | --- | --- | --- |
| Step a: Retrieve Activation Code | Your workstation | Activation email | Activation code |
| Step b: Generate License Activation Key File | The AWS Elemental system, via an SSH client like PuTTY | Activation code | Key file (.key ) |
| Step c: Download Licenses from the AWS Elemental User Community | Your workstation | Key file (.key ) | Tarball file (.tgz) |
| Step d: Install the License Files | Your workstation | Unlicensed software with limited functionality | Fully licensed, full-feature software |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
