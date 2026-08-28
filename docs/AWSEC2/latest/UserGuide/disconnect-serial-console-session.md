---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disconnect-serial-console-session.html
---

# Disconnect from the EC2 Serial Console
<a name="disconnect-serial-console-session"></a>

If you no longer need to be connected to your instance's EC2 Serial Console, you can disconnect from it. When you disconnect from the serial console, any shell session running on the instance will continue to run. If you want to end the shell session, you'll need to end it before disconnecting from the serial console.

**Considerations**
+ The serial console connection typically lasts for 1 hour unless you disconnect from it. However, during system maintenance, Amazon EC2 will disconnect the serial console session.
+ It takes 30 seconds to tear down a session after you've disconnected from the serial console to allow a new session.

The way to disconnect from the serial console depends on the client.

**Browser-based client**
To disconnect from the serial console, close the serial console in-browser terminal window.

**Standard OpenSSH client**
To disconnect from the serial console, use the following command to close the SSH connection. This command must be run immediately following a new line.

```
~.
```

The command that you use for closing an SSH connection might be different depending on the SSH client that you're using.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
