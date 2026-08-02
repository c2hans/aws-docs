---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/filtering-an-sns-topic-subscription.html
---

# Filtering an SNS topic subscription
<a name="filtering-an-sns-topic-subscription"></a>

 [Amazon SNS subscription filter policies](https://docs.aws.amazon.com/sns/latest/dg/sns-subscription-filter-policies.html):

1. Navigate to the subscription of the SNS topic.

1. Under Subscription filter policy, select"Edit".

1. Expand "Subscription filter policy" and toggle the "Subscription filter policy" option to enable filters.

1. Select the "Message Body" scope.

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
