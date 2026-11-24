---
source_url: https://docs.aws.amazon.com/ses/latest/dg/eb-addons.html
---

# Email Add Ons

Email Add Ons extend Mail Manager with email security services from SES-approved providers. An Add On can evaluate sender IP reputation before Mail Manager accepts a message, or scan accepted messages for spam, phishing, and malware.

Each Add On works in one part of the email flow. Traffic policy Add Ons evaluate the sender IP address before rule set processing. Rule set Add Ons scan message content after the traffic policy accepts the message.

Add Ons use metered pricing. Review the current price and terms on the Add On details page before subscribing. For more information, see [SES pricing](https://aws.amazon.com/ses/pricing/).

## How Email Add Ons work
<a name="eb-addons-how-it-works"></a>

Using an Add On involves two resources:

1. An *Add On subscription* records your acceptance of the provider's terms and pricing.

1. An *Add On instance* represents the subscribed service in your account. Traffic policies and rule sets reference the Add On instance Amazon Resource Name (ARN).

When you subscribe through the Mail Manager console, the console creates both resources. When you use the Mail Manager API, first call [CreateAddonSubscription](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateAddonSubscription.html), and then call [CreateAddonInstance](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateAddonInstance.html) with the returned subscription ID.

## Available Email Add Ons
<a name="eb-addons-available"></a>

The following table shows where each Add On can be used.

| Add On | Provider | Used in | Purpose |
| --- | --- | --- | --- |
| Spamhaus IP Reputation | Spamhaus | Traffic policies | Checks whether the sender IPv4 or IPv6 address appears on the SBL or XBL. |
| Abusix Guardian Mail | Abusix | Traffic policies | Checks whether the sender IPv4 or IPv6 address appears on the Spam, Exploit, or Policy lists. |
| Trend Micro Virus Scanning | Trend Micro | Rule sets | Scans accepted messages for malware. |
| Vade Advanced Email Security | Hornetsecurity | Rule sets | Scans accepted messages for spam, phishing, and malware. |

## Using Email Add Ons in traffic policies
<a name="eb-addons-traffic-policies"></a>

Spamhaus IP Reputation and Abusix Guardian Mail evaluate the sender IP address while Mail Manager applies the traffic policy. Rejecting unwanted senders at this stage prevents their messages from reaching the rule set.

Both Add Ons provide the following result properties.

**Is listed**
Indicates whether the sender IP address appears on any supported list.

**Listed on**
Identifies the specific lists on which the sender IP address appears.

Spamhaus can return `SBL` and `XBL`. Abusix can return `Spam`, `Exploit`, and `Policy`.

### Example: Allow messages only from senders not listed by Spamhaus
<a name="eb-addons-traffic-policy-example"></a>

Configure the traffic policy as follows:
+ *Default action* – `DENY`
+ *Statement action* – `ALLOW`
+ *Condition 1* – Recipient address ends with `@example.com`
+ *Condition 2* – Spamhaus IP Reputation **Is listed** is `False`

The traffic policy accepts a message only when both conditions match. A listed sender or a message for another domain does not match the `ALLOW` statement, so the default `DENY` action applies.

**Warning**
Using `ALLOW` as the default action is not recommended. If no `DENY` statement matches, a default `ALLOW` action can admit unbounded unwanted traffic.

Use **Is listed** for a general reputation check. Use **Listed on** when different lists require different handling.

For more information about creating traffic policies and statements, see [Creating traffic policies and policy statements in the SES console](eb-filters.md#eb-filters-create-console).

## Using Email Add Ons in rule sets
<a name="eb-addons-rule-sets"></a>

Trend Micro Virus Scanning and Vade Advanced Email Security scan message content after the traffic policy accepts the message. Their results can be combined with other rule conditions to select actions such as Drop, Write to S3, Deliver to mailbox, or Relay.

Trend Micro provides the following result properties.

| Property | Values |
| --- | --- |
| Is passed | True, False |
| Category | CLEAN, ERROR, MALWARE |

Vade provides the following result properties.

| Property | Values |
| --- | --- |
| Is passed | True, False |
| Category | CLEAN, ERROR, SPAM, PHISHING, MALWARE |
| Verdict | A detailed classification such as spam:high, phishing, malware, or transactional:purchases. |

**Note**
For both content-scanning Add Ons, an **Is passed** value of `True` can accompany an `ERROR` category. If your workflow must accept only messages that were scanned and found clean, match **Category** to `CLEAN` and handle `ERROR` separately.

### Example: Drop phishing and malware, then deliver other messages
<a name="eb-addons-rule-set-example"></a>

Create the following rules in priority order:

1. Create a rule named `drop-all-malicious-emails`. Set the Vade Advanced Email Security **Category** condition to `PHISHING` or `MALWARE`, and add the **Drop** action.

1. Create a rule named `forward-to-mailbox` with no conditions. Add the **Deliver to mailbox** action.

Vade adds its result to the processed message. For example:

```
X-SES-Vade-Advanced-Email-Security-AddonVerdict: spam:high
X-SES-Vade-Advanced-Email-Security-Category: SPAM
X-SES-Vade-Advanced-Email-Security-IsPassed: false
```

When the destination is , the spam result can help route the message to the recipient's Junk folder. For the complete workflow, see [Improving email security with SES Mail Manager and Hornetsecurity's Vade Advanced Email Security Add On](https://aws.amazon.com/blogs/messaging-and-targeting/improving-email-security-with-amazon-ses-mail-manager-and-hornetsecuritys-vade-advanced-email-security-add-on/) on the AWS Messaging and Targeting Blog.

For more information about defining rule conditions and actions, see [Rule conditions](eb-rules-conditions.md) and [Rule actions](eb-rules-actions.md).

## Common Email Add On use cases
<a name="eb-addons-use-cases"></a>
+ Reject senders with poor IP reputation before Mail Manager processes message content.
+ Reduce unnecessary rule processing and storage by rejecting unwanted traffic early.
+ Drop phishing or malware while delivering clean messages.
+ Route spam to a junk-mail workflow.
+ Store suspicious messages in Amazon S3 for investigation.
+ Apply different actions to transactional, commercial, community, and suspicious messages by using detailed Vade verdicts.

## Subscribing to Email Add Ons in the Mail Manager console
<a name="eb-addons-subscribe-console"></a>

**To subscribe to an Email Add On using the console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Email Add Ons** under **Mail Manager**.

1. Choose an Add On to open its details page.

1. Review the product description, supported use, result mapping, pricing, and terms.

1. Choose **Subscribe**.

1. Read the **Terms and Conditions**, select **I accept**, and then choose **Subscribe**.

After subscription, the Add On is available when you create a compatible traffic policy or rule condition.

To view subscription details or access support, choose the subscribed Add On. The **General details** section includes the subscription date and ARN. The **Support** tab includes links to AWS Support.

### Unsubscribing from an Email Add On
<a name="eb-addons-unsubscribe-console"></a>

Before you unsubscribe, remove the Add On from every traffic policy or rule set that references it.

**To unsubscribe from an Email Add On using the console**

1. On the **Email Add Ons** page, choose the subscribed Add On.

1. Choose **Unsubscribe**.

1. Enter `confirm` in the confirmation field.

1. Choose **Unsubscribe**.

When you use the API, delete the Add On instance before you delete its subscription. The subscription cannot be deleted while an instance uses it.

## Email Add On limitations and recommendations
<a name="eb-addons-considerations"></a>
+ You can have one subscription for each Add On name.
+ You can have one instance for each subscription.
+ Each Add On supports either traffic policies or rule sets, as shown in [Available Email Add Ons](#eb-addons-available).
+ Traffic policy Add Ons inspect the sender IP address. They do not scan message content.
+ Rule set Add Ons scan only messages accepted by the traffic policy.
+ Place inexpensive conditions, such as recipient matching, before an Add On condition. Rule conditions run in order and stop when no recipients remain.
+ Use a traffic policy with a default `DENY` action. Add explicit `ALLOW` statements for accepted traffic.
+ Use the Add On result in the Mail Manager condition for security enforcement. Use generated `X-SES-` headers for downstream routing only after the Add On has processed the message.
+ Review current pricing before enabling an Add On. Using an Add On can incur charges under its published pricing.
