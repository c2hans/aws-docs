---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_UpdateConfigurationSet.html
---

# UpdateConfigurationSet
<a name="API_UpdateConfigurationSet"></a>

Updates an existing configuration set.

This operation performs a partial update. Only the attributes that you include in the request are updated; any omitted attribute is left unchanged.

## Request Syntax
<a name="API_UpdateConfigurationSet_RequestSyntax"></a>

```
POST /v2/email/update-configuration-sets HTTP/1.1
Content-type: application/json

{
   "ConfigurationSetName": "{{string}}",
   "MessageSecurityOptions": {
      "SigningScheme": { ... }
   }
}
```

## URI Request Parameters
<a name="API_UpdateConfigurationSet_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateConfigurationSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_UpdateConfigurationSet_RequestSyntax) **   <a name="SES-UpdateConfigurationSet-request-ConfigurationSetName"></a>
The name of the configuration set to update.
Type: String
Required: Yes

 ** [MessageSecurityOptions](#API_UpdateConfigurationSet_RequestSyntax) **   <a name="SES-UpdateConfigurationSet-request-MessageSecurityOptions"></a>
The security options that apply to the MIME message itself for messages sent with the configuration set.
Type: [MessageSecurityOptions](API_MessageSecurityOptions.md) object
Required: No

## Response Syntax
<a name="API_UpdateConfigurationSet_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateConfigurationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateConfigurationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_UpdateConfigurationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/UpdateConfigurationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/UpdateConfigurationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/UpdateConfigurationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/UpdateConfigurationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/UpdateConfigurationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/UpdateConfigurationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/UpdateConfigurationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/UpdateConfigurationSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/UpdateConfigurationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/UpdateConfigurationSet)
