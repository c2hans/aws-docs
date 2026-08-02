---
source_url: https://docs.aws.amazon.com/solutions/cell-based-architecture-on-aws/index.html
---

# Guidance for Cell-Based Architecture on AWS

## Overview

This Guidance helps customers understand the concepts of implementing a cell-based architecture. This architecture shows fault isolation between cells, which are independent replicas of the system. Customers can use this Guidance to prevent outages caused by a software bug, failed deployment, or overload, ultimately reducing the impact to end-customers.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/cell-based-architecture-on-aws.pdf)

![Architecture diagram](/images/solutions/cell-based-architecture-on-aws/images/cell-based-architecture-on-aws-1.png)

1. **Step 1**: Clients connect to the routing layer. The routing layer redirects the client to the assigned cell using an HTTP redirect.
1. **Step 2**: Routing information (user to cell mapping) is stored in Amazon DynamoDB. There is a fixed number of independent clusters that store copies of the data. For new users, the cell router pushes the new user information to all clusters.
1. **Step 3**: The architecture is divided into a large number of independent cells of fixed size. The cells contain all application logic and storage.
1. **Step 4**: Each cell has monitoring and alerting capabilities using Amazon CloudWatch.
1. **Step 5**: There is also a central dashboard which contains aggregated information (such as number of cells with and without errors).
1. **Step 6**: Cell creation and update is automated using AWS Step Functions, AWS CodePipeline, AWS CodeDeploy, and AWS CloudFormation. Updates are first deployed to a canary cell. Disaster recovery for cells is fully automated.
1. **Step 7**: Changes are streamed from all cells to a central data lake, where they can be queried using SQL in Amazon Athena.
1. **Step 8**: A rebalancer can move users between cells, and also create new cells as needed. After a successful move, it updates the user-to-cell assignment. The old cell retains a marker to redirect clients to the new cell (not pictured in the diagram).
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-cell-based-architecture-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

By isolating faults to business service partitions, this Guidance promotes operational excellence by ensuring that the business can continue to run services. This aligns fault isolation with individual users or sets of users. In contrast to the more traditional approach, which has users in the same failure domain of a single business system, this new approach has users in different failure domains. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Any use of cryptography is kept at a minimum with the intention of it being replaced for production use. Randomly generated API keys and JSON Web tokens are used for authentication. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance implements the Well-architected best practice of a cellular architecture. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Cost Optimization

To ensure cost optimization, only the smallest AWS Fargate container instance types are used. Deployment and workflows run on Step Functions to minimize compute cost. Monitoring uses synthetic canaries that are started only when needed. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
