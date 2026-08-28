---
source_url: https://docs.aws.amazon.com/sustainability/latest/APIReference/API_GetEstimatedCarbonEmissions.html
---

# GetEstimatedCarbonEmissions
<a name="API_GetEstimatedCarbonEmissions"></a>

Returns estimated carbon emission values based on customer grouping and filtering parameters. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_GetEstimatedCarbonEmissions_RequestSyntax"></a>

```
POST /v1/estimated-carbon-emissions HTTP/1.1
Content-type: application/json

{
   "EmissionsTypes": [ "{{string}}" ],
   "FilterBy": {
      "Dimensions": {
         "{{string}}" : [ "{{string}}" ]
      }
   },
   "Granularity": "{{string}}",
   "GranularityConfiguration": {
      "FiscalYearStartMonth": {{number}}
   },
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
<a name="API_GetEstimatedCarbonEmissions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEstimatedCarbonEmissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TimePeriod](#API_GetEstimatedCarbonEmissions_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-request-TimePeriod"></a>
 The date range for fetching estimated carbon emissions. The range must include the start date of a month for that month's data to be included in the response.
Type: [TimePeriod](API_TimePeriod.md) object
Required: Yes

 ** [EmissionsTypes](#API_GetEstimatedCarbonEmissions_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-request-EmissionsTypes"></a>
The emission types to include in the results. If absent, returns `TOTAL_LBM_CARBON_EMISSIONS` and `TOTAL_MBM_CARBON_EMISSIONS` emissions types.
Type: Array of strings
Valid Values: `TOTAL_LBM_CARBON_EMISSIONS | TOTAL_MBM_CARBON_EMISSIONS | TOTAL_SCOPE_1_CARBON_EMISSIONS | TOTAL_SCOPE_2_LBM_CARBON_EMISSIONS | TOTAL_SCOPE_2_MBM_CARBON_EMISSIONS | TOTAL_SCOPE_3_LBM_CARBON_EMISSIONS | TOTAL_SCOPE_3_MBM_CARBON_EMISSIONS`
Required: No

 ** [FilterBy](#API_GetEstimatedCarbonEmissions_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-request-FilterBy"></a>
 The criteria for filtering estimated carbon emissions. To determine which dimensions are available to be filtered by, you can first call [GetEstimatedCarbonEmissionsDimensionValues](API_GetEstimatedCarbonEmissionsDimensionValues.md)
Type: [FilterExpression](API_FilterExpression.md) object
Required: No

 ** [Granularity](#API_GetEstimatedCarbonEmissions_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-request-Granularity"></a>
 The time granularity for the results. If absent, uses `MONTHLY` time granularity. The smallest supported granularity for carbon emissions is `MONTHLY`.
 If requesting partial time periods, data will be returned based on the smallest supported granularity. For example, requesting `2025-04-01T00:00:00Z` to `2026-04-01T00:00:00Z` with `YEARLY_CALENDAR` granularity will return the last 9 months for 2025 and the first 3 months of 2026.
Type: String
Valid Values: `YEARLY_CALENDAR | YEARLY_FISCAL | QUARTERLY_CALENDAR | QUARTERLY_FISCAL | MONTHLY`
Required: No

 ** [GranularityConfiguration](#API_GetEstimatedCarbonEmissions_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-request-GranularityConfiguration"></a>
Configuration for fiscal year calculations when using `YEARLY_FISCAL` or `QUARTERLY_FISCAL` granularity.
Type: [GranularityConfiguration](API_GranularityConfiguration.md) object
Required: No

 ** [GroupBy](#API_GetEstimatedCarbonEmissions_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-request-GroupBy"></a>
The dimensions available for grouping estimated carbon emissions.
Type: Array of strings
Valid Values: `USAGE_ACCOUNT_ID | REGION | SERVICE`
Required: No

 ** [MaxResults](#API_GetEstimatedCarbonEmissions_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-request-MaxResults"></a>
The maximum number of results to return in a single call. Default is 1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** [NextToken](#API_GetEstimatedCarbonEmissions_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_GetEstimatedCarbonEmissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Results": [
      {
         "DimensionsValues": {
            "string" : "string"
         },
         "EmissionsValues": {
            "string" : {
               "Unit": "string",
               "Value": number
            }
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
<a name="API_GetEstimatedCarbonEmissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_GetEstimatedCarbonEmissions_ResponseSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-response-Results"></a>
The result of the requested inputs.
Type: Array of [EstimatedCarbonEmissions](API_EstimatedCarbonEmissions.md) objects

 ** [NextToken](#API_GetEstimatedCarbonEmissions_ResponseSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissions-response-NextToken"></a>
The pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_GetEstimatedCarbonEmissions_Errors"></a>

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
<a name="API_GetEstimatedCarbonEmissions_Examples"></a>

### GetEstimatedCarbonEmissions
<a name="API_GetEstimatedCarbonEmissions_Example_1"></a>

This example illustrates one usage of GetEstimatedCarbonEmissions.

#### Sample Request
<a name="API_GetEstimatedCarbonEmissions_Example_1_Request"></a>

```
POST /v1/estimated-carbon-emissions
{
    "TimePeriod": {
        "Start": "2025-01-01T00:00:00Z",
        "End": "2025-12-31T23:59:59.999Z"
    },
    "GroupBy": [
        "SERVICE"
    ],
    "EmissionsTypes": [
        "TOTAL_LBM_CARBON_EMISSIONS",
        "TOTAL_MBM_CARBON_EMISSIONS",
        "TOTAL_SCOPE_1_CARBON_EMISSIONS",
        "TOTAL_SCOPE_2_LBM_CARBON_EMISSIONS",
        "TOTAL_SCOPE_2_MBM_CARBON_EMISSIONS",
        "TOTAL_SCOPE_3_LBM_CARBON_EMISSIONS",
        "TOTAL_SCOPE_3_MBM_CARBON_EMISSIONS"
    ],
    "Granularity": "MONTHLY"
}
```

#### Sample Response
<a name="API_GetEstimatedCarbonEmissions_Example_1_Response"></a>

```
{
    "Results": [
        {
            "DimensionsValues": {
                "SERVICE": "AmazonEC2"
            },
            "EmissionsValues": {
                "TOTAL_LBM_CARBON_EMISSIONS": {
                    "Unit": "MTCO2e",
                    "Value": 1
                },
                "TOTAL_MBM_CARBON_EMISSIONS": {
                    "Unit": "MTCO2e",
                    "Value": 1
                },
                "TOTAL_SCOPE_1_CARBON_EMISSIONS": {
                    "Unit": "MTCO2e",
                    "Value": 1
                },
                "TOTAL_SCOPE_2_LBM_CARBON_EMISSIONS": {
                    "Unit": "MTCO2e",
                    "Value": 1
                },
                "TOTAL_SCOPE_2_MBM_CARBON_EMISSIONS": {
                    "Unit": "MTCO2e",
                    "Value": 1
                },
                "TOTAL_SCOPE_3_LBM_CARBON_EMISSIONS": {
                    "Unit": "MTCO2e",
                    "Value": 1
                },
                "TOTAL_SCOPE_3_MBM_CARBON_EMISSIONS": {
                    "Unit": "MTCO2e",
                    "Value": 1
                }
            },
            "ModelVersion": "v3.0.0",
            "TimePeriod": {
                "Start": "2025-01-01T00:00:00Z",
                "End": "2025-02-01T00:00:00Z"
            }
        }
    ]
}
```

## See Also
<a name="API_GetEstimatedCarbonEmissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sustainability-2018-05-10/GetEstimatedCarbonEmissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sustainability-2018-05-10/GetEstimatedCarbonEmissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sustainability-2018-05-10/GetEstimatedCarbonEmissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sustainability-2018-05-10/GetEstimatedCarbonEmissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sustainability-2018-05-10/GetEstimatedCarbonEmissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sustainability-2018-05-10/GetEstimatedCarbonEmissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sustainability-2018-05-10/GetEstimatedCarbonEmissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sustainability-2018-05-10/GetEstimatedCarbonEmissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sustainability-2018-05-10/GetEstimatedCarbonEmissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sustainability-2018-05-10/GetEstimatedCarbonEmissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sustainability. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sustainability` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
