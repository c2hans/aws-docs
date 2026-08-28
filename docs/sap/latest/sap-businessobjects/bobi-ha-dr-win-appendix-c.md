---
source_url: https://docs.aws.amazon.com/sap/latest/sap-businessobjects/bobi-ha-dr-win-appendix-c.html
---

# Additional Tips
<a name="bobi-ha-dr-win-appendix-c"></a>

## Tagging AWS Resources
<a name="bobi-ha-dr-win-tagging-resources"></a>

Adding tags to AWS objects will make it much easier to manage the SAP HA environment, and can also help you search for resources quickly. You can use Amazon EC2 API calls in conjunction with a special tag filter. For more information about tagging resources, see the [AWS documentation](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tagging-resources.html).

## Third-Party Software Components
<a name="bobi-ha-dr-win-3rd-party-sw-components"></a>

Additional third-party components might be integral to running business processes within an SAP environment. After you determine your requirements, consider leveraging some of the concepts discussed in this guide, such as:
+ Installing third-party software components on multiple instances
+ Creating Amazon EBS-backed AMI images of key third-party systems, so you can launch them on demand in case of failures
+ Using multiple interfaces to control access to specific software components
+ Using multiple Availability Zones for critical third-party software components

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
