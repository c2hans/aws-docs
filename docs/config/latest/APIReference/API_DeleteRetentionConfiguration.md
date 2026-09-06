---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteRetentionConfiguration.html
---

# DeleteRetentionConfiguration
<a name="API_DeleteRetentionConfiguration"></a>

Deletes the retention configuration.

## Request Syntax
<a name="API_DeleteRetentionConfiguration_RequestSyntax"></a>

```
{
   "RetentionConfigurationName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRetentionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RetentionConfigurationName](#API_DeleteRetentionConfiguration_RequestSyntax) **   <a name="config-DeleteRetentionConfiguration-request-RetentionConfigurationName"></a>
The name of the retention configuration to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

## Response Elements
<a name="API_DeleteRetentionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteRetentionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One or more of the specified parameters are not valid. Verify that your parameters are valid and try again.
HTTP Status Code: 400

 ** NoSuchRetentionConfigurationException **
You have specified a retention configuration that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRetentionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DeleteRetentionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DeleteRetentionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeleteRetentionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DeleteRetentionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeleteRetentionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DeleteRetentionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DeleteRetentionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DeleteRetentionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DeleteRetentionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeleteRetentionConfiguration)
