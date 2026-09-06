---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSet.html
---

# CreateConfigurationSet
<a name="API_CreateConfigurationSet"></a>

Create a configuration set. *Configuration sets* are groups of rules that you can apply to the emails you send using Amazon Pinpoint. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.

## Request Syntax
<a name="API_CreateConfigurationSet_RequestSyntax"></a>

```
POST /v1/email/configuration-sets HTTP/1.1
Content-type: application/json

{
   "ConfigurationSetName": "{{string}}",
   "DeliveryOptions": {
      "SendingPoolName": "{{string}}",
      "TlsPolicy": "{{string}}"
   },
   "ReputationOptions": {
      "LastFreshStart": {{number}},
      "ReputationMetricsEnabled": {{boolean}}
   },
   "SendingOptions": {
      "SendingEnabled": {{boolean}}
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TrackingOptions": {
      "CustomRedirectDomain": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConfigurationSet_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConfigurationSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_CreateConfigurationSet_RequestSyntax) **   <a name="pinpoint-CreateConfigurationSet-request-ConfigurationSetName"></a>
The name of the configuration set.
Type: String
Required: Yes

 ** [DeliveryOptions](#API_CreateConfigurationSet_RequestSyntax) **   <a name="pinpoint-CreateConfigurationSet-request-DeliveryOptions"></a>
An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
Type: [DeliveryOptions](API_DeliveryOptions.md) object
Required: No

 ** [ReputationOptions](#API_CreateConfigurationSet_RequestSyntax) **   <a name="pinpoint-CreateConfigurationSet-request-ReputationOptions"></a>
An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.
Type: [ReputationOptions](API_ReputationOptions.md) object
Required: No

 ** [SendingOptions](#API_CreateConfigurationSet_RequestSyntax) **   <a name="pinpoint-CreateConfigurationSet-request-SendingOptions"></a>
An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
Type: [SendingOptions](API_SendingOptions.md) object
Required: No

 ** [Tags](#API_CreateConfigurationSet_RequestSyntax) **   <a name="pinpoint-CreateConfigurationSet-request-Tags"></a>
An array of objects that define the tags (keys and values) that you want to associate with the configuration set.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [TrackingOptions](#API_CreateConfigurationSet_RequestSyntax) **   <a name="pinpoint-CreateConfigurationSet-request-TrackingOptions"></a>
An object that defines the open and click tracking options for emails that you send using the configuration set.
Type: [TrackingOptions](API_TrackingOptions.md) object
Required: No

## Response Syntax
<a name="API_CreateConfigurationSet_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateConfigurationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateConfigurationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The resource specified in your request already exists.
HTTP Status Code: 400

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** ConcurrentModificationException **
The resource is being modified by another operation or thread.
HTTP Status Code: 500

 ** LimitExceededException **
There are too many instances of the specified resource type.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_CreateConfigurationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/CreateConfigurationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/CreateConfigurationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/CreateConfigurationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/CreateConfigurationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/CreateConfigurationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/CreateConfigurationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/CreateConfigurationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/CreateConfigurationSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/CreateConfigurationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/CreateConfigurationSet)
