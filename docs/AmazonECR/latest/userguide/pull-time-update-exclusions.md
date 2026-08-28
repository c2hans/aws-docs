---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-time-update-exclusions.html
---

# Pull-time update exclusions
<a name="pull-time-update-exclusions"></a>

Amazon ECR updates the `LastRecordedPullTime` timestamp on every pull except for pulls by AWS Inspector. Pull-time update exclusions allow you to specify IAM role ARNs that should not update image pull times when they pull images, such as pulls by third-party scanners (such as Crowdstrike, Snyk, and Trivy). This is useful for images that are used for testing or CI/CD purposes where you don't want the pull time to affect lifecycle policy decisions.

When a role in the exclusion list pulls an image, the pull time remains unchanged. Any other role continues to update pull time (current behavior). You can configure up to 100 exclusions per account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
