---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/distributed-load-testing-api.html
---

# Distributed load testing API
<a name="distributed-load-testing-api"></a>

This load testing solution helps you to expose test result data in a secure manner. The API acts as a "front door" for access to testing data stored in Amazon DynamoDB. You can also use the APIs to access any extended functionality you build into the solution.

This solution uses an Amazon Cognito user pool integrated with Amazon API Gateway for identification and authorization. When a user pool is used with the API, clients are only allowed to call user pool activated methods after they provide a valid identity token.

For more information on running tests directly via the API, refer to [Signing Requests](https://docs.aws.amazon.com/apigateway/api-reference/signing-requests/) in the Amazon API Gateway REST API Reference documentation.

The following operations are available in the solution’s API.

**Note**
For more information about `testScenario` and other parameters, refer to [scenarios](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/source/api-services/lib/scenarios/index.js#L267) and [payload example](https://github.com/aws-solutions/distributed-load-testing-on-aws/blob/main/source/webui/src/pages/scenarios/CreateTestScenarioPage.tsx#L281-L388) in the GitHub repository.

 **Stack Info**
+  [GET /stack-info](#get-stack-info)

 **Scenarios**
+  [GET /scenarios](#get-scenarios)
+  [POST /scenarios](#post-scenarios)
+  [OPTIONS /scenarios](#options-scenarios)
+  [GET /scenarios/{testId}](#get-scenarios-testid)
+  [POST /scenarios/{testId}](#post-scenarios-testid)
+  [DELETE /scenarios/{testId}](#delete-scenarios-testid)
+  [OPTIONS /scenarios/{testId}](#options-scenarios-testid)

 **Test Runs**
+  [GET /scenarios/{testId}/testruns](#get-scenarios-testid-testruns)
+  [GET /scenarios/{testId}/testruns/{testRunId}](#get-scenarios-testid-testruns-testrunid)
+  [DELETE /scenarios/{testId}/testruns/{testRunId}](#delete-scenarios-testid-testruns-testrunid)

 **Baseline**
+  [GET /scenarios/{testId}/baseline](#get-scenarios-testid-baseline)
+  [PUT /scenarios/{testId}/baseline](#put-scenarios-testid-baseline)
+  [DELETE /scenarios/{testId}/baseline](#delete-scenarios-testid-baseline)

 **Tasks**
+  [GET /tasks](#get-tasks)
+  [OPTIONS /tasks](#options-tasks)

 **Regions**
+  [GET /regions](#get-regions)
+  [OPTIONS /regions](#options-regions)

## GET /stack-info
<a name="get-stack-info"></a>

### Description
<a name="get-stack-info-description"></a>

The `GET /stack-info` operation retrieves information about the deployed stack including creation time, region, and version. This endpoint is used by the front-end.

### Response
<a name="get-stack-info-response"></a>

 **200 - Success**

| Name | Description |
| --- | --- |
|  `created_time`  | ISO 8601 timestamp when the stack was created (for example, `2025-09-09T19:40:22Z`) |
|  `region`  | AWS region where the stack is deployed (for example, `us-east-1`) |
|  `version`  | Version of the deployed solution (for example, `v4.0.0`) |

 **Error Responses**
+  `403` - Forbidden: Insufficient permissions to access stack information
+  `404` - Not found: Stack information not available
+  `500` - Internal server error

## GET /scenarios
<a name="get-scenarios"></a>

### Description
<a name="get-scenarios-description"></a>

The `GET /scenarios` operation allows you to retrieve a list of test scenarios.

### Response
<a name="get-scenarios-response"></a>

| Name | Description |
| --- | --- |
|  `data`  | A list of scenarios including the ID, name, description, status, run time, tags, total runs, and last run for each test |

## POST /scenarios
<a name="post-scenarios"></a>

### Description
<a name="post-scenarios-description"></a>

The `POST /scenarios` operation allows you to create or schedule a test scenario.

### Request body
<a name="post-scenarios-request"></a>

| Name | Description |
| --- | --- |
|  `testName`  | The name of the test |
|  `testDescription`  | The description of the test |
|  `testTaskConfigs`  | An object that specifies `concurrency` (the number of parallel runs), `taskCount` (the number of tasks needed to run a test), and `region` for the scenario |
|  `testScenario`  | The test definition including concurrency, test time, host, and method for the test |
|  `testType`  | The test type (for example, `simple`, `jmeter`) |
|  `fileType`  | The upload file type (for example, `none`, `script`, `zip`) |
|  `tags`  | An array of strings for categorizing tests. Optional field with a maximum length of 5 (for example, `["blue", "3.0", "critical"]`) |
|  `scheduleDate`  | The date to run a test. Only provided if scheduling a test (for example, `2021-02-28`) |
|  `scheduleTime`  | The time to run a test. Only provided if scheduling a test (for example, `21:07`) |
|  `scheduleStep`  | The step in the schedule process. Only provided if scheduling a recurring test. (Available steps include `create` and `start`) |
|  `cronvalue`  | The cron value for customizing recurring scheduling. If used, omit scheduleDate and scheduleTime. |
|  `cronExpiryDate`  | Required date so the cron expires and doesn’t run indefinitely. |
|  `recurrence`  | The recurrence of a scheduled test. Only provided if scheduling a recurring test (for example, `daily`, `weekly`, `biweekly`, or `monthly`) |

### Response
<a name="post-scenarios-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the test |
|  `testName`  | The name of the test |
|  `status`  | The status of the test |

## OPTIONS /scenarios
<a name="options-scenarios"></a>

### Description
<a name="options-scenarios-description"></a>

The `OPTIONS /scenarios` operation provides a response for the request with the correct CORS response headers.

### Response
<a name="options-scenarios-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the test |
|  `testName`  | The name of the test |
|  `status`  | The status of the test |

## GET /scenarios/{testId}
<a name="get-scenarios-testid"></a>

### Description
<a name="get-scenarios-testid-description"></a>

The `GET /scenarios/{testId}` operation allows you to retrieve the details of a specific test scenario.

### Request parameters
<a name="get-scenarios-testid-request"></a>

 `testId`
+ The unique ID of the test

  Type: String

  Required: Yes

 `latest`
+ Query parameter to return only the latest test run. Default is `true`

  Type: Boolean

  Required: No

 `history`
+ Query parameter to include test run history in the response. Default is `true`. Set to `false` to exclude history

  Type: Boolean

  Required: No

### Response
<a name="get-scenarios-testid-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the test |
|  `testName`  | The name of the test |
|  `testDescription`  | The description of the test |
|  `testType`  | The type of test that is run (for example, `simple`, `jmeter`) |
|  `fileType`  | The type of file that is uploaded (for example, `none`, `script`, `zip`) |
|  `tags`  | An array of strings for categorizing tests |
|  `status`  | The status of the test |
|  `startTime`  | The time and date when the last test started |
|  `endTime`  | The time and date when the last test ended |
|  `testScenario`  | The test definition including concurrency, test time, host, and method for the test |
|  `taskCount`  | The number of tasks needed to run the test |
|  `taskIds`  | A list of task IDs for running tests |
|  `results`  | The final results of the test |
|  `history`  | A list of final results of past tests (excluded when `history=false`) |
|  `totalRuns`  | The total number of test runs for this scenario |
|  `lastRun`  | The timestamp of the last test run |
|  `errorReason`  | An error message generated when an error occurs |
|  `nextRun`  | The next scheduled run (for example, `2017-04-22 17:18:00`) |
|  `scheduleRecurrence`  | The recurrence of the test (for example, `daily`, `weekly`, `biweekly`, `monthly`) |

## POST /scenarios/{testId}
<a name="post-scenarios-testid"></a>

### Description
<a name="post-scenarios-testid-description"></a>

The `POST /scenarios/{testId}` operation allows you to cancel a specific test scenario.

### Request parameter
<a name="post-scenarios-testid-request"></a>

 `testId`
+ The unique ID of the test

  Type: String

  Required: Yes

### Response
<a name="post-scenarios-testid-response"></a>

| Name | Description |
| --- | --- |
|  `status`  | The status of the test |

## DELETE /scenarios/{testId}
<a name="delete-scenarios-testid"></a>

### Description
<a name="delete-scenarios-testid-description"></a>

The `DELETE /scenarios/{testId}` operation allows you to delete all data related to a specific test scenario.

### Request parameter
<a name="delete-scenarios-testid-request"></a>

 `testId`
+ The unique ID of the test

  Type: String

  Required: Yes

### Response
<a name="delete-scenarios-testid-response"></a>

| Name | Description |
| --- | --- |
|  `status`  | The status of the test |

## OPTIONS /scenarios/{testId}
<a name="options-scenarios-testid"></a>

### Description
<a name="options-scenarios-testid-description"></a>

The `OPTIONS /scenarios/{testId}` operation provides a response for the request with the correct CORS response headers.

### Response
<a name="options-scenarios-testid-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the test |
|  `testName`  | The name of the test |
|  `testDescription`  | The description of the test |
|  `testType`  | The type of test that is run (for example, `simple`, `jmeter`) |
|  `fileType`  | The type of file that is uploaded (for example, `none`, `script`, `zip`) |
|  `status`  | The status of the test |
|  `startTime`  | The time and date when the last test started |
|  `endTime`  | The time and date when the last test ended |
|  `testScenario`  | The test definition including concurrency, test time, host, and method for the test |
|  `taskCount`  | The number of tasks needed to run the test |
|  `taskIds`  | A list of task IDs for running tests |
|  `results`  | The final results of the test |
|  `history`  | A list of final results of past tests |
|  `errorReason`  | An error message generated when an error occurs |

## GET /scenarios/{testId}/testruns
<a name="get-scenarios-testid-testruns"></a>

### Description
<a name="get-scenarios-testid-testruns-description"></a>

The `GET /scenarios/{testId}/testruns` operation retrieves test run IDs for a specific test scenario, optionally filtered by time range. When `latest=true`, returns only the single most recent test run.

### Request parameters
<a name="get-scenarios-testid-testruns-request"></a>

 `testId`
+ The test scenario ID

  Type: String

  Required: Yes

 `latest`
+ Return only the most recent test run ID

  Type: Boolean

  Default: `false`

  Required: No

 `start_timestamp`
+ ISO 8601 timestamp to filter test runs from (inclusive). For example, `2024-01-01T00:00:00Z`

  Type: String (date-time format)

  Required: No

 `end_timestamp`
+ ISO 8601 timestamp to filter test runs until (inclusive). For example, `2024-12-31T23:59:59Z`

  Type: String (date-time format)

  Required: No

 `limit`
+ Maximum number of test runs to return (ignored when `latest=true`)

  Type: Integer (minimum: 1, maximum: 100)

  Default: `20`

  Required: No

 `next_token`
+ Pagination token from previous response to get next page

  Type: String

  Required: No

### Response
<a name="get-scenarios-testid-testruns-response"></a>

 **200 - Success**

| Name | Description |
| --- | --- |
|  `testRuns`  | Array of test run objects, each containing `testRunId` (string) and `startTime` (ISO 8601 date-time) |
|  `pagination`  | Object containing `limit` (integer) and `next_token` (string or null). Token is null if no more results |

 **Error Responses**
+  `400` - Invalid timestamp format or parameters
+  `404` - Test scenario not found
+  `500` - Internal server error

### Example usage
<a name="get-scenarios-testid-testruns-examples"></a>
+ Latest test run only: `GET /scenarios/test123/testruns?latest=true`
+ Latest within time range: `GET /scenarios/test123/testruns?latest=true&start_timestamp=2024-01-01T00:00:00Z`
+ Next page request: `GET /scenarios/test123/testruns?limit=20&next_token=eyJ0ZXN0SWQiOiJzZVFVeTEyTEtMIiwic3RhcnRUaW1lIjoiMjAyNC0wMS0xM1QxNjo0NTowMFoifQ==`

## GET /scenarios/{testId}/testruns/{testRunId}
<a name="get-scenarios-testid-testruns-testrunid"></a>

### Description
<a name="get-scenarios-testid-testruns-testrunid-description"></a>

The `GET /scenarios/{testId}/testruns/{testRunId}` operation retrieves complete results and metrics for a specific test run. Optionally omit history results with `history=false` for faster response.

### Request parameters
<a name="get-scenarios-testid-testruns-testrunid-request"></a>

 `testId`
+ The test scenario ID

  Type: String

  Required: Yes

 `testRunId`
+ The specific test run ID

  Type: String

  Required: Yes

 `history`
+ Include history array in response. Set to `false` to omit history for faster response

  Type: Boolean

  Default: `true`

  Required: No

### Response
<a name="get-scenarios-testid-testruns-testrunid-response"></a>

 **200 - Success**

| Name | Description |
| --- | --- |
|  `testId`  | The unique ID of the test (for example, `seQUy12LKL`) |
|  `testRunId`  | The specific test run ID (for example, `2DEwHItEne`) |
|  `testDescription`  | Description of the load test |
|  `testType`  | The type of test (for example, `simple`, `jmeter`) |
|  `status`  | The status of the test run: `complete`, `running`, `failed`, or `cancelled`  |
|  `startTime`  | The time and date when the test started (for example, `2025-09-09 21:01:00`) |
|  `endTime`  | The time and date when the test ended (for example, `2025-09-09 21:18:29`) |
|  `succPercent`  | Success percentage (for example, `100.00`) |
|  `testTaskConfigs`  | Array of task configuration objects containing `region`, `taskCount`, and `concurrency`  |
|  `completeTasks`  | Object mapping regions to completed task counts |
|  `results`  | Object containing detailed metrics including `avg_lt` (average latency), percentiles (`p0_0`, `p50_0`, `p90_0`, `p95_0`, `p99_0`, `p99_9`, `p100_0`), `avg_rt` (average response time), `avg_ct` (average connection time), `stdev_rt` (standard deviation response time), `concurrency`, `throughput`, `succ` (success count), `fail` (failure count), `bytes`, `testDuration`, `metricS3Location`, `rc` (response codes array), and `labels` array |
|  `testScenario`  | Object containing test configuration with `execution`, `reporting`, and `scenarios` properties |
|  `history`  | Array of historical test results (excluded when `history=false`) |

 **Error Responses**
+  `400` - Invalid testId or testRunId
+  `404` - Test run not found
+  `500` - Internal server error

## DELETE /scenarios/{testId}/testruns/{testRunId}
<a name="delete-scenarios-testid-testruns-testrunid"></a>

### Description
<a name="delete-scenarios-testid-testruns-testrunid-description"></a>

The `DELETE /scenarios/{testId}/testruns/{testRunId}` operation deletes all data and artifacts related to a specific test run. The test run data is removed from DynamoDB, while the actual test data in S3 remains unchanged.

### Request parameters
<a name="delete-scenarios-testid-testruns-testrunid-request"></a>

 `testId`
+ The test scenario ID

  Type: String

  Required: Yes

 `testRunId`
+ The specific test run ID to delete

  Type: String

  Required: Yes

### Response
<a name="delete-scenarios-testid-testruns-testrunid-response"></a>

 **204 - Success**

Test run successfully deleted (no content returned)

 **Error Responses**
+  `400` - Invalid testId or testRunId
+  `403` - Forbidden: Insufficient permissions to delete test run
+  `404` - Test run not found
+  `409` - Conflict: Test run is currently running and cannot be deleted
+  `500` - Internal server error

## GET /scenarios/{testId}/baseline
<a name="get-scenarios-testid-baseline"></a>

### Description
<a name="get-scenarios-testid-baseline-description"></a>

The `GET /scenarios/{testId}/baseline` operation retrieves the designated baseline test result for a scenario. Returns either the baseline test run ID or the full baseline results depending on the `data` parameter.

### Request parameters
<a name="get-scenarios-testid-baseline-request"></a>

 `testId`
+ The test scenario ID

  Type: String

  Required: Yes

 `data`
+ Return full baseline test run data if `true`, otherwise just the testRunId

  Type: Boolean

  Default: `false`

  Required: No

### Response
<a name="get-scenarios-testid-baseline-response"></a>

 **200 - Success**

When `data=false` (default):

| Name | Description |
| --- | --- |
|  `testId`  | The test scenario ID (for example, `seQUy12LKL`) |
|  `baselineTestRunId`  | The baseline test run ID (for example, `2DEwHItEne`) |

When `data=true`:

| Name | Description |
| --- | --- |
|  `testId`  | The test scenario ID (for example, `seQUy12LKL`) |
|  `baselineTestRunId`  | The baseline test run ID (for example, `2DEwHItEne`) |
|  `baselineData`  | Complete test run results object (same structure as `GET /scenarios/{testId}/testruns/{testRunId}`) |

 **Error Responses**
+  `400` - Invalid testId parameter
+  `404` - Test scenario not found or no baseline set
+  `500` - Internal server error

## PUT /scenarios/{testId}/baseline
<a name="put-scenarios-testid-baseline"></a>

### Description
<a name="put-scenarios-testid-baseline-description"></a>

The `PUT /scenarios/{testId}/baseline` operation designates a specific test run as the baseline for performance comparison. Only one baseline can be set per scenario.

### Request parameters
<a name="put-scenarios-testid-baseline-request"></a>

 `testId`
+ The test scenario ID

  Type: String

  Required: Yes

### Request body
<a name="put-scenarios-testid-baseline-request-body"></a>

| Name | Description |
| --- | --- |
|  `testRunId`  | The test run ID to set as baseline (for example, `2DEwHItEne`) |

### Response
<a name="put-scenarios-testid-baseline-response"></a>

 **200 - Success**

| Name | Description |
| --- | --- |
|  `message`  | Confirmation message (for example, `Baseline set successfully`) |
|  `testId`  | The test scenario ID (for example, `seQUy12LKL`) |
|  `baselineTestRunId`  | The baseline test run ID that was set (for example, `2DEwHItEne`) |

 **Error Responses**
+  `400` - Invalid testId or testRunId
+  `404` - Test scenario or test run not found
+  `409` - Conflict: Test run cannot be set as baseline (for example, failed test)
+  `500` - Internal server error

## DELETE /scenarios/{testId}/baseline
<a name="delete-scenarios-testid-baseline"></a>

### Description
<a name="delete-scenarios-testid-baseline-description"></a>

The `DELETE /scenarios/{testId}/baseline` operation clears the baseline value for a scenario by setting it to an empty string.

### Request parameters
<a name="delete-scenarios-testid-baseline-request"></a>

 `testId`
+ The test scenario ID

  Type: String

  Required: Yes

### Response
<a name="delete-scenarios-testid-baseline-response"></a>

 **204 - Success**

Baseline successfully cleared (no content returned)

 **Error Responses**
+  `400` - Invalid testId
+  `500` - Internal server error

## GET /tasks
<a name="get-tasks"></a>

### Description
<a name="get-tasks-description"></a>

The `GET /tasks` operation allows you to retrieve a list of running Amazon Elastic Container Service (Amazon ECS) tasks.

### Response
<a name="get-tasks-response"></a>

| Name | Description |
| --- | --- |
|  `tasks`  | A list of task IDs for running tests |

## OPTIONS /tasks
<a name="options-tasks"></a>

### Description
<a name="options-tasks-description"></a>

The `OPTIONS /tasks` tasks operation provides a response for the request with the correct CORS response headers.

### Response
<a name="options-tasks-response"></a>

| Name | Description |
| --- | --- |
|  `taskIds`  | A list of task IDs for running tests |

## GET /regions
<a name="get-regions"></a>

### Description
<a name="get-regions-description"></a>

The `GET /regions` operation allows you to retrieve the regional resource information necessary to run a test in that Region.

### Response
<a name="get-regions-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The Region ID |
|  `ecsCloudWatchLogGroup`  | The name of the Amazon CloudWatch log group for the Amazon Fargate tasks in the Region |
|  `region`  | The Region in which the resources in the table exist |
|  `subnetA`  | The ID of one of the subnets in the Region |
|  `subnetB`  | The ID of one of the subnets in the Region |
|  `taskCluster`  | The name of the AWS Fargate cluster in the Region |
|  `taskDefinition`  | The ARN of the task definition in the Region |
|  `taskImage`  | The name of the task image in the Region |
|  `taskSecurityGroup`  | The ID of the security group in the Region |

## OPTIONS /regions
<a name="options-regions"></a>

### Description
<a name="options-regions-description"></a>

The `OPTIONS /regions` operation provides a response for the request with the correct CORS response headers.

### Response
<a name="options-regions-response"></a>

| Name | Description |
| --- | --- |
|  `testId`  | The Region ID |
|  `ecsCloudWatchLogGroup`  | The name of the Amazon CloudWatch log group for the Amazon Fargate tasks in the Region |
|  `region`  | The Region in which the resources in the table exist |
|  `subnetA`  | The ID of one of the subnets in the Region |
|  `subnetB`  | The ID of one of the subnets in the Region |
|  `taskCluster`  | The name of the AWS Fargate cluster in the Region |
|  `taskDefinition`  | The ARN of the task definition in the Region |
|  `taskImage`  | The name of the task image in the Region |
|  `taskSecurityGroup`  | The ID of the security group in the Region |
