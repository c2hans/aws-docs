---
source_url: https://docs.aws.amazon.com/solutions/building-geolocation-systems-for-the-betting-and-gaming-industry-on-aws/index.html
---

---
title: 'Guidance for Building Geolocation Systems for the Betting & Gaming Industry on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-geolocation-systems-for-the-betting-and-gaming-industry-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Building Geolocation Systems for the Betting & Gaming Industry on AWS

## Overview

This Guidance helps betting and gaming service providers build geolocation verification systems suitable for use by licensed betting and gaming operators. Geolocation verification systems are often legally required to ensure that players are located within proper gaming jurisdictions when they place bets. This Guidance is designed to help enterprises build their own geolocation service that comes with low cost per check, flexible integration options, and high availability. In addition, service providers can access high-quality geospatial data from trusted data providers to better serve their customers. This Guidance should not be construed as legal advice; enterprises that use this Guidance to build a geolocation service should consult their own counsel to determine whether the service built complies with applicable law. The Integrity SDK provides enhanced features related to device verification, and it is available for use by request. To get access to the SDK and the onboarding guide, contact [Sales Support](https://aws.amazon.com/contact-us/sales-support/) .

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-geolocation-systems-for-the-betting-and-gaming-industry-on-aws.pdf)

![Architecture diagram](/images/solutions/building-geolocation-systems-for-the-betting-and-gaming-industry-on-aws/images/building-geolocation-systems-for-the-betting-and-gaming-industry-on-aws-1.png)

1. **Step 1**: The provider's software development kit (SDK) calls the provider's authentication service to authenticate and/or register users.
1. **Step 2**: The provider's authentication service calls Amazon Cognito to retrieve temporary credentials, granting users the ability to update their location.
1. **Step 3**: The Integrity SDK, within Provider's betting and gaming app, performs device integrity checks and sends device location to the Amazon Location Service to determine device position.
1. **Step 4**: The provider's SDK sends location data to the compliance rules engine (CRE) built by the provider. The provider uses the CRE to determine if bets are allowed based upon location data and other evaluations.
1. **Step 5**: The CRE sends location data to Amazon Location, retrieves a list of geofences previously uploaded by the provider, and receives geospatial evaluation. If the CRE determines bets are allowed, it sends an expiring token back to the device.
1. **Step 6**: The CRE forwards device wager eligibility and location data to Amazon EventBridge. EventBridge forwards data to Amazon Simple Queue Service (Amazon SQS) for distribution to the betting operators. Data is sent through AWS Lambda to Amazon DynamoDB to support the provider portal and to Amazon CloudWatch for logging and monitoring.
1. **Step 7**: Upon a wager attempt, the provider's app checks for a valid token. If confirmed, it forwards the wager to the betting operator.
1. **Step 8**: The betting operator receives messages from the provider's Amazon SQS endpoint to determine compliance posture prior to allowing wagering.
1. **Step 9**: A secure provider portal using the provider's DynamoDB provides auditing information to the betting operator and regulator.
1. **Step 10**: The geofence boundary management is maintained by the Provider, who updates their Amazon Location geofence collection.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance facilitates the telemetry and traceability of player locations so that your betting & gaming operator customers can troubleshoot problems and regulators can confirm the proper operation of your system. Wager eligibility and location data are forwarded via EventBridge using Lambda to a DynamoDB table, to provide auditable information to your customers and regulators. CloudWatch stores the collected logs, metrics, and events from your applications and workload components so that authorized users can understand the system’s internal state and health and audit geolocation events. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All data are encrypted in transit in this Guidance, and data stored within Amazon Location are encrypted at rest by default. In addition, all user data stored in DynamoDB are fully encrypted at rest. DynamoDB encryption at rest provides enhanced security by encrypting all your data at rest using encryption keys stored in AWS Key Management Service (AWS KMS). In addition, the DynamoDB service should be restricted to be accessed only from the customer’s VPC using a VPC endpoint. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance anticipates demand spikes associated with seasonal sports wagering events in the betting and gaming industry. Instances scale automatically when you’re using Lambda, which quickly locates free capacity within its compute fleet every time an event notification is received for your function and runs your code up to the allocated concurrency. DynamoDB is designed for 99.99% availability for regional tables. You can also monitor historical data about any events or issues that might affect your AWS environment. For example, AWS CloudTrail provides a record of various user or service actions. You can use CloudWatch to collect and analyze metrics related to your Amazon Location account and set CloudWatch to notify you if a metric meets certain conditions. You can also use AWS Health Dashboard to verify the status of Amazon Location. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses serverless automatic scaling components to meet the spikes in demand associated with betting and gaming traffic. Serverless components, such as EventBridge and Lambda, scale up or down automatically to meet demand requirements, providing a more consistent user experience and low average latency. Additionally, the AWS global infrastructure is built around AWS Regions, each providing multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. You should select the Region closest to your betting and gaming customers for Amazon Location. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance relies solely on serverless components, with the exception of your application. As a result, you can minimize your IT maintenance costs because you won’t need to spin up instances and install applications on them. You will only be charged for the resources you use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses components that automatically scale, reducing the environmental impact of the infrastructure by avoiding provisioning unused capacity. EventBridge, Lambda, and Amazon SQS automatically scale to handle your workload, consuming only the minimum required resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Building geolocation verification for iGaming and sports betting on AWS**: This blog post demonstrates how to build a geolocation verification system for iGaming and sports betting applications using AWS services, ensuring compliance with regional regulations and enhancing user experience through accurate location-based access control.

[Learn more](https://aws.amazon.com/blogs/gametech/building-geolocation-verification-for-igaming-and-sports-betting-on-aws/)

- **ForecastGeofenceEvents**: This API Reference demonstrates how to evaluate device positions against geofence geometries from a given geofence collection.

[Learn more](/location/latest/APIReference/API_ForecastGeofenceEvents.html)

- **Verify device positions**: This developer guide demonstrates how to verify device positions using the Amazon Location APIs.

[Learn more](/location/latest/developerguide/verify-device-positions.html)

- **OpenBet**: OpenBet used this Guidance to build a flexible, transparent, cost-effective geolocation solution to help betting and gaming operators meet compliance requirements and detect fraudulent activity.

[Learn more](https://aws.amazon.com/solutions/case-studies/openbet-case-study/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
