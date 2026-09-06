---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/introduction.html
---

# Migrating on-premises servers to AWS over private networks by using AWS Transform MGN
<a name="introduction"></a>

*Mike Kuznetsov and Dipin Jain, Amazon Web Services*

Many companies migrate to Amazon Web Services (AWS) from isolated or semi-isolated network environments such as on-premises data centers or other cloud or hybrid infrastructures. Such isolated networks typically do not allow any egress traffic to external endpoints, which is required for migration over the network. Other companies do allow HTTPS egress traffic from their internal networks but do not permit specific communications on [network ports](https://docs.aws.amazon.com/mgn/latest/ug/Network-Requirements.html#Communication-TCP-1500) required by [AWS Transform MGN](https://aws.amazon.com/application-migration-service/), which is the primary AWS service for [large lift-and-shift migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/welcome.html). In a third scenario, HTTPS traffic is allowed from both source and staging areas, but data replication traffic is required to go over the private channel for compliance reasons.

MGN [supports these use cases](https://docs.aws.amazon.com/mgn/latest/ug/installing-agent-blocked.html) and allows you to migrate from secured isolated environments by using only private or hybrid private/public network connectivity. This guide describes these three scenarios, ranging from the two hybrid public/private models to the fully isolated one, and focuses on detailed steps and infrastructure requirements for the most restrictive, private-only option. It builds on the AWS Prescriptive Guidance pattern [Connect to MGN data and control planes over a private network](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/connect-to-application-migration-service-data-and-control-planes-over-a-private-network.html) by providing:
+ Additional details on required connectivity in each scenario
+ Explanations of AWS resources that must be created
+ Automation options for building the testing infrastructure on AWS and deploying the infrastructure during the migration phase
+ Options for monitoring and troubleshooting connectivity for each use case

For more information about how MGN works, see these blog posts:
+ [Accelerate your Migration with AWS Transform MGN](https://aws.amazon.com/blogs/mt/accelerate-your-migration-with-aws-application-migration-service/)
+ [How to Use the New AWS Transform MGN for Lift-and-Shift Migrations](https://aws.amazon.com/blogs/aws/how-to-use-the-new-aws-application-migration-service-for-lift-and-shift-migrations/)
