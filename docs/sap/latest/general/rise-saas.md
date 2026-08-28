---
source_url: https://docs.aws.amazon.com/sap/latest/general/rise-saas.html
---

# Connecting to SaaS from RISE
<a name="rise-saas"></a>

When modernizing the SAP landscape, you may subscribe to several SAP cloud solutions or SaaS from independent software vendors to complement RISE with SAP solution.

When the cloud solutions are running on AWS (in the same AWS region or different AWS regions), the connectivity from RISE with SAP is kept within the AWS global network without requiring internet connectivity. The connectivity is retained through the provided squid proxy server within RISE with SAP VPC.For more information, see [Amazon VPC FAQs - Does traffic go over the internet when two instances communicate using public IP addresses or when instances communicate with a public AWS service endpoint ?](https://aws.amazon.com/vpc/faqs/).

![Connecting to cloud solutions or SaaS from RISE.](http://docs.aws.amazon.com/sap/latest/general/images/rise-saas1.png)

If your cloud is running on other data centre or with another cloud service provider, then you need internet connectivity.

![Connecting to cloud solutions or SaaS from RISE.](http://docs.aws.amazon.com/sap/latest/general/images/rise-saas2.png)

SaaS cloud solutions do not offer connectivity via VPN, Direct Connect or any other means of private connectivity. You can implement a centralized egress to internet architecture to manage this connectivity. For more information, see [Centralized egress to internet](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-egress-to-internet.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
