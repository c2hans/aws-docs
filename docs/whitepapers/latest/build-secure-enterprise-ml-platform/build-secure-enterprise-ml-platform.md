---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Build a Secure Enterprise Machine Learning Platform on AWS
<a name="build-secure-enterprise-ml-platform"></a>

Publication date: **May 11, 2021**

## Abstract
<a name="abstract"></a>

This whitepaper helps cloud engineers, security engineers, Machine Learning Ops (MLOps) engineers, and data scientists understand the various components of building a secure enterprise machine learning (ML) platform. It provides prescriptive guidance on building a secure ML platform on Amazon Web Services (AWS).

## Introduction
<a name="introduction"></a>

Building an enterprise ML platform for regulated industries such as financial services can be a complex architectural, operational, and governance challenge. There are many architecture design considerations, including AWS account design, networking architecture, security, automation pipelines, data management, and model serving architecture in an ML platform implementation. In addition, organizations need to think about operational considerations such as the monitoring of pipelines, model training, and production model hosting environment, as well as establishing incident response processes for the ML platform operation. Lastly, having strong governance controls such as guardrails, model management, auditability, and data and model lineage tracking are essential to meet the stringent regulatory and compliance requirements faced by regulated customers.

AWS provides a wide range of services for building highly flexible, secure, and scalable ML platforms for the most demanding use cases and requirements. This paper provides architecture patterns, code samples, and best practices for building an enterprise ML platform on AWS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
