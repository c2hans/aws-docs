---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/business-continuity-1.html
---

# Business Continuity
<a name="business-continuity-1"></a>

 AWS recommends that you periodically schedule business continuity process validations by executing disaster recovery (DR) tests. This planned activity will help to flush out any potential unknowns and help the organization to deal with any real disaster in a streamlined manner. Depending on your disaster recovery architecture, business continuity may include:
+ Backup/recovery of database from AmazonS3
+ Creation of systems from AMI and point-in-time recovery via snapshots
+ Changing the EC2 instance size of pilot light system
+ Validation of integration (AD/DNS, email, third party, and so on.)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
