---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformApplication.html
---

# CreatePlatformApplication
<a name="API_CreatePlatformApplication"></a>

Creates a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging), to which devices and mobile apps may register. You must specify `PlatformPrincipal` and `PlatformCredential` attributes when using the `CreatePlatformApplication` action.

 `PlatformPrincipal` and `PlatformCredential` are received from the notification service.
+ For ADM, `PlatformPrincipal` is `client id` and `PlatformCredential` is `client secret`.
+ For APNS and `APNS_SANDBOX` using certificate credentials, `PlatformPrincipal` is `SSL certificate` and `PlatformCredential` is `private key`.
+ For APNS and `APNS_SANDBOX` using token credentials, `PlatformPrincipal` is `signing key ID` and `PlatformCredential` is `signing key`.
+ For Baidu, `PlatformPrincipal` is `API key` and `PlatformCredential` is `secret key`.
+ For GCM (Firebase Cloud Messaging) using key credentials, there is no `PlatformPrincipal`. The `PlatformCredential` is `API key`.
+ For GCM (Firebase Cloud Messaging) using token credentials, there is no `PlatformPrincipal`. The `PlatformCredential` is a JSON formatted private key file. When using the AWS CLI or AWS SDKs, the file must be in string format and special characters must be ignored. To format the file correctly, Amazon SNS recommends using the following command: `SERVICE_JSON=$(jq @json < service.json)`.
+ For MPNS, `PlatformPrincipal` is `TLS certificate` and `PlatformCredential` is `private key`.
+ For WNS, `PlatformPrincipal` is `Package Security Identifier` and `PlatformCredential` is `secret key`.

You can use the returned `PlatformApplicationArn` as an attribute for the `CreatePlatformEndpoint` action.

## Request Parameters
<a name="API_CreatePlatformApplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Attributes** Attributes.entry.N.key (key)Attributes.entry.N.value (value)
For a list of attributes, see [`SetPlatformApplicationAttributes`](https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html).
Type: String to string map
Required: Yes

 ** Name **
Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.
Type: String
Required: Yes

 ** Platform **
The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS\_SANDBOX, and GCM (Firebase Cloud Messaging).
Type: String
Required: Yes

## Response Elements
<a name="API_CreatePlatformApplication_ResponseElements"></a>

The following element is returned by the service.

 ** PlatformApplicationArn **
 `PlatformApplicationArn` is returned.
Type: String

## Errors
<a name="API_CreatePlatformApplication_Errors"></a>

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

## Examples
<a name="API_CreatePlatformApplication_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_CreatePlatformApplication_Example_1"></a>

This example illustrates one usage of CreatePlatformApplication.

#### Sample Request
<a name="API_CreatePlatformApplication_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=CreatePlatformApplication
&Name=gcmpushapp
&Platform=GCM
&Attributes.entry.1.key=PlatformCredential
&Attributes.entry.1.value=AIzaSyClE2lcV2zEKTLYYo645zfk2jhQPFeyxDo
&Attributes.entry.2.key=PlatformPrincipal
&Attributes.entry.2.value=There+is+no+principal+for+GCM
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreatePlatformApplication_Example_1_Response"></a>

```
<CreatePlatformApplicationResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <CreatePlatformApplicationResult>
        <PlatformApplicationArn>arn:aws:sns:us-west-2:123456789012:app/GCM/gcmpushapp</PlatformApplicationArn>
    </CreatePlatformApplicationResult>
    <ResponseMetadata>
        <RequestId>b6f0e78b-e9d4-5a0e-b973-adc04e8a4ff9</RequestId>
    </ResponseMetadata>
</CreatePlatformApplicationResponse>
```

## See Also
<a name="API_CreatePlatformApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/CreatePlatformApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/CreatePlatformApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/CreatePlatformApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/CreatePlatformApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/CreatePlatformApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/CreatePlatformApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/CreatePlatformApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/CreatePlatformApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/CreatePlatformApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/CreatePlatformApplication)
