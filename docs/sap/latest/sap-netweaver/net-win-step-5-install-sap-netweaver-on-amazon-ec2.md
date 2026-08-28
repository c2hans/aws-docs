---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-step-5-install-sap-netweaver-on-amazon-ec2.html
---

# Step 5: Install SAP NetWeaver on Amazon EC2
<a name="net-win-step-5-install-sap-netweaver-on-amazon-ec2"></a>

You are now ready to install SAP NetWeaver on this EC2 instance using the downloaded software. Proceed with the instructions in the SAP installation guide for your version of SAP NetWeaver.

You will need to do this for a minimum of:
+ the ASCS instance
+ the DB instance (on the installed database server)
+ the PAS instance

and optionally for:
+ other AAS instances
+ ERS instance on the second ASCS node (in different AZ)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
