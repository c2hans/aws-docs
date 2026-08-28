---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/batch-remediate-backlog.html
---

# Batch remediate a backlog of findings using the API
<a name="batch-remediate-backlog"></a>

The Web UI and the AWS Security Hub CSPM custom action are convenient for remediating a small number of findings interactively. To work through a large backlog of existing findings programmatically — for example, immediately after deploying the solution — call the solution’s REST API directly.

The same REST API that backs the Web UI (named **AutomatedSecurityResponseApi** in the API Gateway console) exposes a `POST /findings/action` endpoint that accepts a batch of findings to remediate in a single request. This lets you script remediation of a backlog rather than selecting findings by hand.

**Note**
This endpoint is available only when the Web UI is enabled (deploy the Admin stack with `ShouldDeployWebUI` set to "yes"). You can find the API’s invoke URL for the `prod` stage in the API Gateway console for the **AutomatedSecurityResponseApi** API.

## Authenticate
<a name="batch-remediate-authenticate"></a>

All API requests require an Amazon Cognito access token issued for the solution’s user pool, passed in the `Authorization` header as a bearer token. The token must carry the `asr-api/api` scope. Use a token for one of the solution’s roles (Admin, Delegated Admin, or Account Operator); the same role-based authorization that applies in the Web UI applies to the API. For unattended automation, obtain a token using the machine-to-machine (client credentials) OAuth flow rather than an interactive user sign-in.

## Collect the findings to remediate
<a name="batch-remediate-collect"></a>

Use `POST /findings` to search and page through the findings you want to remediate, and collect the `findingId` of each. The findings returned are scoped to the accounts your role is authorized for, so an Account Operator receives only findings for their assigned accounts.

## Call the findings action endpoint
<a name="batch-remediate-call"></a>

Send the collected finding IDs to `POST /findings/action` with an `actionType` of `Remediate`. Each finding is routed through the Orchestrator exactly as it would be from the Web UI.

```
POST /findings/action
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "actionType": "Remediate",
  "findingIds": [
    "arn:aws:securityhub:us-east-1:111111111111:security-control/Lambda.1/finding/...",
    "arn:aws:securityhub:us-east-1:111111111111:security-control/S3.5/finding/..."
  ]
}
```

 `actionType` also accepts `RemediateAndGenerateTicket` (remediate and open a ticket in your configured ticketing channel), and `Suppress` / `Unsuppress` to change a finding’s Security Hub workflow status. A `Remediate` or `RemediateAndGenerateTicket` request returns HTTP `202` with a body of `{"status": "IN_PROGRESS"}`; `Suppress` and `Unsuppress` return HTTP `200`.

**Important**
Send at most **50 finding IDs per request**. To remediate a larger backlog, split the finding IDs into batches of 50 or fewer and issue one request per batch. The API is also protected by rate-based rules (see the AWS WAF configuration in [API Gateway Security Policy](security.md#api-gateway-security-policy)), so pace successive batches rather than sending them all at once.

## Monitor progress
<a name="batch-remediate-monitor"></a>

Remediations initiated through the API run asynchronously, just like those started from the Web UI. Track their progress on the **Execution History** page of the Web UI, through the solution’s Amazon SNS notifications, or by querying `POST /remediations`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
