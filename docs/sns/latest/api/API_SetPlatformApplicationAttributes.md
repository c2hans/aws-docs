---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html
---

# SetPlatformApplicationAttributes
<a name="API_SetPlatformApplicationAttributes"></a>

Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see [Using Amazon SNS Mobile Push Notifications](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html). For information on configuring attributes for message delivery status, see [Using Amazon SNS Application Attributes for Message Delivery Status](https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html).

## Request Parameters
<a name="API_SetPlatformApplicationAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Attributes** Attributes.entry.N.key (key)Attributes.entry.N.value (value)
A map of the platform application attributes. Attributes in this map include the following:
+  `PlatformCredential` – The credential received from the notification service.
  + For ADM, `PlatformCredential`is client secret.
  + For Apple Services using certificate credentials, `PlatformCredential` is private key.
  + For Apple Services using token credentials, `PlatformCredential` is signing key.
  + For GCM (Firebase Cloud Messaging) using key credentials, there is no `PlatformPrincipal`. The `PlatformCredential` is `API key`.
  + For GCM (Firebase Cloud Messaging) using token credentials, there is no `PlatformPrincipal`. The `PlatformCredential` is a JSON formatted private key file. When using the AWS CLI, the file must be in string format and special characters must be ignored. To format the file correctly, Amazon SNS recommends using the following command: `SERVICE_JSON=`jq @json <<< cat service.json``.
+  `PlatformPrincipal` – The principal received from the notification service.
  + For ADM, `PlatformPrincipal`is client id.
  + For Apple Services using certificate credentials, `PlatformPrincipal` is SSL certificate.
  + For Apple Services using token credentials, `PlatformPrincipal` is signing key ID.
  + For GCM (Firebase Cloud Messaging), there is no `PlatformPrincipal`.
+  `EventEndpointCreated` – Topic ARN to which `EndpointCreated` event notifications are sent.
+  `EventEndpointDeleted` – Topic ARN to which `EndpointDeleted` event notifications are sent.
+  `EventEndpointUpdated` – Topic ARN to which `EndpointUpdate` event notifications are sent.
+  `EventDeliveryFailure` – Topic ARN to which `DeliveryFailure` event notifications are sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.
+  `SuccessFeedbackRoleArn` – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
+  `FailureFeedbackRoleArn` – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
+  `SuccessFeedbackSampleRate` – Sample rate percentage (0-100) of successfully delivered messages.
The following attributes only apply to `APNs` token-based authentication:
+  `ApplePlatformTeamID` – The identifier that's assigned to your Apple developer account team.
+  `ApplePlatformBundleID` – The bundle identifier that's assigned to your iOS app.
Type: String to string map
Required: Yes

 ** PlatformApplicationArn **
 `PlatformApplicationArn` for `SetPlatformApplicationAttributes` action.
Type: String
Required: Yes

## Errors
<a name="API_SetPlatformApplicationAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

## Examples
<a name="API_SetPlatformApplicationAttributes_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_SetPlatformApplicationAttributes_Example_1"></a>

This example illustrates one usage of SetPlatformApplicationAttributes.

#### Sample Request
<a name="API_SetPlatformApplicationAttributes_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=SetPlatformApplicationAttributes
&Attributes.entry.1.key=EventEndpointCreated&PlatformApplicationArn=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3Aapp%2FGCM%2Fgcmpushapp
&Attributes.entry.1.value=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3Atopicarn
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_SetPlatformApplicationAttributes_Example_1_Response"></a>

```
<SetPlatformApplicationAttributesResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>cf577bcc-b3dc-5463-88f1-3180b9412395</RequestId>
    </ResponseMetadata>
</SetPlatformApplicationAttributesResponse>
```

## See Also
<a name="API_SetPlatformApplicationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/SetPlatformApplicationAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/SetPlatformApplicationAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/SetPlatformApplicationAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/SetPlatformApplicationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/SetPlatformApplicationAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/SetPlatformApplicationAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/SetPlatformApplicationAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/SetPlatformApplicationAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/SetPlatformApplicationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/SetPlatformApplicationAttributes)
