---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchHoursOfOperations.html
---

# SearchHoursOfOperations
<a name="API_SearchHoursOfOperations"></a>

Searches the hours of operation in an Connect Customer instance, with optional filtering.

## Request Syntax
<a name="API_SearchHoursOfOperations_RequestSyntax"></a>

```
POST /search-hours-of-operations HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "HoursOfOperationSearchCriteria"
      ],
      "OrConditions": [
         "HoursOfOperationSearchCriteria"
      ],
      "StringCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "SearchFilter": {
      "TagFilter": {
         "AndConditions": [
            {
               "TagKey": "{{string}}",
               "TagValue": "{{string}}"
            }
         ],
         "OrConditions": [
            [
               {
                  "TagKey": "{{string}}",
                  "TagValue": "{{string}}"
               }
            ]
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
<a name="API_SearchHoursOfOperations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchHoursOfOperations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchHoursOfOperations_RequestSyntax) **   <a name="connect-SearchHoursOfOperations-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchHoursOfOperations_RequestSyntax) **   <a name="connect-SearchHoursOfOperations-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchHoursOfOperations_RequestSyntax) **   <a name="connect-SearchHoursOfOperations-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchHoursOfOperations_RequestSyntax) **   <a name="connect-SearchHoursOfOperations-request-SearchCriteria"></a>
The search criteria to be used to return hours of operations.
Type: [HoursOfOperationSearchCriteria](API_HoursOfOperationSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchHoursOfOperations_RequestSyntax) **   <a name="connect-SearchHoursOfOperations-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [HoursOfOperationSearchFilter](API_HoursOfOperationSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchHoursOfOperations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "HoursOfOperations": [
      {
         "Config": [
            {
               "Day": "string",
               "EndTime": {
                  "Hours": number,
                  "Minutes": number
               },
               "StartTime": {
                  "Hours": number,
                  "Minutes": number
               }
            }
         ],
         "Description": "string",
         "HoursOfOperationArn": "string",
         "HoursOfOperationId": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "ParentHoursOfOperations": [
            {
               "Arn": "string",
               "Id": "string",
               "Name": "string"
            }
         ],
         "Tags": {
            "string" : "string"
         },
         "TimeZone": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchHoursOfOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchHoursOfOperations_ResponseSyntax) **   <a name="connect-SearchHoursOfOperations-response-ApproximateTotalCount"></a>
The total number of hours of operations which matched your search query.
Type: Long

 ** [HoursOfOperations](#API_SearchHoursOfOperations_ResponseSyntax) **   <a name="connect-SearchHoursOfOperations-response-HoursOfOperations"></a>
Information about the hours of operations.
Type: Array of [HoursOfOperation](API_HoursOfOperation.md) objects

 ** [NextToken](#API_SearchHoursOfOperations_ResponseSyntax) **   <a name="connect-SearchHoursOfOperations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

## Errors
<a name="API_SearchHoursOfOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_SearchHoursOfOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchHoursOfOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchHoursOfOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchHoursOfOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchHoursOfOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchHoursOfOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchHoursOfOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchHoursOfOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchHoursOfOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchHoursOfOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchHoursOfOperations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
