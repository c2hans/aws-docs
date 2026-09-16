---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteAnomalyMonitor.html
---

# DeleteAnomalyMonitor
<a name="API_DeleteAnomalyMonitor"></a>

Deletes a cost anomaly monitor.

## Request Syntax
<a name="API_DeleteAnomalyMonitor_RequestSyntax"></a>

```
{
   "MonitorArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAnomalyMonitor_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MonitorArn](#API_DeleteAnomalyMonitor_RequestSyntax) **   <a name="awscostmanagement-DeleteAnomalyMonitor-request-MonitorArn"></a>
The unique identifier of the cost anomaly monitor that you want to delete.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

## Response Elements
<a name="API_DeleteAnomalyMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAnomalyMonitor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** UnknownMonitorException **
The cost anomaly monitor does not exist for the account.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAnomalyMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/DeleteAnomalyMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/DeleteAnomalyMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/DeleteAnomalyMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/DeleteAnomalyMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/DeleteAnomalyMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/DeleteAnomalyMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/DeleteAnomalyMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/DeleteAnomalyMonitor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/DeleteAnomalyMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/DeleteAnomalyMonitor)
