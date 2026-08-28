---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/m2m-api-access.html
---

# Using the ASR API programmatically
<a name="m2m-api-access"></a>

If you want to integrate ASR into your own systems for example, a security orchestration platform, a ticketing or ChatOps workflow, or a custom dashboard — and drive remediations from there instead of the Web UI, you can call the Automated Security Response on AWS (ASR) API directly. With the ASR API, you can automate and monitor remediations from tooling you already operate.

To do this, use a machine-to-machine (M2M) client with the OAuth 2.0 `client_credentials` grant. When the Web UI is enabled, the solution provisions the Amazon Cognito OAuth scope `asr-api/full-access`. This scope grants the client access to the ASR API. You create the M2M app client yourself after deployment. The solution does not create one, so no machine credential exists until you opt in.

A token with the `asr-api/full-access` scope has **Full Access** — the same capability as the solution administrator role, including the ability to manage other users. Treat the credentials with the same care as administrator sign-in credentials.

**Prerequisites**
Deploy the ASR administrator stack with the Web UI enabled (`ShouldDeployWebUI=yes`, the default). This creates the Amazon Cognito user pool, the API, and the `asr-api/full-access` scope. You also need:
AWS CLI v2 authenticated to the ASR administrator account
 `curl` and `jq` for the token and API examples below

## Step 1: Create the M2M app client after deployment
<a name="m2m-create-client"></a>

Find the user pool id in the administrator stack’s `UserPoolId` **Output**, then create a confidential client granted **both** required OAuth 2.0 scopes — `asr-api/api` (Amazon API Gateway requires this scope to admit the request to the API) and `asr-api/full-access` (the backend authorizes Full Access on this scope). A client granted only `asr-api/api` reaches the API but receives a `403` rejection, because the backend treats it as an unprivileged machine token.

```
export AWS_REGION="us-east-1"
export STACK_NAME="<ASR-administrator-stack-name>"

export USER_POOL_ID="$(aws cloudformation describe-stacks \
  --stack-name "$STACK_NAME" --region "$AWS_REGION" \
  --query "Stacks[0].Outputs[?OutputKey=='UserPoolId'].OutputValue" --output text)"

CREATE_OUT="$(aws cognito-idp create-user-pool-client \
  --user-pool-id "$USER_POOL_ID" --region "$AWS_REGION" \
  --client-name "ASR-M2M-FullAccess" \
  --generate-secret \
  --allowed-o-auth-flows client_credentials \
  --allowed-o-auth-flows-user-pool-client \
  --allowed-o-auth-scopes "asr-api/api" "asr-api/full-access" \
  --output json)"

export M2M_CLIENT_ID="$(echo "$CREATE_OUT" | jq -r '.UserPoolClient.ClientId')"
export CLIENT_SECRET="$(echo "$CREATE_OUT" | jq -r '.UserPoolClient.ClientSecret')"
```

The response contains `UserPoolClient.ClientId` and `UserPoolClient.ClientSecret`. **Cognito shows you the secret value only once.** Cognito requires the secret to be generated when the client is created (`--generate-secret`); there is no command to add a secret to an existing client later.

## Step 2: Store the secret in your own secret store
<a name="m2m-store-secret"></a>

 **The solution never stores this secret.** It is intentionally kept out of AWS CloudFormation outputs and template state. You are responsible for capturing the returned client secret and storing it securely in your own secret store — for example AWS Secrets Manager, AWS Systems Manager Parameter Store (Secure String), or your organization’s vault.
+ Store the secret immediately; you cannot retrieve it again later.
+ Restrict read access to the integration that needs it.
+ Anyone who holds this secret can obtain Full Access tokens for ASR, so guard it accordingly.

## Step 3: Retrieve an access token (client\_credentials flow)
<a name="m2m-get-token"></a>

The token endpoint is derived from the user pool’s hosted domain. Request a token using HTTP Basic auth (`client_id:client_secret`), the `client_credentials` grant, and both scopes:

```
export DOMAIN_PREFIX="$(aws cognito-idp describe-user-pool \
  --user-pool-id "$USER_POOL_ID" --region "$AWS_REGION" \
  --query "UserPool.Domain" --output text)"
export TOKEN_URL="https://${DOMAIN_PREFIX}.auth.${AWS_REGION}.amazoncognito.com/oauth2/token"

export ACCESS_TOKEN="$(curl -s -X POST "$TOKEN_URL" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "${M2M_CLIENT_ID}:${CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=asr-api/api asr-api/full-access" \
  | jq -r '.access_token')"
```

Access tokens are valid for **1 hour**, and the `client_credentials` grant does not issue a refresh token. **Cache and reuse a token for the duration of its validity** rather than requesting a new one for every API call. Request a new token shortly before the current one expires — for example, one to two minutes before the 1-hour mark — using the credentials you already hold.

Caching the token keeps your integration within the Cognito token endpoint rate limits and reduces cost. A correctly caching integration needs only about one token request per hour. Requesting a new token for every API call is slower and unnecessarily costly.

## Step 4: Call the ASR API
<a name="m2m-call-api"></a>

Send the access token as a `Authorization: Bearer <access_token>` header on any ASR API path. API Gateway validates the token and the `asr-api/api` scope before the request reaches the backend, and the backend grants Full Access on the `asr-api/full-access` scope:

```
# Find the API base URL in the administrator stack's APIEndpoint Output, then
# call an endpoint your integration uses.
curl -s -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  "https://<api-id>.execute-api.${AWS_REGION}.amazonaws.com/prod/<endpoint>"
```

You do not need additional network or firewall configuration for programmatic callers. The API’s AWS WAF protections already admit authenticated machine clients (non-browser user agents from cloud IP ranges) while blocking abusive traffic. Machine activity is attributed to the client ID in the ASR API logs, and AWS CloudTrail records every token issuance.

## Step 5: Rotate or disable the client
<a name="m2m-rotate-disable"></a>

Because a secret cannot be added, replaced, or removed on an existing Cognito app client, rotation and disablement operate on the **client** itself:
+  **Rotate:** create a second M2M client (repeat Step 1 with a different `--client-name`), migrate your integration to its credentials, confirm it can obtain tokens, then delete the old client.
+  **Disable:** delete the client to immediately revoke machine access.

```
aws cognito-idp delete-user-pool-client \
  --user-pool-id "$USER_POOL_ID" \
  --client-id "$M2M_CLIENT_ID" \
  --region "$AWS_REGION"
```

## Detect denied machine tokens (optional)
<a name="m2m-denied-tokens"></a>

When Amazon CloudWatch alarms are enabled, ASR ships an opt-in alarm (`ASR-Cognito-M2MForbidden`) on the `ASR/M2MForbiddenAuthorization` metric. The API AWS Lambda function emits this metric whenever a machine token is denied for lacking the `asr-api/full-access` scope — a non-zero count signals a misconfigured client or probing. The alarm uses ASR’s shared SNS alarm topic, which has no subscriber by default; subscribe a channel to be notified.

## Enable Amazon Cognito logging and threat protection
<a name="m2m-cognito-logging"></a>

We recommend that you enable native log delivery and Advanced Security on the ASR user pool for visibility into authentication activity.

### Amazon Cognito native log delivery
<a name="amazon-cognito-native-log-delivery"></a>

With this option, you can deliver sign-in and token events to Amazon CloudWatch Logs. In the [Amazon Cognito console]({console-url}cognito/), open your user pool and choose **Logging**. Enable log delivery to a CloudWatch Logs log group. Set the log level to `ERROR` or `INFO` depending on how much detail you need.

Amazon Cognito records token issuance in [AWS CloudTrail]({docs-url}cognito/latest/developerguide/logging-using-cloudtrail.html). To retain and query these audit records in Amazon CloudWatch Logs, configure a management-event CloudTrail trail in the account that owns the user pool. Configure the trail to deliver logs to a CloudWatch Logs log group. For more information, see [Monitoring CloudTrail Log Files with Amazon CloudWatch Logs]({docs-url}awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html).

### Amazon Cognito Advanced Security and threat protection
<a name="amazon-cognito-advanced-security-and-threat-protection"></a>

With this option, you get compromised-credential detection and risk-based adaptive authentication. In the [Amazon Cognito console]({console-url}cognito/), open your user pool, choose **Advanced Security**, and set the mode to **Enforced**.

**Additional cost**
If you enable Advanced Security, you incur additional per-authentication charges. For more information about Amazon Cognito pricing, see [Amazon Cognito pricing]({aws-url}/cognito/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
