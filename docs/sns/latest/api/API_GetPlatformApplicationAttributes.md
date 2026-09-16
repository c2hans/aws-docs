---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_GetPlatformApplicationAttributes.html
---

# GetPlatformApplicationAttributes
<a name="API_GetPlatformApplicationAttributes"></a>

Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see [Using Amazon SNS Mobile Push Notifications](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

## Request Parameters
<a name="API_GetPlatformApplicationAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** PlatformApplicationArn **
 `PlatformApplicationArn` for GetPlatformApplicationAttributesInput.
Type: String
Required: Yes

## Response Elements
<a name="API_GetPlatformApplicationAttributes_ResponseElements"></a>

The following element is returned by the service.

 **Attributes** Attributes.entry.N.key (key)Attributes.entry.N.value (value)
Attributes include the following:
+  `AppleCertificateExpiryDate` – The expiry date of the SSL certificate used to configure certificate-based authentication.
+  `ApplePlatformTeamID` – The Apple developer account ID used to configure token-based authentication.
+  `ApplePlatformBundleID` – The app identifier used to configure token-based authentication.
+  `AuthenticationMethod` – Returns the credential type used when sending push notifications from application to APNS/APNS\_Sandbox, or application to GCM.
  + APNS – Returns the token or certificate.
  + GCM – Returns the token or key.
+  `EventEndpointCreated` – Topic ARN to which EndpointCreated event notifications should be sent.
+  `EventEndpointDeleted` – Topic ARN to which EndpointDeleted event notifications should be sent.
+  `EventEndpointUpdated` – Topic ARN to which EndpointUpdate event notifications should be sent.
+  `EventDeliveryFailure` – Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.
Type: String to string map

## Errors
<a name="API_GetPlatformApplicationAttributes_Errors"></a>

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
<a name="API_GetPlatformApplicationAttributes_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_GetPlatformApplicationAttributes_Example_1"></a>

This example illustrates one usage of GetPlatformApplicationAttributes.

#### Sample Request
<a name="API_GetPlatformApplicationAttributes_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=GetPlatformApplicationAttributes
&PlatformApplicationArn=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3Aapp%2FGCM%2Fgcmpushapp
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetPlatformApplicationAttributes_Example_1_Response"></a>

```
<GetPlatformApplicationAttributesResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <GetPlatformApplicationAttributesResult>
        <Attributes>
            <entry>
                <key>AllowEndpointPolicies</key>
                <value>false</value>
            </entry>
        </Attributes>
    </GetPlatformApplicationAttributesResult>
    <ResponseMetadata>
        <RequestId>74848df2-87f6-55ed-890c-c7be80442462</RequestId>
    </ResponseMetadata>
</GetPlatformApplicationAttributesResponse>
```

## See Also
<a name="API_GetPlatformApplicationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/GetPlatformApplicationAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/GetPlatformApplicationAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/GetPlatformApplicationAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/GetPlatformApplicationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/GetPlatformApplicationAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/GetPlatformApplicationAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/GetPlatformApplicationAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/GetPlatformApplicationAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/GetPlatformApplicationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/GetPlatformApplicationAttributes)
