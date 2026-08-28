---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Introduction
<a name="introduction"></a>

The workflows, applications, and methods used for the design and verification of semiconductors, integrated circuits (ICs), and printed circuit boards (PCBs) have been largely unchanged since the invention of computer-aided engineering (CAE) and electronic design automation (EDA) software. The computing requirements, however, have dramatically increased as device geometries have shrunk and electronics systems and integrated circuits have become more complex. CAE, EDA, and emerging workloads such as computational lithography and metrology have driven the need for massive-scale computing and data management in next-generation connected products.

IT and EDA support organizations face the challenge of providing the infrastructure required to run workflows in a way that meets schedule and budget requirements. They must invest in increasingly large server farms and high-performance storage systems to enable high quality, fast turnaround of workflows. A lot of overall design time is spent verifying components. Workflows like the characterization of intellectual property (IP) cores, functional verification, and timing analysis have a spiky demand and limit engineering productivity. This creates a need to have enough compute capacity to minimize the time that engineers wait for results, but can result in underutilization of resources between runs of the workflows. New and upgraded IC fabrication technologies have increased peak compute and storage requirements, challenging organizations to find ways to meet the needs of silicon development teams while managing costs.

Semiconductor companies today use AWS to deploy infrastructure on an as-needed basis with pay-as-you-go pricing. The massive scale of AWS enables them to run CAE and EDA workflows as quickly as possible with no upfront capital expenditures or long term commitments. They benefit from a more rapid, flexible deployment of CAE and EDA infrastructure to run the complete IC design flow, from register-transfer-level (RTL) design to the delivery of GDSII files to a foundry for chip fabrication. AWS gives them access to the latest compute, storage, network technologies, and higher-level services that enable them to meet the ever-increasing demands of semiconductor design workloads so they can innovate faster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
