---
source_url: https://docs.aws.amazon.com/sustainability/latest/APIReference/API_GetEstimatedCarbonEmissionsDimensionValues.html
---

# GetEstimatedCarbonEmissionsDimensionValues
<a name="API_GetEstimatedCarbonEmissionsDimensionValues"></a>

Returns the possible dimension values available for a customer's account. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_RequestSyntax"></a>

```
POST /v1/estimated-carbon-emissions-dimension-values HTTP/1.1
Content-type: application/json

{
   "Dimensions": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Dimensions](#API_GetEstimatedCarbonEmissionsDimensionValues_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissionsDimensionValues-request-Dimensions"></a>
The dimensions available for grouping estimated carbon emissions.
Type: Array of strings
Valid Values: `USAGE_ACCOUNT_ID | REGION | SERVICE`
Required: Yes

 ** [TimePeriod](#API_GetEstimatedCarbonEmissionsDimensionValues_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissionsDimensionValues-request-TimePeriod"></a>
 The date range for fetching the dimension values. The range must include the start date of a month for that month's dimensions to be included in the response.
Type: [TimePeriod](API_TimePeriod.md) object
Required: Yes

 ** [MaxResults](#API_GetEstimatedCarbonEmissionsDimensionValues_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissionsDimensionValues-request-MaxResults"></a>
The maximum number of results to return in a single call. Default is 1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** [NextToken](#API_GetEstimatedCarbonEmissionsDimensionValues_RequestSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissionsDimensionValues-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Results": [
      {
         "Dimension": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetEstimatedCarbonEmissionsDimensionValues_ResponseSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissionsDimensionValues-response-NextToken"></a>
The pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [Results](#API_GetEstimatedCarbonEmissionsDimensionValues_ResponseSyntax) **   <a name="sustainability-GetEstimatedCarbonEmissionsDimensionValues-response-Results"></a>
The list of possible dimensions over which the emissions data is aggregated.
Type: Array of [DimensionEntry](API_DimensionEntry.md) objects

## Errors
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_Errors"></a>

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
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_Examples"></a>

### GetEstimatedCarbonEmissionsDimensionValues
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_Example_1"></a>

This example illustrates one usage of GetEstimatedCarbonEmissionsDimensionValues.

#### Sample Request
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_Example_1_Request"></a>

```
POST /v1/estimated-carbon-emissions-dimension-values
{
    "TimePeriod": {
        "Start": "2025-01-01T00:00:00Z",
        "End": "2025-12-31T23:59:59.999Z"
    },
    "Dimensions": [
        "SERVICE",
        "REGION",
        "USAGE_ACCOUNT_ID"
    ]
}
```

#### Sample Response
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_Example_1_Response"></a>

```
{
    "Results": [
        {
            "Dimension": "SERVICE",
            "Value": "AmazonEC2"
        },
        {
            "Dimension": "SERVICE",
            "Value": "AmazonS3"
        },
        {
            "Dimension": "SERVICE",
            "Value": "AmazonCloudFront"
        },
        {
            "Dimension": "REGION",
            "Value": "global"
        },
        {
            "Dimension": "REGION",
            "Value": "us-east-1"
        },
        {
            "Dimension": "REGION",
            "Value": "us-west-2"
        },
        {
            "Dimension": "USAGE_ACCOUNT_ID",
            "Value": "111222333444"
        }
    ]
}
```

## See Also
<a name="API_GetEstimatedCarbonEmissionsDimensionValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sustainability-2018-05-10/GetEstimatedCarbonEmissionsDimensionValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sustainability. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sustainability` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
