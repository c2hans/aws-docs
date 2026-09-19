---
source_url: https://docs.aws.amazon.com/solutions/security-incident-response-on-aws/index.html
---

---
title: 'Guidance for Security Incident Response on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/security-incident-response-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Security Incident Response on AWS

Reduce threats by responding effectively to security vulnerabilities

## Overview

This Guidance helps you to effectively respond to a security incident based on decisions that are specified in your incident response plan. The response involves characterizing the nature of the incident and making changes, which may involve activities including restoration of operational status, identification and remediation of root cause, and gathering evidence pursuant to civil or criminal prosecution.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/security-incident-response-on-aws.pdf)

![Architecture diagram](/images/solutions/security-incident-response-on-aws/images/security-incident-response-on-aws-1.png)

1. **Step 1**: Establish an incident response team and incident response plan.
1. **Step 2**: Deploy an AWS Config configuration recorder and delivery channel to all operating Regions in all member accounts. Review service control policies (SCPs) for examples of deny list policy strategies. Configure the delivery channel to send to the AWS Config Amazon Simple Storage Service (Amazon S3) bucket in the Log Archive account.
1. **Step 3**: Enable AWS Security Hub for your organization using the AWS Security Hub and AWS Organizations user guide to centralize security findings for a single account. Configure cross-Region aggregation to centralize Regional security findings to one Region.
1. **Step 4**: Delegate the administration of AWS Security Hub to the Security Tooling Account to allow the security team to manage the Security Hub and any findings outside of the management account.
1. **Step 5**: Respond to the incident based on the incident response plan. This can include recovery of systems, remediating findings, or isolating affected systems. The Automated Security Response on AWS solution creates predefined response and remediation actions based on industry compliance standards.
1. **Step 6**: Send security event logs to a centralized Amazon S3 bucket in the Log Archive account for retention as required.
## Related content

- **read the whitepaper**

[read the whitepaper](/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
