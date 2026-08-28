---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/logging-versions.html
---

# Verified Access logging versions
<a name="logging-versions"></a>

By default, the Verified Access logging system uses Open Cybersecurity Schema Framework (OCSF) version 0.1. For sample logs that use version 0.1 see [OCSF version 0.1 log examples for Verified Access](ocsfv01-examples.md).

The latest logging version is compatible with OCSF version 1.0.0-rc.2. For more information about the schema, see [OCSF Schema](https://schema.ocsf.io/1.0.0-rc.2/classes/access_activity). For sample logs that use version 1.0.0-rc.2, see [OCSF version 1.0.0-rc.2 log examples for Verified Access](ocsfv1-examples.md).

Note that you can't use OCSF version 0.1 if the Verified Access endpoint uses the TCP protocol.

**To upgrade the logging version using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access instances**.

1. Select the appropriate Verified Access instance.

1. On the **Verified Access instance logging configuration** tab, choose **Modify Verified Access instance logging configuration**.

1. Select **ocsf-1.0.0-rc.2** from the **Update log version** drop-down list.

1. Choose **Modify Verified Access instance logging configuration**.

**To upgrade the logging version using the AWS CLI**
Use the [modify-verified-access-instance-logging-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-verified-access-instance-logging-configuration.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
