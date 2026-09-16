---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_GetBillingGroupCostReport.html
---

# GetBillingGroupCostReport
<a name="API_GetBillingGroupCostReport"></a>

Retrieves the margin summary report, which includes the AWS cost and charged amount (pro forma cost) by AWS service for a specific billing group.

## Request Syntax
<a name="API_GetBillingGroupCostReport_RequestSyntax"></a>

```
POST /get-billing-group-cost-report HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "BillingPeriodRange": {
      "ExclusiveEndBillingPeriod": "{{string}}",
      "InclusiveStartBillingPeriod": "{{string}}"
   },
   "GroupBy": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetBillingGroupCostReport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetBillingGroupCostReport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_GetBillingGroupCostReport_RequestSyntax) **   <a name="billingconductor-GetBillingGroupCostReport-request-Arn"></a>
The Amazon Resource Number (ARN) that uniquely identifies the billing group.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: Yes

 ** [BillingPeriodRange](#API_GetBillingGroupCostReport_RequestSyntax) **   <a name="billingconductor-GetBillingGroupCostReport-request-BillingPeriodRange"></a>
A time range for which the margin summary is effective. You can specify up to 12 months.
Type: [BillingPeriodRange](API_BillingPeriodRange.md) object
Required: No

 ** [GroupBy](#API_GetBillingGroupCostReport_RequestSyntax) **   <a name="billingconductor-GetBillingGroupCostReport-request-GroupBy"></a>
A list of strings that specify the attributes that are used to break down costs in the margin summary reports for the billing group. For example, you can view your costs by the AWS service name or the billing period.
Type: Array of strings
Valid Values: `PRODUCT_NAME | BILLING_PERIOD`
Required: No

 ** [MaxResults](#API_GetBillingGroupCostReport_RequestSyntax) **   <a name="billingconductor-GetBillingGroupCostReport-request-MaxResults"></a>
The maximum number of margin summary reports to retrieve.
Type: Integer
Valid Range: Minimum value of 200. Maximum value of 300.
Required: No

 ** [NextToken](#API_GetBillingGroupCostReport_RequestSyntax) **   <a name="billingconductor-GetBillingGroupCostReport-request-NextToken"></a>
The pagination token used on subsequent calls to get reports.
Type: String
Required: No

## Response Syntax
<a name="API_GetBillingGroupCostReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BillingGroupCostReportResults": [
      {
         "Arn": "string",
         "Attributes": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "AWSCost": "string",
         "Currency": "string",
         "Margin": "string",
         "MarginPercentage": "string",
         "ProformaCost": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetBillingGroupCostReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BillingGroupCostReportResults](#API_GetBillingGroupCostReport_ResponseSyntax) **   <a name="billingconductor-GetBillingGroupCostReport-response-BillingGroupCostReportResults"></a>
The list of margin summary reports.
Type: Array of [BillingGroupCostReportResultElement](API_BillingGroupCostReportResultElement.md) objects

 ** [NextToken](#API_GetBillingGroupCostReport_ResponseSyntax) **   <a name="billingconductor-GetBillingGroupCostReport-response-NextToken"></a>
The pagination token used on subsequent calls to get reports.
Type: String

## Errors
<a name="API_GetBillingGroupCostReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
 ** RetryAfterSeconds **
Number of seconds you can retry after the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
 ** ResourceId **
Resource identifier that was not found.
 ** ResourceType **
Resource type that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Number of seconds you can safely retry after the call.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't match with the constraints specified by AWS services.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason the request's validation failed.
HTTP Status Code: 400

## See Also
<a name="API_GetBillingGroupCostReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/GetBillingGroupCostReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/GetBillingGroupCostReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/GetBillingGroupCostReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/GetBillingGroupCostReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/GetBillingGroupCostReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/GetBillingGroupCostReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/GetBillingGroupCostReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/GetBillingGroupCostReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/GetBillingGroupCostReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/GetBillingGroupCostReport)
