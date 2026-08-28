---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-containerize-javaee/introduction.html
---

# Containerizing traditional Java EE applications for the AWS Cloud
<a name="introduction"></a>

*Mayuki Yamabe and Michal Urbaniak, Amazon Web Services*

## Overview
<a name="overview.340397dd-93f2-56a1-8749-f0fff14c4fb3"></a>

Although Java Enterprise Edition (EE) is the dominant framework for enterprise applications, it can be challenging to migrate your Java EE applications to the Amazon Web Services (AWS) Cloud without refactoring your application's business logic and data models. This guide helps you overcome that challenge by using a containerization strategy for migrating your Java EE application to the AWS Cloud, while preserving the application's server-side business logic and data model. The strategy is based on refactoring your application into microservices and then running the application on a modernized container platform.

The "heart" of an application is the business logic and data model, which are tightly coupled with longstanding business rules and requirements. This tight coupling makes applications more difficult to refactor. In this guide, we recommend a strategy to preserve the server-side business logic and data model as much as possible, while modernizing your application's underlying technologies by using Docker containers and container orchestration platforms, such as Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS).

The following diagram shows a design pattern for refactoring a traditional Java EE application into a containerized application.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-containerize-javaee/images/guide-img/34f6e23c-ad3a-4f13-8f30-05bf7b07cc57/images/aa0a279a-95ee-4008-950f-0a1b2007d43b.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
