---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-test-execution-role.html
---

# Test run fails with an access denied error
<a name="next-gen-troubleshoot-test-execution-role"></a>

**Symptom:** A test run fails with an `AccessDenied` error from AWS FIS or one of the targeted services.

The following table lists possible causes and solutions.

| Cause | Solution |
| --- | --- |
| Execution role trust policy doesn't allow AWS FIS | Verify the role trusts fis.amazonaws.com and that the aws:SourceAccount and aws:SourceArn conditions match your account. For the trust policy, see [IAM execution roles for resilience testing](next-gen-resilience-testing-iam.md). |
| Execution role missing permissions for the test template | Each test template runs a different set of AWS FIS actions. Attach the permissions policy for the template you are running. For the policies, see [IAM execution roles for resilience testing](next-gen-resilience-testing-iam.md). |
| Multi-account role chain not configured | For a multi-account test, verify the orchestrator role can assume the target role in each account that contains targeted resources. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
