---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/appendix-b.html
---

# Appendix B: How controls for presigned URLs affect AWS services
<a name="appendix-b"></a>

This appendix describes interactions between the AWS services that use presigned URLs, as described in [Appendix A](appendix-a.md), and the controls described earlier in this guide.

## Guardrail for s3:signatureAge
<a name="guardrail-for-s3-signature-age"></a>

The Amazon S3 console isn't disrupted by the maximum expiration of 5 minutes that's set by the `s3:signatureAge` condition key. The Amazon S3 console generates presigned URLs when you choose the **Download** button and applies its own 5-minute expiration time. A maximum duration that's shorter than 2 minutes might create random failures based on clock synchronization and latencies.

Amazon S3 Object Lambda uses an expiration time of 61 seconds, so setting conditions on an `s3:signatureAge` value of 61 seconds or more won't cause any disruption. Shorter durations might be less reliable and might cause intermittent failures.

Amazon S3 cross-Region **CopyObject** isn't disrupted by a maximum expiration of 5 minutes. However, shorter durations might create random failures based on clock synchronization and latencies.

In AWS Lambda, **GetFunction** provides a URL to objects outside the customer account, so customer policies don't affect the generated URLs.

Amazon Redshift Spectrum has been tested with an `s3:signatureAge` condition of 16 minutes. However, shorter durations might cause disruption.

## Guardrail for s3:authType when not using network restrictions
<a name="guardrail-for-s3-auth-type-when-not-using-network-restrictions"></a>

The Amazon S3 console is usually affected by the `s3:authType` guardrail. The console routes to Amazon S3 based on the local network configuration. If the local network routes to Amazon S3 in a way that the network restriction allows, the Amazon S3 console would still work. However, if it's routed through a proxy or the public internet in a way that isn't allowed, usage would be blocked. However, blocking usage is probably the intent of this policy.

Amazon S3 Object Lambda is affected if the Lambda function isn't connected to an appropriate VPC. In this configuration, the VPC must have a NAT gateway, not to access the S3 bucket, but to call **WriteGetObjectResponse**.

Amazon S3 cross-Region **CopyObject** is disrupted if this guardrail is applied to a bucket policy without the recommended exception for when `aws:viaAWSService` is **true**.

Amazon Redshift Spectrum is affected by the `s3:authType` guardrail unless enhanced VPC routing is used. Currently, [Redshift Spectrum supports enhanced VPC routing only with serverless clusters, not with provisioned clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/spectrum-enhanced-vpc.html).
