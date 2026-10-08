---
source_url: https://docs.aws.amazon.com/solutions/identity-management-and-access-control-on-aws/index.html
---

---
title: 'Guidance for Identity Management & Access Control on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/identity-management-and-access-control-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Identity Management & Access Control on AWS

## Overview

The Guidance for the Identity Management & Access Control (IMAC) capability will help you build and monitor permissions in your environment. This Guidance will help you to structure your organization and organize your resources within defined isolated groups following the principal of least privilege (PoLP). This Guidance will help your team develop a framework to manage your environment and provide access to your services.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/identity-management-and-access-control-on-aws.pdf)

![Architecture diagram](/images/solutions/identity-management-and-access-control-on-aws/images/identity-management-and-access-control-on-aws-1.png)

1. **Step 1**: (CF2 - S2) On your management account, create an AWS IAM Identity Center instance and set up your organization.
1. **Step 2**: (CF2 - S1) Create the initial set of recommended accounts to configure your foundation. Follow the recommendations included in the Production Starter Organization.
1. **Step 3**: (CF2 - S2) Connect to your external IdP, or create the Users and Groups within AWS IAM Identity Center to organize access across your environment. Create permission sets for access to your management account and assign them to the management account users
1. **Step 4**: (CF2 - S6) Delegate AWS IAM Identity Center to your Shared Services account, log in with the AWS IAM Identity Center role, create permission sets, and assign them to the groups and users for the member accounts in your AWS organization.
1. **Step 5**: (CF2 - S5) Using your AWS IAM Identity Center role to administer the management account, create Preventive Controls using Service Control Policies in the management account, and delegate the security, network, and operation services to their corresponding AWS accounts in your environment.
[Read usage guidelines](/solutions/guidance-disclaimers/)
