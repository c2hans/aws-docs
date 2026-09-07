---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/mcp-server-integration.html
---

# MCP Server integration
<a name="mcp-server-integration"></a>

If you deployed the optional MCP Server component during solution deployment, you can integrate the Distributed Load Testing solution with AI development tools that support the Model Context Protocol. The MCP Server provides programmatic access to retrieve, manage, and analyze load tests through AI assistants.

Customers can connect to the DLT MCP Server using the client of their choice (Amazon Q, Claude, etc.), which each have slightly different configuration instructions. This section provides setup instructions for MCP Inspector, Kiro CLI, Cline, and Amazon Quick.

## Step 1: Get MCP endpoint and access token
<a name="get-mcp-credentials"></a>

Before configuring any MCP client, you need to retrieve your MCP Server endpoint and access token from the DLT web console.

1. Navigate to the **MCP Server** page in the Distributed Load Testing web console.

1. Locate the **MCP Server Endpoint** section.

1. Copy the endpoint URL using the **Copy Endpoint URL** button. The endpoint URL follows the format: `https://{gateway-id}.gateway.bedrock-agentcore.{region}.amazonaws.com/mcp`

1. Locate the **Access Token** section.

1. Copy the access token using the **Copy Access Token** button.

**Important**
Keep your access token secure and do not share it publicly. The token provides read-only access to your Distributed Load Testing solution through the MCP interface.

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

1. Choose **Invoke** to execute the tool and view the response.

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
