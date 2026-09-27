---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/mcp-tools-specification.html
---

# MCP tools specification
<a name="mcp-tools-specification"></a>

The Distributed Load Testing solution exposes a set of MCP tools that enable AI agents to interact with test scenarios and results. These tools provide high-level, abstracted capabilities that align with how AI agents process information, allowing them to focus on analysis and insights rather than detailed API contracts.

The MCP Server supports two access modes, controlled by the `MCPServerAccessMode` AWS CloudFormation parameter:
+  **ReadOnly** (default) — Only read tools are registered. Agents see 7 tools via `tools/list`. No mutating operations are available.
+  **ReadWrite** — Both read and write tools are registered. Agents see all tools (read \+ write) via `tools/list` and can create tests, trigger runs, manage schedules, and upload scripts.

The access mode is set at deployment time. To change the access mode after initial deployment, perform a CloudFormation stack update with the new `MCPServerAccessMode` parameter value. The change takes effect when the stack update completes — no other manual steps are required.

In ReadOnly mode, write tools are not registered at all — agents never see them in `tools/list`. The AWS Identity and Access Management (IAM) policy on the MCP Server’s AWS Lambda function is scoped accordingly. ReadOnly permits only GET requests to the API. ReadWrite permits GET, POST, PUT, and DELETE.

## Read tools
<a name="read-tools"></a>

### list\_scenarios
<a name="list-scenarios-tool"></a>

#### Description
<a name="list-scenarios-tool-description"></a>

The `list_scenarios` tool retrieves a list of all available test scenarios with basic metadata.

#### Endpoint
<a name="list-scenarios-tool-endpoint"></a>

 `GET /scenarios`

#### Parameters
<a name="list-scenarios-tool-parameters"></a>

None

#### Response
<a name="list-scenarios-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | Unique identifier for the test scenario |
|  `testName`  | Name of the test scenario |
|  `status`  | Current status of the test scenario |
|  `startTime`  | When the test was created or last run |
|  `testDescription`  | Description of the test scenario |

### get\_scenario\_details
<a name="get-scenario-details-tool"></a>

#### Description
<a name="get-scenario-details-tool-description"></a>

The `get_scenario_details` tool retrieves the test configuration and most recent test run for a single test scenario.

The response reports the scenario’s traffic shape mode. A `nativeRunMode` object indicates Native mode, and its absence indicates Standard mode. For a Native scenario, the `concurrency`, `rampUp`, and `holdFor` fields do not reflect the load the run generated. The load comes from the script instead. For more information, refer to [Traffic shape modes](design-considerations.md#traffic-shape-modes-architecture).

#### Endpoint
<a name="get-scenario-details-tool-endpoint"></a>

 `GET /scenarios/<test_id>?history=false&results=false`

#### Request parameter
<a name="get-scenario-details-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

#### Response
<a name="get-scenario-details-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testTaskConfigs`  | Task configuration for each Region |
|  `testScenario`  | Test definition and parameters |
|  `status`  | Current test status |
|  `startTime`  | Test start timestamp |
|  `endTime`  | Test end timestamp (if completed) |

### list\_test\_runs
<a name="list-test-runs-tool"></a>

#### Description
<a name="list-test-runs-tool-description"></a>

The `list_test_runs` tool retrieves a list of test runs for a specific test scenario, sorted newest to oldest. Returns a maximum of 30 results. Only one of `limit` or `start_timestamp` may be provided, not both.

#### Endpoint
<a name="list-test-runs-tool-endpoint"></a>

 `GET /scenarios/<testid>/testruns/?limit=<limit>`

or

 `GET /scenarios/<testid>/testruns/?start_timestamp=<start_timestamp>`

#### Request parameters
<a name="list-test-runs-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

 `limit`
+ Maximum number of test runs to return. Cannot be used with `start_timestamp`.

  Type: Integer

  Default: 20

  Maximum: 30

  Required: No

 `start_timestamp`
+ Return all test runs going back to this timestamp. Cannot be used with `limit`.

  Type: String (ISO 8601 date-time format, for example `2024-01-15T14:30:00.000Z`)

  Required: No

#### Response
<a name="list-test-runs-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testRuns`  | Array of test run summaries with performance metrics and percentiles for each run |

### get\_test\_run
<a name="get-test-run-tool"></a>

#### Description
<a name="get-test-run-tool-description"></a>

The `get_test_run` tool retrieves detailed results for a single test run with regional and endpoint breakdowns.

#### Endpoint
<a name="get-test-run-tool-endpoint"></a>

 `GET /scenarios/<testid>/testruns/<testrunid>`

#### Request parameters
<a name="get-test-run-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

 `test_run_id`
+ The unique identifier for the specific test run

  Type: String

  Required: Yes

#### Response
<a name="get-test-run-tool-response"></a>

| Name | Description |
| --- | --- |
|  `results`  | Complete test run data including regional results breakdown, endpoint-specific metrics, performance percentiles (p50, p90, p95, p99), success and failure counts, response times and latency, and test configuration used for the run |

### get\_latest\_test\_run
<a name="get-latest-test-run-tool"></a>

#### Description
<a name="get-latest-test-run-tool-description"></a>

The `get_latest_test_run` tool retrieves the most recent test run for a specific test scenario.

#### Endpoint
<a name="get-latest-test-run-tool-endpoint"></a>

 `GET /scenarios/<testid>/testruns/?limit=1`

**Note**
Results are sorted by time using a Global Secondary Index (GSI), so that the most recent test run is returned.

#### Request parameter
<a name="get-latest-test-run-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

#### Response
<a name="get-latest-test-run-tool-response"></a>

| Name | Description |
| --- | --- |
|  `results`  | Latest test run data with the same format as `get_test_run`  |

### get\_baseline\_test\_run
<a name="get-baseline-test-run-tool"></a>

#### Description
<a name="get-baseline-test-run-tool-description"></a>

The `get_baseline_test_run` tool retrieves the baseline test run for a specific test scenario. The baseline is used for performance comparison purposes.

#### Endpoint
<a name="get-baseline-test-run-tool-endpoint"></a>

 `GET /scenarios/<test_id>/baseline`

#### Request parameter
<a name="get-baseline-test-run-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

#### Response
<a name="get-baseline-test-run-tool-response"></a>

| Name | Description |
| --- | --- |
|  `baselineData`  | Baseline test run data for comparison purposes, including all metrics and configuration from the designated baseline run |

### get\_test\_run\_artifacts
<a name="get-test-run-artifacts-tool"></a>

#### Description
<a name="get-test-run-artifacts-tool-description"></a>

The `get_test_run_artifacts` tool retrieves Amazon S3 bucket information for accessing test artifacts including logs, error files, and results.

#### Endpoint
<a name="get-test-run-artifacts-tool-endpoint"></a>

 `GET /scenarios/<testid>/testruns/<testrunid>`

#### Request parameters
<a name="get-test-run-artifacts-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

 `test_run_id`
+ The unique identifier for the specific test run

  Type: String

  Required: Yes

#### Response
<a name="get-test-run-artifacts-tool-response"></a>

| Name | Description |
| --- | --- |
|  `bucketName`  | S3 bucket name where artifacts are stored |
|  `testRunPath`  | Path prefix for current artifact storage (version 4.0\+) |
|  `testScenarioPath`  | Path prefix for legacy artifact storage (pre-version 4.0) |

## Write tools
<a name="write-tools"></a>

Write tools are only available when `MCPServerAccessMode` is set to `ReadWrite`. They enable agents to create, modify, and execute test scenarios.

### create\_test
<a name="create-test-tool"></a>

#### Description
<a name="create-test-tool-description"></a>

The `create_test` tool creates a new load test scenario without executing it. The test is saved and can be run later with `start_run`. For script-based tests (jmeter, k6, locust), call `upload_test_script` first and pass the returned `test_id`.

#### Parameters
<a name="create-test-tool-parameters"></a>

 `test_id`
+ The test scenario’s unique identifier. Omit for simple HTTP tests (system generates one). Required for script-based tests — use the `test_id` returned by `upload_test_script`.

  Type: String

  Required: No (required for script-based tests)

 `test_name`
+ Human-readable name for the test scenario

  Type: String

  Required: Yes

 `test_description`
+ Description of what this test validates

  Type: String

  Required: Yes

 `test_type`
+ Test type. `simple` for HTTP endpoint tests configured inline. `jmeter`, `k6`, or `locust` for script-based tests that reference an uploaded script file.

  Type: String

  Required: Yes

 `test_task_configs`
+ Regional task configuration. Each entry specifies a Region, the number of AWS Fargate tasks, and concurrent virtual users per task. Total concurrent users for a Region = `task_count` × `concurrency`.

  Type: Array of objects (each with `region`, `task_count`, `concurrency`)

  Required: Yes

 `test_scenario`
+ Test execution scenario defining the load profile and target endpoint(s). Contains `execution` (ramp-up, hold-for, scenario name) and `scenarios` (named scenario definitions with either a `requests` array for simple tests or a `script` string for script-based tests).

  Type: Object

  Required: Yes

 `show_live`
+ Whether to enable live monitoring during test execution.

  Type: Boolean

  Default: `false`

  Required: No

 `tags`
+ Tags for organizing test scenarios. Maximum 5 tags.

  Type: Array of strings

  Required: No

 `native_run_mode`
+ An object that selects the traffic shape mode. Omit it for Standard mode, where the solution controls the load. Include it for Native mode, where your uploaded script controls the load. For more information, refer to [Traffic shape modes](design-considerations.md#traffic-shape-modes-architecture).

  Type: Object

  Required: No

Native mode differs from Standard mode as follows:
+ The object requires one field, `max_test_duration_seconds`, with a maximum of 24 hours.
+ Only script-based tests (`jmeter`, `k6`, or `locust`) accept Native mode.
+ Simple HTTP Endpoint tests always run in Standard mode.
+  `test_task_configs` remains required, and each entry still requires `concurrency`.
+ A request that sets `concurrency` with `native_run_mode` returns success.
+ The load the test generates is the load your script declares.
+ Total load per Region is your script’s load multiplied by `task_count`.

#### Response
<a name="create-test-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the created test |
|  `testName`  | Name of the test |
|  `status`  | Status of the test (for example, `created`) |

### update\_test
<a name="update-test-tool"></a>

#### Description
<a name="update-test-tool-description"></a>

The `update_test` tool updates an existing test scenario’s configuration. This is a full replace — the entire test configuration must be provided, not just changed fields. The test must not be currently running.

#### Parameters
<a name="update-test-tool-parameters"></a>

Same as `create_test`, except `test_id` is required and must reference an existing test.

#### Response
<a name="update-test-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the updated test |
|  `testName`  | Name of the test |
|  `status`  | Status of the test |

### delete\_test
<a name="delete-test-tool"></a>

#### Description
<a name="delete-test-tool-description"></a>

The `delete_test` tool permanently deletes a test scenario and all associated data including test run history, schedules, and Amazon CloudWatch dashboards. This action cannot be undone. The test must not be currently running.

#### Parameters
<a name="delete-test-tool-parameters"></a>

 `test_id`
+ The test scenario’s unique identifier

  Type: String

  Required: Yes

#### Response
<a name="delete-test-tool-response"></a>

| Name | Description |
| --- | --- |
|  `status`  | Confirmation of deletion |

### start\_run
<a name="start-run-tool"></a>

#### Description
<a name="start-run-tool-description"></a>

The `start_run` tool starts execution of a test scenario. The MCP Server fetches the test’s stored configuration and triggers execution. Returns immediately with status `queued`. Use `get_latest_test_run` to poll for completion.

#### Parameters
<a name="start-run-tool-parameters"></a>

 `test_id`
+ The test scenario’s unique identifier

  Type: String

  Required: Yes

#### Response
<a name="start-run-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the test |
|  `status`  | Status of the test (for example, `queued`) |

### stop\_run
<a name="stop-run-tool"></a>

#### Description
<a name="stop-run-tool-description"></a>

The `stop_run` tool stops a currently running test. Sends a cancellation signal to all running Fargate tasks. The test status transitions to `cancelled`. Partial results are available via `get_latest_test_run`.

#### Parameters
<a name="stop-run-tool-parameters"></a>

 `test_id`
+ The test scenario’s unique identifier

  Type: String

  Required: Yes

#### Response
<a name="stop-run-tool-response"></a>

| Name | Description |
| --- | --- |
|  `status`  | Confirmation of cancellation |

### create\_simple\_schedule
<a name="create-simple-schedule-tool"></a>

#### Description
<a name="create-simple-schedule-tool-description"></a>

The `create_simple_schedule` tool creates a one-time scheduled test that runs automatically at a specified date and time. Requires all standard test configuration fields plus schedule fields.

#### Parameters
<a name="create-simple-schedule-tool-parameters"></a>

All `create_test` parameters (with `test_id` optional, same rules), plus:

 `schedule_date`
+ Date for the scheduled run. Must be in the future.

  Type: String (format: `YYYY-MM-DD`)

  Required: Yes

 `schedule_time`
+ Time for the scheduled run.

  Type: String (format: `HH:MM`, 24-hour)

  Required: Yes

 `schedule_timezone`
+ IANA timezone for schedule interpretation (for example, `America/New_York`, `UTC`).

  Type: String

  Default: `UTC`

  Required: No

#### Response
<a name="create-simple-schedule-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the test |
|  `status`  | Status of the test (for example, `scheduled`) |
|  `nextRun`  | Next scheduled execution time |

### create\_cron\_schedule
<a name="create-cron-schedule-tool"></a>

#### Description
<a name="create-cron-schedule-tool-description"></a>

The `create_cron_schedule` tool creates a recurring scheduled test that runs automatically according to a cron expression. Requires all standard test configuration fields plus cron schedule fields.

#### Parameters
<a name="create-cron-schedule-tool-parameters"></a>

All `create_test` parameters (with `test_id` optional, same rules), plus:

 `cron_value`
+ Cron expression for recurring schedule. Standard 5-field format (for example, `0 9 * * *` for daily at 9:00 AM).

  Type: String

  Required: Yes

 `recurrence`
+ Human-readable recurrence label (for example, `daily`, `weekly`).

  Type: String

  Required: Yes

 `cron_expiry_date`
+ Date when the recurring schedule stops executing.

  Type: String (format: `YYYY-MM-DD`)

  Required: No

 `schedule_timezone`
+ IANA timezone for schedule interpretation.

  Type: String

  Default: `UTC`

  Required: No

#### Response
<a name="create-cron-schedule-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the test |
|  `status`  | Status of the test (for example, `scheduled`) |
|  `nextRun`  | Next scheduled execution time |

### update\_simple\_schedule
<a name="update-simple-schedule-tool"></a>

#### Description
<a name="update-simple-schedule-tool-description"></a>

The `update_simple_schedule` tool updates the schedule configuration for an existing one-time scheduled test. Full replace of the test configuration including schedule fields. The test must be in `scheduled` status.

#### Parameters
<a name="update-simple-schedule-tool-parameters"></a>

Same as `create_simple_schedule`, except `test_id` is required and must reference an existing scheduled test.

#### Response
<a name="update-simple-schedule-tool-response"></a>

Same as `create_simple_schedule`.

### update\_cron\_schedule
<a name="update-cron-schedule-tool"></a>

#### Description
<a name="update-cron-schedule-tool-description"></a>

The `update_cron_schedule` tool updates the schedule configuration for an existing recurring scheduled test. Full replace of the test configuration including cron schedule fields. The test must be in `scheduled` status.

#### Parameters
<a name="update-cron-schedule-tool-parameters"></a>

Same as `create_cron_schedule`, except `test_id` is required and must reference an existing scheduled test.

#### Response
<a name="update-cron-schedule-tool-response"></a>

Same as `create_cron_schedule`.

### upload\_test\_script
<a name="upload-test-script-tool"></a>

#### Description
<a name="upload-test-script-tool-description"></a>

The `upload_test_script` tool uploads a script file (JMeter `.jmx`, k6 `.js`, Locust `.py`, or `.zip`) required for script-based tests. Must be called before `create_test` or `update_test` for script-based tests. Returns a `test_id` and `script_filename` for use in subsequent tool calls.

#### Parameters
<a name="upload-test-script-tool-parameters"></a>

 `test_id`
+ The test scenario’s unique identifier. Omit for new tests (system generates one). Provide for existing tests to upload to the correct location.

  Type: String

  Required: No

 `test_type`
+ Test type: `jmeter`, `k6`, or `locust`.

  Type: String

  Required: Yes

 `file_extension`
+ File extension: `jmx`, `js`, `py`, or `zip`.

  Type: String

  Required: Yes

 `file_content`
+ Base64-encoded file content.

  Type: String

  Required: Yes

#### Response
<a name="upload-test-script-tool-response"></a>

| Name | Description |
| --- | --- |
|  `test_id`  | The test ID (generated or provided) |
|  `script_filename`  | Filename in S3 (format: `<test_id>.<extension>`). Reference this in `test_scenario.scenarios`. |

## Workflow guides
<a name="workflow-guides"></a>

Workflow guides are multi-step recipes that help agents chain multiple tools together for common operations. The `get_workflow_guides` tool returns structured step-by-step guidance for each workflow.

### get\_workflow\_guides
<a name="get-workflow-guides-tool"></a>

#### Description
<a name="get-workflow-guides-tool-description"></a>

The `get_workflow_guides` tool returns step-by-step workflow recipes for common multi-tool DLT operations. Returns structured guidance on which tools to call, in what order, and how to interpret results between steps.

#### Parameters
<a name="get-workflow-guides-tool-parameters"></a>

 `workflow`
+ The workflow to retrieve guidance for. One of: `run_and_monitor`, `baseline_comparison`, `schedule_test`, `create_and_run`, `update_and_run`.

  Type: String

  Required: Yes

#### Response
<a name="get-workflow-guides-tool-response"></a>

| Name | Description |
| --- | --- |
|  `workflow`  | Workflow identifier |
|  `description`  | Brief description of the workflow’s purpose |
|  `steps`  | Array of step objects, each with `step` (number), `action` (what to do), `tool` (which MCP tool to call, or null for non-tool steps), and `details` (specific instructions) |

### Available workflows
<a name="available-workflows"></a>

#### run\_and\_monitor
<a name="workflow-run-and-monitor"></a>

Start an existing test run and poll until completion.

1. Find the test using `list_scenarios` or `get_scenario_details`

1. Start the test run using `start_run`

1. Poll for completion using `get_latest_test_run` (recommended interval: 30 seconds; handle initial 404 for 1–3 minutes while Amazon Elastic Container Service (Amazon ECS) tasks launch)

1. Report results once a terminal status is reached (`complete`, `failed`, or `cancelled`)

#### baseline\_comparison
<a name="workflow-baseline-comparison"></a>

Run a test and compare results against a stored baseline.

1. Find the test using `list_scenarios` or `get_scenario_details`

1. Start the test run using `start_run`

1. Poll for completion using `get_latest_test_run` (recommended interval: 30 seconds)

1. Retrieve the baseline using `get_baseline_test_run` (skip comparison if no baseline is set)

1. Compare metrics (average response time, latency, throughput, percentiles, error rate)

#### schedule\_test
<a name="workflow-schedule-test"></a>

Create a test with a recurring or one-time schedule.

1. Determine schedule type (one-time → `create_simple_schedule`, recurring → `create_cron_schedule`)

1. Upload test script if script-based using `upload_test_script`

1. Create the scheduled test with full configuration plus schedule fields

1. Verify the schedule was created using `get_scenario_details` (check `status: scheduled` and `nextRun`)

Constraints: minimum 1-hour interval between recurring runs, interval must exceed test duration, cron must specify exactly one minute value.

#### create\_and\_run
<a name="workflow-create-and-run"></a>

Create a new test from scratch and immediately execute it.

1. Upload test script if script-based using `upload_test_script`

1. Create the test using `create_test`

1. Start the test run using `start_run` with the returned `test_id`

1. Poll for completion using `get_latest_test_run` (recommended interval: 30 seconds)

1. Report results

#### update\_and\_run
<a name="workflow-update-and-run"></a>

Modify an existing test’s configuration and immediately re-execute it.

1. Retrieve current configuration using `get_scenario_details`

1. Upload new script if changing the script using `upload_test_script`

1. Update the test configuration using `update_test` (full replace — include all fields)

1. Start the test run using `start_run`

1. Poll for completion using `get_latest_test_run` (recommended interval: 30 seconds)

1. Report results

**Note**
All MCP tools leverage existing API endpoints. No modifications to the underlying APIs are required to support MCP functionality.
