---
source_url: https://docs.aws.amazon.com/ses/latest/dg/eb-addlist.html
---

# Address Lists

An Address List is a Regional Mail Manager resource that stores reusable email addresses, domains, and supported wildcard patterns. A traffic policy or rule condition can check whether an address matches the list.

An Address List does not allow, deny, route, or drop email by itself. The traffic-policy statement or rule action defines what happens after the membership check.

Address lists are useful when you manage thousands of domains. Store recipient domains in a reusable list for traffic-policy filtering. Store sender or recipient domains in a list for rule-set routing. You can update the list as domains change instead of maintaining thousands of repeated conditions across traffic policies and rules.

The following diagram shows address lists used across three ingress-point flows. Each traffic policy filters recipients before accepting email. Each rule set routes or processes the accepted email.

![Three horizontal Mail Manager flows use open, mutual TLS, and authenticated ingress points. Each traffic policy uses an address list to filter recipients before accepting email. Each rule set can use an address list to select sender or recipient addresses for routing and other actions. Address lists can contain thousands of reusable addresses and domains.](https://docs.aws.amazon.com/ses/latest/dg/images/address-list-flows.png)

The ingress endpoint does not reference an Address List directly. Each ingress endpoint references one traffic policy and one rule set. Conditions in those resources reference the Address List.

## How address lists solve large-scale address management
<a name="what-are-address-lists"></a>

Without an Address List, a traffic policy or rule must contain each address or domain as a separate value or condition. The configuration becomes difficult to review and update when it contains hundreds or thousands of domains.

With an Address List, the policy or rule contains one membership condition that references the list. You maintain the addresses separately from the filtering and routing logic. The same list can be referenced by more than one traffic policy or rule set.
+ **Centralized membership** – Add or remove a domain in one resource instead of changing every policy or rule that uses the group.
+ **Reusable filtering** – Use a maintained recipient list in traffic policies assigned to open, authenticated, or mutual TLS ingress endpoints.
+ **Reusable routing** – Use sender or recipient lists in rules that relay, archive, scan, store, or send accepted email.
+ **Separate data from behavior** – Update which addresses belong to a group without rebuilding the conditions and actions that use the group.

## How address-list membership is evaluated
<a name="how-address-lists-work"></a>

Traffic policies and rule sets use address lists at different stages of message processing.

1. The ingress endpoint's traffic policy can check whether each SMTP envelope recipient is in an Address List. A matching statement allows or denies that recipient. A denied recipient does not enter rule-set processing.

1. After the traffic policy accepts at least one recipient, the ingress endpoint receives the message and passes it to the assigned rule set.

1. A rule can check an address from the SMTP envelope or message headers against an Address List. The rule's conditions select the recipients for which its actions run.

The following table compares the available membership checks.

| Configuration | Address properties | Result |
| --- | --- | --- |
| Traffic policy | RECIPIENT | Allows or denies each SMTP envelope recipient before the message enters rule-set processing. |
| Rule | RECIPIENT, MAIL\_FROM, SENDER, FROM, TO, and CC | Selects the recipients for which the rule's configured actions run. |

Use `IS_TRUE` when the condition must match an address in the list. Use `IS_FALSE` when the condition must match an address that is not in the list. Each membership condition references one Address List.

**Envelope addresses and message headers have different purposes**
`RECIPIENT` and `MAIL_FROM` come from the SMTP envelope. `FROM`, `SENDER`, `TO`, and `CC` come from message headers. Do not use a message-header address by itself as proof of the sender's identity. A sender can provide those header values.

## Address-list use cases
<a name="eb-addlist-use-cases"></a>

| Goal | Where to use the list | Pattern |
| --- | --- | --- |
| Reject mail for unknown recipients | Traffic policy | Use DENY as the default action. Add an ALLOW statement for recipients in the approved-address list. |
| Restrict application outbound destinations | Traffic policy on an authenticated ingress endpoint | Allow only recipients in an approved-destination list. |
| Exclude suspended or invalid addresses | Traffic policy | Use IS\_FALSE with the invalid-address list and combine it with the other conditions that the message must meet. |
| Route departments or customer domains separately | Rule set | Check recipient membership, then relay or deliver the selected recipients to the matching destination. |
| Process selected sender groups differently | Rule set | Check MAIL\_FROM, SENDER, or FROM membership, then run the required archive, inspection, or routing actions. |

**Related example**
The [AWS Messaging Blog outbound email walkthrough](https://aws.amazon.com/blogs/messaging-and-targeting/streamlining-outbound-emails-with-amazon-ses-mail-manager/) uses a default `DENY` traffic policy, a `Valid-Address` list, and an `Invalid-Email-List`. Accepted messages then pass through rules that scan, isolate, archive, and send email.

## Recommendations for address lists
<a name="best-practices-and-considerations"></a>
+ Use separate lists for separate purposes and trust boundaries. For example, use `valid-inbound-recipients` and `approved-outbound-destinations` instead of one list for both flows.
+ Use `DENY` as the traffic policy's default action, and add explicit `ALLOW` statements for recipients that the ingress endpoint must accept.
+ Store address-list entries in lowercase for consistent maintenance and comparison.
+ Use exact addresses and domains unless a wildcard is required. Test a wildcard against representative matching and nonmatching addresses before using it in a traffic policy or rule.
+ Review the imported and failed item counts after every bulk import.
+ Before removing a member from a shared list, identify every traffic policy and rule that references the list. A membership change affects every reference.

**Topics**
+ [How address lists solve large-scale address management](#what-are-address-lists)
+ [How address-list membership is evaluated](#how-address-lists-work)
+ [Address-list use cases](#eb-addlist-use-cases)
+ [Recommendations for address lists](#best-practices-and-considerations)
+ [Create and manage Address Lists](setting-up-address-lists.md)
+ [Use Address Lists in traffic policies and rules](using-address-lists-in-traffic-policies-and-rule-sets.md)
