---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/sns-topic.html
---

# Amazon SNS topic - Remediation Progress
<a name="sns-topic"></a>

Automated Security Response on AWS creates an Amazon SNS topic, SO0111-ASR\_Topic. This topic is used to post updates about remediation progress. Following are the three possible notifications sent to this topic.

```
Remediation queued for [.replaceable]`<standard>` control [.replaceable]`<control_ID>` in account [.replaceable]`<account_ID>`
```

```
Remediation failed for [.replaceable]`<standard>` control [.replaceable]`<control_ID>` in account [.replaceable]`<account_ID>`
```

```
[.replaceable]`<control_ID>` remediation was successfully invoke via AWS Systems Manager in account [.replaceable]`<account_ID>`
```

This is the completion message. It indicates that the remediation completed without error; however, the definitive test for successful remediation is the AWS Config check and/or manual validation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
