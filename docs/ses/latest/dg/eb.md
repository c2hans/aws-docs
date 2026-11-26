---
source_url: https://docs.aws.amazon.com/ses/latest/dg/eb.html
---

# Mail Manager for Amazon SES

Amazon SES is a managed email service, and Mail Manager provides its managed email gateway capabilities. With Mail Manager, you can control email that enters or leaves your organization through Simple Mail Transfer Protocol (SMTP). You can apply reusable controls for filtering, security inspection, routing, application processing, delivery, and archiving.

Organizations often build separate gateways and integrations for each email flow. With Mail Manager, you can place consistent controls between internet senders, applications, partners, existing mail systems, and final destinations without operating the SMTP infrastructure. Use separate ingress points when flows need different authentication, filtering, processing, or operational boundaries.

Use Mail Manager when you need SMTP gateway controls for inbound or outbound email flows. For more information about sending application-generated email through the Amazon SES API or SMTP interface, see [Set up email sending with Amazon SES](send-email.md). For more information about receiving email with SES receipt rules, see [Email receiving with Amazon SES](receiving-email.md).

To create and manage Mail Manager resources, you need an AWS account and AWS Identity and Access Management (IAM) permissions for the required SES actions. For more information about access to SES, see [Identity and access management in Amazon SES](control-user-access.md). Some Mail Manager resources and rule actions require additional resource policies. For more information, see [Permission policies for Mail Manager](eb-policies.md).

For more information about the end-to-end email flow, common use cases, architecture walkthroughs, and steps to create your first flow, see [Getting started with Mail Manager](eb-getting-started.md).

Use the following topics to configure the resources that make up an email flow and its supporting security, permissions, archiving, and monitoring capabilities.
+ Use [Ingress endpoints](eb-ingress.md) to provide managed SMTP ingress points for internet senders, applications, mail servers, and partners. Choose open, authenticated, or mutual TLS client access and supported public or private network connectivity.
+ Use [Traffic policies and policy statements](eb-filters.md) to accept or reject each SMTP envelope recipient before rule-set processing. Evaluate recipients, sender IP addresses, TLS versions, address-list membership, and supported Email Add On results.
+ Use [Rule sets and rules](eb-rules.md) to match accepted email or individual recipients and run ordered actions. Actions can scan, modify, archive, store, invoke applications, stop processing, or deliver email.
+ Use [SMTP relay](eb-relay.md) to deliver email from a rule action to an existing public SMTP server, such as a hosted mailbox provider, on-premises mail server, or email gateway.
+ Use [Address Lists](eb-addlist.md) to maintain reusable groups of email addresses, domains, and supported wildcard patterns for traffic-policy filtering and rule-set routing.
+ Use [Email archiving](eb-archiving.md) to retain selected inbound and outbound email in managed, searchable storage. Search, download, or export matching messages.
+ Use [Email Add Ons](eb-addons.md) to add email security services from SES-approved providers. Check sender reputation before accepting email, or scan accepted messages for spam, phishing, and malware.
+ Use [Permission policies for Mail Manager](eb-policies.md) to configure the permission and resource policies required by ingress points, relays, archives, and rule actions.
+ Use [Mail Manager logging](eb-logging.md) to deliver application logs, traffic-policy debug logs, and rule-set logs to supported destinations. Inspect accepted and rejected traffic, rule matches, action results, and delivery outcomes.

For an end-to-end routing and archiving example, see [Mail Manager – Amazon SES introduces new email routing and archiving features](https://aws.amazon.com/blogs/messaging-and-targeting/mail-manager-amazon-ses-introduces-new-email-routing-and-archiving-features/) on the AWS Messaging Blog.

**Topics**
+ [Getting started with Mail Manager](eb-getting-started.md)
+ [Ingress endpoints](eb-ingress.md)
+ [Traffic policies and policy statements](eb-filters.md)
+ [Rule sets and rules](eb-rules.md)
+ [SMTP relay](eb-relay.md)
+ [Address Lists](eb-addlist.md)
+ [Email archiving](eb-archiving.md)
+ [Email Add Ons](eb-addons.md)
+ [Permission policies for Mail Manager](eb-policies.md)
+ [Mail Manager logging](eb-logging.md)
