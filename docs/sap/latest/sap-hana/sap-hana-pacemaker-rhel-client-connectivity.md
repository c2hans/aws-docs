---
source_url: https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-pacemaker-rhel-client-connectivity.html
---

# Client Connectivity
<a name="sap-hana-pacemaker-rhel-client-connectivity"></a>

For proper SAP HANA database connectivity:
+ Ensure that the Overlay IP can be correctly resolved in all application servers
+ DNS configuration or local host entries must be valid
+ Network routing must be properly configured
+ SAP HANA client libraries must be installed and up to date

Ensure that the connectivity data for the SAP HANA Database references the hostname associated with the Overlay IP. For more information see SAP Documentation: [Setting Connectivity Data for the SAP HANA Database](https://help.sap.com/docs/SLTOOLSET/39c32e9783f6439e871410848f61544c/b7ed2d55b0a7f857e10000000a441470.html?version=CURRENT_VERSION_SWPM20)

Test database connectivity using R3trans utility:

```
sidadm> R3trans -d
```

Review additional connections to SAP HANA that require High Availability. While application connectivity should use the overlay IP, administrative tools (SAP HANA Studio, hdbsql commands, monitoring tools) require direct connectivity to individual SAP HANA instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
