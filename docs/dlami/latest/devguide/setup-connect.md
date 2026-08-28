---
source_url: https://docs.aws.amazon.com/dlami/latest/devguide/setup-connect.html
---

# Connecting to a DLAMI instance
<a name="setup-connect"></a>

After you [launch a DLAMI instance](launch.md) and the instance is running, you can connect to it from a client (Windows, macOS, or Linux) using SSH. For instructions, see [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the *Amazon EC2 User Guide*.

Keep a copy of the SSH login command handy in case you want to set up a Jupyter Notebook server after you log in. To connect to the Jupyter webpage, you use a variation of that command.

**Next step**
[Setting up a Jupyter Notebook server on a DLAMI instance](setup-jupyter.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Deep Learning AMI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlami` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
