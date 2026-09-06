---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/ecr.html
---

# Amazon Elastic Container Registry
<a name="ecr"></a>

[Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that's secure, scalable, and reliable.

Amazon ECR stores images in Amazon S3 buckets that Amazon ECR manages. Each Amazon ECR repository has an encryption configuration, which is set when the repository is created. By default, Amazon ECR uses server-side encryption with Amazon S3-managed (SSE-S3) encryption keys. For more information, see [Encryption at rest](https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html) (Amazon ECR documentation).

Consider the following encryption best practices for this service:
+ Instead of using the default server-side encryption with Amazon S3-managed (SSE-S3) encryption keys, use customer managed KMS keys stored in AWS KMS. This key type provides the most granular control options.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/ecr.html)
+ Do not revoke the grants that Amazon ECR creates by default when you provision a repository. This can affect functionality, such as accessing data, encrypting new images pushed to the repository, or decrypting them when they are pulled.
+ Use AWS CloudTrail to record the requests that Amazon ECR sends to AWS KMS. The log entries contain an encryption context key to make them more easily identifiable.
+ Configure Amazon ECR policies to control access from specific Amazon VPC endpoints or specific VPCs. Effectively, this isolates network access to a specific Amazon ECR resource, allowing access from only the specific VPC. By establishing a virtual private network (VPN) connection with an Amazon VPC endpoint, you can encrypt data in transit.
+ Amazon ECR supports resource-based policies. Using these policies, you can restrict access based on the source IP address or the specific AWS service.
