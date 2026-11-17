---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/introduction.html
---

# Autonomous Driving Data Framework (ADDF) security and operations guide
<a name="introduction"></a>

*Andreas Falkenberg, Srinivas Reddy Cheruku, Torsten Reitemeyer, and Junjie Tang, Amazon Web Services*

Autonomous Driving Data Framework (ADDF) is an open-source project designed to provide reusable, modular code artifacts for automotive teams who want to implement common tasks for advanced driver-assistance systems (ADAS), such as configuring centralized data storage, data processing pipelines, visualization mechanisms, search interfaces, simulation workloads, analytics interfaces, and prebuilt dashboards. You find the full ADDF codebase on Github under awslabs in the repository autonomous-driving-data-framework. Using ADDF, you can share, modify, or create fully customizable modules that reduce the amount of effort required to create and deploy these solutions.

This guide helps you understand best practices for securely deploying and operating ADDF in the AWS Cloud. It covers the following topics:
+ [ADDF architecture and terminology](addf-architecture-terminology.md) – Review the general architecture, workflows, and important terms.
+ [Shared responsibility model](shared-responsibility-model.md) – Understand your role and the role of AWS in securing your ADDF deployment and cloud resources.
+ [ADDF security review process](addf-security-review-process.md) – Because ADDF is an open-source project, review how AWS and contributors complete security reviews.
+ [Built-in security features](built-in-security-features.md) – Review how security best practices and features are built into the ADDF open-source project and its deployment framework.
+ [Secure setup and operation](secure-setup-and-operation.md) – Learn how to deploy and operate ADDF in the AWS Cloud.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for DevOps teams, infrastructure engineers, administrators, IT security staff, and incident response teams who assess, deploy, customize, and operate the Autonomous Driving Data Framework (ADDF). You can apply the recommendations in this guide to proof-of-concept or production environments.

This guide assumes you have no prior knowledge of ADDF.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This guide helps you set up and operate the Autonomous Driving Data Framework (ADDF) in development and production environments, and follow security best practices.
