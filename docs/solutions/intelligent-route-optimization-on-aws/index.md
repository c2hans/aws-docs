---
source_url: https://docs.aws.amazon.com/solutions/intelligent-route-optimization-on-aws/index.html
---

---
title: 'Guidance for Intelligent Route Optimization on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/intelligent-route-optimization-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Intelligent Route Optimization on AWS

Reduce fuel costs and improve logistics operations with a route optimization tool

## Overview

This Guidance provides a fleet planning tool for route optimization and tracking, helping you optimize orders, reduce costs, and improve your fleet and delivery operations. It is a cloud-based solution that combines historical data, such as traffic, routes, and customer data, with location services, such as route planning, near real-time tracking, geocoding, and analytics. It helps you better manage the distinct categories of deliveries (discrete, non-discrete, and instant deliveries), with a flexible tool to handle multiple vehicle types (such as trucks, scooters, and bikes). A web-based dispatcher interface for planning and monitoring, with a mobile driver application for navigation and proof of delivery, is also implemented with this Guidance.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/intelligent-route-optimization-on-aws.pdf)

![Architecture diagram](/images/solutions/intelligent-route-optimization-on-aws/images/intelligent-route-optimization-on-aws-1.png)

1. **Step 1**: Users access the application through a web-based UI that uses AWS Amplify libraries to connect to AWS.
1. **Step 2**: Amplify allows the application to display interactive maps, autocomplete addresses, and place markers by connecting with Amazon Location Service.
1. **Step 3**: The application connects to the AWS Cloud through AWS AppSync, which acts as a central hub to interact with other AWS resources.
1. **Step 4**: Itineraries are stored in Amazon DynamoDB, where the application can query and update them with single-digit millisecond performance.
1. **Step 5**: Itineraries are optimized using Amazon Location Route Matrix API. This API returns a matrix with the distance between each pair of points of the itinerary. The matrix is then used to optimize the route based on the shortest distance between each pair of waypoints.
1. **Step 6**: Once an itinerary starts, an asset outfitted with an Internet of Things (IoT) sensor sends position updates to AWS IoT Core using the message queuing telemetry transport (MQTT) protocol.
1. **Step 7**: AWS IoT Core routes the messages to a Location Service Tracker, which stores the position updates for up to 30 days.
1. **Step 8**: Users of the application can track the assets on the map in near real-time. This is achieved by polling the updates from the Amazon Location tracker through an AWS Lambda custom AWS AppSync resolver.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-intelligent-route-optimization-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance can be deployed using the Amplify command line interface (CLI). This means that all infrastructure components are expressed as infrastructure as code (IaC) so you can easily deploy changes and adapt this to enhance your operational excellence. Additionally, all of the Lambda functions in this Guidance are instrumented to emit JSON structured logs through the usage of AWS Lambda Powertools for TypeScript. This allows operators to aggregate and query logs, as well as extract metrics and set alarms. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The backend of this Guidance has two entry points: an AWS AppSync API and an AWS IoT Core endpoint. The first leverages an Amazon Cognito user Pools where you can create groups that users belong to. The AWS IoT Core endpoint instead uses X.509 client certificates that are issued and managed by AWS IoT Core. Finally, the frontend application also uses Cognito, both for storing users (user pool), and for obtaining temporary credentials (identity pool). [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses AWS managed services for all of its public endpoints (AWS AppSync and AWS IoT Core), which allows the Guidance to be highly available. You can also deploy the frontend with both AWS Amplify Hosting or Amazon Simple Storage Service (Amazon S3) coupled with Amazon CloudFront, both of which will make it globally distributed and highly available. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS IoT Core, AWS AppSync, Lambda, and Amazon Location are purpose-built services for this Guidance that enhance your performance efficiency. AWS IoT Core is a managed service that accepts connections from IoT devices, using industry standards for authentication (TLS) and connection protocols (MQTT). AWS AppSync was chosen as a managed service that allows you to expose APIs to web and mobile applications and allows you to request only the right amount of data (using GraphQL). Lambda was chosen because of its serverless and managed nature, that allows it to scale up and down based on traffic. Finally, Amazon Location was chosen as a secure and cost-effective mean to access location-based data from multiple vetted providers. This Guidance can be deployed in any of the AWS commercial Regions where these services are supported. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses pay-as-you-go billing for all services, and scales to continually match your demand with only the minimum resources required. You can also opt into Compute Saving Plans to materialize cost savings on Lambda, which is used extensively throughout this Guidance. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses event-driven processing that relies on ephemeral compute environments (Lambda) and managed services for the entry points (AWS AppSync and AWS IoT Core), allowing this Guidance to be elastic and scale in function of the load. Managed services shift responsibility for maintaining high-average utilization, and sustainability optimization of the deployed hardware from you to AWS. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
