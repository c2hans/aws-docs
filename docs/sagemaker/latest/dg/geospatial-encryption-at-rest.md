---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-encryption-at-rest.html
---

# SageMaker geospatial capabilities
<a name="geospatial-encryption-at-rest"></a>

You can protect your data at rest using encryption for SageMaker geospatial.
<a name="geospatial-encryption-at-rest-gmk"></a>
**Server-Side Encryption with Amazon SageMaker geospatial owned key (Default)**
Amazon SageMaker geospatial capabilities encrypts all your data, including computational results from your `EarthObservationJobs` and `VectorEnrichmentJobs` along with all your service metadata. There is no data that is stored within Amazon SageMaker AI unencrypted. It uses a default AWS owned key to encrypt all your data.
<a name="geospatial-encryption-at-rest-ksm"></a>
**Server-Side Encryption with KMS Keys Stored in AWS Key Management Service (SSE-KMS)**
Amazon SageMaker geospatial capabilities supports encryption using a customer-owned KMS key. For more information, see [Use AWS KMS Permissions for Amazon SageMaker geospatial capabilities](https://docs.aws.amazon.com/sagemaker/latest/dg/geospatial-kms.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
