---
source_url: https://docs.aws.amazon.com/solutions/integrating-amazon-connect-with-sap-sales-and-service-cloud-on-aws/index.html
---

# Guidance for Integrating Amazon Connect Customer Customer with SAP Sales and Service Cloud on AWS

## Overview

<p>This Guidance demonstrates the integration of Connect Customer with the SAP<a href="https://www.sap.com/products/crm/sales-cloud.html">Sales</a>and<a href="https://www.sap.com/products/crm/service-cloud.html">Service</a>Clouds using an AWS Cloud Development Kit (AWS CDK) template. This template provides for the deployment of a connector enabling seamless voice integration between the solutions. The integration reduces call handle time and provides agents with insights to deliver personalized service based on the online customer journey derived from Connect Customer. Additionally, the integration incorporates generative artificial intelligence (AI) capabilities to provide call analytics and call transcript summarization available directly in the customer or account timeline within SAP Sales & Service Clouds. The modular design of this Guidance also provides for additional Connect Customer features to be enabled with ease in the SAP Sales and Service Clouds environments as required.</p>

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/integrating-amazon-connect-with-sap-sales-and-service-cloud-on-aws.pdf)

![Architecture diagram](/images/solutions/integrating-amazon-connect-with-sap-sales-and-service-cloud-on-aws/images/integrating-amazon-connect-with-sap-sales-and-service-cloud-on-aws-1.png)

1. **Step 1a**: The SAP Sales and Service Cloud is a software-as-a-service (SaaS) hosted in a SAP managed AWS account.
1. **Step 1b**: The Connector/Contact Control Panel (CCP) files are stored in an Amazon Simple Storage Service (Amazon S3) bucket, making it available through Amazon CloudFront as a static site. An administrative user deploys the sample code accompanying this Guidance. The sample code can be used to integrate the CCP with the SAP Sales and Service Cloud through an iFrame integration within the browser.
1. **Step 1c**: An agent logs in to the SAP Sales and Service Cloud with their SAP credentials. The agent then logs in to the CCP using their Amazon Connect Customer agent credentials and sets themselves as available.
1. **Step 2**: An end-customer with an issue calls the help desk number.
1. **Step 3a**: Amazon Connect Customer routes the call to the available agent.
1. **Step 3b**: The custom CCP communicates with the SAP Sales and Service Cloud through browser events. The SAP Sales and Service Cloud processes the information it received through these browser events.
1. **Step 4**: When the call ends, Amazon Connect Customer sends a call summary to the respective Amazon S3 bucket.
1. **Step 5**: After the call, Amazon Connect Customer sends an event to Amazon EventBridge.
1. **Step 6**: EventBridge triggers an AWS Lambda function based on a rule match.
1. **Step 7**: Based on the event details, the Lambda function fetches the call summary from the Amazon S3 bucket.
1. **Step 8**: Using a REST API provided by Amazon API Gateway, the Lambda function sends the summary to the SAP Sales and Service, which then displays the call summary as part of the call record.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-integrating-amazon-connect-with-sap-sales-and-service-cloud-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
