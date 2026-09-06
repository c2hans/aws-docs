---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchHoursOfOperationOverrides.html
---

# SearchHoursOfOperationOverrides
<a name="API_SearchHoursOfOperationOverrides"></a>

Searches the hours of operation overrides.

## Request Syntax
<a name="API_SearchHoursOfOperationOverrides_RequestSyntax"></a>

```
POST /search-hours-of-operation-overrides HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "HoursOfOperationOverrideSearchCriteria"
      ],
      "DateCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      },
      "OrConditions": [
         "HoursOfOperationOverrideSearchCriteria"
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
<a name="API_SearchHoursOfOperationOverrides_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchHoursOfOperationOverrides_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchHoursOfOperationOverrides_RequestSyntax) **   <a name="connect-SearchHoursOfOperationOverrides-request-InstanceId"></a>
The identifier of the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchHoursOfOperationOverrides_RequestSyntax) **   <a name="connect-SearchHoursOfOperationOverrides-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchHoursOfOperationOverrides_RequestSyntax) **   <a name="connect-SearchHoursOfOperationOverrides-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchHoursOfOperationOverrides_RequestSyntax) **   <a name="connect-SearchHoursOfOperationOverrides-request-SearchCriteria"></a>
The search criteria to be used to return hours of operations overrides.
Type: [HoursOfOperationOverrideSearchCriteria](API_HoursOfOperationOverrideSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchHoursOfOperationOverrides_RequestSyntax) **   <a name="connect-SearchHoursOfOperationOverrides-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [HoursOfOperationSearchFilter](API_HoursOfOperationSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchHoursOfOperationOverrides_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "HoursOfOperationOverrides": [
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
         "EffectiveFrom": "string",
         "EffectiveTill": "string",
         "HoursOfOperationArn": "string",
         "HoursOfOperationId": "string",
         "HoursOfOperationOverrideId": "string",
         "Name": "string",
         "OverrideType": "string",
         "RecurrenceConfig": {
            "RecurrencePattern": {
               "ByMonth": [ number ],
               "ByMonthDay": [ number ],
               "ByWeekdayOccurrence": [ number ],
               "Frequency": "string",
               "Interval": number
            }
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchHoursOfOperationOverrides_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchHoursOfOperationOverrides_ResponseSyntax) **   <a name="connect-SearchHoursOfOperationOverrides-response-ApproximateTotalCount"></a>
The total number of hours of operations which matched your search query.
Type: Long

 ** [HoursOfOperationOverrides](#API_SearchHoursOfOperationOverrides_ResponseSyntax) **   <a name="connect-SearchHoursOfOperationOverrides-response-HoursOfOperationOverrides"></a>
Information about the hours of operations overrides.
Type: Array of [HoursOfOperationOverride](API_HoursOfOperationOverride.md) objects

 ** [NextToken](#API_SearchHoursOfOperationOverrides_ResponseSyntax) **   <a name="connect-SearchHoursOfOperationOverrides-response-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

## Errors
<a name="API_SearchHoursOfOperationOverrides_Errors"></a>

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
<a name="API_SearchHoursOfOperationOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchHoursOfOperationOverrides)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchHoursOfOperationOverrides)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchHoursOfOperationOverrides)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchHoursOfOperationOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchHoursOfOperationOverrides)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchHoursOfOperationOverrides)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchHoursOfOperationOverrides)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchHoursOfOperationOverrides)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchHoursOfOperationOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchHoursOfOperationOverrides)
