---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_ExecuteScheduledQuery.html
---

# ExecuteScheduledQuery
<a name="API_query_ExecuteScheduledQuery"></a>

 You can use this API to run a scheduled query manually.

If you enabled `QueryInsights`, this API also returns insights and metrics related to the query that you executed as part of an Amazon SNS notification. `QueryInsights` helps with performance tuning of your query. For more information about `QueryInsights`, see [Using query insights to optimize queries in Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/using-query-insights.html).

## Request Syntax
<a name="API_query_ExecuteScheduledQuery_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "InvocationTime": {{number}},
   "QueryInsights": {
      "Mode": "{{string}}"
   },
   "ScheduledQueryArn": "{{string}}"
}
```

## Request Parameters
<a name="API_query_ExecuteScheduledQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_query_ExecuteScheduledQuery_RequestSyntax) **   <a name="timestream-query_ExecuteScheduledQuery-request-ClientToken"></a>
Not used.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: No

 ** [InvocationTime](#API_query_ExecuteScheduledQuery_RequestSyntax) **   <a name="timestream-query_ExecuteScheduledQuery-request-InvocationTime"></a>
The timestamp in UTC. Query will be run as if it was invoked at this timestamp.
Type: Timestamp
Required: Yes

 ** [QueryInsights](#API_query_ExecuteScheduledQuery_RequestSyntax) **   <a name="timestream-query_ExecuteScheduledQuery-request-QueryInsights"></a>
Encapsulates settings for enabling `QueryInsights`.
Enabling `QueryInsights` returns insights and metrics as a part of the Amazon SNS notification for the query that you executed. You can use `QueryInsights` to tune your query performance and cost.
Type: [ScheduledQueryInsights](API_query_ScheduledQueryInsights.md) object
Required: No

 ** [ScheduledQueryArn](#API_query_ExecuteScheduledQuery_RequestSyntax) **   <a name="timestream-query_ExecuteScheduledQuery-request-ScheduledQueryArn"></a>
ARN of the scheduled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Elements
<a name="API_query_ExecuteScheduledQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_query_ExecuteScheduledQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the necessary permissions to access the account settings.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request.
HTTP Status Code: 400

 ** InvalidEndpointException **
The requested endpoint is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** ScheduledQueryArn **
The ARN of the scheduled query.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to excessive requests.
HTTP Status Code: 400

 ** ValidationException **
 Invalid or malformed request.
HTTP Status Code: 400

## Examples
<a name="API_query_ExecuteScheduledQuery_Examples"></a>

### Scheduled query notification message for the ENABLED\_WITH\_RATE\_CONTROL mode
<a name="API_query_ExecuteScheduledQuery_Example_1"></a>

The following example shows a successful scheduled query notification message for the `ENABLED_WITH_RATE_CONTROL` mode of the `QueryInsights` parameter.

```
"SuccessNotificationMessage": {
    "type": "MANUAL_TRIGGER_SUCCESS",
    "arn": "arn:aws:timestream:<Region>:<Account>:scheduled-query/sq-test-49c6ed55-c2e7-4cc2-9956-4a0ecea13420-80e05b035236a4c3",
    "scheduledQueryRunSummary": {
        "invocationEpochSecond": 1723710546,
        "triggerTimeMillis": 1723710547490,
        "runStatus": "MANUAL_TRIGGER_SUCCESS",
        "executionStats": {
            "executionTimeInMillis": 17343,
            "dataWrites": 1024,
            "bytesMetered": 0,
            "cumulativeBytesScanned": 600,
            "recordsIngested": 1,
            "queryResultRows": 1
        },
        "queryInsightsResponse": {
            "querySpatialCoverage": {
                "max": {
                    "value": 1.0,
                    "tableArn": "arn:aws:timestream:<Region>:<Account>:database/BaseDb/table/BaseTable",
                    "partitionKey": [
                        "measure_name"
                    ]
                }
            },
            "queryTemporalRange": {
                "max": {
                    "value": 2399999999999,
                    "tableArn": "arn:aws:timestream:<Region>:<Account>:database/BaseDb/table/BaseTable"
                }
            },
            "queryTableCount": 1,
            "outputRows": 1,
            "outputBytes": 59
        }
    }
}
```

### Scheduled query notification message for the DISABLED mode
<a name="API_query_ExecuteScheduledQuery_Example_2"></a>

The following example shows a successful scheduled query notification message for the `DISABLED` mode of the `QueryInsights` parameter.

```
"SuccessNotificationMessage": {
    "type": "MANUAL_TRIGGER_SUCCESS",
    "arn": "arn:aws:timestream:<Region>:<Account>:scheduled-query/sq-test-fa109d9e-6528-4a0d-ac40-482fa05e657f-140faaeecdc5b2a7",
    "scheduledQueryRunSummary": {
        "invocationEpochSecond": 1723711401,
        "triggerTimeMillis": 1723711402144,
        "runStatus": "MANUAL_TRIGGER_SUCCESS",
        "executionStats": {
            "executionTimeInMillis": 17992,
            "dataWrites": 1024,
            "bytesMetered": 0,
            "cumulativeBytesScanned": 600,
            "recordsIngested": 1,
            "queryResultRows": 1
        }
    }
}
```

### Failure notification message for the ENABLED\_WITH\_RATE\_CONTROL mode
<a name="API_query_ExecuteScheduledQuery_Example_3"></a>

The following example shows a failed scheduled query notification message for the `ENABLED_WITH_RATE_CONTROL` mode of the `QueryInsights` parameter.

```
"FailureNotificationMessage": {
    "type": "MANUAL_TRIGGER_FAILURE",
    "arn": "arn:aws:timestream:<Region>:<Account>:scheduled-query/sq-test-b261670d-790c-4116-9db5-0798071b18b1-b7e27a1d79be226d",
    "scheduledQueryRunSummary": {
        "invocationEpochSecond": 1727915513,
        "triggerTimeMillis": 1727915513894,
        "runStatus": "MANUAL_TRIGGER_FAILURE",
        "executionStats": {
            "executionTimeInMillis": 10777,
            "dataWrites": 0,
            "bytesMetered": 0,
            "cumulativeBytesScanned": 0,
            "recordsIngested": 0,
            "queryResultRows": 4
        },
        "errorReportLocation": {
            "s3ReportLocation": {
                "bucketName": "amzn-s3-demo-bucket",
                "objectKey": "4my-organization-f7a3c5d065a1a95e/1727915513/MANUAL/1727915513894/5e14b3df-b147-49f4-9331-784f749b68ae"
            }
        },
        "failureReason": "Schedule encountered some errors and is incomplete. Please take a look at error report for further details"
    }
}
```

### Failure notification message for the DISABLED mode
<a name="API_query_ExecuteScheduledQuery_Example_4"></a>

The following example shows a failed scheduled query notification message for the `DISABLED` mode of the `QueryInsights` parameter.

```
"FailureNotificationMessage": {
    "type": "MANUAL_TRIGGER_FAILURE",
    "arn": "arn:aws:timestream:<Region>:<Account>:scheduled-query/sq-test-b261670d-790c-4116-9db5-0798071b18b1-b7e27a1d79be226d",
    "scheduledQueryRunSummary": {
        "invocationEpochSecond": 1727915194,
        "triggerTimeMillis": 1727915195119,
        "runStatus": "MANUAL_TRIGGER_FAILURE",
        "executionStats": {
            "executionTimeInMillis": 10777,
            "dataWrites": 0,
            "bytesMetered": 0,
            "cumulativeBytesScanned": 0,
            "recordsIngested": 0,
            "queryResultRows": 4
        },
        "errorReportLocation": {
            "s3ReportLocation": {
                "bucketName": "amzn-s3-demo-bucket",
                "objectKey": "4my-organization-b7e27a1d79be226d/1727915194/MANUAL/1727915195119/08dea9f5-9a0a-4e63-a5f7-ded23247bb98"
            }
        },
        "failureReason": "Schedule encountered some errors and is incomplete. Please take a look at error report for further details"
    }
}
```

## See Also
<a name="API_query_ExecuteScheduledQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-query-2018-11-01/ExecuteScheduledQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-query-2018-11-01/ExecuteScheduledQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/ExecuteScheduledQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-query-2018-11-01/ExecuteScheduledQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/ExecuteScheduledQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-query-2018-11-01/ExecuteScheduledQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-query-2018-11-01/ExecuteScheduledQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-query-2018-11-01/ExecuteScheduledQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-query-2018-11-01/ExecuteScheduledQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/ExecuteScheduledQuery)
