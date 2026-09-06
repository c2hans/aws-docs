---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/introduction.html
---

# Rehosting your applications in a multi-account architecture on AWS by using VPC interface endpoints
<a name="introduction"></a>

*Dipin Jain and Saurabh Shankar, Amazon Web Services*

Many organizations rehost (lift and shift) their applications to AWS from isolated or semi-isolated network environments, including on-premises data centers and other cloud or hybrid infrastructures, by using [AWS Transform MGN](https://aws.amazon.com/application-migration-service/). These isolated networks typically do not allow any egress traffic to the public endpoints that are described in the [network requirements for MGN](https://docs.aws.amazon.com/mgn/latest/ug/Network-Requirements.html#Communication-TCP-1500). You can address this limitation by using virtual private cloud (VPC) interface endpoints, as discussed in the AWS Prescriptive Guidance pattern [Connect to MGN data and control planes over a private network](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/connect-to-application-migration-service-data-and-control-planes-over-a-private-network.html).

Many organizations also use a multi-account landing zone (MALZ) architecture for isolation, security, and per-account billing benefits. To enable lift-and-shift migration by using MGN over a secured network to multiple target AWS accounts, you must create VPC interface endpoints in every target AWS account. This adds to the cost and complexity of managing those resources.

This guide discusses options for centralizing VPC interface endpoints for rehosting your applications in a multi-account architecture on AWS. These options simplify the architecture and reduce costs for such use cases.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This guide provides solutions for three rehosting use cases. It focuses on reducing costs and operational overhead, and improving security and resource utilization.

Use cases:
+ Your applications are mapped to different business units, and you want to migrate them to different AWS target accounts in the same AWS Region to simplify billing and isolation.

  The [solution to this scenario](solution-1.md) involves creating VPC endpoints in a central AWS networking account and using AWS Transit Gateway to connect to target application accounts.
+ You want to migrate your applications to different AWS target accounts in multiple AWS Regions to keep your applications close to your users or to facilitate disaster recovery. This is an extension of the first use case.

  The [solution to this scenario](solution-2.md) involves creating VPC endpoints for each AWS Region in an AWS central networking account, and enabling cross-account access by using a peered transit gateway and Amazon Route 53.
+ Your applications are mapped to different business units, and you want to migrate them to different AWS target accounts in the same AWS Region for billing and isolation purposes. You also want to use fewer VPCs for MGN staging, and you want to centrally manage routing for the staging VPCs to reduce costs and administrative overhead.

  The [solution to this scenario](solution-3.md) involves sharing VPC endpoints by using a shared staging area subnet, with AWS Organizations and AWS Resource Access Manager (AWS RAM).

## Intended audience
<a name="intended-audience"></a>

This guide is for migration consultants, application architects, infrastructure architects, and application owners who are looking for solutions for these use cases.
