---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateContext.html
---

# CreateContext
<a name="API_CreateContext"></a>

Creates a *context*. A context is a lineage tracking entity that represents a logical grouping of other tracking or experiment entities. Some examples are an endpoint and a model package. For more information, see [Amazon SageMaker ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html).

## Request Syntax
<a name="API_CreateContext_RequestSyntax"></a>

```
{
   "ContextName": "{{string}}",
   "ContextType": "{{string}}",
   "Description": "{{string}}",
   "Properties": {
      "{{string}}" : "{{string}}"
   },
   "Source": {
      "SourceId": "{{string}}",
      "SourceType": "{{string}}",
      "SourceUri": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateContext_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContextName](#API_CreateContext_RequestSyntax) **   <a name="sagemaker-CreateContext-request-ContextName"></a>
The name of the context. Must be unique to your account in an AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9]([-_]*[a-zA-Z0-9]){0,119}`
Required: Yes

 ** [ContextType](#API_CreateContext_RequestSyntax) **   <a name="sagemaker-CreateContext-request-ContextType"></a>
The context type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [Description](#API_CreateContext_RequestSyntax) **   <a name="sagemaker-CreateContext-request-Description"></a>
The description of the context.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** [Properties](#API_CreateContext_RequestSyntax) **   <a name="sagemaker-CreateContext-request-Properties"></a>
A list of properties to add to the context.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2500.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`
Required: No

 ** [Source](#API_CreateContext_RequestSyntax) **   <a name="sagemaker-CreateContext-request-Source"></a>
The source type, ID, and URI.
Type: [ContextSource](API_ContextSource.md) object
Required: Yes

 ** [Tags](#API_CreateContext_RequestSyntax) **   <a name="sagemaker-CreateContext-request-Tags"></a>
A list of tags to apply to the context.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateContext_ResponseSyntax"></a>

```
{
   "ContextArn": "string"
}
```

## Response Elements
<a name="API_CreateContext_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextArn](#API_CreateContext_ResponseSyntax) **   <a name="sagemaker-CreateContext-response-ContextArn"></a>
The Amazon Resource Name (ARN) of the context.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:context/.*`

## Errors
<a name="API_CreateContext_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateContext)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateContext)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateContext)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateContext)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateContext)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateContext)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateContext)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateContext)
