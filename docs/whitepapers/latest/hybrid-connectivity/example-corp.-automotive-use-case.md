---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/example-corp.-automotive-use-case.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Example Corp. Automotive use case
<a name="example-corp.-automotive-use-case"></a>

 This section of the whitepaper demonstrates how the considerations, requirement definition questions, and decision trees are used to help you decide on the optimal hybrid network design. Identifying and capturing requirements is important since they are used as input to the decision trees. Capturing requirements upfront avoids further design iterations. Halting a project altogether if the design must be revisited and having valuable resources on hold can be minimized and ideally avoided when requirements are understood upfront.

 Example Corp. Automotive will be used throughout this section as the illustrative customer. They are looking to initially deploy their first analytics project on AWS. The analytics project is focused on analyzing data from cars manufactured by the company and other datasets that already exist in the company’s data centers. Initially, the company’s architecture group thinks they will need an AWS account, an Amazon VPC, and few subnets to host production and development environments. The project team is eager to get started, and they requested development environment access as soon as possible. They aim to go in production three months from now.

 Example Corp. Automotive also plans to use AWS for several additional projects, such as migrating their ERP systems, Virtual Desktop Infrastructure (VDI), and another 20 applications from on-premises to AWS over the next 6 months. Some requirements for additional projects are still being defined, but it’s clear that their AWS Cloud usage is going to grow.

 The architecture team decided to leverage the approach outlined in this whitepaper. They used the requirement definition questions outlined under each consideration to capture the inputs to make their design decisions.

 They start with requirements related to the connectivity type which are summarized in the following table.

*Table 4 – Example Automotive Corp reliability inputs*

- ** **Time to Deploy ****
  - **Requirement definition questions:**  What is the required timeline for the deployment? Hours, days, weeks, or months?
  - **Answers:**  +  **Dev/Test:** 1 month <br />+  **Production:** 3 months

- ** **Security** **
  - **Requirement definition questions:**  Do your security requirements and policies allow the usage of encrypted connections over the internet to connect to AWS or mandate the usage of private network connections?  / **Answers:**  +  **Dev/Test:** Site-to-Site VPN acceptable <br />+  **Production:** Private network required
  - **Requirement definition questions:**  When leveraging private network connections, does the network layer have to provide encryption in transit?  / **Answers:**  No, application layer encryption will be used.

- ** **SLA** **
  - **Requirement definition questions:**  Is hybrid connectivity SLA with service credits required?  / **Answers:**  +  **Dev/Test:** No <br />+  **Production:** Yes
  - **Requirement definition questions:**  What is the uptime target?  / **Answers:**  +  **Dev/Test:** N/A <br />+  **Production:** 99.99%
  - **Requirement definition questions:**  Does the entire hybrid network adhere to the uptime target?  / **Answers:**  +  **Dev/Test:** N/A <br />+  **Production:** Yes

- ** **Performance** **
  - **Requirement definition questions:**  What is the required throughput?  / **Answers:**  +  **Dev/Test:** 100 Mbps <br />+  **Production:** 500 Mbps growing to 2 Gbps
  - **Requirement definition questions:**  What is the maximum acceptable latency between AWS and on-premises network?  / **Answers:**  +  **Dev/Test:** No hard requirements <br />+  **Production:** Less than 30 ms
  - **Requirement definition questions:**  What is the maximum acceptable network jitter?  / **Answers:**  +  **Dev/Test:** No hard requirements <br />+  **Production:** Minimum jitter required

- ** **Cost** **
  - **Requirement definition questions:**  How much data would you send to AWS per month?  / **Answers:**  +  **Dev/Test:** 2 TB <br />+  **Production:** 20 TB growing to 50 TB
  - **Requirement definition questions:**  How much data would you send from AWS per month?  / **Answers:**  +  **Dev/Test:** 1 TB <br />+  **Production:** 10 TB growing to 25 TB
  - **Requirement definition questions:**  Is this connectivity permanent?  / **Answers:**  Yes

 Based on requirements received, the architecture team followed the connectivity type decision tree from Figure 9. It allowed the architecture team to decide on the connectivity type for the development and test and production environments. For the production environment, they considered the immediate as well as the upcoming requirements. For development and test Example Corp. Automotive will establish a site-to-site VPN over the internet. For production, they are going to work with a service provider to connect their corporate network with AWS Direct Connect. Example Corp. Automotive initially considered using a Direct Connect Hosted Connection, however due to the requirements for an [AWS provided SLA](https://aws.amazon.com/directconnect/sla/) they selected Direct Connect Dedicated Connections.

 After deciding on the connectivity type, the next step is to capture the requirements which impacts the connectivity design selection. This is related with the logical design, such how the connections are configured and which AWS services to use to support business and technical requirements.

 To capture the scalability and communication model requirements, the architecture team used the requirement definition questions from the associated sections of this whitepaper. The requirements related to those two considerations are summarized in the following table.

*Table 5 – Requirement definition questions*

- ** **Scalability** **
  - **Requirement definition questions:**  What is the current or anticipated number of VPCs which require connectivity to on-premises sites?  / **Answers:**  2 initially, growing to 30 in 6 months
  - **Requirement definition questions:**  Are these VPCs deployed in a single AWS Region or multiple Regions?  / **Answers:**  Single Region
  - **Requirement definition questions:**  How many on-premises sites need to be connected to AWS?  / **Answers:**  2 data centers
  - **Requirement definition questions:**  How many customer gateway devices do you have, per site, that need to connect to AWS?  / **Answers:**  2 routers per data center
  - **Requirement definition questions:**  How many routes are expected to be advertised to AWS VPCs as well as the number of expected routes to be received from AWS side?  / **Answers:**  +  **Routes to be advertised to AWS**: 20 routes <br />+  **Routes to be received from AWS**: 1 `/16` route
  - **Requirement definition questions:**  Is there any plan to consider bandwidth increase of the connection to AWS in the near future?  / **Answers:**  +   **Dev/Test**: 100 Mbps <br />+  **Production**: 500Mbps growing to 2Gbps.

- ** **Connectivity design models** **
  - **Requirement definition questions:**  Is there a requirement for inter-VPC communication to be enabled (within a Region and/or across Regions)?  / **Answers:**  Yes, within an AWS Region
  - **Requirement definition questions:**  Is there a requirement to access AWS public endpoints services directly from on-premises?  / **Answers:**  Yes
  - **Requirement definition questions:**  Is there a requirement to access AWS services using VPC endpoints from on premises?  / **Answers:**  No

 Based on inputs, the architecture team followed the decision tree from the Connectivity Design section. After anticipating that the number of VPCs is going to grow from 2 to 30 in the next 6 months, the architecture team decided to use AWS Transit Gateway as the termination gateway for the connection and for inter-VPC routing. Independent AWS Transit Gateways will terminate the VPN connection used for development and testing, and for the production connectivity with AWS Direct Connect. The usage of separated AWS Transit Gateways makes change management simpler and provides a clear demarcation between dev/test and production environments. For the production, AWS Direct Connect gateway is required because of AWS Transit Gateway. A public VIF will be used for access to AWS public endpoint services. Figure 14 illustrates the path taken on the decision tree based on requirements collected.

![Diagram showing Example Corp. Automotive connection design decision tree](http://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/example-connection-design-decision-tree.png)

 After deciding on the solution to meet the scalability and communication model requirements, the next step is to capture the requirements associated with reliability. This is related to the required level of availability and resilience.

 To capture the reliability requirements, the architecture team used the requirement definition questions from the associated section of this whitepaper. The requirements are summarized in the following table.

*Table 6 – Reliability requirement questions*

- ** Reliability **
  - **Requirement definition questions:**  What is the impact magnitude on the business in case of a connectivity failure to AWS?  / **Answers:**  +  **Dev/Test**: Low <br />+  **Production**: High
  - **Requirement definition questions:**  From a business point of view, does the cost of following a connectivity failure to AWS outweigh the cost of deploying a highly reliable connectivity model to AWS?  / **Answers:**  +  **Dev/Test**: No <br />+  **Production**: Yes

 Based on inputs received, the architecture team followed the decision tree from the reliability considerations sections covered previously on this whitepaper. After considering the uptime target of 99.99% for the production connectivity and the high business impact if there was a service interruption, the architecture team decided to use 2 Direct Connect locations and have 2 links from each on-premises data center to each Direct Connect location (4 links in total). The VPN connectivity used for development and testing will also use two VPN connections for additional redundancy. Using route engineering techniques discussed in the reliability section, connectivity will be configured as follows:
+  For development and testing, traffic is going to be load balanced using ECMP over the 2 tunnels going to the primary data center. This allows for higher throughput. The tunnels going to the secondary data center are going to be used in case of failure of the primary tunnels.
+  For production, the latency between on-premises and AWS over either of the Direct Connect locations is very similar. In this case, it has been decided to load balance the traffic between AWS and on-premises over the two connections going to the primary data center for the on-premises systems deployed in the primary data center. Similarly, for on-premises systems running in the secondary data center, traffic is going to be load balanced between the two connections to the secondary data center. In case of failure of the connections, BGP will facilitate an automated failover.

 Figure 15 illustrates the path taken on the decision tree based on requirements collected.

![Diagram showing Example Corp. Automotive reliability decision tree](http://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/example-reliability-decision-tree.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
