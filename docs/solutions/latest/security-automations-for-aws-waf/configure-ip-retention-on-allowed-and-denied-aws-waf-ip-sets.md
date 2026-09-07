---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/configure-ip-retention-on-allowed-and-denied-aws-waf-ip-sets.html
---

# Configure IP retention on Allowed and Denied AWS WAF IP sets
<a name="configure-ip-retention-on-allowed-and-denied-aws-waf-ip-sets"></a>

You can configure IP retention on Allowed and Denied AWS WAF IP sets that the solution creates. The following sections explain how it works and provide the steps to set it up.

## How it works
<a name="how-it-works"></a>

 **Architecture diagram depicting the AWS WAF allowed and denied lists and other AWS resources**

![ip retention](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/ip-retention.png)

1. When a user updates (add or delete an IP address) the Allowed or Denied WAF IP set, this action invokes an AWS WAF `UpdateIPSet` API call and creates an event.

1. An [Amazon EventBridge](https://aws.amazon.com/eventbridge/) events rule detects the events based on a predefined event pattern, and invokes a Lambda function to set the retention period for all the IP addresses that exist in the IP set after the update.

1. The Lambda function processes the events, extracts relevant data to IP retention (such as IP set name, ID, scope, IP addresses), and inserts it into a DynamoDB table. It also inserts an `ExpirationTime` attribute for each DynamoDB item. The solution calculates the expiration time by adding a user-defined retention period to the event time. The table has [DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) and [Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) turned on. The TTL attribute is `ExpirationTime`.

1. When an item reaches its expiration time, TTL is invoked and DynamoDB deletes the item from the table after its expiration time. Upon deletion of the item, the deleted item is added to the DynamoDB stream, which invokes a Lambda function for downstream processing.

1. The Lambda function obtains the information about the deleted item from the DynamoDB stream and makes an AWS WAF API call to remove the expired IP addresses included in the item from the target AWS WAF IP set.

## Turn on IP retention
<a name="turn-on-ip-retention"></a>

Follow these steps to turn on IP retention:

1. In the Cloudformation stack that you [deploy](deploy-the-solution.md) or [update](update-the-solution.md), enter the **IP Retention Period (Minutes) for Allowed IP Set** and **IP Retention Period (Minutes) for Denied IP Set**. The minimum retention period is 15 minutes. The solution treats any number between `0` and `15` as `15`. For more information about deployment configuration, refer to [Step 1. Launch the stack](step-1.-launch-the-stack.md).

1. Enter an email address if you want to receive an email notification when expired IP addresses are removed from the AWS WAF IP set. If you choose to receive an email notification, you must confirm subscription using the link in the email you receive after the solution successfully deploys. For more information about deployment configuration, refer to [Step 1. Launch the stack](step-1.-launch-the-stack.md).

1. Update the AWS WAF IP set by adding or deleting IP addresses. This initiates the IP retention process and creates an DynamoDB item, including an IP expiration list. This expiration list consists of IP addresses that exist in the AWS WAF IP set after your update it.

1. Once the DynamoDB item reaches its expiration time and is deleted from the table, the solution deletes the IP addresses included in the item’s IP expiration list from the WAF IP set.

**Note**
Depending on the time when DynamoDB deletes an item expired by TTL, the actual delete operation of an expired IP address from the AWS WAF IP set can vary. DynamoDB TTL deletion mainly depends on the size and activity level of a table. Expect a delay in the AWS WAF delete operation because of the potential delay in the DynamoDB delete operation. In general, the solution deletes expired IP addresses from the AWS WAF IP set shortly after DynamoDB TTL deletion. For more information, refer to [DynamoDB Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html) in the *Amazon DynamoDB Developer Guide*.
