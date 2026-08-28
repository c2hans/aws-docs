---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListScheduledQueries.html
---

# ListScheduledQueries
<a name="API_ListScheduledQueries"></a>

Lists all scheduled queries in your account and region. You can filter results by state to show only enabled or disabled queries.

## Request Syntax
<a name="API_ListScheduledQueries_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "scheduleType": "{{string}}",
   "state": "{{string}}"
}
```

## Request Parameters
<a name="API_ListScheduledQueries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListScheduledQueries_RequestSyntax) **   <a name="CWL-ListScheduledQueries-request-maxResults"></a>
The maximum number of scheduled queries to return. Valid range is 1 to 1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListScheduledQueries_RequestSyntax) **   <a name="CWL-ListScheduledQueries-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [scheduleType](#API_ListScheduledQueries_RequestSyntax) **   <a name="CWL-ListScheduledQueries-request-scheduleType"></a>
Filter scheduled queries by schedule type. Valid values are `CUSTOMER_MANAGED` and `AWS_MANAGED`. If not specified, scheduled queries of all schedule types are returned.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`
Required: No

 ** [state](#API_ListScheduledQueries_RequestSyntax) **   <a name="CWL-ListScheduledQueries-request-state"></a>
Filter scheduled queries by state. Valid values are `ENABLED` and `DISABLED`. If not specified, all scheduled queries are returned.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_ListScheduledQueries_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "scheduledQueries": [
      {
         "creationTime": number,
         "destinationConfiguration": {
            "lookupTableConfiguration": {
               "description": "string",
               "kmsKeyId": "string",
               "roleArn": "string",
               "tableName": "string",
               "tags": {
                  "string" : "string"
               }
            },
            "s3Configuration": {
               "destinationIdentifier": "string",
               "kmsKeyId": "string",
               "ownerAccountId": "string",
               "roleArn": "string"
            }
         },
         "lastExecutionStatus": "string",
         "lastTriggeredTime": number,
         "lastUpdatedTime": number,
         "name": "string",
         "scheduledQueryArn": "string",
         "scheduleExpression": "string",
         "scheduleType": "string",
         "state": "string",
         "timezone": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListScheduledQueries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListScheduledQueries_ResponseSyntax) **   <a name="CWL-ListScheduledQueries-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

 ** [scheduledQueries](#API_ListScheduledQueries_ResponseSyntax) **   <a name="CWL-ListScheduledQueries-response-scheduledQueries"></a>
An array of scheduled query summary information.
Type: Array of [ScheduledQuerySummary](API_ScheduledQuerySummary.md) objects

## Errors
<a name="API_ListScheduledQueries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListScheduledQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/ListScheduledQueries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/ListScheduledQueries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ListScheduledQueries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/ListScheduledQueries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ListScheduledQueries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/ListScheduledQueries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/ListScheduledQueries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/ListScheduledQueries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/ListScheduledQueries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ListScheduledQueries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
