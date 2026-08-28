---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateSubscriptionFilterFirehose-Account.html
---

# Step 3: Create an account-level subscription filter policy
<a name="CreateSubscriptionFilterFirehose-Account"></a>

Switch to the sending account, which is 111111111111 in this example. You will now create the account-level subscription filter policy in the sending account. In this example, the filter causes every log event containing the string `ERROR` in all but two log groups to be delivered to the destination you previously created.

```
aws logs put-account-policy \
    --policy-name "CrossAccountFirehoseExamplePolicy" \
    --policy-type "SUBSCRIPTION_FILTER_POLICY" \
    --policy-document '{"DestinationArn":"arn:aws:logs:us-east-1:222222222222:destination:testFirehoseDestination", "FilterPattern": "{$.userIdentity.type = AssumedRole}", "Distribution": "Random"}' \
    --selection-criteria 'LogGroupName NOT IN ["LogGroupToExclude1", "LogGroupToExclude2"]' \
    --scope "ALL"
```

The sending account's log groups and the destination must be in the same AWS Region. However, the destination can point to an AWS resource such as a Firehose stream that is located in a different Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
