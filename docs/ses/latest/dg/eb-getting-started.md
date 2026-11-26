---
source_url: https://docs.aws.amazon.com/ses/latest/dg/eb-getting-started.html
---

# Getting started with Mail Manager

Amazon SES is a managed email service, and Mail Manager provides its managed email gateway capabilities. With Mail Manager, you can control email that enters or leaves your organization through Simple Mail Transfer Protocol (SMTP). You can use managed SMTP ingress points, traffic filtering, ordered processing rules, security integrations, delivery to existing mail systems or the internet, and searchable archiving.

Organizations often build separate gateways and integrations to filter unwanted email, route messages between systems, apply security checks, retain compliance copies, and process application email. With Mail Manager, you can combine these controls into reusable resources for separate email flows without operating the SMTP infrastructure.

You can configure an email flow in the SES console without writing code.

## How email flows through Mail Manager
<a name="eb-getting-started-email-flow"></a>

An email passes through the following stages:

1. The **source** is an internet sender, application, partner, appliance, or mail server that starts an SMTP connection.

1. The **ingress point** receives the SMTP connection for the flow. Its type controls whether the sender connects without credentials, with a username and password, or with a mutual Transport Layer Security (TLS) client certificate. The ingress point can use a public endpoint or supported private Amazon VPC connectivity. For more information about ingress point types and network options, see [Ingress endpoints](eb-ingress.md).

1. The assigned **traffic policy** accepts or rejects each SMTP envelope recipient before rule-set processing. Conditions can check the recipient, sender IP address, TLS version, [Address Lists](eb-addlist.md) membership, or supported [Email Add Ons](eb-addons.md) results. The policy can also reject messages above a configured maximum size. For more information about traffic policy evaluation and configuration, see [Traffic policies and policy statements](eb-filters.md).

1. After the traffic policy accepts at least one recipient, the assigned **rule set** processes the email. Ordered rules select email or individual recipients and run actions for each selection. For more information about rule processing, see [Rule sets and rules](eb-rules.md).

1. The configured **outcomes** can scan or modify the email, keep a copy in [Email archiving](eb-archiving.md), write it to Amazon S3, invoke Lambda, stop processing, or deliver it through an [SMTP relay](eb-relay.md) or another supported destination. For more information about the complete action list, see [Rule actions](eb-rules-actions.md).

1. Use **operational data** from [Mail Manager logging](eb-logging.md) and metrics to inspect traffic policy evaluation results, rule matches, action results, and delivery outcomes.

The flow starts at the source, passes through the ingress point and traffic policy, enters the rule set, and ends in one or more configured outcomes. An ingress point always references one traffic policy and one rule set. You can reuse either resource across ingress points or create separate resources when flows need different controls.

**Note**
Use `DENY` as the traffic policy default action, and add explicit `ALLOW` statements for the traffic that the ingress point must accept. Using `ALLOW` as the default action is not recommended because it accepts traffic that does not match a `DENY` statement, including traffic that you did not explicitly approve.

## Choosing a Mail Manager use case
<a name="eb-getting-started-use-cases"></a>

The following table maps common customer problems to Mail Manager patterns.

| Use case | Mail Manager pattern | Detailed guidance |
| --- | --- | --- |
| Protect and route internet email to hosted mailboxes | Receive email through an open ingress point. Allow only intended recipients, apply security and archive actions, and relay accepted email to Google Workspace, Microsoft 365, or another SMTP server. | [Receive internet email and relay it to hosted mailboxes](eb-ingress-use-cases.md#eb-ingress-use-case-inbound-gateway) |
| Control email from applications and mail servers | Use an authenticated ingress point, restrict permitted destinations, scan and archive accepted email, and then send it to the internet or an SMTP gateway. | [Send application or mail server email through a managed SMTP pipeline](eb-ingress-use-cases.md#eb-ingress-use-case-authenticated-smtp) |
| Inspect and isolate suspicious email | Filter sender and connection attributes in the traffic policy. Use Email Add Ons and rule actions to scan accepted email, isolate suspicious content, and stop it before delivery. | [Inspect and isolate suspicious email](eb-ingress-use-cases.md#eb-ingress-use-case-security-gateway) |
| Retain email for compliance and investigation | Archive selected inbound or outbound email in managed, searchable storage. Search, download, or export matching messages when needed. | [Archive email in transit](eb-ingress-use-cases.md#eb-ingress-use-case-archiving) |
| Process documents and application requests sent by email | Route dedicated recipient addresses through security checks, store or archive the message, and invoke application logic with Lambda. | [Process documents submitted by email](eb-ingress-use-cases.md#eb-ingress-use-case-document-intake) |

For more patterns, including email-to-SMS, tenant-isolated flows, and certificate-authenticated partners, see [Ingress point use cases and recommendations](eb-ingress-use-cases.md).

## Reviewing architecture walkthroughs
<a name="eb-getting-started-walkthroughs"></a>

The following AWS Messaging Blog posts show how Mail Manager resources work together in complete inbound, outbound, security, archiving, and application-processing architectures.
+ For a broad introduction to routing and archiving, see [Mail Manager – Amazon SES introduces new email routing and archiving features](https://aws.amazon.com/blogs/messaging-and-targeting/mail-manager-amazon-ses-introduces-new-email-routing-and-archiving-features/) on the AWS Messaging Blog.
+ For inbound delivery to hosted mailboxes, see [How to use SES Mail Manager SMTP Relay action to deliver inbound email to Google Workspace and Microsoft 365](https://aws.amazon.com/blogs/messaging-and-targeting/how-to-use-ses-mail-manager-smtp-relay-action-to-deliver-inbound-email-to-google-workspace-and-microsoft-365/) on the AWS Messaging Blog.
+ For outbound filtering, security scanning, archiving, and delivery, see [Streamlining outbound emails with Amazon SES Mail Manager](https://aws.amazon.com/blogs/messaging-and-targeting/streamlining-outbound-emails-with-amazon-ses-mail-manager/) on the AWS Messaging Blog.
+ For email security patterns, see [How Amazon SES Mail Manager Elevates Email Security and Efficiency](https://aws.amazon.com/blogs/messaging-and-targeting/how-amazon-ses-mail-manager-elevates-email-security-and-efficiency/) on the AWS Messaging Blog.
+ For a multi-tenant document-intake application, see [Build an AI email pipeline with Amazon Bedrock and SES Mail Manager](https://aws.amazon.com/blogs/messaging-and-targeting/build-an-ai-email-pipeline-with-amazon-bedrock-and-ses-mail-manager/) on the AWS Messaging Blog.

## Getting started with Mail Manager using the SES console
<a name="eb-get-started-console"></a>

A complete flow uses a traffic policy to control which SMTP connections and envelope recipients to accept, a rule set to process accepted email, and an ingress point to receive the connection and apply both resources. The following procedure creates these resources in the order required by the console workflow.

### Meeting Mail Manager prerequisites
<a name="eb-get-started-console-prerequisites"></a>

Before you begin, make sure that you meet the following prerequisites.
+ You need an AWS account.
+ The AWS Identity and Access Management (IAM) user or role that you use must have permission to create and manage Mail Manager traffic policies, rule sets, and ingress points. For more information about access to SES, see [Identity and access management in Amazon SES](control-user-access.md).

### Creating an Mail Manager flow
<a name="eb-get-started-console-create-flow"></a>

**To get started with Mail Manager using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation panel, choose **Mail Manager** and choose any of the **Get started with Mail Manager** buttons on the **Mail Manager overview** page.

1. On the **Get set up** page, choose **Create traffic policy** on the **Create a traffic policy** card.

   1. Complete the workflow on the **Create a traffic policy** page. For more information about creating a traffic policy, see [Creating traffic policies and policy statements in the SES console](eb-filters.md#eb-filters-create-console).

   1. After creating your first traffic policy and policy statements, use your browser's back button to return to the **Get set up** page or choose **Get set up** under **Mail Manager** in the left navigation panel.

1. On the **Get set up** page, choose **Create rule set** on the **Create a rule set** card.

   1. Complete the workflow on the **Create a rule set** page. For more information about creating a rule set, see [Create and manage rule sets in the SES console](eb-rules-setup.md#eb-rules-create-console).

   1. After creating your first rule set and rules, use your browser's back button to return to the **Get set up** page or choose **Get set up** under **Mail Manager** in the left navigation panel.

1. After you create the traffic policy and rule set, return to the **Get set up** page. Choose **Create ingress endpoint** on the **Create an ingress endpoint** card.

   1. On the **Email ingress endpoint** page, assign the traffic policy and rule set that you created. For more information about creating an ingress point, see [Creating and managing ingress points](eb-ingress.md#eb-ingress-create-console).

After the ingress point becomes active, the flow can receive email subject to its assigned traffic policy and rule set. For more information about provisioning status and endpoint configuration, see [Creating and managing ingress points](eb-ingress.md#eb-ingress-create-console). To verify the flow, send an email from the configured source to an accepted recipient. Then confirm that the expected rule actions completed by checking the configured destination, archive, application, or logs.

Create additional ingress points when inbound or outbound flows need different sources, authentication requirements, accepted recipients, processing actions, destinations, or operational owners.

### Cleaning up Mail Manager resources
<a name="eb-get-started-console-clean-up"></a>

**Important**
Processing email with Mail Manager can incur charges. To avoid unintended email processing and related charges, delete the resources that you created when you no longer need the flow. For current pricing, see [Amazon SES pricing](https://aws.amazon.com/ses/pricing/) on the AWS website.

**To delete the resources created in this tutorial**

1. Delete the ingress point first. For instructions on deleting an ingress point, see [Creating and managing ingress points](eb-ingress.md#eb-ingress-create-console).

1. Delete the traffic policy if no other ingress point uses it. For instructions on deleting a traffic policy, see [Creating traffic policies and policy statements in the SES console](eb-filters.md#eb-filters-create-console).

1. Delete the rule set if no other ingress point uses it. For instructions on deleting a rule set, see [Create and manage rule sets in the SES console](eb-rules-setup.md#eb-rules-create-console).

### Next steps
<a name="eb-get-started-console-next-steps"></a>

Use the following topics to extend the flow for your requirements.
+ For more information about common flow patterns and their detailed guidance, see [Choosing a Mail Manager use case](#eb-getting-started-use-cases).
+ For more information about adding sender-reputation and content-security checks, see [Email Add Ons](eb-addons.md).
+ For more information about retaining and searching email, see [Email archiving](eb-archiving.md).
