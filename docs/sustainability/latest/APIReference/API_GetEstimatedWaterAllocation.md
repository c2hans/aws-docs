---
source_url: https://docs.aws.amazon.com/sustainability/latest/APIReference/API_GetEstimatedWaterAllocation.html
---

# GetEstimatedWaterAllocation
<a name="API_GetEstimatedWaterAllocation"></a>

Returns estimated water allocation values based on customer grouping and filtering parameters. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_GetEstimatedWaterAllocation_RequestSyntax"></a>

```
POST /v1/estimated-water-allocation HTTP/1.1
Content-type: application/json

{
   "AllocationTypes": [ "{{string}}" ],
   "FilterBy": {
      "Dimensions": {
         "{{string}}" : [ "{{string}}" ]
      }
   },
   "Granularity": "{{string}}",
   "GroupBy": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_GetEstimatedWaterAllocation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEstimatedWaterAllocation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TimePeriod](#API_GetEstimatedWaterAllocation_RequestSyntax) **   <a name="sustainability-GetEstimatedWaterAllocation-request-TimePeriod"></a>
 The date range for fetching estimated water allocation. The range must include the start date of a year for that year's data to be included in the response.
Type: [TimePeriod](API_TimePeriod.md) object
Required: Yes

 ** [AllocationTypes](#API_GetEstimatedWaterAllocation_RequestSyntax) **   <a name="sustainability-GetEstimatedWaterAllocation-request-AllocationTypes"></a>
The allocation types to include in the results. If absent, returns `TOTAL_WATER_WITHDRAWALS` allocation types.
Type: Array of strings
Valid Values: `TOTAL_WATER_WITHDRAWALS`
Required: No

 ** [FilterBy](#API_GetEstimatedWaterAllocation_RequestSyntax) **   <a name="sustainability-GetEstimatedWaterAllocation-request-FilterBy"></a>
 The criteria for filtering estimated water allocation. To determine which dimensions are available to be filtered by, you can first call [GetEstimatedWaterAllocationDimensionValues](API_GetEstimatedWaterAllocationDimensionValues.md)
Type: [FilterExpression](API_FilterExpression.md) object
Required: No

 ** [Granularity](#API_GetEstimatedWaterAllocation_RequestSyntax) **   <a name="sustainability-GetEstimatedWaterAllocation-request-Granularity"></a>
The time granularity for the results. Only `YEARLY_CALENDAR` time granularity is currently supported for water allocation. Defaults to `YEARLY_CALENDAR` if absent.
 If requesting partial time periods, data will be returned based on the smallest supported granularity. For example, requesting `2025-04-01T00:00:00Z` to `2026-04-01T00:00:00Z` with `YEARLY_CALENDAR` will return all the data for 2026 only.
Type: String
Valid Values: `YEARLY_CALENDAR | YEARLY_FISCAL | QUARTERLY_CALENDAR | QUARTERLY_FISCAL | MONTHLY`
Required: No

 ** [GroupBy](#API_GetEstimatedWaterAllocation_RequestSyntax) **   <a name="sustainability-GetEstimatedWaterAllocation-request-GroupBy"></a>
The dimensions available for grouping estimated water allocation.
Type: Array of strings
Valid Values: `USAGE_ACCOUNT_ID | REGION | SERVICE`
Required: No

 ** [MaxResults](#API_GetEstimatedWaterAllocation_RequestSyntax) **   <a name="sustainability-GetEstimatedWaterAllocation-request-MaxResults"></a>
The maximum number of results to return in a single call. Default is 1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** [NextToken](#API_GetEstimatedWaterAllocation_RequestSyntax) **   <a name="sustainability-GetEstimatedWaterAllocation-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_GetEstimatedWaterAllocation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Results": [
      {
         "AllocationValues": {
            "string" : {
               "Unit": "string",
               "Value": number
            }
         },
         "DimensionsValues": {
            "string" : "string"
         },
         "ModelVersion": "string",
         "TimePeriod": {
            "End": "string",
            "Start": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetEstimatedWaterAllocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_GetEstimatedWaterAllocation_ResponseSyntax) **   <a name="sustainability-GetEstimatedWaterAllocation-response-Results"></a>
The result of the requested inputs.
Type: Array of [EstimatedWaterAllocation](API_EstimatedWaterAllocation.md) objects

 ** [NextToken](#API_GetEstimatedWaterAllocation_ResponseSyntax) **   <a name="sustainability-GetEstimatedWaterAllocation-response-NextToken"></a>
The pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_GetEstimatedWaterAllocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_GetEstimatedWaterAllocation_Examples"></a>

### GetEstimatedWaterAllocation
<a name="API_GetEstimatedWaterAllocation_Example_1"></a>

This example illustrates one usage of GetEstimatedWaterAllocation.

#### Sample Request
<a name="API_GetEstimatedWaterAllocation_Example_1_Request"></a>

```
POST /v1/estimated-water-allocation
{
    "TimePeriod": {
        "Start": "2025-01-01T00:00:00Z",
        "End": "2025-12-31T23:59:59.999Z"
    },
    "GroupBy": [
        "SERVICE"
    ],
    "AllocationTypes": [
        "TOTAL_WATER_WITHDRAWALS"
    ],
    "Granularity": "YEARLY_CALENDAR"
}
```

#### Sample Response
<a name="API_GetEstimatedWaterAllocation_Example_1_Response"></a>

```
{
    "Results": [
        {
            "DimensionsValues": {
                "SERVICE": "AmazonEC2"
            },
            "AllocationValues": {
                "TOTAL_WATER_WITHDRAWALS": {
                    "Unit": "m3",
                    "Value": 1
                }
            },
            "ModelVersion": "v1.0.0",
            "TimePeriod": {
                "Start": "2025-01-01T00:00:00Z",
                "End": "2025-12-31T23:59:59.999Z"
            }
        }
    ]
}
```

## See Also
<a name="API_GetEstimatedWaterAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sustainability-2018-05-10/GetEstimatedWaterAllocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sustainability-2018-05-10/GetEstimatedWaterAllocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sustainability-2018-05-10/GetEstimatedWaterAllocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sustainability-2018-05-10/GetEstimatedWaterAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sustainability-2018-05-10/GetEstimatedWaterAllocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sustainability-2018-05-10/GetEstimatedWaterAllocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sustainability-2018-05-10/GetEstimatedWaterAllocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sustainability-2018-05-10/GetEstimatedWaterAllocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sustainability-2018-05-10/GetEstimatedWaterAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sustainability-2018-05-10/GetEstimatedWaterAllocation)
