---
source_url: https://docs.aws.amazon.com/solutions/log-storage-on-aws/index.html
---

---
title: 'Guidance for Log Storage on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/log-storage-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Log Storage on AWS

## Overview

The Log Storage capability enables you to collect and store your environment logs centrally and securely in tamper resistant storage. This will enable you to evaluate, monitor, alert, and audit access and actions performed on your cloud resources and objects.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/log-storage-on-aws.pdf)

![Architecture diagram](/images/solutions/log-storage-on-aws/images/log-storage-on-aws-1.png)

1. **Step 1**: In your log archive account, create an Amazon Simple Storage Service (Amazon S3) logging bucket for your AWS CloudTrail instance.
1. **Step 2**: Configure the bucket policy to allow CloudTrail to write objects. Configure the ownership of the objects delivered to the bucket to be transferred to the log archive account.
1. **Step 3**: In the log archive account, in the same Region you created your bucket, create an AWS Key Management Service (AWS KMS) key. Use it to encrypt the bucket at rest.
1. **Step 4**: Sign back in to your management account, and deploy an organizational AWS CloudTrail instance to all your accounts in your organization. Use the AWS KMS key to encrypt the trail, and use the bucket in the log archive account as the recipient of the events recorded by the trail.
1. **Step 5**: Deploy service control policies across the organization and to the log archive account to protect the logs stored in the bucket and the trail in your organization, so it does not stop recording or get deleted.
[Read usage guidelines](/solutions/guidance-disclaimers/)
