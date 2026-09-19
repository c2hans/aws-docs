---
source_url: https://docs.aws.amazon.com/solutions/ai-enhanced-amazon-connect-customer-experience/index.html
---

---
title: 'Guidance for AI enhanced Amazon Connect Customer customer experience'
canonical_url: https://docs.aws.amazon.com/solutions/ai-enhanced-amazon-connect-customer-experience/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for AI enhanced Amazon Connect Customer customer experience

## Overview

This Guidance demonstrates how to harness Amazon Q in Connect to revolutionize your customer service operations through AI-powered automation and agent assistance. By implementing this solution, businesses can deliver 24/7 omnichannel support while significantly improving operational efficiency. The integration enables natural, conversational customer interactions through generative AI, seamless escalation to human agents when needed, and empowers service representatives with real-time AI assistance. This modern approach to customer service helps organizations reduce response times, increase first-contact resolution rates, and enhance overall customer satisfaction while optimizing operational costs and enabling support teams to focus on high-value interactions.

## Benefits

### Enhance customer self-service

Deploy intelligent, conversational support that resolves customer inquiries without agent intervention. Amazon Q in Connect leverages natural language understanding to provide contextual responses from your knowledge base, improving first-contact resolution rates.

### Streamline support escalation

Enable seamless transitions from AI-powered self-service to human agents when needed. Customers maintain context as they move between chat, voice, video, or screen sharing channels, creating a cohesive support experience that increases satisfaction.

### Optimize support resources

Automate routine inquiries while directing complex issues to human agents. This approach reduces wait times, allows agents to focus on high-value interactions, and captures complete interaction history for continuous improvement of both AI and human-assisted support.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/ai-enhanced-amazon-connect-customer-experience.pdf)

![Architecture diagram](/images/solutions/ai-enhanced-amazon-connect-customer-experience/images/ai-enhanced-amazon-connect-customer-experience-1.png)

1. **Step 1**: A customer navigates to a website hosted in Amazon Simple Storage Service (Amazon S3) and delivered globally through Amazon CloudFront.
1. **Step 2**: The customer initiates a support request using the Amazon Connect Customer communication widget embedded in the website.
1. **Step 3**: The communication widget initiates a chat session with Amazon Connect Customer. Amazon Q in Connect handles questions like FAQs, policies, and troubleshooting with natural language understanding to provide conversational, contextual responses rather than scripted answers.
1. **Step 4**: Amazon Q in Connect responds to customer inquiries using a knowledge base stored in Amazon S3.
1. **Step 5**: If the customer requires additional assistance, the conversation seamlessly escalates to a human agent via chat, voice call, video session, or screen share, ensuring complete issue resolution and customer satisfaction.
1. **Step 6**: Amazon Connect Customer helps resolve customer issues through either AI-powered self-service responses or human agent assistance, capturing the complete interaction history for continuous service improvement.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/small-medium-business/ai-enhanced-amazon-connect-customer-experience.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/Guidance-for-AI-enhanced-customer-experience-with-Amazon-Connect)

[Read usage guidelines](/solutions/guidance-disclaimers/)
