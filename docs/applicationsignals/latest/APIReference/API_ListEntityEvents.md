---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListEntityEvents.html
---

# ListEntityEvents
<a name="API_ListEntityEvents"></a>

Returns a list of change events for a specific entity, such as deployments, configuration changes, or other state-changing activities. This operation helps track the history of changes that may have affected service performance.

## Request Syntax
<a name="API_ListEntityEvents_RequestSyntax"></a>

```
POST /events?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "Entity": {
      "{{string}}" : "{{string}}"
   },
   "StartTime": {{number}}
}
```

## URI Request Parameters
<a name="API_ListEntityEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListEntityEvents_RequestSyntax) **   <a name="applicationsignals-ListEntityEvents-request-uri-MaxResults"></a>
The maximum number of change events to return in one operation. If you omit this parameter, the default of 50 is used.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [NextToken](#API_ListEntityEvents_RequestSyntax) **   <a name="applicationsignals-ListEntityEvents-request-uri-NextToken"></a>
Include this value, if it was returned by the previous operation, to get the next set of change events.

## Request Body
<a name="API_ListEntityEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_ListEntityEvents_RequestSyntax) **   <a name="applicationsignals-ListEntityEvents-request-EndTime"></a>
The end of the time period to retrieve change events for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: `1698778057`
Type: Timestamp
Required: Yes

 ** [Entity](#API_ListEntityEvents_RequestSyntax) **   <a name="applicationsignals-ListEntityEvents-request-Entity"></a>
The entity for which to retrieve change events. This specifies the service, resource, or other entity whose event history you want to examine.
This is a string-to-string map. It can include the following fields.
+  `Type` designates the type of object this is.
+  `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service`, `RemoteService`, or `AWS::Service`.
+  `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Environment` specifies the location where this object is hosted, or what it belongs to.
+  `AwsAccountId` specifies the account where this object is in.
Below is an example of a service.
 `{ "Type": "Service", "Name": "visits-service", "Environment": "petclinic-test" }`
Below is an example of a resource.
 `{ "Type": "AWS::Resource", "ResourceType": "AWS::DynamoDB::Table", "Identifier": "Customers" }`
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: Yes

 ** [StartTime](#API_ListEntityEvents_RequestSyntax) **   <a name="applicationsignals-ListEntityEvents-request-StartTime"></a>
The start of the time period to retrieve change events for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: `1698778057`
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_ListEntityEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChangeEvents": [
      {
         "AccountId": "string",
         "ChangeEventType": "string",
         "Entity": {
            "string" : "string"
         },
         "EventId": "string",
         "EventName": "string",
         "Region": "string",
         "Timestamp": number,
         "UserName": "string"
      }
   ],
   "EndTime": number,
   "NextToken": "string",
   "StartTime": number
}
```

## Response Elements
<a name="API_ListEntityEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeEvents](#API_ListEntityEvents_ResponseSyntax) **   <a name="applicationsignals-ListEntityEvents-response-ChangeEvents"></a>
An array of structures, where each structure contains information about one change event that occurred for the specified entity during the requested time period.
Type: Array of [ChangeEvent](API_ChangeEvent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 250 items.

 ** [EndTime](#API_ListEntityEvents_ResponseSyntax) **   <a name="applicationsignals-ListEntityEvents-response-EndTime"></a>
The end of the time period that the returned change events apply to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: `1698778057`
Type: Timestamp

 ** [NextToken](#API_ListEntityEvents_ResponseSyntax) **   <a name="applicationsignals-ListEntityEvents-response-NextToken"></a>
Include this value in your next use of this API to get the next set of change events.
Type: String

 ** [StartTime](#API_ListEntityEvents_ResponseSyntax) **   <a name="applicationsignals-ListEntityEvents-response-StartTime"></a>
The start of the time period that the returned change events apply to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: `1698778057`
Type: Timestamp

## Errors
<a name="API_ListEntityEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListEntityEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/ListEntityEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/ListEntityEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ListEntityEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/ListEntityEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ListEntityEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/ListEntityEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/ListEntityEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/ListEntityEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/ListEntityEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ListEntityEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
