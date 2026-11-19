---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_ConfigureTags.html
---

# ConfigureTags

Configures which resource tag keys are tracked by Health for your account. This operation replaces the existing configuration with the specified tag keys. Only configured tag keys will appear in Health event data.

## Request Syntax
<a name="API_ConfigureTags_RequestSyntax"></a>

```
{
   "tagKeys": [
      {
         "enabledForEventBridge": {{boolean}},
         "key": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ConfigureTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [tagKeys](#API_ConfigureTags_RequestSyntax) **   <a name="AWSHealth-ConfigureTags-request-tagKeys"></a>
The list of resource tag keys to configure for Health event tracking.
Type: Array of [ConfigureTagsTagKey](API_ConfigureTagsTagKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_ConfigureTags_ResponseSyntax"></a>

```
{
   "configuredTagKeys": [
      {
         "enabledForEventBridge": boolean,
         "key": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ConfigureTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredTagKeys](#API_ConfigureTags_ResponseSyntax) **   <a name="AWSHealth-ConfigureTags-response-configuredTagKeys"></a>
The list of resource tag keys that were successfully configured.
Type: Array of [ResourceTagKey](API_ResourceTagKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

## Errors
<a name="API_ConfigureTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ConfigureTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/ConfigureTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/ConfigureTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/ConfigureTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/ConfigureTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/ConfigureTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/ConfigureTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/ConfigureTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/ConfigureTags)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/ConfigureTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/ConfigureTags)
