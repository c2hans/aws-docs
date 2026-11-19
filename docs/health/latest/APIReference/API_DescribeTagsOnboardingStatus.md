---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeTagsOnboardingStatus.html
---

# DescribeTagsOnboardingStatus

Returns the current onboarding status of the Health tags feature for your account.

## Response Syntax
<a name="API_DescribeTagsOnboardingStatus_ResponseSyntax"></a>

```
{
   "status": "string"
}
```

## Response Elements
<a name="API_DescribeTagsOnboardingStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_DescribeTagsOnboardingStatus_ResponseSyntax) **   <a name="AWSHealth-DescribeTagsOnboardingStatus-response-status"></a>
The current onboarding status of the tags feature for the account.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_DescribeTagsOnboardingStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeTagsOnboardingStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeTagsOnboardingStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeTagsOnboardingStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeTagsOnboardingStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeTagsOnboardingStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeTagsOnboardingStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeTagsOnboardingStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeTagsOnboardingStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeTagsOnboardingStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeTagsOnboardingStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeTagsOnboardingStatus)
