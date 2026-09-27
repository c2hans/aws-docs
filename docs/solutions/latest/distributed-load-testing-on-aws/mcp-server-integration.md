---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/mcp-server-integration.html
---

# MCP Server integration
<a name="mcp-server-integration"></a>

If you deployed the optional MCP Server component during solution deployment, you can integrate the Distributed Load Testing solution with AI development tools that support the Model Context Protocol. The MCP Server provides programmatic access to retrieve, manage, and analyze load tests through AI assistants.

You can connect to the DLT MCP Server using the client of your choice (Kiro CLI, Claude, and so on), which each have slightly different configuration instructions. This section provides setup instructions for MCP Inspector, Kiro CLI, Cline, and Amazon Quick.

## Step 1: Get MCP endpoint and access token
<a name="get-mcp-credentials"></a>

Before configuring any MCP client, you need to retrieve your MCP Server endpoint and access token from the DLT web console.

1. Navigate to the **MCP Server** page in the Distributed Load Testing web console.

1. Locate the **MCP Server Endpoint** section.

1. Copy the endpoint URL using the **Copy Endpoint URL** button. The endpoint URL follows the format: `https://{gateway-id}.gateway.bedrock-agentcore.{region}.amazonaws.com/mcp`

1. Locate the **Access Token** section.

1. Copy the access token using the **Copy Access Token** button.

**Important**
Keep your access token secure. Don’t share it publicly. By default, the token provides read-only access to your Distributed Load Testing solution through the MCP interface. If the MCP Server is deployed in ReadWrite access mode, the token also permits create, update, and delete operations. For more information, refer to [MCP tools specification](mcp-tools-specification.md) in the Developer Guide.

![MCP Server credentials page showing endpoint and access token](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/mcp-credentials.png)

## Step 2: Test with MCP Inspector
<a name="mcp-inspector-setup"></a>

The Model Context Protocol offers [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector), a tool to directly connect to MCP servers and invoke tools. This provides a convenient UI and sample network requests for testing your MCP Server connection before configuring AI clients.

**Note**
MCP Inspector requires version 0.17 or later. All requests can also be made with JSON RPC directly, but MCP Inspector provides a more user-friendly interface.

 **Install and launch MCP Inspector**

1. Install npm if necessary.

1. Run the following command to launch MCP Inspector:

   ```
   npx @modelcontextprotocol/inspector
   ```

 **Configure the connection**

1. In the MCP Inspector interface, enter your MCP Server Endpoint URL.

1. Add an Authorization header with your access token.

1. Choose **Connect** to establish the connection.

![MCP Inspector configuration screen](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/mcp-inspector-config.png)

 **Invoke tools**

Once connected, you can test the available MCP tools:

1. Browse the list of available tools in the left panel.

1. Select a tool (for example, `list_scenarios`).

1. Provide any required parameters.

1. Choose **Invoke** to run the tool and view the response.

![MCP Inspector showing available tools and invocation](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/mcp-inspector-tools.png)

## Step 3: Configure AI development clients
<a name="configuring-ai-clients"></a>

After verifying your MCP Server connection with MCP Inspector, you can configure your preferred AI development client.

### Kiro CLI
<a name="q-cli-configuration"></a>

Kiro CLI (formerly Amazon Q Developer CLI) provides command-line access to AI-assisted development with MCP Server integration.

 **Configuration steps**

1. Edit the `mcp.json` configuration file. For more information on configuration file location, refer to [Model Context Protocol (MCP)](https://kiro.dev/docs/cli/mcp/) in the *Kiro CLI documentation*.

1. Add your DLT MCP Server configuration:

   ```
   {
     "mcpServers": {
       "dlt-mcp": {
         "type": "http",
         "url": "https://<gateway-id>.gateway.bedrock-agentcore.<region>.amazonaws.com/mcp",
         "headers": {
           "Authorization": "Bearer <access-token>"
         }
       }
     }
   }
   ```

Replace `<gateway-id>` and `<region>` with the values from your MCP Server Endpoint URL, and `<access-token>` with the value you copied in Step 1.

 **Verify the configuration**

1. In a terminal, type `kiro-cli` to launch Kiro CLI.

1. Type `/mcp` to see all available MCP servers.

1. Type `/tools` to see available tools provided by `dlt-mcp` and other configured MCP servers.

1. Verify that `dlt-mcp` successfully initializes.

### Cline
<a name="cline-configuration"></a>

Cline is an AI coding assistant that supports MCP Server integration.

 **Configuration steps**

1. In Cline, navigate to **Manage MCP Servers** > **Configure** > **Configure MCP Servers**.

1. Update the `cline_mcp_settings.json` file:

   ```
   {
     "mcpServers": {
       "dlt-mcp": {
         "type": "streamableHttp",
         "url": "https://<gateway-id>.gateway.bedrock-agentcore.<region>.amazonaws.com/mcp",
         "headers": {
           "Authorization": "Bearer <access-token>"
         }
       }
     }
   }
   ```

   Replace `<gateway-id>` and `<region>` with the values from your MCP Server Endpoint URL, and `<access-token>` with the value you copied in Step 1.

1. Save the configuration file.

1. Restart Cline to apply the changes.

### Amazon Quick
<a name="amazon-q-suite-configuration"></a>

Amazon Quick (formerly Amazon Quick Suite) provides a comprehensive AI assistant platform with support for MCP Server actions.

 **Prerequisites**

Before configuring the MCP Server in Amazon Quick, you need to retrieve OAuth credentials from your DLT deployment’s Cognito user pool:

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Select the Distributed Load Testing stack.

1. In the **Outputs** tab, locate and copy the **Cognito User Pool ID** associated with your DLT deployment.

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/).

1. Select the user pool using the User Pool ID from the CloudFormation outputs.

1. In the left navigation, select **App integration** > **App clients**.

1. Locate the app client with the name ending in `m2m` (machine-to-machine) and select it.

1. On the app client details page, copy the **Client ID**. To reveal the **Client secret**, choose **Show client secret**, then copy the value.

1. Return to the user pool and get the user pool domain from the **Domain** tab.

1. Construct the token endpoint URL by appending `/oauth2/token` to the end of the domain.

 **Configuration steps**

1. In Amazon Quick, create a new agent or select an existing agent.

1. Add an agent prompt that describes how to interact with the DLT MCP Server.

1. Add a new action and select **MCP Server action**.

1. Configure the MCP Server details:
   +  **MCP Server URL**: Your DLT MCP endpoint
   +  **Authentication Type**: Service-based authentication
   +  **Token Endpoint**: Your Cognito token endpoint URL
   +  **Client ID**: The client ID from the m2m app client
   +  **Client Secret**: The client secret from the m2m app client

1. Save the MCP Server action configuration.

1. Add the new MCP Server action to your agent.

 **Launch and test the agent**

1. Launch the agent in Amazon Quick.

1. Start a conversation with the agent using natural language prompts.

1. The agent will use the MCP tools to retrieve and analyze your load testing data.

## Rotate the MCP Server client secret
<a name="rotate-mcp-client-secret"></a>

If you use service-based (machine-to-machine) authentication to connect an MCP client to the solution, you are responsible for rotating the client secret that the client uses.

### Which credential this applies to
<a name="mcp-credential-types"></a>

The solution issues two different MCP credentials. Only one of them requires manual rotation.

| Credential | Used by | Rotation |
| --- | --- | --- |
|  **User access token** — copied from the **MCP Server** page of the web console | MCP Inspector, Kiro CLI, Cline, and other clients that send an `Authorization: Bearer` header | None required. This is a short-lived Amazon Cognito access token that expires approximately one hour after it is issued. To get a new token, return to the **MCP Server** page and copy it again. |
|  **Machine-to-machine client ID and client secret** — retrieved from the Amazon Cognito user pool | Amazon Quick, and any other client configured for service-based authentication |  **Manual rotation required.** The client secret is long-lived and does not expire on its own. |

The remainder of this section applies to the machine-to-machine client secret. The solution creates this credential as an Amazon Cognito app client named ` <stack-name>-userpool-client-m2m` when you deploy with **Deploy Optional MCP Server** set to `Yes`. For retrieval instructions, refer to the prerequisites in [Amazon Quick](#amazon-q-suite-configuration).

**Important**
Treat the client secret as you would any other long-lived credential:
Do not commit it to source control, embed it in application code, or paste it into issue trackers, chat, or documentation.
Do not write it to logs, build output, or CI/CD job output.
Store it in a secrets manager such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), or in the encrypted credential store of the MCP client that consumes it. Do not keep it in a plaintext file.
Grant access to the secret only to those who need it, such as you and the services that consume the secret.

### Recommended rotation cadence
<a name="mcp-secret-rotation-cadence"></a>

Rotate the machine-to-machine client secret at least every 90 days. Rotate immediately, outside of the regular schedule, whenever any of the following occurs:
+ You suspect or confirm that the secret was exposed.
+ An operator with access to the secret leaves the team or changes roles.
+ You retire an MCP client that was configured with the secret.

### Rotate the secret
<a name="mcp-secret-rotation-steps"></a>

An Amazon Cognito app client supports up to two active client secrets at the same time. Rotate by adding a second secret, migrating your MCP clients to it, and then deleting the original — no interruption to MCP access.

The client ID does not change during rotation, so you do not need to update the solution’s AWS CloudFormation stack, the MCP Server endpoint, or the token endpoint. Only the secret value stored in your MCP client changes.

1. Add a second client secret. Amazon Cognito generates the value and returns it in the response.

   ```
   aws cognito-idp add-user-pool-client-secret \
     --user-pool-id <user-pool-id> \
     --client-id <m2m-client-id> \
     --region <region>
   ```
**Important**
Copy the `ClientSecretValue` from the response and store it securely before continuing. Amazon Cognito returns the generated secret value only in this response and never reveals it again — neither `list-user-pool-client-secrets` nor the Amazon Cognito console will display it. If you lose the value, delete the secret and add a new one.

   The original secret remains valid at this point, so any MCP client still configured with it continues to work.

1. Update each MCP client to use the new secret. For Amazon Quick, edit the MCP Server action and replace the **Client Secret** value, leaving **MCP Server URL**, **Token Endpoint**, and **Client ID** unchanged. Save the action.

1. Validate that the new secret issues tokens. Request a client credentials grant from your user pool’s token endpoint.

   ```
   curl -X POST https://<user-pool-domain>/oauth2/token \
     -H 'Content-Type: application/x-www-form-urlencoded' \
     -d 'grant_type=client_credentials' \
     -d 'client_id=<m2m-client-id>' \
     -d 'client_secret=<new-client-secret>' \
     -d 'scope=dlt-mcp-gateway/read'
   ```

   A successful response contains an `access_token` field. Then confirm end-to-end access by invoking an MCP tool from the client you reconfigured — for example, ask the agent to list your test scenarios.

1. List the client’s secrets to identify the original one. Each secret is identified by a `ClientSecretId` in the format ` <client-id>--<epoch-create-time> `. Use the `ClientSecretCreateDate` field to distinguish the original secret from the one you just added.

   ```
   aws cognito-idp list-user-pool-client-secrets \
     --user-pool-id <user-pool-id> \
     --client-id <m2m-client-id> \
     --region <region>
   ```

1. Invalidate the original secret. After this call, Amazon Cognito no longer issues tokens to any client presenting the old secret.

   ```
   aws cognito-idp delete-user-pool-client-secret \
     --user-pool-id <user-pool-id> \
     --client-id <m2m-client-id> \
     --client-secret-id <old-client-secret-id> \
     --region <region>
   ```

**Note**
Two constraints apply when you rotate:
An app client can have a maximum of two secrets. If two already exist, delete the one you no longer need before adding another.
You cannot delete the last remaining secret on an app client.
The `add-user-pool-client-secret` command also accepts an optional `--client-secret` parameter for supplying your own value. If you supply a value, Amazon Cognito does not return it in the response, so you must store it before making the call. We recommend letting Amazon Cognito generate the secret.

### If the secret was exposed
<a name="mcp-secret-exposed"></a>

Rotate using the preceding steps, and complete step 5 (deleting the old secret) as soon as possible rather than waiting for a maintenance window. Then take the following additional actions.
+  **Account for tokens already issued.** Deleting a secret stops Amazon Cognito from issuing new tokens, but access tokens obtained with the exposed secret remain valid until they expire — up to approximately one hour. Deleting the secret does not invalidate them.
+  **Limit what those tokens can do.** If your deployment uses `ReadWrite` access mode, perform an AWS CloudFormation stack update with **MCP Server Access Mode** set to `ReadOnly`. This removes the write tools and restricts the MCP Server Lambda function’s IAM permissions to `GET` requests, so outstanding tokens cannot create, modify, delete, or start test scenarios. Refer to [MCP tools specification](mcp-tools-specification.md) in the Developer Guide for the behavior of each access mode.
+  **Review what the credential was used for.** Check the solution’s test run history and the Amazon CloudWatch Logs for the MCP Server Lambda function for unexpected activity. If the deployment used `ReadWrite` access mode, also review your test scenarios and the contents of the `public/test-scenarios/` prefix of the scenarios bucket for unauthorized changes.

**Note**
To reject all MCP requests immediately, regardless of token validity, perform a stack update with **Deploy Optional MCP Server** set to `No`. This deletes the AgentCore Gateway.
Use this only when you must guarantee that no outstanding token can reach the MCP Server. Setting the parameter to `No` also deletes the machine-to-machine app client. Setting it back to `Yes` creates a new app client with a **new client ID** and a new secret. You must then reconfigure every MCP client with both the new client ID and the new secret.

## Example prompts
<a name="example-prompts"></a>

The following examples demonstrate how to interact with your AI assistant to analyze load testing data through the MCP interface. Customize the test IDs, date ranges, and criteria to match your specific testing needs.

For detailed information about available MCP tools and their parameters, refer to [MCP tools specification](mcp-tools-specification.md) in the Developer Guide.

### Simple test results query
<a name="simple-test-results-query"></a>

Natural language interaction with the MCP Server can be as simple as `Show me the load tests that have completed in the last 24 hours with their associated completion status` or can be more descriptive such as

```
Use list_scenarios to find my load tests. Then use get_latest_test_run to show me the basic execution data and performance metrics for the most recent test. If the results look concerning, also get the detailed performance metrics using get_test_run.
```

### Interactive performance analysis with progressive disclosure
<a name="interactive-performance-analysis"></a>

```
I need to analyze my load test performance, but I'm not sure which specific tests to focus on. Please help me by:

1. First, use list_scenarios to show me available test scenarios
2. Ask me which tests I want to analyze based on the list you show me
3. For my selected tests, use list_test_runs to get the test run history
4. Then use get_test_run with the test_run_id to get detailed response times, throughput, and error rates
5. If I want to compare tests, use get_baseline_test_run to compare against the baseline
6. If there are any issues, use get_test_run_artifacts to help me understand what went wrong

Please guide me through this step by step, asking for clarification whenever you need more specific information.
```

### Production readiness validation
<a name="production-readiness-validation"></a>

```
Help me validate if my API is ready for production deployment:

1. Use list_scenarios to find recent test scenarios
2. For the most recent test scenario, use get_latest_test_run to get basic execution data
3. Use get_test_run with that test_run_id to get detailed response times, error rates, and throughput
4. Use get_scenario_details with the test_id to show me what load patterns and endpoints were tested
5. If I have a baseline, use get_baseline_test_run to compare current results with the baseline
6. Provide a clear go/no-go recommendation based on the performance data
7. If there are any concerns, use get_test_run_artifacts to help identify potential issues

My SLA requirements are: response time under [X]ms, error rate under [Y]%.
```

### Performance trend analysis
<a name="performance-trend-analysis"></a>

```
Analyze the performance trend for my load tests over the past [TIME_PERIOD]:

1. Use list_scenarios to get all test scenarios
2. For each scenario, use list_test_runs with start_date and end_date to get tests from that period
3. Use get_test_run for the key test runs to get detailed metrics
4. Use get_baseline_test_run to compare against the baseline
5. Identify any significant changes in response times, error rates, or throughput
6. If you detect performance degradation, use get_test_run_artifacts on the problematic tests to help identify causes
7. Present the trend analysis in a clear format showing whether performance is improving, stable, or degrading

Focus on completed tests and limit results to [N] tests if there are too many.
```

### Troubleshooting failed tests
<a name="troubleshooting-failed-tests"></a>

```
Help me troubleshoot my failed load tests:

1. Use list_scenarios to find test scenarios
2. For each scenario, use list_test_runs to find recent test runs
3. Use get_test_run with the test_run_id to get the basic execution data and failure information
4. Use get_test_run_artifacts to get detailed error messages and logs
5. Use get_scenario_details to understand what was being tested when it failed
6. If I have a similar test that passed, use get_baseline_test_run to identify differences
7. Summarize the causes of failure and suggest next steps for resolution

Show me the most recent [N] failed tests from the past [TIME_PERIOD].
```
