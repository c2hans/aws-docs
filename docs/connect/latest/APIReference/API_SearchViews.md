---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchViews.html
---

# SearchViews
<a name="API_SearchViews"></a>

Searches views based on name, description, or tags.

## Request Syntax
<a name="API_SearchViews_RequestSyntax"></a>

```
POST /search-views HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "ViewSearchCriteria"
      ],
      "OrConditions": [
         "ViewSearchCriteria"
      ],
      "StringCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      },
      "ViewStatusCondition": "{{string}}",
      "ViewTypeCondition": "{{string}}"
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
<a name="API_SearchViews_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchViews_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchViews_RequestSyntax) **   <a name="connect-SearchViews-request-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [MaxResults](#API_SearchViews_RequestSyntax) **   <a name="connect-SearchViews-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchViews_RequestSyntax) **   <a name="connect-SearchViews-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchViews_RequestSyntax) **   <a name="connect-SearchViews-request-SearchCriteria"></a>
The search criteria, including field names and comparison types.
Type: [ViewSearchCriteria](API_ViewSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchViews_RequestSyntax) **   <a name="connect-SearchViews-request-SearchFilter"></a>
Filters to apply to the search, such as tag-based filters.
Type: [ViewSearchFilter](API_ViewSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchViews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "Views": [
      {
         "Arn": "string",
         "Content": {
            "Actions": [ "string" ],
            "InputSchema": "string",
            "Template": "string"
         },
         "CreatedTime": number,
         "Description": "string",
         "Id": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "Status": "string",
         "Tags": {
            "string" : "string"
         },
         "Type": "string",
         "Version": number,
         "VersionDescription": "string",
         "ViewContentSha256": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchViews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchViews_ResponseSyntax) **   <a name="connect-SearchViews-response-ApproximateTotalCount"></a>
The approximate total number of views that match the search criteria.
Type: Long

 ** [NextToken](#API_SearchViews_ResponseSyntax) **   <a name="connect-SearchViews-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [Views](#API_SearchViews_ResponseSyntax) **   <a name="connect-SearchViews-response-Views"></a>
A list of views that match the search criteria.
Type: Array of [View](API_View.md) objects

## Errors
<a name="API_SearchViews_Errors"></a>

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
<a name="API_SearchViews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchViews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchViews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchViews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchViews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchViews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchViews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchViews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchViews)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchViews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchViews)
