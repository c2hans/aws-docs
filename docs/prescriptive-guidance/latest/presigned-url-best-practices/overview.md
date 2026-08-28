---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/overview.html
---

# Overview of presigned URLs
<a name="overview"></a>

A presigned URL is a type of HTTP request that's recognized by the [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) service. What differentiates this type of request from all other AWS requests is the [X-Amz-Expires query parameter](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html). As with other authenticated requests, presigned URL requests include a signature. For presigned URL requests, this signature is transmitted in `X-Amz-Signature`. The signature uses Signature Version 4 cryptographic operations to encode all other request parameters.

**Notes**:
+ [Signature Version 2 is currently in the process of being deprecated](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingAWSSDK.html#UsingAWSSDK-sig2-deprecation), but it is still supported in some AWS Regions. This guide applies to Signature Version 4 signing.
+ The receiving service could process unsigned headers, but support for that option is limited and targeted, in line with best practices. Unless otherwise noted, assume that all headers must be signed for a request to be accepted.

The `X-Amz-Expires` parameter allows a signature to be processed as valid with a greater deviation from the encoded date time. Other aspects of signature validity are still evaluated. The signing credentials, if temporary, must not be expired at the time the signature is processed. The signing credentials must be attached to an IAM principal who has sufficient authorization at the time of processing.

**Presigned URLs are a subset of presigned requests**

A presigned URL is not the only method to sign a request for a future time. Amazon S3 also supports POST requests, which are commonly presigned as well. A presigned POST signature allows uploads that comply with a signed policy and has an expiration date that's embedded in that policy.

Signatures for requests can be future dated, although this is uncommon. As long as the underlying credentials are valid, the signature algorithm doesn't prohibit future dating. However, these requests can't be successfully processed until their valid timing window, which makes future dating impractical for most use cases.

**What does a presigned request allow?**

A presigned request can only allow actions that are allowed by the credentials that were used to sign the request. If the credentials implicitly or explicitly deny the action that's specified by the presigned request, the presigned request is denied when it's sent. This applies to the following:
+ Session policies that are associated with the credentials
+ Identity-based policies that are associated with the principal who is associated with the credentials
+ Resource policies that affect the session or principal
+ Service control policies that affect the session or principal
+ Resource control policies that affect the session or principal

## Motivations for using presigned requests
<a name="motivations"></a>

As a security engineer, you should be aware of what motivates solution builders to use presigned URLs. Understanding what is necessary and what is optional will help you communicate with solution builders. Motivations might include the following:
+ To support a non-IAM authentication mechanism while benefiting from scalability in Amazon S3. A core motivation is to communicate directly with Amazon S3 to benefit from the built-in scalability provided by this service. Without this direct communication, a solution would need to support the load from retransmitting bytes that are sent in **PutObject** and **GetObject** calls. Depending on total load, this requirement adds scaling challenges a solution builder might want to avoid.

  Other means of communicating directly with Amazon S3, such as using temporary credentials in AWS Security Token Service (AWS STS) or Signature Version 4 signatures outside URLs, might not be appropriate for your use case.  Amazon S3 identifies users through AWS credentials, whereas presigned requests presume identification through mechanisms other than AWS credentials. Bridging this difference while maintaining the direct communication for data is achievable through presigned requests.
+ To benefit from a browser's native understanding of URLs. URLs are understood by browsers, whereas AWS STS credentials and Signature Version 4 signatures are not. This is beneficial when integrating with browser-based solutions. Alternative solutions require more code, will use more memory for large files, and might be treated differently by extensions such as malware and virus scanners.

### Comparison with temporary AWS STS credentials
<a name="comparison-with-temporary-9999999999999999sts--credentials.1588ac49-9032-563d-9fb0-8c4e4cb699e6"></a>

Temporary credentials are similar to presigned requests. They both expire, allow scoping of access, and are commonly used to bridge non-IAM credentials to usage that requires AWS credentials.

You can tightly scope a temporary AWS STS credential to a single S3 object and action, but this can result in scaling challenges because AWS STS APIs have limits. (For more information, see the article [How can I resolve API throttling or "Rate exceeded" errors for IAM and AWS STS](https://repost.aws/knowledge-center/iam-sts-throttling-error) on the AWS re:Post website.) In addition, each generated credential requires an AWS STS API call, which adds latency and a new dependency that might affect resilience. A temporary AWS STS credential also has a minimum expiration time of 15 minutes, whereas a presigned request can support shorter durations. (60 seconds is practical given the right conditions.)

### Comparison with signature-only solutions
<a name="comparison-with-signature-only-solutions.ad9ad2ae-ad01-5696-9b90-4eb10c00a794"></a>

The only inherently secret component of a presigned request is its Signature Version 4 signature. If a client knows the other details of a request and is provided with a valid signature that matches those details, it can send a valid request. Without a valid signature, it cannot.

Presigned URLs and signature-only solutions are cryptographically similar. However, signature-only solutions have practical advantages such as the ability to use an HTTP header instead of a query string parameter to transmit the signature (see the [Logging interactions and mitigations](logging-interactions.md) section). Administrators should also consider that query strings are more commonly treated as metadata, whereas headers are less commonly streated as such.

On the other hand, AWS SDKs provide less support for generating and using signatures directly. Building a signature-only solution requires more custom code. From a practical perspective, using libraries instead of custom code for security is a general best practice, so the code for signature-only solutions requires extra scrutiny.

Signature-only solutions do not use the `X-Amz-Expires` query string and provide no explicit validity period. IAM manages the implicit validity periods of signatures that don't have an explicit expiration time. Those implicit periods aren't published. They don't typically change, but they are managed with security in mind, so you shouldn't take a dependency on the validity periods. There's a tradeoff between having explicit control over the expiration date and having IAM manage the expiration.

As an administrator, you might prefer a signature-only solution. However, in a practical sense, you'll need to support solutions as built.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
