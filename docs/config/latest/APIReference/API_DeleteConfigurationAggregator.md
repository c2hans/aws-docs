---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteConfigurationAggregator.html
---

# DeleteConfigurationAggregator
<a name="API_DeleteConfigurationAggregator"></a>

Deletes the specified configuration aggregator and the aggregated data associated with the aggregator.

## Request Syntax
<a name="API_DeleteConfigurationAggregator_RequestSyntax"></a>

```
{
   "ConfigurationAggregatorName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteConfigurationAggregator_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationAggregatorName](#API_DeleteConfigurationAggregator_RequestSyntax) **   <a name="config-DeleteConfigurationAggregator-request-ConfigurationAggregatorName"></a>
The name of the configuration aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

## Response Elements
<a name="API_DeleteConfigurationAggregator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteConfigurationAggregator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchConfigurationAggregatorException **
You have specified a configuration aggregator that does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DeleteConfigurationAggregator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DeleteConfigurationAggregator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DeleteConfigurationAggregator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeleteConfigurationAggregator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DeleteConfigurationAggregator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeleteConfigurationAggregator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DeleteConfigurationAggregator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DeleteConfigurationAggregator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DeleteConfigurationAggregator)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DeleteConfigurationAggregator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeleteConfigurationAggregator)
