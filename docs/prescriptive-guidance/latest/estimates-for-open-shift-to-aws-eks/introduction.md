---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/introduction.html
---

# Effort estimation framework for migrating OpenShift to Amazon EKS
<a name="introduction"></a>

*Pratap Kumar Nanda and Pradip kumar Pandey, Amazon Web Services*

## Overview
<a name="overview"></a>

Many organizations underestimate the effort required for container platform migrations. Based on observed patterns, teams often need more time and resources than initially planned, which can lead to budget overruns and extended timelines.

This guide provides a structured approach to building accurate effort estimates when migrating from Red Hat OpenShift to Amazon Elastic Kubernetes Service (EKS). We address common complexity areas that impact migration timelines, including:
+ Operator dependencies and custom resource definitions
+ Security policy translation and implementation
+ Container image registry migration
+ Network architecture and connectivity requirements

### Service availability
<a name="service-availability"></a>

Some AWS services aren't available in all AWS Regions. For Region availability, see [AWS services by Region. ](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
