---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/introduction.html
---

# Establishing guardrails and monitoring for presigned URLs

*Antonio Aga Rossi and Ed Gummett, Amazon Web Services*

Security is a critical concern for all companies and a key pillar in the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html). As a security engineer, you can implement administrative guardrails that align with organizational control requirements. In the AWS Well-Architected Framework, [guardrails](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/definitions.html#id-adc431e7-de7a-4b38-c6ec-4b3aee17d8c7) define the boundaries that limit activity.

This guide provides background information and best practices for using presigned URLs with [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) objects. Presigned URLs allow users or applications that have valid credentials to generate requests that are signed in advance and remain valid until a defined expiration time. A common use case for presigned URLs is to extend access to objects or resources by sharing these requests. Systems or users that have the rights to perform a specific request generate shared presigned requests. They can then send these requests to other systems or users to extend the ability to perform that same request.

In this guide, you will learn:
+ The concepts of presigned URLs
+ Use cases for presigned URLs
+ Recommended and optional guardrails
+ Monitoring options
+ Examples of how AWS services use presigned URLs

## Best practices
<a name="best-practices"></a>

The following sections of this guide discuss best practices that you should consider as a security engineer. The guidelines include:
+ [Foundational best practices](foundational-best-practices.md), which are practices that every organization should follow.
+ [Additional guardrails](additional-guardrails.md), which are practices that you should consider, but might decide to implement partially or with exceptions. These practices provide additional control and defense in depth, but you should balance them against overall complexity.
+ [Logging interactions](logging-interactions.md), which might result from devices or services that fall under your responsibility or your customer's responsibility in the AWS shared responsibility model. This section includes precautions to limit the information that logs make accessible.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for architects and security engineers who are responsible for implementing security controls in the AWS Cloud.

## Objectives
<a name="objectives"></a>

As a security engineer, you want to be aware of how solution builders implement security and the type of access your end users have. This guide covers one type of access, presigned URLs, which are often used with [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Presigned URLs give builders a way to bridge authentication mechanisms.

In Amazon S3, presigned URLs are a distinct category of requests. You can monitor and manage these requests to help ensure that they are used only where your use case requires them. This guide helps you provide this type of high-level oversight.

After reading this guide, you will understand what a presigned URL is, when builders typically use it, and why.

## Prerequisites
<a name="prerequisites"></a>

If your company has not defined a security policy, control objectives, or standards, as described in the guide [Implementing security controls on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/sec-controls-gov-model.html), complete those governance tasks before you proceed with this guide.

Before you begin, also review the recommended and optional best practices for control and monitoring. For more information, see:
+ [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (AWS Organizations documentation)
+ [Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) (AWS Organizations documentation)
+ [Bucket policies for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) (Amazon S3 documentation)
+ [Logging requests with server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) (Amazon S3 documentation)
+ [Logging Amazon S3 API calls using AWS CloudTrail](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging.html) (Amazon S3 documentation)
