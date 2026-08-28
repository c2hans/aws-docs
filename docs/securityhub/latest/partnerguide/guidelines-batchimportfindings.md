---
source_url: https://docs.aws.amazon.com/securityhub/latest/partnerguide/guidelines-batchimportfindings.html
---

# Guidelines for using the `BatchImportFindings` API
<a name="guidelines-batchimportfindings"></a>

When using the [`BatchImportFindings`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html) API operation to send findings to AWS Security Hub CSPM, use the following guidelines.
+ You must call [`BatchImportFindings`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html) using the account that is associated with the findings. The identifier of the associated account is the value of the `AwsAccountId` attribute for the finding.
+ Send the largest batch that you can. Security Hub CSPM accepts up to 100 findings per batch, up to 240 KB per finding, and up to 6 MB per batch.
+ The throttle rate limit is 10 TPS per account per Region, with a burst of 30 TPS.
+ You must implement a mechanism to retain the state of findings if throttling or network issues exist. You also need the finding state so that you can submit finding updates as a finding moves in and out of compliance.
+ For information about the maximum lengths of strings and other limitations, see [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) in the *AWS Security Hub User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
