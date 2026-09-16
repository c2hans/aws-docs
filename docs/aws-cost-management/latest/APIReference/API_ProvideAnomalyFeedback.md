---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ProvideAnomalyFeedback.html
---

# ProvideAnomalyFeedback
<a name="API_ProvideAnomalyFeedback"></a>

Modifies the feedback property of a given cost anomaly.

## Request Syntax
<a name="API_ProvideAnomalyFeedback_RequestSyntax"></a>

```
{
   "AnomalyId": "{{string}}",
   "Feedback": "{{string}}"
}
```

## Request Parameters
<a name="API_ProvideAnomalyFeedback_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnomalyId](#API_ProvideAnomalyFeedback_RequestSyntax) **   <a name="awscostmanagement-ProvideAnomalyFeedback-request-AnomalyId"></a>
A cost anomaly ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** [Feedback](#API_ProvideAnomalyFeedback_RequestSyntax) **   <a name="awscostmanagement-ProvideAnomalyFeedback-request-Feedback"></a>
Describes whether the cost anomaly was a planned activity or you considered it an anomaly.
Type: String
Valid Values: `YES | NO | PLANNED_ACTIVITY`
Required: Yes

## Response Syntax
<a name="API_ProvideAnomalyFeedback_ResponseSyntax"></a>

```
{
   "AnomalyId": "string"
}
```

## Response Elements
<a name="API_ProvideAnomalyFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnomalyId](#API_ProvideAnomalyFeedback_ResponseSyntax) **   <a name="awscostmanagement-ProvideAnomalyFeedback-response-AnomalyId"></a>
The ID of the modified cost anomaly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`

## Errors
<a name="API_ProvideAnomalyFeedback_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_ProvideAnomalyFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/ProvideAnomalyFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/ProvideAnomalyFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ProvideAnomalyFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/ProvideAnomalyFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ProvideAnomalyFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/ProvideAnomalyFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/ProvideAnomalyFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/ProvideAnomalyFeedback)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/ProvideAnomalyFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ProvideAnomalyFeedback)
