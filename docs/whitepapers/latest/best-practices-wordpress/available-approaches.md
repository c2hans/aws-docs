---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/available-approaches.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Available approaches
<a name="available-approaches"></a>

 AWS has a number of different options for provisioning virtual machines. There are three main ways to host your own WordPress website on AWS:
+  Amazon Lightsail
+  Amazon Elastic Compute Cloud (Amazon EC2)
+  AWS Marketplace

 [Amazon Lightsail](https://aws.amazon.com/lightsail) is a service that allows you to quickly launch a virtual private server (a Lightsail instance) to host a WordPress website. Lightsail is the easiest way to get started if you don’t need highly configurable instance types or access to advanced networking features.

 [Amazon EC2](https://aws.amazon.com/ec2/) is a web service that provides resizable compute capacity so you can launch a virtual server within minutes. Amazon EC2 provides more configuration and management options than Lightsail, which is desirable in more advanced architectures. You have administrative access to your EC2 instances and can install any software packages you choose, including WordPress.

 [AWS Marketplace](https://aws.amazon.com/marketplace) is an online store where you can find, buy, and quickly deploy software that runs on AWS. You can use 1-Click deployment to launch preconfigured WordPress images directly to Amazon EC2 in your own AWS account in just a few minutes. There are a number of Marketplace vendors offering ready-to-run WordPress instances.

 This whitepaper covers the Lightsail option as the recommended implementation for a single server WordPress website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
