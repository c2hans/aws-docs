---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupingStatuses.html
---

# ListGroupingStatuses
<a name="API_ListGroupingStatuses"></a>

Returns the status of the last grouping or ungrouping action for each resource in the specified application group.

## Request Syntax
<a name="API_ListGroupingStatuses_RequestSyntax"></a>

```
POST /list-grouping-statuses HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Group": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListGroupingStatuses_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListGroupingStatuses_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Group](#API_ListGroupingStatuses_RequestSyntax) **   <a name="ARG-ListGroupingStatuses-request-Group"></a>
The application group identifier, expressed as an Amazon resource name (ARN) or the application group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}|arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: Yes

 ** [Filters](#API_ListGroupingStatuses_RequestSyntax) **   <a name="ARG-ListGroupingStatuses-request-Filters"></a>
The filter name and value pair that is used to return more specific results from a list of resources.
Type: Array of [ListGroupingStatusesFilter](API_ListGroupingStatusesFilter.md) objects
Required: No

 ** [MaxResults](#API_ListGroupingStatuses_RequestSyntax) **   <a name="ARG-ListGroupingStatuses-request-MaxResults"></a>
The maximum number of resources and their statuses returned in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListGroupingStatuses_RequestSyntax) **   <a name="ARG-ListGroupingStatuses-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value provided by a previous call's `NextToken` response to indicate where the output should continue from.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9+/]*={0,2}$`
Required: No

## Response Syntax
<a name="API_ListGroupingStatuses_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Group": "string",
   "GroupingStatuses": [
      {
         "Action": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "ResourceArn": "string",
         "Status": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListGroupingStatuses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Group](#API_ListGroupingStatuses_ResponseSyntax) **   <a name="ARG-ListGroupingStatuses-response-Group"></a>
The application group identifier, expressed as an Amazon resource name (ARN) or the application group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}|arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`

 ** [GroupingStatuses](#API_ListGroupingStatuses_ResponseSyntax) **   <a name="ARG-ListGroupingStatuses-response-GroupingStatuses"></a>
Returns details about the grouping or ungrouping status of the resources in the specified application group.
Type: Array of [GroupingStatusesItem](API_GroupingStatusesItem.md) objects

 ** [NextToken](#API_ListGroupingStatuses_ResponseSyntax) **   <a name="ARG-ListGroupingStatuses-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9+/]*={0,2}$`

## Errors
<a name="API_ListGroupingStatuses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The request includes one or more parameters that violate validation rules.
HTTP Status Code: 400

 ** ForbiddenException **
The caller isn't authorized to make the request. Check permissions.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal error occurred while processing the request. Try again later.
HTTP Status Code: 500

 ** MethodNotAllowedException **
The request uses an HTTP method that isn't allowed for the specified resource.
HTTP Status Code: 405

 ** TooManyRequestsException **
You've exceeded throttling limits by making too many requests in a period of time.
HTTP Status Code: 429

## See Also
<a name="API_ListGroupingStatuses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/ListGroupingStatuses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/ListGroupingStatuses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/ListGroupingStatuses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/ListGroupingStatuses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/ListGroupingStatuses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/ListGroupingStatuses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/ListGroupingStatuses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/ListGroupingStatuses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/ListGroupingStatuses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/ListGroupingStatuses)
