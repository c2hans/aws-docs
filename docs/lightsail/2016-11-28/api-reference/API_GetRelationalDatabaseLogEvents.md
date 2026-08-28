---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRelationalDatabaseLogEvents.html
---

# GetRelationalDatabaseLogEvents
<a name="API_GetRelationalDatabaseLogEvents"></a>

Returns a list of log events for a database in Amazon Lightsail.

## Request Syntax
<a name="API_GetRelationalDatabaseLogEvents_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "logStreamName": "{{string}}",
   "pageToken": "{{string}}",
   "relationalDatabaseName": "{{string}}",
   "startFromHead": {{boolean}},
   "startTime": {{number}}
}
```

## Request Parameters
<a name="API_GetRelationalDatabaseLogEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_GetRelationalDatabaseLogEvents_RequestSyntax) **   <a name="Lightsail-GetRelationalDatabaseLogEvents-request-endTime"></a>
The end of the time interval from which to get log events.
Constraints:
+ Specified in Coordinated Universal Time (UTC).
+ Specified in the Unix time format.

  For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input `1538424000` as the end time.
Type: Timestamp
Required: No

 ** [logStreamName](#API_GetRelationalDatabaseLogEvents_RequestSyntax) **   <a name="Lightsail-GetRelationalDatabaseLogEvents-request-logStreamName"></a>
The name of the log stream.
Use the `get relational database log streams` operation to get a list of available log streams.
Type: String
Required: Yes

 ** [pageToken](#API_GetRelationalDatabaseLogEvents_RequestSyntax) **   <a name="Lightsail-GetRelationalDatabaseLogEvents-request-pageToken"></a>
The token to advance to the next or previous page of results from your request.
To get a page token, perform an initial `GetRelationalDatabaseLogEvents` request. If your results are paginated, the response will return a next forward token and/or next backward token that you can specify as the page token in a subsequent request.
Type: String
Required: No

 ** [relationalDatabaseName](#API_GetRelationalDatabaseLogEvents_RequestSyntax) **   <a name="Lightsail-GetRelationalDatabaseLogEvents-request-relationalDatabaseName"></a>
The name of your database for which to get log events.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [startFromHead](#API_GetRelationalDatabaseLogEvents_RequestSyntax) **   <a name="Lightsail-GetRelationalDatabaseLogEvents-request-startFromHead"></a>
Parameter to specify if the log should start from head or tail. If `true` is specified, the log event starts from the head of the log. If `false` is specified, the log event starts from the tail of the log.
For PostgreSQL, the default value of `false` is the only option available.
Type: Boolean
Required: No

 ** [startTime](#API_GetRelationalDatabaseLogEvents_RequestSyntax) **   <a name="Lightsail-GetRelationalDatabaseLogEvents-request-startTime"></a>
The start of the time interval from which to get log events.
Constraints:
+ Specified in Coordinated Universal Time (UTC).
+ Specified in the Unix time format.

  For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input `1538424000` as the start time.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_GetRelationalDatabaseLogEvents_ResponseSyntax"></a>

```
{
   "nextBackwardToken": "string",
   "nextForwardToken": "string",
   "resourceLogEvents": [
      {
         "createdAt": number,
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetRelationalDatabaseLogEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextBackwardToken](#API_GetRelationalDatabaseLogEvents_ResponseSyntax) **   <a name="Lightsail-GetRelationalDatabaseLogEvents-response-nextBackwardToken"></a>
A token used for advancing to the previous page of results from your get relational database log events request.
Type: String

 ** [nextForwardToken](#API_GetRelationalDatabaseLogEvents_ResponseSyntax) **   <a name="Lightsail-GetRelationalDatabaseLogEvents-response-nextForwardToken"></a>
A token used for advancing to the next page of results from your get relational database log events request.
Type: String

 ** [resourceLogEvents](#API_GetRelationalDatabaseLogEvents_ResponseSyntax) **   <a name="Lightsail-GetRelationalDatabaseLogEvents-response-resourceLogEvents"></a>
An object describing the result of your get relational database log events request.
Type: Array of [LogEvent](API_LogEvent.md) objects

## Errors
<a name="API_GetRelationalDatabaseLogEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** AccountSetupInProgressException **
Lightsail throws this exception when an account is still in the setup in progress state.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetRelationalDatabaseLogEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
