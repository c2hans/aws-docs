---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceStates.html
---

# ListServiceStates
<a name="API_ListServiceStates"></a>

Returns information about the last deployment and other change states of services. This API provides visibility into recent changes that may have affected service performance, helping with troubleshooting and change correlation.

## Request Syntax
<a name="API_ListServiceStates_RequestSyntax"></a>

```
POST /service/states HTTP/1.1
Content-type: application/json

{
   "AttributeFilters": [
      {
         "AttributeFilterName": "{{string}}",
         "AttributeFilterValues": [ "{{string}}" ]
      }
   ],
   "AwsAccountId": "{{string}}",
   "EndTime": {{number}},
   "IncludeLinkedAccounts": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTime": {{number}}
}
```

## URI Request Parameters
<a name="API_ListServiceStates_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListServiceStates_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttributeFilters](#API_ListServiceStates_RequestSyntax) **   <a name="applicationsignals-ListServiceStates-request-AttributeFilters"></a>
A list of attribute filters to narrow down the services. You can filter by platform, environment, or other service attributes.
Type: Array of [AttributeFilter](API_AttributeFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [AwsAccountId](#API_ListServiceStates_RequestSyntax) **   <a name="applicationsignals-ListServiceStates-request-AwsAccountId"></a>
The AWS account ID to filter service states by. Use this to limit results to services from a specific account.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [EndTime](#API_ListServiceStates_RequestSyntax) **   <a name="applicationsignals-ListServiceStates-request-EndTime"></a>
The end of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, `1698778057`.
Type: Timestamp
Required: Yes

 ** [IncludeLinkedAccounts](#API_ListServiceStates_RequestSyntax) **   <a name="applicationsignals-ListServiceStates-request-IncludeLinkedAccounts"></a>
If you are using this operation in a monitoring account, specify `true` to include service states from source accounts in the returned data.
Type: Boolean
Required: No

 ** [MaxResults](#API_ListServiceStates_RequestSyntax) **   <a name="applicationsignals-ListServiceStates-request-MaxResults"></a>
The maximum number of service states to return in one operation. If you omit this parameter, the default of 20 is used.
Type: Integer
Valid Range: Maximum value of 250.
Required: No

 ** [NextToken](#API_ListServiceStates_RequestSyntax) **   <a name="applicationsignals-ListServiceStates-request-NextToken"></a>
Include this value, if it was returned by the previous operation, to get the next set of service states.
Type: String
Required: No

 ** [StartTime](#API_ListServiceStates_RequestSyntax) **   <a name="applicationsignals-ListServiceStates-request-StartTime"></a>
The start of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, `1698778057`.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_ListServiceStates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EndTime": number,
   "NextToken": "string",
   "ServiceStates": [
      {
         "AttributeFilters": [
            {
               "AttributeFilterName": "string",
               "AttributeFilterValues": [ "string" ]
            }
         ],
         "LatestChangeEvents": [
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
         "Service": {
            "string" : "string"
         }
      }
   ],
   "StartTime": number
}
```

## Response Elements
<a name="API_ListServiceStates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndTime](#API_ListServiceStates_ResponseSyntax) **   <a name="applicationsignals-ListServiceStates-response-EndTime"></a>
The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, `1698778057`.
Type: Timestamp

 ** [NextToken](#API_ListServiceStates_ResponseSyntax) **   <a name="applicationsignals-ListServiceStates-response-NextToken"></a>
Include this value in your next use of this API to get the next set of service states.
Type: String

 ** [ServiceStates](#API_ListServiceStates_ResponseSyntax) **   <a name="applicationsignals-ListServiceStates-response-ServiceStates"></a>
An array of structures, where each structure contains information about the state of one service, including its latest change events such as deployments.
Type: Array of [ServiceState](API_ServiceState.md) objects
Array Members: Minimum number of 0 items. Maximum number of 250 items.

 ** [StartTime](#API_ListServiceStates_ResponseSyntax) **   <a name="applicationsignals-ListServiceStates-response-StartTime"></a>
The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, `1698778057`.
Type: Timestamp

## Errors
<a name="API_ListServiceStates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceStates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/ListServiceStates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/ListServiceStates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ListServiceStates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/ListServiceStates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ListServiceStates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/ListServiceStates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/ListServiceStates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/ListServiceStates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/ListServiceStates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ListServiceStates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
