---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/introduction.html
---

# Evaluate downgrading Oracle databases to Standard Edition 2 on AWS
<a name="introduction"></a>

*Lanre (Lan-Ray) showunmi and Bhavesh Rathod, Amazon Web Services*

This document provides guidance for reducing your Oracle licensing costs by downgrading from Oracle Database Enterprise Edition (EE) to Oracle Database Standard Edition 2 (SE2). By following this guide, you can perform an in-depth assessment of your Enterprise Edition Oracle databases. You can then determine which databases can be safely downgraded to Standard Edition 2 during migration to [Amazon Relational Database Service (Amazon RDS) for Oracle](https://aws.amazon.com/rds/oracle/). This guide also applies if you are already running Amazon RDS for Oracle Database EE and you want to downgrade to Oracle Database SE2.

## Overview
<a name="overview"></a>

Oracle Database EE is the default deployment option for production workloads in many organizations. This might be partly to the result of a common misconception that the Oracle Database SE2 is not capable of supporting enterprise-class applications. Both the Enterprise Edition and the Standard Edition 2 Oracle databases share a common code base, so technically they offer similar functionalities.

Oracle Database EE offers additional options, but it's significantly more expensive than Oracle Database SE2. Downgrading to Oracle Database SE2 gives you an opportunity to reduce the overall total cost of ownership of your databases. Applications with no or minimum usage of Enterprise Edition features are good candidates for downgrades to Oracle Database SE2.

This guide does not provide licensing advice. For specific licensing information, consult your own Oracle license agreements. You can engage specialized [AWS Oracle Competency Partners](https://aws.amazon.com/partners/competencies/oracle/?partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc&awsf.partner-solutions-filter-partner-type=*all&awsf.partner-solutions-filter-partner-location=*all) that have helped many AWS customers interpret Oracle licensing and proceed with their migration.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

By using this guide, you can derive the following business outcomes:
+ **Cost savings on Oracle database licensing fees** – Downgrading to Standard Edition 2 reduces the total cost of running your applications.
+ **Reduced need for significant upfront costs** – Amazon RDS for Oracle offers the License Included option so that you pay only for what you use.
+ **Efficient assessment** – You can perform a bulk assessment of your databases to determine suitability for a downgrade to Standard Edition 2.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
