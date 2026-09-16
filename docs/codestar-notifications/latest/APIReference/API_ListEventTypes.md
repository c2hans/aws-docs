---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListEventTypes.html
---

# ListEventTypes
<a name="API_ListEventTypes"></a>

Returns information about the event types available for configuring notifications.

## Request Syntax
<a name="API_ListEventTypes_RequestSyntax"></a>

```
POST /listEventTypes HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListEventTypes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListEventTypes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListEventTypes_RequestSyntax) **   <a name="codestarnotifications-ListEventTypes-request-Filters"></a>
The filters to use to return information by service or resource type.
Type: Array of [ListEventTypesFilter](API_ListEventTypesFilter.md) objects
Required: No

 ** [MaxResults](#API_ListEventTypes_RequestSyntax) **   <a name="codestarnotifications-ListEventTypes-request-MaxResults"></a>
A non-negative integer used to limit the number of returned results. The default number is 50. The maximum number of results that can be returned is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListEventTypes_RequestSyntax) **   <a name="codestarnotifications-ListEventTypes-request-NextToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Pattern: `^[\w/+=]+$`
Required: No

## Response Syntax
<a name="API_ListEventTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EventTypes": [
      {
         "EventTypeId": "string",
         "EventTypeName": "string",
         "ResourceType": "string",
         "ServiceName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEventTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventTypes](#API_ListEventTypes_ResponseSyntax) **   <a name="codestarnotifications-ListEventTypes-response-EventTypes"></a>
Information about each event, including service name, resource type, event ID, and event name.
Type: Array of [EventTypeSummary](API_EventTypeSummary.md) objects

 ** [NextToken](#API_ListEventTypes_ResponseSyntax) **   <a name="codestarnotifications-ListEventTypes-response-NextToken"></a>
An enumeration token that can be used in a request to return the next batch of the results.
Type: String
Pattern: `^[\w/+=]+$`

## Errors
<a name="API_ListEventTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The value for the enumeration token used in the request to return the next batch of the results is not valid.
HTTP Status Code: 400

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListEventTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/ListEventTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/ListEventTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/ListEventTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/ListEventTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/ListEventTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/ListEventTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/ListEventTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/ListEventTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/ListEventTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/ListEventTypes)
