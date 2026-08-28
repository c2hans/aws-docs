---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/servers.html
---

# Step 1: Prepare the Amazon DCV servers
<a name="servers"></a>

You must have a fleet of Amazon DCV servers with which you intend to use Session Manager. For more information about installing Amazon DCV servers, see [Installing the Amazon DCV server](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing.html) in the *Amazon DCV Administrator Guide*.

On Linux and macOS Amazon DCV servers, Session Manager uses a local service user named `dcvsmagent`. This user is automatically created when the Session Manager agent is installed. You must grant this service user administrator privileges for Amazon DCV so that it can perform actions on behalf of other users. To grant the Session Manager service user administrator privileges, do the following:

**To add the local service user for Linux and macOS Amazon DCV servers**

1. Open `/etc/dcv/dcv.conf` using your preferred text editor.

1. Add the `administrators` parameter to the `[security]` section and specify the Session Manager user. For example:

   ```
   [security]
   administrators=["dcvsmagent"]
   ```

1. Save and close the file.

1. Stop and restart the Amazon DCV server.

Session Manager is only able to create Amazon DCV sessions on behalf of users that already exist on the Amazon DCV server. If a request is made to create a session for a user that doesn't exist, the request fails. Therefore, you must ensure that each intended end user has a valid system user on the Amazon DCV server.

**Tip**
If you intend to use multiple broker hosts or Amazon DCV servers with agents, we recommend that you configure only one broker and one Amazon DCV server with an agent by performing the following steps, creating Amazon Machine Images (AMI) of the hosts with the completed configurations, and then using the AMIs to launch the remaining brokers and Amazon DCV servers. Alternatively, you can use AWS Systems Manager to run the commands on multiple instances remotely.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
