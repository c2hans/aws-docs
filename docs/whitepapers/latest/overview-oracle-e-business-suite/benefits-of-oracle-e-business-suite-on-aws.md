---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/benefits-of-oracle-e-business-suite-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Benefits of Oracle E-Business Suite on AWS
<a name="benefits-of-oracle-e-business-suite-on-aws"></a>

 The following sections discuss some of the key benefits of running Oracle E-Business Suite on AWS.

## Agility and speed
<a name="agility-and-speed"></a>

 Traditional deployment involves a long procurement process in which each stage is time-intensive and requires large capital outlay and multiple approvals. With AWS, you can provision new infrastructure and Oracle E-Business Suite environments in minutes, compared to waiting weeks or months to procure and deploy traditional infrastructure.

## Lower total cost of ownership
<a name="lower-total-cost-of-ownership"></a>

 In an on-premises environment, you typically pay hardware support costs, virtualization licensing and support, data center costs, and so on. You can eliminate or reduce all of these costs by moving to AWS. You benefit from the economies of scale and efficiencies provided by AWS, and pay only for the compute, storage, and other resources you use.

## Cost savings for non-production environments
<a name="cost-savings-for-non-production-environments"></a>

 You can shut down your non-production environments when you are not using them and save costs. For example, if you are using a development environment for only 40 hours a week (eight hours a day, five days a week), you can shut down the environment when it’s not in use. You pay only for 40 hours of Amazon EC2 compute charges instead of 168 hours (24 hours a day, seven days a week) for an on-premises environment running all the time; this can result in a saving of 75% for EC2 compute charges.

## Replace capital expenditure (CapEx) with operating expenditure (OpEx)
<a name="replace-capital-expenditure-capex-with-operating-expenditure-opex"></a>

 You can start an Oracle E-Business Suite implementation or project on AWS without any upfront cost or commitment for compute, storage, or network infrastructure.

## Unlimited environments
<a name="unlimited-environments"></a>

 In an on-premises environment, you usually have a limited set of environments to work with; provisioning additional environments takes a long time or might not be possible at all. You do not face these restrictions when using AWS; you can create virtually any number of new environments in minutes as required.

 You can have a different environment for each major project so that each team can work independently with the resources they need without interfering with other teams; the teams can then converge at a common integration environment when they are ready. You can shut down these environments when the project finishes and stop paying for them.

## Have Moore’s Law work for you instead of against you
<a name="have-moores-law-work-for-you-instead-of-against-you"></a>

 [Moore's Law](https://en.wikipedia.org/wiki/Moore's_law) refers to the observation that the number of transistors on a microchip doubles every two years. In an on-premises environment, you end up owning hardware that depreciates in value every year. You are locked into the price and capacity of the hardware after it is acquired, plus you have ongoing hardware support costs. With AWS, you can switch your underlying instances to the faster, more powerful next-generation AWS instance types as they become available.

## Right-size anytime
<a name="right-size-anytime"></a>

Customers often over-size environments for initial phases, and are then unable to cope with growth in later phases. With AWS, you can scale the usage up or down at any time. You pay only for the computing capacity you use, for the duration you use it. Instance sizes can be changed in minutes through the AWS Management Console or the AWS Application Programming Interface (API) or Command Line Interface (CLI). Assess the resource usage on current system and launch with appropriate size instances for the enterprise resource planning (ERP) environment to reduce the cost overhead.

## Low-cost Disaster Recovery
<a name="low-cost-disaster-recovery"></a>

 You can build extremely low-cost standby Disaster Recovery (DR) environments for your existing deployments and incur costs only for the duration of the outage. [AWS Application Migration Service](https://aws.amazon.com/application-migration-service/) brings significant savings on DR total cost of ownership (TCO) compared to traditional DR solutions.

## Ability to test application performance
<a name="ability-to-test-application-performance"></a>

Although performance testing is recommended prior to any major change to an Oracle E-Business Suite environment, most customers only performance test their Oracle E-Business Suite application during the initial launch in the yet-to-be-deployed production hardware. Later releases are usually never performance tested due to the expense and lack of environment required for performance testing.

With AWS, you can minimize the risk of discovering performance issues later in production. An AWS Cloud environment can be created easily and quickly just for the duration of the performance test and only used when needed. Again, you are charged only for the hours the environment is used.

## No end of life for hardware or platform
<a name="no-end-of-life-for-hardware-or-platform"></a>

All hardware platforms have end-of-life dates, at which point the hardware is no longer supported and you are forced to buy new hardware again. In the AWS Cloud, you can simply upgrade the platform instances to new AWS instance types in a single click at no cost for the upgrade.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
