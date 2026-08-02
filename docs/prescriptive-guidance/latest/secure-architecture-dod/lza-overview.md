---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-architecture-dod/lza-overview.html
---

# Overview of the Landing Zone Accelerator
<a name="lza-overview"></a>

In order to build a landing zone in AWS that conforms to the ﻿Defense Information Systems Agency (DISA) Secure Cloud Computing Architecture ﻿(SCCA), you must have certain elements in place to help you meet the minimum requirements. AWS has created the [Landing Zone Accelerator (LZA)](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html) to help you deploy a landing zone that conforms to the necessary requirements. Using the LZA solution, you can deploy the environment by using a set of configuration files. These configuration files help you focus on the delivery of an environment instead of learning each individual AWS service and how to deploy it.

The following image shows services involved in the LZA deployment. The numbers indicate the workflow, from modification of the configuration files to configuration of AWS services in the workload accounts.

![Architecture diagram of AWS services used to deploy the Landing Zone Accelerator on AWS (LZA).](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-architecture-dod/images/guide-img/9ef8ed3c-685a-4e51-9cc4-4701568d9bae/images/df55b61a-552b-4e2c-b7fd-f785927c229b.png)

This solution is architected to align with AWS best practices and conform to multiple global compliance frameworks. When used in coordination with services such as [AWS Control Tower](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html), this solution provides a comprehensive, low-code solution across more than 35 AWS services and features. Specifically, this solution helps you manage and govern a multi-account environment that is built to support highly-regulated workloads and complex compliance requirements. LZA helps you establish platform readiness with security, compliance, and operational capabilities. This guide includes specific notes regarding use of this solution to support alignment with [﻿United States (US) Federal and Department of Defense (DoD) guidance﻿](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/united-states-us-federal-and-department-of-defense-dod.html).

AWS provides the LZA solution as an open source project that was built by using the [AWS Cloud Development Kit (AWS CDK)﻿﻿](https://docs.aws.amazon.com/cdk/v2/guide/home.html). You can install it directly into your environment, giving you full access to the infrastructure as code (IaC) solution.

Through a simplified set of configuration files, you can:
+ Configure additional functionality, guardrails, and security services, such as [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) managed rules and [AWS Security Hub CSPM﻿](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html).
+ Manage your foundational networking topology through services such as [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html), [AWS Transit Gateway﻿](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), and [AWS Network Firewall﻿](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html).
+ Generate additional workload accounts by using the [AWS Control Tower Account Factory﻿](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html).

There are no additional charges or upfront commitments required to use Landing Zone Accelerator on AWS. You pay only for the AWS services that you turn on to set up your platform and operate your guardrails. This solution can also support non-standard AWS partitions, including the AWS GovCloud (US), AWS Secret, and AWS Top Secret Regions.

|
|
| Important: The LZA solution does not, by itself, make you compliant. It provides the foundational infrastructure from which you can integrate additional complementary solutions. The information contained in the [LZA implementation guide](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html) is not exhaustive. You must review, evaluate, assess, and approve the solution in compliance with your organization's particular security features, tools, and configurations. It is the sole responsibility of you and your organization to determine which regulatory requirements are applicable and to ensure that you comply with all requirements. Although this solution discusses both the technical and administrative requirements, this solution does not help you comply with the non-technical administrative requirements. |
| --- |

## Planning your LZA deployment on AWS
<a name="planning"></a>

AWS has created a detailed [﻿implementation guide﻿](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html) for deploying the Landing Zone Accelerator (LZA) solution on AWS. For an architecture diagram and an overview of the deployment steps, see [Architecture diagram](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/architecture-diagram.html) in the *Landing Zone Accelerator on AWS Implementation Guide*. Your environment must meet [﻿prerequisites﻿](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/prerequisites.html) before deploying the solution. Using the requirements in the SCCA components and requirements chapter in this guide, you can choose between the deployment options that are described in the [LZA implementation guide](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html).
