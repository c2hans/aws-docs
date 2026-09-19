---
source_url: https://docs.aws.amazon.com/solutions/configuring-virtual-care-on-salesforce-using-amazon-chime/index.html
---

---
title: 'Guidance for Configuring Virtual Care on Salesforce Using Amazon Chime'
canonical_url: https://docs.aws.amazon.com/solutions/configuring-virtual-care-on-salesforce-using-amazon-chime/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Configuring Virtual Care on Salesforce Using Amazon Chime

## Overview

The Guidance shows how to implement Salesforce Virtual Care, which integrates Amazon Chime with Salesforce Health Cloud to facilitate accessible video and audio support for patient-clinician interactions. Virtual Care sessions use automatic speech recognition to generate real-time audio transcriptions, displayed as running captions directly on the interface. By using this Guidance, you can scale digital engagement, offer improved care-team efficiency, remove barriers to healthcare, and provide a more connected, equitable experience.

## Benefits

### Enhance patient experience

Deliver seamless telehealth services through integrated video conferencing and near real-time transcription capabilities. Improve healthcare access while maintaining HIPAA compliance through encrypted communications and secure credential management.

### Streamline clinical workflows

Reduce administrative burden by automating appointment management and clinical documentation through seamless Salesforce Health Cloud integration. Ensure operational reliability with comprehensive event monitoring and robust failure handling through Amazon EventBridge and Amazon SQS.

### Accelerate healthcare transformation

Implement a turnkey telehealth solution that integrates with existing Salesforce Health Cloud deployments for a complete patient view. Scale digital engagement while reducing costs through managed AWS services that eliminate infrastructure management overhead.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/configuring-virtual-care-on-salesforce-using-amazon-chime.pdf)

![Architecture diagram](/images/solutions/configuring-virtual-care-on-salesforce-using-amazon-chime/images/configuring-virtual-care-on-salesforce-using-amazon-chime-1.png)

1. **Step 1**: A patient requests an appointment through their healthcare provider's self-service application.
1. **Step 2**: Events from Amazon Chime SDK move over the default event bus from the Amazon Chime SDK control plane to Amazon EventBridge.
1. **Step 3**: An EventBridge rule that filters aws.chime events and a predefined input transformer rule modify the event and create a platform event in Health Cloud.
1. **Step 4**: During an active appointment session through a Salesforce-connected app, Amazon Chime SDK communicates to the Amazon Chime media services endpoint to receive transcription requests.
1. **Step 5**: Amazon Transcribe or Amazon Transcribe Medical receives and processes the transcription requests.
1. **Step 6**: For event delivery-failure handling: An Amazon Simple Queue Service (Amazon SQS) queue serves as a dead-letter queue (DLQ). AWS Key Management Service (AWS KMS) encrypts all messages stored in the Amazon SQS DLQ. An Amazon CloudWatch alarm monitors the Amazon SQS DLQ depth and invokes an alert when the configured threshold is exceeded. An Amazon Simple Notification Service (Amazon SNS) topic sends email notifications to interested parties when the CloudWatch alarm is invoked.
1. **Step 7**: AWS Secrets Manager securely stores Salesforce credentials and connection secrets.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-simplifying-virtual-appointments-using-salesforce-health-cloud-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
