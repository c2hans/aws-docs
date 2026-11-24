---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/autofill-guides.html
---

# Automatically fill step-by-step guides using AI agents

AI agents can fill in fields in a step-by-step guide during a contact and during after contact work. The AI agent reasons over the conversation and suggests values for fields in a view. The agent reviews the values, edits them if needed, and continues to the next step of the guide.

To fill fields during after contact work using conversational analytics instead, see [Prefill guides for after contact work](integrate-views-conversational-analytics.md).

Automatic form population is only supported for voice and chat contacts. Email and task contacts aren't supported.

## Prerequisites
<a name="autofill-guides-prerequisites"></a>
+ Agent assist set up for your instance. For more information, see [Initial set-up for AI agents](ai-agent-initial-setup.md).
+ A step-by-step guide that includes a custom view, shown to agents with a **Show view** block. For more information, see [Use step-by-step guides](use-step-by-step-guides.md).
+ The **Connect assistant - View** security profile permission for your agents.
+ One of the following security profile permissions for your agents:

<table>
<thead>
  <tr><th>Permission</th><th>Enables autofill in</th></tr>
</thead>
<tbody>
  <tr><td><b>Auto form population - custom views</b></td><td>Step-by-step guides</td></tr>
  <tr><td><b>Auto form population - all supported applications</b></td><td>Every supported application, including step-by-step guides</td></tr>
</tbody>
</table>

## Step 1: Turn on autofill for fields in the view
<a name="autofill-guides-step1"></a>

1. Open your view in the UI builder.

1. Choose a form component. These components support autofill: **Text Input**, **Text Area**, **Dropdown**, **Checkbox Group**, **Radio Group**, **Date Picker**, **Time Picker**, and **Toggle**.

1. In the **Customize** panel, on the **Properties** tab, under **AI Assisted Autofill**, configure the following:

<table>
<thead>
  <tr><th>Setting</th><th>Default</th><th>What it does</th></tr>
</thead>
<tbody>
  <tr><td><b>AI Assisted Autofill</b></td><td>On</td><td>Lets the AI agent fill this field.</td></tr>
  <tr><td><b>Field definition</b></td><td>Empty</td><td>Describes what the field holds, in up to 500 characters. For example: "The customer's order number, 8 digits." Specific definitions produce more accurate values.</td></tr>
  <tr><td><b>Auto accept inputs</b></td><td>On</td><td>Fills the field without asking the agent to accept the value. The agent can still edit it. Turn this off to have agents accept or reject each value.</td></tr>
</tbody>
</table>

   The following image shows the settings for an **Order number** field. The field definition describes the format of an order number.
![The UI builder with an Order number field selected. The Properties tab of the Customize panel shows AI Assisted Autofill turned on, a field definition for the order number, and Auto accept inputs turned on.](https://docs.aws.amazon.com/connect/latest/adminguide/images/autofill-guides-view-config.png)

1. Repeat for each field. Autofill is on by default for every new form component, so turn it off for fields the AI agent shouldn't fill.

1. Save and publish the view.

## Step 2: Set up the flow
<a name="autofill-guides-step2"></a>

Autofill needs an AI agent session and a live transcript on the contact. Set both up in the flow the contact enters before it reaches an agent.

1. Open the flow.

1. Add a **Connect assistant** block, and choose your AI agent for agent assist. For more information, see [Connect assistant](connect-assistant-block.md).

1. Add a **Set recording, analytics, and processing behavior** block, and turn on real-time conversational analytics for the channel. For more information, see [Set recording and analytics behavior](set-recording-behavior.md).

1. Save and publish the flow.

## What agents see
<a name="autofill-guides-agents"></a>

When the guide opens, an **AI Assisted Form Population** header appears above the view. The header has two controls:
+ **Regenerate form population**: asks the AI agent to fill the fields again from the latest conversation. Agents wait a short time between regenerations.
+ **Autofill on**: a toggle that turns autofill on or off for the form.

The following image shows a guide at the start of a call. The customer hasn't given any order details yet, so both fields show **Not enough info**.

![A guide in the agent workspace during a voice call, with the AI Assisted Form Population header above an order form. The Category and Order number fields both show Not enough info.](https://docs.aws.amazon.com/connect/latest/adminguide/images/autofill-guides-agent-start.png)

Each field shows its status:

| Field label | Meaning |
| --- | --- |
| Generating… | The AI agent is reasoning over the value to populate. |
| Suggestion | The AI agent has a value. If Auto accept inputs is off, the agent accepts or rejects it. |
| (Value filled in) | Auto accept inputs is on, so the value went straight into the field. |
| Not enough info | The conversation hasn't covered this field yet. The agent can choose Regenerate form population later. |
| Suggested value couldn't be applied | The value didn't fit the field, such as a date in the wrong format. |
| Please confirm this field before saving | The agent tried to save before reviewing a suggestion. |

The following image shows the same form a few seconds later. The **Category** field has a suggestion for the agent to accept or reject. The **Order number** field has **Auto accept inputs** turned on, so the value is already filled in.

![The order form after autofill. The Category field shows a suggested value of Smart Home, with accept and reject icons. The Order number field is filled in with 1234-ABCD-N550.](https://docs.aws.amazon.com/connect/latest/adminguide/images/autofill-guides-agent-suggestion.png)

To see why the AI agent chose a value, the agent chooses the info icon on the field. A pop-up shows the AI agent's reasoning. The pop-up is titled **New suggestion reasoning** for a suggestion and **Applied input reasoning** for a value that the AI agent filled in automatically.

The following image shows the reasoning for a suggestion.

![The New suggestion reasoning pop-up for the Category field. The reasoning states that the agent and customer both mentioned a smart home product.](https://docs.aws.amazon.com/connect/latest/adminguide/images/autofill-guides-agent-suggestion-reasoning.png)

The following image shows the reasoning for a value the AI agent filled in automatically.

![The Applied input reasoning pop-up for the Order number field. The customer stated the order number, and the AI agent formatted it with dashes and capital letters.](https://docs.aws.amazon.com/connect/latest/adminguide/images/autofill-guides-agent-applied-reasoning.png)

## Troubleshooting
<a name="autofill-guides-troubleshooting"></a>

| Problem | Cause |
| --- | --- |
| The header doesn't appear. | The agent's security profile lacks Connect assistant - View or an autofill permission, or the contact is an email or task. |
| The header doesn't appear, and permissions are set. | The flow has no Connect assistant block, so the contact has no AI agent session. |
| Every field shows Not enough info. | The customer hasn't given enough detail yet, or the contact has no transcript. Check that real-time conversational analytics is on in the flow. |
