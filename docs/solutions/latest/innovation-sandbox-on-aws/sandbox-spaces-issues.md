---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/sandbox-spaces-issues.html
---

# Sandbox Spaces issues

If you have problems with Sandbox Spaces, first check that Sandbox Spaces is turned on in **Settings** and on the lease, and that the lease is **Active**. The web UI shows the reason for most errors in the Sandbox Space itself. The following sections describe the causes that need action from you.

## Administrator can’t turn on Sandbox Spaces
<a name="sandbox-spaces-cannot-turn-on"></a>

The **Settings** page rejects **Enable Sandbox Spaces** in either of the following cases:
+ No model is enabled. Choose **Add models** in the **Sandbox Spaces** section, enable at least one model, and then turn on the setting. For more information, refer to [Managing Sandbox Spaces](administrator-guide.md#manage-sandbox-spaces).
+ The Region where the solution is deployed isn’t one of the managed Regions. Add the Region to **ISB Managed Regions** on the AccountPool stack, and then turn on the setting. For more information, refer to [Update managed Regions](step1-deploy-accountpool-stack.md#update-managed-regions).

## A user can’t open a Sandbox Space
<a name="sandbox-spaces-cannot-open"></a>

The **Open Space** button is missing or unavailable when any of the following is true:
+ The lease isn’t in the **Active** state. Check the status of the lease on the **Leases** page. For the list of statuses, refer to [Lease states in Innovation Sandbox](manager-guide.md#understand-lease-states).
  +  **Pending Approval** or **Provisioning**: Ask the user to wait until the lease becomes **Active**. Don’t request another lease, because that creates a second request for the same work.
  +  **Frozen**: Unfreeze the lease. For more information, refer to [Unfreezing a lease](troubleshooting.md#unfreezing-a-lease).
  + The lease has ended, for example **Lease Duration Expired**, **Lease Manually Terminated**, or **Terminated by User**: Ask the user to request a new lease.
+ Sandbox Spaces is turned off for the lease, the lease template, or the whole deployment. A template or lease that has it turned on while the deployment setting is off shows **Disabled (overridden)**. Turn on the setting in **Settings**, or edit the lease. For more information, refer to [Editing Sandbox Spaces settings on lease templates and leases](manager-guide.md#manage-lease-sandbox-spaces).
+ The user has access to the lease only through a group. Only the lease owner and users who were added to the lease individually can open its Sandbox Space. Add the user to the lease as an individual user. For more information, refer to [Sharing a lease with additional users and groups](manager-guide.md#lease-sharing).
+ No enabled model is available for the lease. Enable a model in **Settings**. If the lease or its template limits the models, edit the list so that it includes at least one enabled model.

## The agent rejects a user’s messages because of permissions
<a name="sandbox-spaces-permission-errors"></a>

The agent runs commands with the permission set that is assigned to the user on the lease. It rejects the user’s messages when it can’t use that permission set:
+  **No permission set is assigned.** The user has no assignment on the lease, or the assigned permission set grants no permissions. Open the **Assignments** tab of the lease, assign a permission set to the user, and wait for the assignment to show **Active**.
+  **The permission set has a permissions boundary.** Sandbox Spaces doesn’t support permission sets that have a permissions boundary, whether AWS managed or customer managed. The user keeps normal IAM Identity Center access to the account. Change the user’s assignment to a permission set without a permissions boundary. The lease must allow that permission set. For more information, refer to [Creating lease templates](manager-guide.md#creating-lease-templates).
+  **The permission set is too large.** The agent can’t use a permission set that has more than 10 managed policies attached or an inline policy of more than 1,648 characters as compact JSON. The user sees a message that the agent couldn’t determine their permissions, and trying again doesn’t help. Reduce the number of attached policies or inline statements, or assign a smaller permission set.

## Replies in a chat are stopped by the model’s content filter
<a name="sandbox-spaces-content-filter-lock"></a>

The page shows a **Content filter stopped the reply** error. With some models, the content filter can keep stopping replies after the first one, even for harmless messages, and reloading the page doesn’t help. This is separate from the guardrail of the solution, which blocks a single message. For more information, see [A message is blocked by the safety filter](#sandbox-spaces-blocked-message).

To continue, choose a different model from the model selector in the Sandbox Space, and then send your message again. If the error says that commands may already have run, check their results first.

## A message is blocked by the safety filter
<a name="sandbox-spaces-blocked-message"></a>

A request fails at once and the page shows a **Safety filter blocked the message** error, while the same request worded more plainly works. For example, adding "go ahead without asking" to a request to create a resource can get the message blocked. The Amazon Bedrock guardrail of the solution screens each message for prompt attacks. A sentence that tells the assistant how to behave can be read as an attempt to override it. The guardrail blocks only that message. The message isn’t stored, so it doesn’t affect later messages.

To continue, rephrase the message as a plain request, without instructions about how the assistant should behave, and then send it again.

## A model is missing, or a model doesn’t respond
<a name="sandbox-spaces-model-issues"></a>

 **A model doesn’t appear on the Add Sandbox Spaces models page.** The page lists only models that meet the Sandbox Spaces eligibility requirements: the model accepts text input, produces text output (not speech), supports response streaming, and has an **Active** Amazon Bedrock lifecycle status. A foundation model must support on-demand inference, and an inference profile must be a system-defined profile with an **Active** status whose models all meet the same requirements. Choose the refresh button to reload the list. If a model still doesn’t appear, it doesn’t meet the requirements, and you can’t enable it. A listed model that shows **Price unavailable** has no price and can’t be enabled. Choose a different model.

 **A model that uses an inference profile fails.** The Region Limit SCP blocks cross-Region inference when the `BedrockInferenceProfilePatterns` parameter on the AccountPool stack is empty or doesn’t match the profile. The parameter allows all profiles by default, so check whether someone cleared it or narrowed it. Update the AccountPool stack so that the parameter matches the profile, and then try again. For more information, refer to [Managing Sandbox Spaces](administrator-guide.md#manage-sandbox-spaces).

 **A model stops responding or can’t be used.** Amazon Bedrock can retire a model, or the sandbox account might not have access to it. Ask the user to choose a different model in the Sandbox Space. Disable the model in **Settings** so that other users don’t choose it. If a model describes actions in its replies without running them, try a different model.

## A request is rejected because the agent is already working
<a name="sandbox-spaces-turn-in-progress"></a>

A Sandbox Space runs one request at a time. The agent rejects a new message while it is still working on an earlier one, including a message that was sent from another browser tab or device. Wait for the first response to finish, and use a single browser tab for each Sandbox Space.

## A long-running request stops
<a name="sandbox-spaces-long-running"></a>

The agent stops a request that runs for too long, and some of its actions might have run already:
+ The agent stops after 25 steps in one reply. It tells the user that the request needed more steps and that the commands it ran have taken effect. Ask the user to review what changed, and then ask the agent to continue or to split the task into smaller parts.
+ The request runs out of time. The Worker Lambda function that handles requests has a 15-minute time limit. When a request reaches it, the user sees a message that the request reached its processing time limit and that some actions might have completed or might still be in progress. Ask the user to check the status of the resources in the account before sending the request again, and to break large tasks into smaller requests.
+ A single AWS CLI command that runs longer than two minutes times out. Ask the user to run it in smaller parts, or to check the result in the console.

## Responses are slow when many users chat at the same time
<a name="sandbox-spaces-slow-responses"></a>

The solution processes up to 10 Sandbox Spaces requests at the same time across all users, and Lambda throttles requests beyond that. A throttled message returns to the queue and isn’t retried until the visibility timeout of about 16 minutes passes, so a user can wait a long time. After three failed attempts, the message moves to the dead-letter queue and the agent doesn’t answer it. If users report long waits or no answer, check the **Sandbox Spaces message DLQ** alarm in [Alarms deployed by the solution](monitoring-alarms.md#solution-alarms), and review the throttles and logs of the Worker Lambda function in the **Compute-ISBLogGroup** log group. Ask the affected users to send their messages again.
