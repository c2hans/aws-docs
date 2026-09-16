---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_NotifyUpdateProvisionedProductEngineWorkflowResult.html
---

# NotifyUpdateProvisionedProductEngineWorkflowResult
<a name="API_NotifyUpdateProvisionedProductEngineWorkflowResult"></a>

 Notifies the result of the update engine execution.

## Request Syntax
<a name="API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax"></a>

```
{
   "FailureReason": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "Outputs": [
      {
         "Description": "{{string}}",
         "OutputKey": "{{string}}",
         "OutputValue": "{{string}}"
      }
   ],
   "RecordId": "{{string}}",
   "Status": "{{string}}",
   "WorkflowToken": "{{string}}"
}
```

## Request Parameters
<a name="API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [FailureReason](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax) **   <a name="servicecatalog-NotifyUpdateProvisionedProductEngineWorkflowResult-request-FailureReason"></a>
 The reason why the update engine execution failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [IdempotencyToken](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax) **   <a name="servicecatalog-NotifyUpdateProvisionedProductEngineWorkflowResult-request-IdempotencyToken"></a>
 The idempotency token that identifies the update engine execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [Outputs](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax) **   <a name="servicecatalog-NotifyUpdateProvisionedProductEngineWorkflowResult-request-Outputs"></a>
 The output of the update engine execution.
Type: Array of [RecordOutput](API_RecordOutput.md) objects
Required: No

 ** [RecordId](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax) **   <a name="servicecatalog-NotifyUpdateProvisionedProductEngineWorkflowResult-request-RecordId"></a>
 The identifier of the record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [Status](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax) **   <a name="servicecatalog-NotifyUpdateProvisionedProductEngineWorkflowResult-request-Status"></a>
 The status of the update engine execution.
Type: String
Valid Values: `SUCCEEDED | FAILED`
Required: Yes

 ** [WorkflowToken](#API_NotifyUpdateProvisionedProductEngineWorkflowResult_RequestSyntax) **   <a name="servicecatalog-NotifyUpdateProvisionedProductEngineWorkflowResult-request-WorkflowToken"></a>
 The encrypted contents of the update engine execution payload that Service Catalog sends after the Terraform product update workflow starts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20000.
Pattern: `[0-9A-Za-z+\/\-=]+`
Required: Yes

## Response Elements
<a name="API_NotifyUpdateProvisionedProductEngineWorkflowResult_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_NotifyUpdateProvisionedProductEngineWorkflowResult_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_NotifyUpdateProvisionedProductEngineWorkflowResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/NotifyUpdateProvisionedProductEngineWorkflowResult)
