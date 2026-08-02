---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/mcp-tools-specification.html
---

# MCP tools specification
<a name="mcp-tools-specification"></a>

The Distributed Load Testing solution exposes a set of MCP tools that enable AI agents to interact with test scenarios and results. These tools provide high-level, abstracted capabilities that align with how AI agents process information, allowing them to focus on analysis and insights rather than detailed API contracts.

**Note**
All MCP tools provide read-only access to the solution’s data. No modifications to test scenarios or configurations are supported through the MCP interface.

## list\_scenarios
<a name="list-scenarios-tool"></a>

### Description
<a name="list-scenarios-tool-description"></a>

The `list_scenarios` tool retrieves a list of all available test scenarios with basic metadata.

### Endpoint
<a name="list-scenarios-tool-endpoint"></a>

 `GET /scenarios`

### Parameters
<a name="list-scenarios-tool-parameters"></a>

None

### Response
<a name="list-scenarios-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | Unique identifier for the test scenario |
|  `testName`  | Name of the test scenario |
|  `status`  | Current status of the test scenario |
|  `startTime`  | When the test was created or last run |
|  `testDescription`  | Description of the test scenario |

## get\_scenario\_details
<a name="get-scenario-details-tool"></a>

### Description
<a name="get-scenario-details-tool-description"></a>

The `get_scenario_details` tool retrieves the test configuration and most recent test run for a single test scenario.

### Endpoint
<a name="get-scenario-details-tool-endpoint"></a>

 `GET /scenarios/<test_id>?history=false&results=false`

### Request parameter
<a name="get-scenario-details-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

### Response
<a name="get-scenario-details-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testTaskConfigs`  | Task configuration for each region |
|  `testScenario`  | Test definition and parameters |
|  `status`  | Current test status |
|  `startTime`  | Test start timestamp |
|  `endTime`  | Test end timestamp (if completed) |

## list\_test\_runs
<a name="list-test-runs-tool"></a>

### Description
<a name="list-test-runs-tool-description"></a>

The `list_test_runs` tool retrieves a list of test runs for a specific test scenario, sorted newest to oldest. Returns a maximum of 30 results.

### Endpoint
<a name="list-test-runs-tool-endpoint"></a>

 `GET /scenarios/<testid>/testruns/?limit=<limit>`

or

 `GET /scenarios/<testid>/testruns/?limit=30&start_date=<start_date>&end_date=<end_date>`

### Request parameters
<a name="list-test-runs-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

 `limit`
+ Maximum number of test runs to return

  Type: Integer

  Default: 20

  Maximum: 30

  Required: No

 `start_date`
+ ISO 8601 timestamp to filter runs from specific date

  Type: String (date-time format)

  Required: No

 `end_date`
+ ISO 8601 timestamp to filter runs until specific date

  Type: String (date-time format)

  Required: No

### Response
<a name="list-test-runs-tool-response"></a>

| Name | Description |
| --- | --- |
|  `testRuns`  | Array of test run summaries with performance metrics and percentiles for each run |

## get\_test\_run
<a name="get-test-run-tool"></a>

### Description
<a name="get-test-run-tool-description"></a>

The `get_test_run` tool retrieves detailed results for a single test run with regional and endpoint breakdowns.

### Endpoint
<a name="get-test-run-tool-endpoint"></a>

 `GET /scenarios/<testid>/testruns/<testrunid>`

### Request parameters
<a name="get-test-run-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

 `test_run_id`
+ The unique identifier for the specific test run

  Type: String

  Required: Yes

### Response
<a name="get-test-run-tool-response"></a>

| Name | Description |
| --- | --- |
|  `results`  | Complete test run data including regional results breakdown, endpoint-specific metrics, performance percentiles (p50, p90, p95, p99), success and failure counts, response times and latency, and test configuration used for the run |

## get\_latest\_test\_run
<a name="get-latest-test-run-tool"></a>

### Description
<a name="get-latest-test-run-tool-description"></a>

The `get_latest_test_run` tool retrieves the most recent test run for a specific test scenario.

### Endpoint
<a name="get-latest-test-run-tool-endpoint"></a>

 `GET /scenarios/<testid>/testruns/?limit=1`

**Note**
Results are sorted by time using a Global Secondary Index (GSI), ensuring the most recent test run is returned.

### Request parameter
<a name="get-latest-test-run-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

### Response
<a name="get-latest-test-run-tool-response"></a>

| Name | Description |
| --- | --- |
|  `results`  | Latest test run data with the same format as `get_test_run`  |

## get\_baseline\_test\_run
<a name="get-baseline-test-run-tool"></a>

### Description
<a name="get-baseline-test-run-tool-description"></a>

The `get_baseline_test_run` tool retrieves the baseline test run for a specific test scenario. The baseline is used for performance comparison purposes.

### Endpoint
<a name="get-baseline-test-run-tool-endpoint"></a>

 `GET /scenarios/<test_id>/baseline`

### Request parameter
<a name="get-baseline-test-run-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

### Response
<a name="get-baseline-test-run-tool-response"></a>

| Name | Description |
| --- | --- |
|  `baselineData`  | Baseline test run data for comparison purposes, including all metrics and configuration from the designated baseline run |

## get\_test\_run\_artifacts
<a name="get-test-run-artifacts-tool"></a>

### Description
<a name="get-test-run-artifacts-tool-description"></a>

The `get_test_run_artifacts` tool retrieves Amazon S3 bucket information for accessing test artifacts including logs, error files, and results.

### Endpoint
<a name="get-test-run-artifacts-tool-endpoint"></a>

 `GET /scenarios/<testid>/testruns/<testrunid>`

### Request parameters
<a name="get-test-run-artifacts-tool-request"></a>

 `test_id`
+ The unique identifier for the test scenario

  Type: String

  Required: Yes

 `test_run_id`
+ The unique identifier for the specific test run

  Type: String

  Required: Yes

### Response
<a name="get-test-run-artifacts-tool-response"></a>

| Name | Description |
| --- | --- |
|  `bucketName`  | S3 bucket name where artifacts are stored |
|  `testRunPath`  | Path prefix for current artifact storage (version 4.0\+) |
|  `testScenarioPath`  | Path prefix for legacy artifact storage (pre-version 4.0) |

**Note**
All MCP tools leverage existing API endpoints. No modifications to the underlying APIs are required to support MCP functionality.
