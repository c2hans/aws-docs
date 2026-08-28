---
source_url: https://docs.aws.amazon.com/dcv/latest/access-console/verify-setup.html
---

# Verifying the setup
<a name="verify-setup"></a>

At this point, the Amazon DCV Access Console should be accessible at the public DNS of the Web Client host. Navigate to `https://{{web client DNS}}` in your web browser. It should redirect to the DNS of the Authentication Server.

If you chose to use PAM authentication, you should be able to log in using the credentials of any user on the host the Authentication Server is running on.

If you chose to use Header-Based Authentication, you will need to modify your request headers using an extension like **Requestly**. You should add a new header with the name being what you chose with the Setup Wizard, and the value as the username you want to log in as.

If you have issues, refer to [Troubleshooting](troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
