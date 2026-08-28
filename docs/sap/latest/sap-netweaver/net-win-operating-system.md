---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-operating-system.html
---

# Operating System
<a name="net-win-operating-system"></a>

If you plan on using Windows other than via Amazon EC2 for Windows Server, then ensure that you have the appropriate licenses and tenancy type selected. For more details, refer to your licensing terms and conditions, and see our [Windows on AWS](https://aws.amazon.com/windows/) webpage.

A base AMI is required to launch an Amazon EC2 instance. For SAP NetWeaver workloads on Windows, you need to run Windows Server 2012 R2, or later, because older versions are no longer supported by SAP. If you are using bring your own license (BYOL) instead of license-included for Windows Server, you will need to create your own AMI. See [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/).

Ensure that you have access to the appropriate Windows Server AMIs before proceeding.

As with any operating system, we recommend that you keep the OS up-to-date with the latest patches. You can also refer to the following SAP Notes:
+  [2325651](https://me.sap.com/notes/2325651): Required Windows Patches for SAP Operations

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
