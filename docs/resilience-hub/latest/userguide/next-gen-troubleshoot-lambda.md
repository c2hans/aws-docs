---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-lambda.html
---

# Non-VPC Lambda not appearing
<a name="next-gen-troubleshoot-lambda"></a>

**Symptom:** Lambda function dependencies are not discovered.

**Cause:** Lambda functions not connected to a VPC do not make DNS queries through Route 53 resolvers.

**Solution:** Either connect the Lambda function to a VPC, or manually track its dependencies outside of Resilience Hub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
