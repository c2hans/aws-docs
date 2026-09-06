---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteAssociation.html
---

# DeleteAssociation
<a name="API_DeleteAssociation"></a>

Deletes an association.

## Request Syntax
<a name="API_DeleteAssociation_RequestSyntax"></a>

```
{
   "DestinationArn": "{{string}}",
   "SourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationArn](#API_DeleteAssociation_RequestSyntax) **   <a name="sagemaker-DeleteAssociation-request-DestinationArn"></a>
The Amazon Resource Name (ARN) of the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: Yes

 ** [SourceArn](#API_DeleteAssociation_RequestSyntax) **   <a name="sagemaker-DeleteAssociation-request-SourceArn"></a>
The ARN of the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: Yes

## Response Syntax
<a name="API_DeleteAssociation_ResponseSyntax"></a>

```
{
   "DestinationArn": "string",
   "SourceArn": "string"
}
```

## Response Elements
<a name="API_DeleteAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DestinationArn](#API_DeleteAssociation_ResponseSyntax) **   <a name="sagemaker-DeleteAssociation-response-DestinationArn"></a>
The Amazon Resource Name (ARN) of the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`

 ** [SourceArn](#API_DeleteAssociation_ResponseSyntax) **   <a name="sagemaker-DeleteAssociation-response-SourceArn"></a>
The ARN of the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`

## Errors
<a name="API_DeleteAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteAssociation)
