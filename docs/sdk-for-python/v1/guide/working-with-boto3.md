---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/working-with-boto3.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Working with Boto3
<a name="working-with-boto3"></a>

If you have existing Boto3 code and want to evaluate the AWS SDK for Python, these pages help you get started:
+ [Key differences](working-with-boto3-differences.md) — API-model and execution differences between the two SDKs.
+ [Use both SDKs in one application](working-with-boto3-coexistence.md) — Architectural patterns for running both SDKs together, including configuration, sync/async boundaries, and common pitfalls.
+ [Convert Boto3 operations to the AWS SDK for Python](working-with-boto3-migration.md) — Rewrite individual Boto3 calls using the generated types and async model of the new SDK.
+ [Choosing the right AWS SDK for Python](choosing-sdk.md) — Decision guide for determining the best path for your workload.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
