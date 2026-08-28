---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeHealthServiceStatusForOrganization.html
---

# DescribeHealthServiceStatusForOrganization
<a name="API_DescribeHealthServiceStatusForOrganization"></a>

This operation provides status information on enabling or disabling AWS Health to work with your organization. To call this operation, you must use the organization's management account.

## Response Syntax
<a name="API_DescribeHealthServiceStatusForOrganization_ResponseSyntax"></a>

```
{
   "healthServiceAccessStatusForOrganization": "string"
}
```

## Response Elements
<a name="API_DescribeHealthServiceStatusForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [healthServiceAccessStatusForOrganization](#API_DescribeHealthServiceStatusForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeHealthServiceStatusForOrganization-response-healthServiceAccessStatusForOrganization"></a>
Information about the status of enabling or disabling the AWS Health organizational view feature in your organization.
Valid values are `ENABLED | DISABLED | PENDING`.
Type: String

## Errors
<a name="API_DescribeHealthServiceStatusForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeHealthServiceStatusForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeHealthServiceStatusForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeHealthServiceStatusForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeHealthServiceStatusForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeHealthServiceStatusForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeHealthServiceStatusForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeHealthServiceStatusForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeHealthServiceStatusForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeHealthServiceStatusForOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeHealthServiceStatusForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeHealthServiceStatusForOrganization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
