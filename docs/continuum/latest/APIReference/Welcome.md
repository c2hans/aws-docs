---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

AWS Continuum finds, validates, prioritizes, and remediates code vulnerabilities across the source repositories and AWS resources in your environments. Continuum ingests security findings, confirms which ones are genuinely exploitable, ranks them by risk, and produces patches you can review and apply.

An *environment* is the unit of analysis in AWS Continuum. It brings together the code sources you select from your integrations, an operating policy that governs scanning and patch creation, and the state of the work Continuum performs. An *integration* connects an environment to an external source provider, such as GitHub or Amazon S3. A *collector* registers AWS Config in your account and forwards infrastructure state to the environments it is associated with.

As Continuum processes an environment, it records *scans*, *findings*, and *issues*. A scan builds the selected source and analyzes it. A finding is a single reported vulnerability, which Continuum validates for exploitability. A confirmed finding is promoted into an issue, a remediation work item that carries severity, validation evidence, and the patches Continuum produces to resolve it.

This API reference describes the operations and data types for AWS Continuum.

For more information, see the [AWS Continuum User Guide](https://docs.aws.amazon.com/continuum/latest/userguide/what-is-continuum.html). For information about service quotas, see [Quotas](https://docs.aws.amazon.com/continuum/latest/userguide/quotas.html).

This document was last published on October 29, 2026.
