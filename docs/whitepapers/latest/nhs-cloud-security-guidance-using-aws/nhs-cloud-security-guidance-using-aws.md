---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/nhs-cloud-security-guidance-using-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Using AWS in the Context of NHS Cloud Security Guidance
<a name="nhs-cloud-security-guidance-using-aws"></a>

Publication date: **September 29, 2021** ([Document history](document-revisions.md))

 Guidance was issued in early 2018 on the use of hyperscale cloud services by UK public sector healthcare organisations and their business partners. The documents comprising the guidance include detailed risk management activities for such organisations to undertake, comprising mostly technical measures appropriate to the level of security required. This whitepaper provides advice corresponding specifically to the measures described, to accelerate organisational alignment with the guidance.

## Introduction
<a name="introduction"></a>

 The explicit guidance on the secure use of hyperscale cloud services was published in January 2018 by four key UK Public Sector Health bodies: NHS Digital, the Department of Health and Social Care, NHS England, and NHS Improvement. That guidance built on the foundation of the [National Cyber-Security Centre’s 14 Cloud Security Principles](https://www.ncsc.gov.uk/guidance/implementing-cloud-security-principles), and adopts the NCSC’s philosophy of devolving risk management to Information Asset Owners, taking a risk-based approach to managing information security in the cloud.

 The guidance also draws a clear delineation between the security of the cloud infrastructure and services delivered from it, and the workloads deployed to that infrastructure. The expectations on organisations using the guidance are that they:
+  Quantify the information security risks involved for their workloads.
+  Satisfy themselves that the cloud provider they use implements the required controls to manage those risks.
+  Adopt the appropriate customer-usable controls for that purpose.

 This whitepaper explains how to achieve the latter when using Amazon Web Services (AWS) for cloud infrastructure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
