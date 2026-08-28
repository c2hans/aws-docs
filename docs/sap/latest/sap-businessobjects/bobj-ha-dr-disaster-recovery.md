---
source_url: https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobj-ha-dr-disaster-recovery.html
---

# Disaster Recovery
<a name="bobj-ha-dr-disaster-recovery"></a>

The DR approach you take for SAP BusinessObjects BI Platform, as for any other enterprise application, depends on your RTO and RPO requirements. As discussed in [SAP Note 2056228](https://me.sap.com/notes/2056228), there are two options for building a DR site for SAP BusinessObjects BI Platform:
+ Fully or selectively using SAP Lifecycle Manager (LCM) or Data Federation Services to promote or distribute the content from the primary system.
+ Periodically copying over the CMS database and FRS contents, and using that to start a secondary system when required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
