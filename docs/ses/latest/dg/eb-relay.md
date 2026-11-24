---
source_url: https://docs.aws.amazon.com/ses/latest/dg/eb-relay.html
---

# SMTP relay

Simple Mail Transfer Protocol (SMTP) can transfer email through one or more servers before the message reaches its final recipient. An SMTP server that passes the message to the next server is a relay. For the SMTP relay model, see [RFC 5321, section 3.6](https://www.rfc-editor.org/rfc/rfc5321.html#section-3.6).

An SES Mail Manager SMTP relay is a reusable destination configuration. It specifies the public SMTP server hostname, port, and authentication that a rule action uses to deliver email. Use a relay when Mail Manager must filter, scan, modify, or archive email before handing it to an existing mailbox provider, on-premises mail server, or email gateway.

The relay resource and SMTP relay action have different purposes. The relay resource defines where and how Mail Manager connects. The action selects the current email and SMTP envelope recipients to send through that relay. For action fields, envelope-sender behavior, failure handling, and action order, see [SMTP relay](eb-rules-actions.md#eb-rules-actions-relay).

The following list provides a text equivalent for the diagram.

Google Workspace mailbox delivery
Internet senders connect to an *Open ingress point* for `example.com` on port 25. A traffic policy with a `DENY` default action allows the intended recipients and requires TLS 1.2 or later. An ordered rule set archives the accepted email and runs the relay action. The unauthenticated SMTP relay connects over TLS to `aspmx.l.google.com` on port 25. Google Workspace then delivers the email to the corporate mailbox.

Microsoft 365 mailbox delivery
Internet senders connect to an *Open ingress point* for `example.org` on port 25. A traffic policy with a `DENY` default action allows the intended recipients and requires TLS 1.2 or later. An ordered rule set archives the accepted email and runs the relay action. The unauthenticated SMTP relay connects over TLS to `example-org.mail.protection.outlook.com` on port 25. Microsoft 365 then delivers the email to the corporate mailbox.

Authenticated SMTP gateway
An application or mail server connects to an *Authenticated ingress point* on port 587. A traffic policy with a `DENY` default action allows the approved domains and limits the maximum message size to 30 MiB. An ordered rule set scans and archives the accepted email before it runs the relay action. The SMTP relay uses the destination username and password from AWS Secrets Manager to connect over TLS to `smtp.gateway.example.net` on port 587.

For every flow, a traffic-policy rejection returns an SMTP rejection before rule-set processing. For accepted email, rule-set application logs record action status, destination SMTP responses, and rejected recipients. Relay metrics count delivered and rejected recipients by relay ID. The final relay outcome changes from `IN_PROGRESS` to `SUCCESS` or `FAILURE`.

The following diagram illustrates these flows.

![Open ingress point and Authenticated ingress point connect to Traffic policy, Rule set, SMTP relay, Public SMTP destination.](https://docs.aws.amazon.com/ses/latest/dg/images/smtp-relay-flows.png)

For an unauthenticated destination, configure the destination to accept connections from the [Mail Manager SMTP relay IP ranges](https://docs.aws.amazon.com/general/latest/gr/ses.html#ses_mm_relay_ip_ranges) for your AWS Region. Do not add these shared IP ranges to your domain's SPF record.

**Note**
The destination must provide a public SMTP endpoint. Private SMTP endpoints are not supported. Mail Manager requires TLS when it connects to the destination.

## How SMTP relay works
<a name="eb-relay-how-it-works"></a>

Email follows these steps when a rule uses an SMTP relay action.

1. A sender connects to an open or authenticated ingress endpoint.

1. The ingress endpoint's traffic policy accepts or rejects each SMTP envelope recipient. Rejected recipients do not enter rule-set processing.

1. The assigned rule set evaluates its rules and runs actions in order for the selected recipients.

1. Earlier actions can archive the email, add headers, or replace SMTP envelope recipients before the relay action runs.

1. The relay action loads the destination from the relay resource and sends the current MIME email to the selected recipients.

1. Rule-set processing waits for a final delivery or rejection outcome for each selected recipient. For logs and metrics, see [Monitor and troubleshoot rule sets](eb-rules-monitoring.md).

A relay uses the configured hostname as a fixed next-hop SMTP server. To let SES resolve recipient domains and deliver directly to their mail servers, use the [Send to internet action](eb-rules-actions.md#eb-rules-actions-send) instead.

## Choosing destination authentication and port
<a name="eb-relay-authentication-port"></a>

Choose authentication and a port according to the service exposed by the destination SMTP server. Authentication on the source ingress endpoint is independent from authentication on the destination relay.

| Destination | Authentication | Common port | When to use |
| --- | --- | --- | --- |
| Mail server or inbound gateway | NoAuthentication. Configure the destination to accept the regional Mail Manager SMTP relay IP ranges. | 25 | Relaying email between mail servers, including delivery to Google Workspace and Microsoft 365. |
| Authenticated SMTP server | SecretArn. The AWS Secrets Manager secret contains the destination username and password. | 587, when supported | Submitting email to a public SMTP server that requires SMTP credentials. |

[RFC 6409](https://www.rfc-editor.org/rfc/rfc6409.html) separates message relay from message submission. SMTP relay between mail servers continues to use port 25. Authenticated message submission normally uses port 587. Always use the port documented by the destination provider.<a name="relay-inbound-tab"></a><a name="relay-outbound-tab"></a>

## Before you create an SMTP relay
<a name="eb-relay-before-you-begin"></a>

1. Configure a public SMTP hostname and port on the destination. Confirm that it accepts TLS connections from Mail Manager.

1. For an unauthenticated destination, allow the [regional Mail Manager SMTP relay IP ranges](https://docs.aws.amazon.com/general/latest/gr/ses.html#ses_mm_relay_ip_ranges). Verify every intended recipient email identity in SES. For identity instructions, see [Creating a domain identity](creating-identities.md#verify-domain-procedure).

1. For an authenticated destination, create an AWS Secrets Manager secret that contains `username` and `password`. Configure the resource and AWS KMS key policies described in [Permission policies for SMTP relay](eb-policies.md#eb-policies-relay).

1. Create the rule set that selects the messages and recipients to relay. For setup instructions, see [Create and manage rule sets](eb-rules-setup.md).

**Warning**
An unauthenticated relay requires verified recipient identities. If any selected recipient is not verified, the relay action rejects the complete send before delivery starts.

## Creating and managing an SMTP relay
<a name="eb-relay-create-console"></a>

**To create an SMTP relay in the SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the navigation pane, under **Mail Manager**, choose **SMTP relays**.

1. Choose **Create SMTP relay**, and enter a unique relay name.

1. Enter the public destination SMTP server hostname and port.

1. For an unauthenticated destination, choose **No authentication**. For an authenticated destination, select the AWS Secrets Manager secret that contains its SMTP username and password.

1. Choose **Create SMTP relay**.

To update a relay, select its name and change its name, destination hostname, port, or authentication. To delete a relay, remove its references from rule sets, and then choose **Delete** on the **SMTP relays** page.

### Creating an SMTP relay with the AWS CLI
<a name="eb-relay-create-cli"></a>

The following command creates an unauthenticated relay to Google Workspace on port 25.

```bash
PROMPT> aws mailmanager create-relay \
  --region {{us-east-1}} \
  --relay-name {{google-workspace}} \
  --server-name aspmx.l.google.com \
  --server-port 25 \
  --authentication '{"NoAuthentication": {}}'
```

Replace the AWS Region and relay name with your values. Before using the relay, configure Google Workspace as described in [Setting up Google Workspace for inbound (unauthenticated) SMTP relay](#eb-relay-inbound-google).

The following command creates an authenticated relay to a public SMTP submission server on port 587.

```bash
PROMPT> aws mailmanager create-relay \
  --region {{us-east-1}} \
  --relay-name {{corporate-submission}} \
  --server-name {{smtp.gateway.example.com}} \
  --server-port 587 \
  --authentication '{
    "SecretArn": "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{mail-manager-relay-credentials}}"
  }'
```

Replace the AWS Region, account ID, relay name, destination hostname, and secret name with your values. For complete field constraints, see [`CreateRelay`](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateRelay.html). To manage the resource with CloudFormation, see [`AWS::SES::MailManagerRelay`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-mailmanagerrelay.html).

### Using Secrets Manager credentials
<a name="eb-relay-secrets-manager"></a>

An authenticated relay reads the destination SMTP username and password from the secret referenced by `SecretArn`. Store the secret as a JSON object with the following keys.

```json
{
  "username": "{{smtp-user}}",
  "password": "{{smtp-password}}"
}
```

Use the exact lowercase keys `username` and `password`. The values must match credentials accepted by the destination SMTP server. For the required secret resource policy and AWS KMS key policy, see [Secrets resource policy](eb-policies.md#eb-policies-relay-secrets) and [KMS CMK policy](eb-policies.md#eb-policies-relay-cmk).

#### Rotating destination credentials
<a name="eb-relay-secrets-rotation"></a>

Updating the secret does not update the credential on the destination SMTP server. Coordinate both changes to avoid authentication failures.

**To rotate SMTP relay credentials**

1. Configure the destination SMTP server to accept the new credential while the previous credential remains valid.

1. Update the secret's `AWSCURRENT` version with the new `username` and `password`.

1. Confirm successful relay deliveries in the rule-set logs and relay metrics.

1. Remove the previous credential from the destination SMTP server.

**Note**
Mail Manager can temporarily use cached credentials. Keep the previous credential valid during the transition when the destination supports overlapping credentials.

## Using SMTP relays with ingress points and rules
<a name="eb-relay-rules-ingress"></a>

An open or authenticated ingress endpoint can reference a rule set that contains an SMTP relay action. The ingress endpoint controls how the sender connects to Mail Manager. The relay resource separately controls how Mail Manager connects to the destination SMTP server.

Actions run in configured order. Common patterns include:
+ `Archive`, and then `Relay`, to retain email before mailbox delivery.
+ `AddHeader`, and then `Relay`, to pass routing or classification information to the destination.
+ `ReplaceRecipient`, and then `Relay`, to deliver to a different SMTP envelope recipient.
+ Separate recipient rules and relay resources to route users to Google Workspace, Microsoft 365, or another mail system.

For complete examples, see [Rule set examples](eb-rules-examples.md). For a complete Google Workspace and Microsoft 365 architecture, see [AWS Messaging Blog: How to use SES Mail Manager SMTP Relay action to deliver inbound email to Google Workspace and Microsoft 365](https://aws.amazon.com/blogs/messaging-and-targeting/how-to-use-ses-mail-manager-smtp-relay-action-to-deliver-inbound-email-to-google-workspace-and-microsoft-365/).

## Monitoring relay delivery
<a name="eb-relay-monitoring"></a>

An SMTP relay action first records delivery as in progress. After the destination reports the outcome for every selected recipient, the action records success or failure. A single action can deliver some recipients and reject others.

Use rule-set application logs to inspect the action status and destination SMTP responses. Use the relay delivery and rejection metrics to monitor outcomes by relay ID. For log fields, metrics, and troubleshooting queries, see [Monitor and troubleshoot rule sets](eb-rules-monitoring.md).

## Recommendations
<a name="eb-relay-recommendations"></a>
+ Use a separate relay resource for each destination, credential set, or operational owner.
+ Use port 25 for mail-server relay. Use port 587 when an authenticated destination provides an SMTP submission service on that port.
+ Use `DENY` as the traffic policy default action and allow only intended recipients and traffic.
+ Put Archive before SMTP relay when the email must be retained before delivery.
+ Use `DROP` as the relay action failure policy when a destination rejection must stop later processing for that recipient.
+ Do not use consecutive SMTP relay actions as automatic failure-only fallback. With `CONTINUE`, recipients delivered by the first action also reach the next action and can receive duplicate email.
+ Test the complete flow with a subdomain before changing the MX record for a production domain.

## SMTP relay use cases
<a name="eb-relay-use-cases"></a>

Use Mail Manager as an inbound SMTP gateway to filter, inspect, and archive email before final delivery to an existing mailbox provider. The following walkthroughs preserve the provider-specific configuration needed for Google Workspace and Microsoft 365.

For an archive-before-delivery example that relays email to an existing mail server, see [AWS Messaging Blog: Archiving and sending to final SMTP server](https://aws.amazon.com/blogs/messaging-and-targeting/archiving-and-sending-to-final-smtp-server/).

### Setting up Google Workspace for inbound (unauthenticated) SMTP relay
<a name="eb-relay-inbound-google"></a>

The following walkthrough shows how to set up Google Workspace to receive email from an unauthenticated Mail Manager SMTP relay. Configure the relay with `aspmx.l.google.com` as the destination hostname, port `25`, and `NoAuthentication`.

For the complete provider configuration and end-to-end mail flow, see [AWS Messaging Blog: How to use SES Mail Manager SMTP Relay action to deliver inbound email to Google Workspace and Microsoft 365](https://aws.amazon.com/blogs/messaging-and-targeting/how-to-use-ses-mail-manager-smtp-relay-action-to-deliver-inbound-email-to-google-workspace-and-microsoft-365/).

**Prerequisites**
+ Access to the Google administrator console ([Google administrator console](https://admin.google.com/) > Apps > Google Workspace > Gmail).
+ Access to the domain nameserver hosting the MX records for the domains which will be used for Mail Manager setup.

**To set up Google Workspace to work with an inbound SMTP relay**
+ **Add Mail Manager SMTP relay IP ranges to the inbound gateway configuration**

  1. In the [Google administrator console](https://admin.google.com/), go to **Apps > Google Workspace > Gmail**.

  1. Select **Spam, Phishing, and Malware**, then go to **Inbound gateway** configuration.

  1. Enable **Inbound gateway**, and configure it with the following details:
![Enable Inbound gateway, and configure it with details.](https://docs.aws.amazon.com/ses/latest/dg/images/GoogleWSInboundGateway.png)
     + In **Gateway IPs**, choose **Add**, and add the ranges for your AWS Region from the [Mail Manager SMTP relay IP ranges](https://docs.aws.amazon.com/general/latest/gr/ses.html#ses_mm_relay_ip_ranges) table.
     + Select **Automatically detect external IP**.
     + Select **Require TLS for connections from the email gateways listed above**.
     + Select **Save** at the bottom of the dialog box to save the configuration. Once saved, the administrator console will show the **Inbound gateway** as enabled.

### Setting up Microsoft 365 for inbound (unauthenticated) SMTP relay
<a name="eb-relay-inbound-ms365"></a>

The following walkthrough shows how to set up Microsoft 365 to receive email from an unauthenticated Mail Manager SMTP relay. Use the hostname from your Microsoft 365 MX record as the relay destination. For example, for `example.com`, use `example-com.mail.protection.outlook.com`, port `25`, and `NoAuthentication`.

For the complete provider configuration and end-to-end mail flow, see [AWS Messaging Blog: How to use SES Mail Manager SMTP Relay action to deliver inbound email to Google Workspace and Microsoft 365](https://aws.amazon.com/blogs/messaging-and-targeting/how-to-use-ses-mail-manager-smtp-relay-action-to-deliver-inbound-email-to-google-workspace-and-microsoft-365/).

**Prerequisites**
+ Access to the Microsoft Security admin center ([Microsoft Security admin center](https://security.microsoft.com/homepage) > Email & collaboration > Policies & Rules > Threat policies).
+ Access to the domain nameserver hosting the MX records for the domains which will be used for Mail Manager setup.

**To set up Microsoft 365 to work with an inbound SMTP relay**

1. **Add Mail Manager SMTP relay IP ranges to the allow list**

   1. In the [Microsoft Security admin center](https://security.microsoft.com/homepage), go to **Email & collaboration > Policies & Rules > Threat policies**.

   1. Select **Anti-spam** under **Policies**.

   1. Select **Connection filter policy** followed by **Edit connection filter policy**.
      + In the **Always allow messages from the following IP addresses or address range** dialog, add the ranges for your AWS Region from the [Mail Manager SMTP relay IP ranges](https://docs.aws.amazon.com/general/latest/gr/ses.html#ses_mm_relay_ip_ranges) table.
      + Select **Save**.

   1. Return to the **Anti-spam** option and choose **Anti-spam inbound policy**.
      + At the bottom of the dialog, select **Edit spam threshold and properties**:
![Enable Inbound gateway, and configure it with details.](https://docs.aws.amazon.com/ses/latest/dg/images/MSO365AntiSpamInboundPolicy.png)
      + Scroll to **Mark as spam** and ensure that **SPF record: hard fail** is set to **Off**.
      + Select **Save**.

1. **Enhanced Filtering configuration (recommended)**

   This option lets Microsoft 365 identify the original connecting IP before the message was received by SES Mail Manager.

   1. **Create an inbound connector**
      + Sign in to the [Exchange admin center](https://admin.exchange.microsoft.com/#/homepage) and go to **Mail flow** > **Connectors**.
      + Select **Add a connector**.
      + In **Connection from**, select **Partner organization** followed by **Next**.
      + Fill in the fields as follows:
        + **Name** – Simple Email Service Mail Manager connector
        + **Description** – Connector for filtering
![Adding a connector.](https://docs.aws.amazon.com/ses/latest/dg/images/MSExAddConnector.png)
      + Select **Next**.
      + In **Authenticating sent email**, select **By verifying that the IP address of the sending server matches one of the following IP addresses, which belong to your partner organization**. Add the ranges for your AWS Region from the [Mail Manager SMTP relay IP ranges](https://docs.aws.amazon.com/general/latest/gr/ses.html#ses_mm_relay_ip_ranges) table.
![In Authenticating sent email, select By verifying that the IP address of the sending server matches one of the following IP addresses, which belong to your partner organization and add the ingress endpoint IPs specific to your region from the following table.](https://docs.aws.amazon.com/ses/latest/dg/images/MSExAuthSentMail.png)
      + Select **Next**.
      + In **Security restrictions**, accept the default **Reject email messages if they aren’t sent over TLS** setting, followed by **Next**.
      + Review your settings and select **Create connector**.

   1. **Enable enhanced filtering**

      Now that the inbound connector has been configured, you will need to enable the enhanced filtering configuration of the connector in the **Microsoft Security admin center**.
      + In the [Microsoft Security admin center](https://security.microsoft.com/homepage), go to **Email & collaboration > Policies & Rules > Threat policies**.
      + Select **Enhanced filtering** under **Rules**.
![Select Enhanced filtering under Rules within Threat policies.](https://docs.aws.amazon.com/ses/latest/dg/images/MSO365ThreatPolicies.png)
      + Select the **Simple Email Service Mail Manager connector** that you created previously to edit its configuration parameters.
      + Select both **Automatically detect and skip the last IP address** and **Apply to entire organization**.
![Edit the previously created connector's configuration.](https://docs.aws.amazon.com/ses/latest/dg/images/MSO365EditConnector.png)
      + Select **Save**.
