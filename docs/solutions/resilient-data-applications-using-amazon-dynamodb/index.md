---
source_url: https://docs.aws.amazon.com/solutions/resilient-data-applications-using-amazon-dynamodb/index.html
---

---
title: 'Guidance for Resilient Data Applications Using Amazon DynamoDB'
canonical_url: https://docs.aws.amazon.com/solutions/resilient-data-applications-using-amazon-dynamodb/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Resilient Data Applications Using Amazon DynamoDB

Improve application resiliency to guard against disruptions and outages

## Overview

This Guidance demonstrates how to architect a resilient, multi-Region application using AWS services, such as Amazon DynamoDB global tables. It illustrates best practices for detecting and responding to Region-scoped outages, providing high availability and minimizing downtime for mission-critical applications. This Guidance helps you achieve application resiliency by dynamically routing traffic away from affected Regions and leveraging global data replication.

## How it works

### Primary

This architecture diagram shows how to set up and build a resilient, multi-Region application. For cross-Region failover and failback, open the other tab.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/resilient-data-applications-using-amazon-dynamodb.pdf)Step 1Check canaries, component-level metrics, regional endpoint metrics, synthetic metrics, and AWS Health API to identify any Region-scoped AWS service incidents (assuming they are operating in a healthy state).Step 2The user's application performs a DNS lookup through Amazon Route 53. Based on the latency-based routing policy, Route 53 returns the Amazon API Gateway endpoint from the Region with the lowest latency. In this case, the Region is us-west-2.Step 3The user's application sends a request to the provided API Gateway endpoint in us-west-2, such as creating a new order. API Gateway receives the request and passes it to the configured AWS Lambda function in the us-west-2 Region.Step 4A Lambda function processes the request from API Gateway and performs the necessary actions. In this case, it writes the new product order to the local Amazon DynamoDB table in us-west-2.Step 5DynamoDB writes the data to the local table in us-west-2 and acknowledges the write success to the Lambda function. The Lambda function returns a response to the user's application through API Gateway, confirming the successful write.Step 6The DynamoDB global table asynchronously replicates the data from the us-west-2 table to the corresponding table in us-east-1.### Cross-Region Failover and Failback

This architecture diagram shows how to perform cross-Region failover and failback in the event of an outage. For setup of the primary Region, open the other tab.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/resilient-data-applications-using-amazon-dynamodb.pdf)Step 1A Region-scoped outage starts in us-west-2, causing intermittent failures and elevated response times for your application in that Region.Step 2Data sources such as canaries, component-level metrics, regional endpoint metrics, synthetic metrics, and AWS Health API help detect issues from the Region-scoped AWS service events and subsequently alert you.Step 3After concluding that there is an outage in the us-west-2 Region, evacuate us-west-2 until the event is resolved. Change the Route 53 Application Recovery Controller (ARC) to disable traffic routing to us-west-2. Consider cutting off traffic at the API Gateway level if you're concerned about the time it takes for DNS changes to propagate.Step 4All traffic will now be routed to the us-east-1 Region. The application should be able to handle the increased traffic, provided service quotas have been adjusted previously. Monitor the us-east-1 Region closely, ensuring the application is functioning properly and handling the increased load.Step 5Once the event in us-west-2 is resolved, start restoring service to that Region. Remove any API Gateway restrictions, change Route 53 ARC routing control to allow traffic to us-west-2 again, and gradually restore traffic using Route 53 weighted routing policies.Step 6Continue monitoring the us-west-2 Region to confirm the application is performing at the expected level of service.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/building-resilient-apps-amazon-dynamodb-global-tables)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch monitors the application's health through metrics from DynamoDB, Lambda, API Gateway, and Route 53. During incidents, metrics help assess user impact for evacuation decisions. CloudWatch Synthetics canaries simulate customer interactions, verifying user experience even without traffic. Canaries complement component metrics by revealing customer-facing issues. CloudWatch dashboards provide a unified view of performance for operations staff. Route 53 ARC checks application readiness. Post-failover, dashboards monitor the failover Region. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

API Gateway HTTPS endpoints encrypt all communications. AWS Identity and Access Management (IAM) implements the principle of least privilege, granting only the necessary permissions for services to function. DynamoDB encrypts data at rest and in transit, while CloudWatch logs are also encrypted, safeguarding your sensitive information. Adopting these security-focused AWS services mitigates the risk of data breaches and strengthens the overall security posture of your application. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

DynamoDB global tables replicate your data across multiple AWS Regions. Automated failover with Route 53 routing and Route 53 ARC helps your application seamlessly continue operating in the event of a disruption. Lambda provides a scalable application layer, decoupling your services from provisioned compute resources. Real-time monitoring with CloudWatch and CloudWatch Synthetics canaries provide the information your team needs to make informed decisions during critical events. These AWS services help you build a robust and highly available application that can withstand unexpected failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Fully managed, serverless AWS services automatically scale to match your workload. DynamoDB, Lambda, API Gateway, and Route 53 dynamically allocate resources so your application can handle traffic surges and fluctuations without compromising the user experience. CloudWatch monitors your application's metrics, enabling you to identify and address performance bottlenecks. Route 53 automatically distributes traffic to the lowest latency Regions, improving responsiveness for your users. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS services automatically scale resources to match your application's needs. Lambda and DynamoDB only charge for the compute and storage resources you consume, eliminating the need for overprovisioning. API Gateway and Lambda work in tandem to launch your application logic only when valid API requests are received, so you pay only for the resources you use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless architecture diagram optimizes resource allocation, reducing the need for provisioned hardware and enabling efficient energy usage. API Gateway and Lambda launch only for valid requests, minimizing compute consumption. DynamoDB allocates storage as needed, preventing waste. Resources scale up during traffic spikes and failovers, then scale down when demand decreases. This automated, precise matching of supply to demand maximizes energy efficiency and reduces energy consumption. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Build resilient applications with Amazon DynamoDB global tables: Part 4**

[Build resilient applications with Amazon DynamoDB global tables: Part 4](https://aws.amazon.com/blogs/database/part-4-build-resilient-applications-with-amazon-dynamodb-global-tables/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
