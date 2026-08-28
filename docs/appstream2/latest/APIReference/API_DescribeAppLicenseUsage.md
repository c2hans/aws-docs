---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeAppLicenseUsage.html
---

# DescribeAppLicenseUsage
<a name="API_DescribeAppLicenseUsage"></a>

Retrieves license included application usage information.

## Request Syntax
<a name="API_DescribeAppLicenseUsage_RequestSyntax"></a>

```
{
   "BillingPeriod": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAppLicenseUsage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BillingPeriod](#API_DescribeAppLicenseUsage_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppLicenseUsage-request-BillingPeriod"></a>
Billing period for the usage record.
Specify the value in *yyyy-mm* format. For example, for August 2025, use *2025-08*.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [MaxResults](#API_DescribeAppLicenseUsage_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppLicenseUsage-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeAppLicenseUsage_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppLicenseUsage-request-NextToken"></a>
Token for pagination of results.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeAppLicenseUsage_ResponseSyntax"></a>

```
{
   "AppLicenseUsages": [
      {
         "BillingPeriod": "string",
         "LicenseType": "string",
         "OwnerAWSAccountId": "string",
         "SubscriptionFirstUsedDate": number,
         "SubscriptionLastUsedDate": number,
         "UserArn": "string",
         "UserId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAppLicenseUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppLicenseUsages](#API_DescribeAppLicenseUsage_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeAppLicenseUsage-response-AppLicenseUsages"></a>
Collection of license usage records.
Type: Array of [AdminAppLicenseUsageRecord](API_AdminAppLicenseUsageRecord.md) objects

 ** [NextToken](#API_DescribeAppLicenseUsage_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeAppLicenseUsage-response-NextToken"></a>
Token for pagination of results.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeAppLicenseUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAppLicenseUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeAppLicenseUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeAppLicenseUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeAppLicenseUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeAppLicenseUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeAppLicenseUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeAppLicenseUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeAppLicenseUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeAppLicenseUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeAppLicenseUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeAppLicenseUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
