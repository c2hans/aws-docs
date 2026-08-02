---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_UpdateScheduledQuery.html
---

# UpdateScheduledQuery
<a name="API_query_UpdateScheduledQuery"></a>

Update a scheduled query.

## Request Syntax
<a name="API_query_UpdateScheduledQuery_RequestSyntax"></a>

```
{
   "ScheduledQueryArn": "{{string}}",
   "State": "{{string}}"
}
```

## Request Parameters
<a name="API_query_UpdateScheduledQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ScheduledQueryArn](#API_query_UpdateScheduledQuery_RequestSyntax) **   <a name="timestream-query_UpdateScheduledQuery-request-ScheduledQueryArn"></a>
ARN of the scheuled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [State](#API_query_UpdateScheduledQuery_RequestSyntax) **   <a name="timestream-query_UpdateScheduledQuery-request-State"></a>
State of the scheduled query.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## Response Elements
<a name="API_query_UpdateScheduledQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_query_UpdateScheduledQuery_Errors"></a>

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

## See Also
<a name="API_query_UpdateScheduledQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-query-2018-11-01/UpdateScheduledQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-query-2018-11-01/UpdateScheduledQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/UpdateScheduledQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-query-2018-11-01/UpdateScheduledQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/UpdateScheduledQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-query-2018-11-01/UpdateScheduledQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-query-2018-11-01/UpdateScheduledQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-query-2018-11-01/UpdateScheduledQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-query-2018-11-01/UpdateScheduledQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/UpdateScheduledQuery)
