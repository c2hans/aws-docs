---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/introduction.html
---

# Choosing an infrastructure as code tool for your organization
<a name="introduction"></a>

*Siamak Heshmati, Mason Cahill, Sandip Gangapadhyay, Sandeep Gawande, and RAJNEESH TYAGI, Amazon Web Services*

*Infrastructure as code (IaC)* is the process of provisioning and managing an application's infrastructure through a set of configuration files. IaC is designed to help you centralize infrastructure management, standardize resources, and scale quickly so that new environments are repeatable, reliable, and consistent. It's a key component of Agile and DevOps practices, such as version control, continuous integration, and continuous deployment.

Choosing an infrastructure as code (IaC) tool is considered a strategic decision for an organization. This decision affects all of the teams that build infrastructure, applications, and services for the company. Each tool has pros and cons; therefore, there is no one-size-fits-all model.

In the past, managing and provisioning infrastructure was a manual process fraught with errors. IaC streamlines these tasks through code and has become a reliable solution for deploying infrastructure. IaC tools empower developers to define and deploy infrastructure by using programming languages. This not only enhances business agility but also accelerates growth and the speed of innovation. In addition, IaC significantly improves security because IaC allows your organization to scan the code before deployment, verifying that the infrastructure is reliable and secure. Ultimately, the right IaC tool is not just a technical decision but a strategic one that directly impacts the overall success of the business.

This guide explores five different IaC tools that can be used to provision AWS resources: AWS CloudFormation, AWS Serverless Application Model (AWS SAM), AWS Cloud Development Kit (AWS CDK), HashiCorp Terraform, and Pulumi. It compares these tools and guides you through the process of choosing one that meets the needs of your team, organization, and cloud talent. The key is to align the chosen IaC tool with your organization goals and the skillsets of your developers. For example, if your team is proficient in JavaScript, you might choose AWS CDK with TypeScript as your primary IaC tool because it optimizes your development workflow.
