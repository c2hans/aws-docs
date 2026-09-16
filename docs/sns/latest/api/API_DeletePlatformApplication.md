---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_DeletePlatformApplication.html
---

# DeletePlatformApplication
<a name="API_DeletePlatformApplication"></a>

Deletes a platform application object for one of the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see [Using Amazon SNS Mobile Push Notifications](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

## Request Parameters
<a name="API_DeletePlatformApplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** PlatformApplicationArn **
 `PlatformApplicationArn` of platform application object to delete.
Type: String
Required: Yes

## Errors
<a name="API_DeletePlatformApplication_Errors"></a>

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
<a name="API_DeletePlatformApplication_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_DeletePlatformApplication_Example_1"></a>

This example illustrates one usage of DeletePlatformApplication.

#### Sample Request
<a name="API_DeletePlatformApplication_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=DeletePlatformApplication
&PlatformApplicationArn=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3Aapp%2FGCM%2Fgcmpushapp
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeletePlatformApplication_Example_1_Response"></a>

```
<DeletePlatformApplicationResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>097dac18-7a77-5823-a8dd-e65476dcb037</RequestId>
    </ResponseMetadata>
</DeletePlatformApplicationResponse>
```

## See Also
<a name="API_DeletePlatformApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/DeletePlatformApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/DeletePlatformApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/DeletePlatformApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/DeletePlatformApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/DeletePlatformApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/DeletePlatformApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/DeletePlatformApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/DeletePlatformApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/DeletePlatformApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/DeletePlatformApplication)
