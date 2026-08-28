---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/session-credentials-security.html
---

# Security best practices
<a name="session-credentials-security"></a>
+ Use [least-privilege IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) on the role. Grant only the specific actions and resources your application needs.
+ Add `aws:SourceAccount` and `aws:SourceArn` conditions in your trust policy to limit which accounts and sessions can assume the role. For more information, see [Cross-service confused deputy prevention](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.
+ Monitor usage with CloudTrail. The `RoleSessionName` identifies the exact stream session that made each API call. See [Auditing with CloudTrail](session-credentials-cloudtrail.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
