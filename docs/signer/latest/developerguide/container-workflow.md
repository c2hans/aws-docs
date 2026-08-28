---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/container-workflow.html
---

# Sign container images in Signer
<a name="container-workflow"></a>

This section describes procedures for signing container images stored in an Open Container Initiative (OCI) compliant container registry. Before you begin, make sure you have completed the prerequisites listed in [Get started with AWS Signer](getting-started.md).

**Note**
If you're coming here from the Amazon ECR image signing documentation, be aware that you must fulfill all of the requirements related to Amazon ECR before beginning these AWS Signer procedures. For more information, see [Signing an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-signing.htm) in the *Amazon Elastic Container Registry User Guide*.

**Topics**
+ [Prerequisites for signing container images](image-signing-prerequisites.md)
+ [Sign an image](image-signing-steps.md)
+ [Locally verify an image after signing](image-verification.md)
+ [Verify an image during in Amazon EKS or Kubernetes clusters](kubernetes-verification.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
