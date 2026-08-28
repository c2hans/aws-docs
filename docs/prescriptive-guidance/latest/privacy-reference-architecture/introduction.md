---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/introduction.html
---

# AWS Privacy Reference Architecture
<a name="introduction"></a>

*Amber Welch, Amazon Web Services*

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

## Notices
<a name="notices"></a>

This guide is provided for the purposes of information only. It isn't legal advice and shouldn't be relied on as legal advice. AWS encourages its customers to obtain appropriate advice on their implementation of privacy and data protection environments, and more generally, applicable laws relevant to their business.

Customers are responsible for making their own independent assessment of the information in this document. This document: (a) is for informational purposes only, (b) represents current AWS product offerings and practices, which are subject to change without notice, and (c) doesn't create any commitments or assurances from AWS and its affiliates, suppliers, or licensors. AWS products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied.

The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document isn't part of, nor does it modify, any agreement between AWS and its customers.

## Introduction
<a name="pra-introduction"></a>

The AWS Privacy Reference Architecture (AWS PRA) provides a set of guidelines specific to the design and configuration of privacy-supporting controls in AWS services. This guide can help you make decisions about people, process, and technology that help support privacy in the AWS Cloud.

### The AWS shared responsibility model and privacy
<a name="the-9999999999999999aws--shared-responsibility-model-and-privacy.53a714cc-c198-5472-bd6f-9f35ddc717aa"></a>

In the AWS Cloud, you share responsibility for security and compliance with AWS. AWS is responsible for security *of* the cloud, which means that AWS is responsible protecting the infrastructure that runs all of the services offered in the AWS Cloud. You are responsible for security *in* the cloud, which means that you are responsible for configuring and managing AWS services in accordance with security and privacy requirements. For more information, see the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

AWS services provide capabilities that allow you to implement your own privacy controls in the cloud in order to support your privacy requirements. Your privacy responsibility varies based on many factors, including the AWS services and AWS Regions you choose, the integration of those services into your IT environment, and the laws and regulations applicable to your organization and workload.

When using AWS services, you maintain control over your content. Specifically, *customer content* is defined as software (including machine images), data, text, audio, video, or images that you or any end user transfer to us for processing, storage, or hosting by AWS services in connection with your account. It also includes any computational results that you or an end user derive by using AWS services. You are responsible for managing the following decisions, which are under your control:
+ The data you choose to collect, store, or process on AWS
+ The AWS services you use with the data
+ The AWS Region where you collect, store, or process data
+ The format and structure of your data and whether it's masked, anonymized, or encrypted
+ How you define, store, rotate, and operate your cryptographic keys for encryption
+ Who has access and when they have access to your data, and how those access rights are granted, managed, and revoked

Once you understand the AWS shared responsibility model and how it generally applies to operating in the cloud, you must determine how it applies to your use case. The AWS services that you choose to use determine the amount of configuration you must perform as part of your organization's privacy responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) is categorized as infrastructure as a service (IaaS). As such, if you use Amazon EC2, you must perform all of the necessary privacy configurations for guest operating systems and for the application software or utilities you install on your EC2 instances. When you use an abstracted service, such as Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB, AWS is responsible for the infrastructure layer, the operating system, and platforms. Your responsibility is to manage and classify the data (customer content) and to configure the policies used to access the endpoints in order to store and retrieve data. For more information about how AWS helps you protect data and privacy, see [Data protection and privacy at AWS](https://aws.amazon.com/compliance/data-protection/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
