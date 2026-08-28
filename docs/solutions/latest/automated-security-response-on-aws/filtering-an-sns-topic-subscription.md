---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/filtering-an-sns-topic-subscription.html
---

# Filtering an SNS topic subscription
<a name="filtering-an-sns-topic-subscription"></a>

 [Amazon SNS subscription filter policies](https://docs.aws.amazon.com/sns/latest/dg/sns-subscription-filter-policies.html):

1. Navigate to the subscription of the SNS topic.

1. Under Subscription filter policy, choose **Edit**.

1. Expand "Subscription filter policy" and toggle the "Subscription filter policy" option to enable filters.

1. Choose the "Message Body" scope.

1. Add your policy to the JSON editor.

1. Save changes.

Example policies:

Filter by account

```
 {
 "finding": {
 "account": [
 "111111111111",
 "222222222222"
 ]
 }
 }
```

Filter for errors

```
 {
 "severity": ["ERROR"]
 }
```

Filter by controls

```
 {
 "finding": {
 "standard_control": ["S3.9","S3.6"]
 }
 }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
