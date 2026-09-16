---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchMetrics.html
---

# SearchMetrics
<a name="API_SearchMetrics"></a>

Searches for metrics in the specified Connect Customer instance using search criteria and optional tag-based filters. Use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_SearchMetrics_RequestSyntax"></a>

```
POST /search-metrics HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "MetricSearchCriteria"
      ],
      "BooleanCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}"
      },
      "OrConditions": [
         "MetricSearchCriteria"
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
<a name="API_SearchMetrics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchMetrics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchMetrics_RequestSyntax) **   <a name="connect-SearchMetrics-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchMetrics_RequestSyntax) **   <a name="connect-SearchMetrics-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchMetrics_RequestSyntax) **   <a name="connect-SearchMetrics-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Required: No

 ** [SearchCriteria](#API_SearchMetrics_RequestSyntax) **   <a name="connect-SearchMetrics-request-SearchCriteria"></a>
The search criteria to filter the metrics.
Type: [MetricSearchCriteria](API_MetricSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchMetrics_RequestSyntax) **   <a name="connect-SearchMetrics-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [MetricSearchFilter](API_MetricSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "Metrics": [
      {
         "Arn": "string",
         "Category": "string",
         "CreatedTime": number,
         "CreatedUser": { ... },
         "CreationMethod": "string",
         "DefaultStat": "string",
         "Description": "string",
         "EffectiveTime": number,
         "Filters": [
            {
               "Id": "string",
               "Type": "string"
            }
         ],
         "Groupings": [ "string" ],
         "Id": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "LastModifiedUser": { ... },
         "MetricCalculation": {
            "Calculation": "string",
            "CalculationComponents": [
               {
                  "Alias": "string",
                  "MetricFilters": [
                     {
                        "BooleanCondition": {
                           "Comparison": "string"
                        },
                        "MetricFilterKey": "string",
                        "Negate": boolean,
                        "NumberCondition": {
                           "Comparison": "string",
                           "Values": [ number ]
                        },
                        "StringCondition": {
                           "Comparison": "string",
                           "Values": [ "string" ]
                        }
                     }
                  ],
                  "MetricId": "string",
                  "MetricName": "string"
               }
            ]
         },
         "Name": "string",
         "PositiveTrendIndicator": "string",
         "PrimaryEventSource": "string",
         "PrimaryEventSourceEffectiveTimestampType": "string",
         "RefreshRate": number,
         "Status": "string",
         "SupportedStats": [ "string" ],
         "SupportsCustomCalculation": boolean,
         "SupportsPreaggregateCalculation": boolean,
         "Tags": {
            "string" : "string"
         },
         "Type": "string",
         "Unit": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchMetrics_ResponseSyntax) **   <a name="connect-SearchMetrics-response-ApproximateTotalCount"></a>
The approximate total number of metrics that matched your search criteria.
Type: Long

 ** [Metrics](#API_SearchMetrics_ResponseSyntax) **   <a name="connect-SearchMetrics-response-Metrics"></a>
The metrics that matched the search criteria.
Type: Array of [MetricDefinition](API_MetricDefinition.md) objects

 ** [NextToken](#API_SearchMetrics_ResponseSyntax) **   <a name="connect-SearchMetrics-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_SearchMetrics_Errors"></a>

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

## Examples
<a name="API_SearchMetrics_Examples"></a>

### Example
<a name="API_SearchMetrics_Example_1"></a>

The following example searches for customer-managed metrics whose name contains "test".

#### Sample Request
<a name="API_SearchMetrics_Example_1_Request"></a>

```
{
    "InstanceId": "12345678-1234-1234-1234-123456789012",
    "SearchCriteria": {
        "AndConditions": [
            {
                "StringCondition": {
                    "ComparisonType": "EXACT",
                    "FieldName": "type",
                    "Value": "CUSTOMER_MANAGED"
                }
            },
            {
                "StringCondition": {
                    "ComparisonType": "CONTAINS",
                    "FieldName": "name",
                    "Value": "test"
                }
            }
        ]
    },
    "MaxResults": 10
}
```

## See Also
<a name="API_SearchMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchMetrics)
