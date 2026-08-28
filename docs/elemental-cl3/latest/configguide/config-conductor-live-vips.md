---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-vips.html
---

# Configuring virtual input switching
<a name="config-conductor-live-vips"></a>

On ECL3; node, you can configure the maximum number of virtual inputs allowed with the virtual input switching feature. The default is 8 inputs on the node. For information about this feature, see [*AWS Elemental Live User Guide*](https://docs.aws.amazon.com/elemental-live/latest/ug).

**To set the number of virtual inputs**

If you want to enable this feature after you've enabled user authentication, you must log into the Elemental Live node as an administrator. Regular users can't log into the worker nodes.

1. On the Elemental Live web interface, go to **Settings** and choose **Advanced**.

1. Enter a number in **Maximum number of virtual inputs**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
