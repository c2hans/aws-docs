---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteFeatureGroup.html
---

# DeleteFeatureGroup
<a name="API_DeleteFeatureGroup"></a>

Delete the `FeatureGroup` and any data that was written to the `OnlineStore` of the `FeatureGroup`. Data cannot be accessed from the `OnlineStore` immediately after `DeleteFeatureGroup` is called.

Data written into the `OfflineStore` will not be deleted. The AWS Glue database and tables that are automatically created for your `OfflineStore` are not deleted.

Note that it can take approximately 10-15 minutes to delete an `OnlineStore` `FeatureGroup` with the `InMemory` `StorageType`.

## Request Syntax
<a name="API_DeleteFeatureGroup_RequestSyntax"></a>

```
{
   "FeatureGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteFeatureGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FeatureGroupName](#API_DeleteFeatureGroup_RequestSyntax) **   <a name="sagemaker-DeleteFeatureGroup-request-FeatureGroupName"></a>
The name of the `FeatureGroup` you want to delete. The name must be unique within an AWS Region in an AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([_-]*[a-zA-Z0-9]){0,63}`
Required: Yes

## Response Elements
<a name="API_DeleteFeatureGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteFeatureGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteFeatureGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteFeatureGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteFeatureGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteFeatureGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteFeatureGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteFeatureGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteFeatureGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteFeatureGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteFeatureGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteFeatureGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteFeatureGroup)
