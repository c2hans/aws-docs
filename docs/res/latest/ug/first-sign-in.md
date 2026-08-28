---
source_url: https://docs.aws.amazon.com/res/latest/ug/first-sign-in.html
---

# Step 2: Sign in for the first time
<a name="first-sign-in"></a>

After the product stack deploys in your account, you receive an email with your credentials. Use the URL to sign in to your account and configure the workspace for other users.

![First sign in email invitation](http://docs.aws.amazon.com/res/latest/ug/images/res-firstsignin.png)

After you sign in for the first time, you can configure settings in the web portal to connect to the SSO provider. For post-deployment configuration information, see the [Configuration guide](configuration-guide.md). Note that `clusteradmin` is a break-glass account— you can use it to create projects and assign user or group membership to those projects; it cannot assign software stacks or deploy a desktop for itself.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
