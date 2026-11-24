---
source_url: https://docs.aws.amazon.com/ses/latest/dg/using-address-lists-in-traffic-policies-and-rule-sets.html
---

# Use Address Lists in traffic policies and rules

A traffic policy and rule set use address lists at different stages. The traffic policy checks recipients while the SMTP client is identifying message recipients. The rule set processes the message only after the traffic policy accepts at least one recipient.

## Using address lists with ingress points
<a name="eb-addlist-ingress-points"></a>

Every ingress endpoint references one traffic policy and one rule set. An Address List can be referenced by conditions in either resource. This relationship is the same for open, authenticated, and mutual TLS ingress endpoints.
+ **Open ingress point** – Use a recipient Address List in the traffic policy to accept only maintained recipient addresses or domains from internet senders.
+ **Authenticated ingress point** – Use a recipient Address List in the traffic policy to restrict where applications and mail servers can send email.
+ **Mutual TLS ingress point** – Use a recipient Address List with the partner connection requirements. Use a rule membership condition when accepted partner email requires separate routing or processing.

For information about choosing and configuring an ingress endpoint, see [Ingress endpoints](eb-ingress.md).

## Using an Address List in a traffic policy
<a name="traffic-policy-example"></a>

A traffic-policy address-list condition can check only the `RECIPIENT` property. The condition evaluates each SMTP envelope recipient separately.

The following example uses `DENY` as the default action. Its `ALLOW` statement accepts a recipient only when the recipient is in the referenced Address List. Other recipients are rejected before the message enters rule-set processing.

```json
{
  "DefaultAction": "DENY",
  "PolicyStatements": [{
    "Action": "ALLOW",
    "Conditions": [{
      "BooleanExpression": {
        "Evaluate": {
          "IsInAddressList": {
            "Attribute": "RECIPIENT",
            "AddressLists": [
              "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-address-list/{{al-0123456789abcdef}}"
            ]
          }
        },
        "Operator": "IS_TRUE"
      }
    }]
  }]
}
```

In the following command, replace the AWS Region, traffic policy name, account ID, and Address List ID with your own values.

```bash
PROMPT> aws mailmanager create-traffic-policy \
  --region {{us-east-1}} \
  --traffic-policy-name {{allow-maintained-recipients}} \
  --policy-statements '[{
    "Action": "ALLOW",
    "Conditions": [{
      "BooleanExpression": {
        "Evaluate": {
          "IsInAddressList": {
            "Attribute": "RECIPIENT",
            "AddressLists": [
              "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-address-list/{{al-0123456789abcdef}}"
            ]
          }
        },
        "Operator": "IS_TRUE"
      }
    }]
  }]' \
  --default-action DENY
```

**Default ALLOW is not recommended**
Using `ALLOW` as the default action accepts every recipient that does not match a `DENY` statement. This includes recipients that you did not explicitly approve. Use `DENY` as the default action and add explicit `ALLOW` statements for the recipients that the ingress endpoint must accept.

For traffic-policy evaluation order and other condition types, see [Traffic policies and policy statements](eb-filters.md).

## Using an Address List in a rule
<a name="rule-set-example"></a>

A rule membership condition supports the following properties.

`RECIPIENT`
Checks each SMTP envelope recipient. Matching narrows the recipients for which the rule's actions run.

`MAIL_FROM`
Checks the SMTP envelope sender.

`SENDER`
Checks the `Sender` message header when present. Otherwise, it checks the `From` header.

`FROM`
Checks the `From` message header.

`TO`
Checks each address in the `To` message header. The condition matches when any address is in the list.

`CC`
Checks each address in the `Cc` message header. The condition matches when any address is in the list.

The following condition selects each SMTP envelope recipient that is in the referenced Address List. Place the condition in a rule's `Conditions` list. Use `IS_FALSE` instead when the rule must select recipients that are not in the list.

```json
{
  "BooleanExpression": {
    "Evaluate": {
      "IsInAddressList": {
        "Attribute": "RECIPIENT",
        "AddressLists": [
          "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-address-list/{{al-0123456789abcdef}}"
        ]
      }
    },
    "Operator": "IS_TRUE"
  }
}
```

**Note**
If a rule checks `TO` or `CC`, a match on any address in that header makes the condition match for the rule's currently selected recipients. Use `RECIPIENT` when the actions must apply only to matching SMTP envelope recipients.

**Message headers do not prove sender identity**
A sender can provide the `From`, `Sender`, `To`, and `Cc` message headers. Do not use membership of a header address by itself to authorize sensitive processing. Combine the condition with the authentication or security results required by your application.

For complete condition structure, `Unless` behavior, and rule examples, see [Rule conditions](eb-rules-conditions.md) and [Rule set examples](eb-rules-examples.md).

**Related example**
The [AWS Messaging Blog outbound email walkthrough](https://aws.amazon.com/blogs/messaging-and-targeting/streamlining-outbound-emails-with-amazon-ses-mail-manager/) shows an Address List traffic-policy check followed by ordered rules that scan, isolate, archive, and send accepted email.

## Changing a shared address list
<a name="eb-addlist-change-management"></a>

A membership change affects every traffic policy and rule that references the list. Before changing a shared list, identify its filtering and routing uses. Test both matching and nonmatching addresses for each affected email flow.

Use separate lists when two email flows have different ownership, trust, or rollout requirements. For example, keep `valid-inbound-recipients` separate from `approved-outbound-destinations`.
