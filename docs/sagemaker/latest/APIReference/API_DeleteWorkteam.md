---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkteam.html
---

# DeleteWorkteam
<a name="API_DeleteWorkteam"></a>

Deletes an existing work team. This operation can't be undone.

## Request Syntax
<a name="API_DeleteWorkteam_RequestSyntax"></a>

```
{
   "WorkteamName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteWorkteam_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WorkteamName](#API_DeleteWorkteam_RequestSyntax) **   <a name="sagemaker-DeleteWorkteam-request-WorkteamName"></a>
The name of the work team to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DeleteWorkteam_ResponseSyntax"></a>

```
{
   "Success": boolean
}
```

## Response Elements
<a name="API_DeleteWorkteam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Success](#API_DeleteWorkteam_ResponseSyntax) **   <a name="sagemaker-DeleteWorkteam-response-Success"></a>
Returns `true` if the work team was successfully deleted; otherwise, returns `false`.
Type: Boolean

## Errors
<a name="API_DeleteWorkteam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_DeleteWorkteam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteWorkteam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteWorkteam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteWorkteam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteWorkteam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteWorkteam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteWorkteam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteWorkteam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteWorkteam)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteWorkteam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteWorkteam)
