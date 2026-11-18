---
source_url: https://docs.aws.amazon.com/connecthealth/latest/userguide/contact-flow-setup.html
---

# Sample contact flow
<a name="contact-flow-setup"></a>

Amazon Connect Health provides a pre-built sample contact flow that routes patient calls to your agent. You can use it to test the agentic capabilities for patient access end to end before you move to production.

The sample flow is deployed automatically at domain creation, whether Amazon Connect Health creates a new Amazon Connect Customer instance or you use an existing one.

## Locate the sample flow
<a name="cf-locate-flow"></a>

To find the sample contact flow:

1. Sign in to your Amazon Connect Customer instance.

1. In the navigation pane, choose **Routing**, then choose **Contact flows**.

1. Search for `connect-health-{DOMAIN_ID}-a2a-inbound-flow-{SUFFIX}`, where `{DOMAIN_ID}` is your Amazon Connect Health domain identifier and `{SUFFIX}` is a unique suffix. For example, `connect-health-dom-a3t6x2l74w8wygb6ezd6h-a2a-inbound-flow-b4a9b035`.

You can assign this flow to your preferred phone number if the provisioned number doesn’t fit your workflows.

The following image shows the sample inbound contact flow in the Amazon Connect Customer flow designer.

![Sample inbound contact flow in the Amazon Connect Customer flow designer](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/sample-contact-flow-a2a.png)

## Provisioned resources
<a name="cf-provisioned-resources"></a>

Amazon Connect Health provisions the following resources as part of the sample contact flow deployment. Each resource name ends with a unique suffix.

| Resource | Naming pattern |
| --- | --- |
| Amazon Connect Customer instance (if created by Amazon Connect Health) |  `connect-health-{DOMAIN_ID}`  |
| Sample contact flow (handles inbound calls) |  `connect-health-{DOMAIN_ID}-a2a-inbound-flow-{SUFFIX}`  |
| Show view flow (shows the escalation view to the staff member) |  `connect-health-{DOMAIN_ID}-a2a-show-view-flow-{SUFFIX}`  |
| Lambda function |  `connect-health-{DOMAIN_ID}-lambda`  |
| Lambda function role |  `connect-health-{DOMAIN_ID}-lambda-role`  |
| Amazon Lex bot |  `connect-health-{DOMAIN_ID}-bot`  |
| Amazon Lex bot role |  `connect-health-{DOMAIN_ID}-lex-bot-role`  |

## Contact attributes and handoff context
<a name="cf-contact-attributes-and-handoff-context"></a>

Contact attributes are key-value pairs that the contact flow sets during a call. The sample flow uses them to start the agent and to look up the handoff context when a call escalates.

When the agent escalates a call, the staff member sees the escalation context in the agent workspace view. The `connect-health-{DOMAIN_ID}-a2a-show-view-flow-{SUFFIX}` flow shows this view. The view looks up the session through the `connect-health-session-id` contact attribute. The context includes the following:
+ Verification status
+ Matched patient
+ Intent
+ Selected provider
+ Location and date
+ Insurance and copay result
+ Escalation reason

Patient details appear in the view only after you sync your EHR integration on the **Home** page of the patient engagement web app.

The sample contact flow sets the following contact attributes:
+  `connect-health-front-desk-agent-id` – The identifier of the agent that handles the call.
+  `connect-health-appointment-type-id` – The appointment type that the agent uses for scheduling. The default is `1004`.
+  `connect-health-appointment-type-kind` – Whether the appointment type ID is `External` or `Internal`. The default is `External`.

To view or change these attributes, open the sample flow in the Amazon Connect Customer flow editor and choose the **Set contact attributes** block.

## Appointment type
<a name="cf-appointment-type"></a>

The flow sets the example visit type ID `1004` in the `connect-health-appointment-type-id` contact attribute. Replace it with the Epic visit type ID that your organization uses.

## Amazon Lex bot
<a name="cf-lex-bot"></a>

The Amazon Lex bot for Amazon Q in Connect connects the call’s audio to the agent. The agent handles language understanding, the greeting, and intent routing.

## Customize the contact flow
<a name="cf-customization"></a>

Amazon Connect Health provisions a sample Amazon Connect Customer contact flow that demonstrates how Amazon Connect Health agents are invoked within a call routing sequence, but it is intentionally generic. Customize the sample contact flow to align with your operational processes, queue structures, escalation policies, and patient communication standards (including privacy and consent practices) before production deployment.

**Important**
When you customize the sample flow, keep the following parts of it. Otherwise, the agent can’t run or staff can’t see the handoff context.
The **Set contact attributes** block that sets the agent ID and appointment type attributes
The tool outcome check after the agent block
The show-view event hook that shows the handoff context to staff
Don’t route the flow back into the agent block.

Customization typically includes the following tasks:
+  **Queue assignments and routing profiles** – Reassign contact flow branches to your existing queues and agent routing profiles configured in your Amazon Connect Customer instance.
+  **Call flow logic** – Update branching conditions and agent handoff sequences to reflect your department processes.
+  **IVR integration** – Integrate the sample flow with your existing interactive voice response (IVR) menus or self-service flows so that Amazon Connect Health agents are reachable within your broader telephony environment.
+  **Localization** – Replace default audio with organization-approved recordings or text-to-speech content that reflects your communication standards.

For guidance on building and modifying contact flows, see [Use the flow designer in Amazon Connect Customer to create flows](https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html) in the *Amazon Connect Customer Administrator Guide*.
