---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-terraform-state.html
---

# Terraform state file not accessible
<a name="next-gen-troubleshoot-terraform-state"></a>

**Symptom:** Resource discovery fails reading the Terraform state file.

**Solutions:**
+ Verify the Amazon S3 bucket and key path are correct.
+ Verify the invoker role has `s3:GetObject` permission on the state file.
+ Verify the state file is in a supported format.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
