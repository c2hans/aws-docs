---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteFlowDefinition.html
---

# DeleteFlowDefinition
<a name="API_DeleteFlowDefinition"></a>

Deletes the specified flow definition.

## Request Syntax
<a name="API_DeleteFlowDefinition_RequestSyntax"></a>

```
{
   "FlowDefinitionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteFlowDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FlowDefinitionName](#API_DeleteFlowDefinition_RequestSyntax) **   <a name="sagemaker-DeleteFlowDefinition-request-FlowDefinitionName"></a>
The name of the flow definition you are deleting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9](-*[a-z0-9]){0,62}`
Required: Yes

## Response Elements
<a name="API_DeleteFlowDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteFlowDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteFlowDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteFlowDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteFlowDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteFlowDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteFlowDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteFlowDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteFlowDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteFlowDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteFlowDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteFlowDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteFlowDefinition)
