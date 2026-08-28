---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformEndpoint.html
---

# CreatePlatformEndpoint
<a name="API_CreatePlatformEndpoint"></a>

Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM (Firebase Cloud Messaging) and APNS. `CreatePlatformEndpoint` requires the `PlatformApplicationArn` that is returned from `CreatePlatformApplication`. You can use the returned `EndpointArn` to send a message to a mobile app or by the `Subscribe` action for subscription to a topic. The `CreatePlatformEndpoint` action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint's ARN is returned without creating a new endpoint. For more information, see [Using Amazon SNS Mobile Push Notifications](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

When using `CreatePlatformEndpoint` with Baidu, two attributes must be provided: ChannelId and UserId. The token field must also contain the ChannelId. For more information, see [Creating an Amazon SNS Endpoint for Baidu](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePushBaiduEndpoint.html).

## Request Parameters
<a name="API_CreatePlatformEndpoint_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Attributes** Attributes.entry.N.key (key)Attributes.entry.N.value (value)
For a list of attributes, see [`SetEndpointAttributes`](https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html).
Type: String to string map
Required: No

 ** CustomUserData **
Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
Type: String
Required: No

 ** PlatformApplicationArn **
 `PlatformApplicationArn` returned from CreatePlatformApplication is used to create a an endpoint.
Type: String
Required: Yes

 ** Token **
Unique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using GCM (Firebase Cloud Messaging) or ADM, the device token equivalent is called the registration ID.
Type: String
Required: Yes

## Response Elements
<a name="API_CreatePlatformEndpoint_ResponseElements"></a>

The following element is returned by the service.

 ** EndpointArn **
EndpointArn returned from CreateEndpoint action.
Type: String

## Errors
<a name="API_CreatePlatformEndpoint_Errors"></a>

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
<a name="API_CreatePlatformEndpoint_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_CreatePlatformEndpoint_Example_1"></a>

This example illustrates one usage of CreatePlatformEndpoint.

#### Sample Request
<a name="API_CreatePlatformEndpoint_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=CreatePlatformEndpoint
&PlatformApplicationArn=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3Aapp%2FGCM%2Fgcmpushapp
&Token=APA91bGi7fFachkC1xjlqT66VYEucGHochmf1VQAr9k...jsM0PKPxKhddCzx6paEsyay9Zn3D4wNUJb8m6HZrBEXAMPLE
&CustomUserData=UserId%3D27576823
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreatePlatformEndpoint_Example_1_Response"></a>

```
<CreatePlatformEndpointResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <CreatePlatformEndpointResult>
        <EndpointArn>arn:aws:sns:us-west-2:123456789012:endpoint/GCM/gcmpushapp/5e3e9847-3183-3f18-a7e8-671c3a57d4b3</EndpointArn>
    </CreatePlatformEndpointResult>
    <ResponseMetadata>
        <RequestId>6613341d-3e15-53f7-bf3c-7e56994ba278</RequestId>
    </ResponseMetadata>
</CreatePlatformEndpointResponse>
```

## See Also
<a name="API_CreatePlatformEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/CreatePlatformEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/CreatePlatformEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/CreatePlatformEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/CreatePlatformEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/CreatePlatformEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/CreatePlatformEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/CreatePlatformEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/CreatePlatformEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/CreatePlatformEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/CreatePlatformEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
