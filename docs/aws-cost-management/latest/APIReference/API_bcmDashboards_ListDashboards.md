---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ListDashboards.html
---

# ListDashboards
<a name="API_bcmDashboards_ListDashboards"></a>

Returns a list of all dashboards in your account.

## Request Syntax
<a name="API_bcmDashboards_ListDashboards_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_bcmDashboards_ListDashboards_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_bcmDashboards_ListDashboards_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_ListDashboards-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_bcmDashboards_ListDashboards_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_ListDashboards-request-nextToken"></a>
The token for the next page of results. Use the value returned in the previous response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_bcmDashboards_ListDashboards_ResponseSyntax"></a>

```
{
   "dashboards": [
      {
         "arn": "string",
         "createdAt": number,
         "description": "string",
         "name": "string",
         "type": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_bcmDashboards_ListDashboards_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dashboards](#API_bcmDashboards_ListDashboards_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_ListDashboards-response-dashboards"></a>
An array of dashboard references, containing basic information about each dashboard.
Type: Array of [DashboardReference](API_bcmDashboards_DashboardReference.md) objects

 ** [nextToken](#API_bcmDashboards_ListDashboards_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_ListDashboards-response-nextToken"></a>
The token to use to retrieve the next page of results. Not returned if there are no more results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_bcmDashboards_ListDashboards_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Verify your IAM permissions and any resource policies.
HTTP Status Code: 400

 ** InternalServerException **
An internal error occurred while processing the request. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling. Reduce the frequency of requests and use exponential backoff.
HTTP Status Code: 400

 ** ValidationException **
The input parameters do not satisfy the requirements. Check the error message for specific validation details.
HTTP Status Code: 400

## See Also
<a name="API_bcmDashboards_ListDashboards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/ListDashboards)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/ListDashboards)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ListDashboards)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/ListDashboards)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ListDashboards)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/ListDashboards)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/ListDashboards)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/ListDashboards)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/ListDashboards)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ListDashboards)
