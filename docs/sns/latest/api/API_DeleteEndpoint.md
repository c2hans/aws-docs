---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_DeleteEndpoint.html
---

# DeleteEndpoint
<a name="API_DeleteEndpoint"></a>

Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see [Using Amazon SNS Mobile Push Notifications](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

When you delete an endpoint that is also subscribed to a topic, then you must also unsubscribe the endpoint from the topic.

## Request Parameters
<a name="API_DeleteEndpoint_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EndpointArn **
 `EndpointArn` of endpoint to delete.
Type: String
Required: Yes

## Errors
<a name="API_DeleteEndpoint_Errors"></a>

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
<a name="API_DeleteEndpoint_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_DeleteEndpoint_Example_1"></a>

This example illustrates one usage of DeleteEndpoint.

#### Sample Request
<a name="API_DeleteEndpoint_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=DeleteEndpoint
&EndpointArn=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3Aendpoint%2FGCM%2Fgcmpushapp%2F5e3e9847-3183-3f18-a7e8-671c3a57d4b3
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteEndpoint_Example_1_Response"></a>

```
<DeleteEndpointResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>c1d2b191-353c-5a5f-8969-fbdd3900afa8</RequestId>
    </ResponseMetadata>
</DeleteEndpointResponse>
```

## See Also
<a name="API_DeleteEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/DeleteEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/DeleteEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/DeleteEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/DeleteEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/DeleteEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/DeleteEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/DeleteEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/DeleteEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/DeleteEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/DeleteEndpoint)
