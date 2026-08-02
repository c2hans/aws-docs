---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/introduction.html
---

# Best practices for using the AWS CDK in TypeScript to create IaC projects
<a name="introduction"></a>

*Sandeep Gawande, Mason Cahill, Sandip Gangapadhyay, Siamak Heshmati, and RAJNEESH TYAGI, Amazon Web Services*

This guide provides recommendations and best practices for using the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) in TypeScript to build and deploy large-scale infrastructure as code (IaC) projects. The AWS CDK is a framework for defining cloud infrastructure in code and provisioning that infrastructure through AWS CloudFormation. If you don't have a well-defined project structure, building and managing an AWS CDK codebase for large-scale projects can be challenging. To deal with these challenges, some organizations use anti-patterns for large-scale projects, but these patterns can slow down your project and create other issues that negatively impact your organization. For example, anti-patterns can complicate and slow down developer onboarding, bug fixes, and the adoption of new features.

This guide provides an alternative to using anti-patterns and shows you how to organize your code for scalability, testing, and alignment with security best practices. You can use this guide to improve code quality for your IaC projects and maximize your business agility. This guide is intended for architects, technical leads, infrastructure engineers, and any other role seeking to build a well-architected AWS CDK project for large-scale projects.

## Objectives
<a name="objectives"></a>

This guide can help you achieve the following targeted business outcomes:
+ **Reduced costs** – You can use the AWS Cloud Development Kit (AWS CDK) to design your own reusable components that meet your organization's security, compliance, and governance requirements. You can also easily share components around your organization, so that you can rapidly bootstrap new projects that align with best practices by default.
+ **Faster time to market** – Take advantage of familiar features in the AWS CDK to accelerate your development process. This increases reusability for deployment and reduces development efforts.
+ **Increased developer productivity **– Developers can use familiar programming languages to define infrastructure. This helps developers express and maintain AWS resources. This can lead to increased developer efficiency and collaboration.

## Attachments
<a name="attachments-b7d5d887-7172-4d47-9f1f-1cf7ae181482"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
