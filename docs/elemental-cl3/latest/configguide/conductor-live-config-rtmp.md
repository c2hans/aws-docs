---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-rtmp.html
---

# Configuring for RTMP inputs
<a name="conductor-live-config-rtmp"></a>

The Elemental Live nodes are configured by default to support RTMP inputs. In this mode, Elemental Live is using processing resources to continually poll for input at the RTMP port. If you don't plan to support RTMP inputs, you can choose to disable these inputs, to release the processing resources.

**To disable polling for RTMP inputs**

If you want to enable this feature after you've enabled user authentication, you must log into the Elemental Live node as an administrator. Regular users can't log into the worker nodes.

1. On the Elemental Live web interface, go to **Settings** and choose **Advanced**.

1. Set **Enable RTMP input** to unselected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
