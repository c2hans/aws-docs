---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/introduction.html
---

# Load testing applications
<a name="introduction"></a>

*Jonatan Reiners and Nicola D Orazio, Amazon Web Services*

Load tests are done to gain reliable information on whether your application is delivering the expected qualities. Although the most common approach is to generate load on your applications, there are different ways you can understand load testing. This guide explores the different ways to load test and what questions can be answered. It will also explain implications of load testing to help prevent pitfalls when running the tests. Finally, the guide will cover several tools and their applicability.

## Important information before you start
<a name="important"></a>

Running load tests on Amazon Web Services (AWS) can initiate security mechanisms. For more information, see the [Amazon Elastic Compute Cloud (Amazon EC2) testing policy](https://aws.amazon.com/ec2/testing/). [Penetration testing](https://aws.amazon.com/security/penetration-testing/) can be run only on permitted AWS services. [Distributed Denial of Service](https://aws.amazon.com/security/ddos-simulation-testing/) (DDoS) testing must be performed by a pre-approved AWS Partner.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
