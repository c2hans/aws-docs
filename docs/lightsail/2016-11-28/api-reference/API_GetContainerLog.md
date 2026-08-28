---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetContainerLog.html
---

# GetContainerLog
<a name="API_GetContainerLog"></a>

Returns the log events of a container of your Amazon Lightsail container service.

If your container service has more than one node (i.e., a scale greater than 1), then the log events that are returned for the specified container are merged from all nodes on your container service.

**Note**
Container logs are retained for a certain amount of time. For more information, see [Amazon Lightsail endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/lightsail.html) in the * AWS General Reference*.

## Request Syntax
<a name="API_GetContainerLog_RequestSyntax"></a>

```
{
   "containerName": "{{string}}",
   "endTime": {{number}},
   "filterPattern": "{{string}}",
   "pageToken": "{{string}}",
   "serviceName": "{{string}}",
   "startTime": {{number}}
}
```

## Request Parameters
<a name="API_GetContainerLog_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [containerName](#API_GetContainerLog_RequestSyntax) **   <a name="Lightsail-GetContainerLog-request-containerName"></a>
The name of the container that is either running or previously ran on the container service for which to return a log.
Type: String
Required: Yes

 ** [endTime](#API_GetContainerLog_RequestSyntax) **   <a name="Lightsail-GetContainerLog-request-endTime"></a>
The end of the time interval for which to get log data.
Constraints:
+ Specified in Coordinated Universal Time (UTC).
+ Specified in the Unix time format.

  For example, if you wish to use an end time of October 1, 2018, at 9 PM UTC, specify `1538427600` as the end time.
You can convert a human-friendly time to Unix time format using a converter like [Epoch converter](https://www.epochconverter.com/).
Type: Timestamp
Required: No

 ** [filterPattern](#API_GetContainerLog_RequestSyntax) **   <a name="Lightsail-GetContainerLog-request-filterPattern"></a>
The pattern to use to filter the returned log events to a specific term.
The following are a few examples of filter patterns that you can specify:
+ To return all log events, specify a filter pattern of `""`.
+ To exclude log events that contain the `ERROR` term, and return all other log events, specify a filter pattern of `"-ERROR"`.
+ To return log events that contain the `ERROR` term, specify a filter pattern of `"ERROR"`.
+ To return log events that contain both the `ERROR` and `Exception` terms, specify a filter pattern of `"ERROR Exception"`.
+ To return log events that contain the `ERROR` *or* the `Exception` term, specify a filter pattern of `"?ERROR ?Exception"`.
Type: String
Required: No

 ** [pageToken](#API_GetContainerLog_RequestSyntax) **   <a name="Lightsail-GetContainerLog-request-pageToken"></a>
The token to advance to the next page of results from your request.
To get a page token, perform an initial `GetContainerLog` request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.
Type: String
Required: No

 ** [serviceName](#API_GetContainerLog_RequestSyntax) **   <a name="Lightsail-GetContainerLog-request-serviceName"></a>
The name of the container service for which to get a container log.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: Yes

 ** [startTime](#API_GetContainerLog_RequestSyntax) **   <a name="Lightsail-GetContainerLog-request-startTime"></a>
The start of the time interval for which to get log data.
Constraints:
+ Specified in Coordinated Universal Time (UTC).
+ Specified in the Unix time format.

  For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, specify `1538424000` as the start time.
You can convert a human-friendly time to Unix time format using a converter like [Epoch converter](https://www.epochconverter.com/).
Type: Timestamp
Required: No

## Response Syntax
<a name="API_GetContainerLog_ResponseSyntax"></a>

```
{
   "logEvents": [
      {
         "createdAt": number,
         "message": "string"
      }
   ],
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetContainerLog_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logEvents](#API_GetContainerLog_ResponseSyntax) **   <a name="Lightsail-GetContainerLog-response-logEvents"></a>
An array of objects that describe the log events of a container.
Type: Array of [ContainerServiceLogEvent](API_ContainerServiceLogEvent.md) objects

 ** [nextPageToken](#API_GetContainerLog_ResponseSyntax) **   <a name="Lightsail-GetContainerLog-response-nextPageToken"></a>
The token to advance to the next page of results from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another `GetContainerLog` request and specify the next page token using the `pageToken` parameter.
Type: String

## Errors
<a name="API_GetContainerLog_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
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
<a name="API_GetContainerLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetContainerLog)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetContainerLog)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetContainerLog)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetContainerLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetContainerLog)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetContainerLog)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetContainerLog)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetContainerLog)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetContainerLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetContainerLog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
