---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchNotifications.html
---

# SearchNotifications
<a name="API_SearchNotifications"></a>

Searches for notifications based on specified criteria and filters. Returns a paginated list of notifications matching the search parameters, ordered by descending creation time. Supports filtering by content and tags.

## Request Syntax
<a name="API_SearchNotifications_RequestSyntax"></a>

```
POST /search-notifications HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "NotificationSearchCriteria"
      ],
      "OrConditions": [
         "NotificationSearchCriteria"
      ],
      "StringCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "SearchFilter": {
      "AttributeFilter": {
         "AndCondition": {
            "TagConditions": [
               {
                  "TagKey": "{{string}}",
                  "TagValue": "{{string}}"
               }
            ]
         },
         "OrConditions": [
            {
               "TagConditions": [
                  {
                     "TagKey": "{{string}}",
                     "TagValue": "{{string}}"
                  }
               ]
            }
         ],
         "TagCondition": {
            "TagKey": "{{string}}",
            "TagValue": "{{string}}"
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_SearchNotifications_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchNotifications_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchNotifications_RequestSyntax) **   <a name="connect-SearchNotifications-request-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchNotifications_RequestSyntax) **   <a name="connect-SearchNotifications-request-MaxResults"></a>
The maximum number of results to return per page. Valid range is 1-100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchNotifications_RequestSyntax) **   <a name="connect-SearchNotifications-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response to retrieve the next page of results.
Type: String
Required: No

 ** [SearchCriteria](#API_SearchNotifications_RequestSyntax) **   <a name="connect-SearchNotifications-request-SearchCriteria"></a>
The search criteria to apply when searching for notifications. Supports filtering by notification ID and message content using comparison types such as STARTS\_WITH, CONTAINS, and EXACT.
Type: [NotificationSearchCriteria](API_NotificationSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchNotifications_RequestSyntax) **   <a name="connect-SearchNotifications-request-SearchFilter"></a>
Filters to apply to the search results, such as tag-based filters.
Type: [NotificationSearchFilter](API_NotificationSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchNotifications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "Notifications": [
      {
         "Arn": "string",
         "Content": {
            "string" : "string"
         },
         "CreatedAt": number,
         "ExpiresAt": number,
         "Id": "string",
         "InstanceId": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "Priority": "string",
         "Recipients": [ "string" ],
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchNotifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchNotifications_ResponseSyntax) **   <a name="connect-SearchNotifications-response-ApproximateTotalCount"></a>
The approximate total number of notifications matching the search criteria.
Type: Long

 ** [NextToken](#API_SearchNotifications_ResponseSyntax) **   <a name="connect-SearchNotifications-response-NextToken"></a>
The token for the next set of results. If present, there are more results available.
Type: String

 ** [Notifications](#API_SearchNotifications_ResponseSyntax) **   <a name="connect-SearchNotifications-response-Notifications"></a>
A list of notifications matching the search criteria.
Type: Array of [NotificationSearchSummary](API_NotificationSearchSummary.md) objects

## Errors
<a name="API_SearchNotifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_SearchNotifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchNotifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchNotifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchNotifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchNotifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchNotifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchNotifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchNotifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchNotifications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchNotifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchNotifications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
