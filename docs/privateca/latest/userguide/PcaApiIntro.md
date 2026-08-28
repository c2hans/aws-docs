---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/PcaApiIntro.html
---

# Use AWS Private CA with the AWS SDK for Java
<a name="PcaApiIntro"></a>

You can use the AWS Private Certificate Authority API to programmatically interact with the service by sending HTTP requests. The service returns HTTP responses. For more information see [AWS Private Certificate Authority API Reference](https://docs.aws.amazon.com/privateca/latest/APIReference/).

In addition to the HTTP API, you can use the AWS SDKs and command line tools to interact with AWS Private CA. This is recommended over the HTTP API. For more information, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/). The following topics show you how to use the [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/) to program the AWS Private CA API.

The [GetCertificateAuthorityCsr](JavaApi-GetCertificateAuthorityCsr.md), [GetCertificate](JavaApi-GetCertificate.md), and [DescribeCertificateAuthorityAuditReport](JavaApi-DescribeCertificateAuthorityAuditReport.md) operations support waiters. You can use waiters to control the progression of your code based on the presence or state of certain resources. For more information, see the following topics, as well as [Waiters in the AWS SDK for Java](https://aws.amazon.com/blogs/developer/waiters-in-the-aws-sdk-for-java/) in the [AWS Developer Blog](https://aws.amazon.com/blogs/developer/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
