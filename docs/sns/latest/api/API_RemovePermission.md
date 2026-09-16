---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_RemovePermission.html
---

# RemovePermission
<a name="API_RemovePermission"></a>

Removes a statement from a topic's access control policy.

**Note**
To remove the ability to change topic permissions, you must deny permissions to the `AddPermission`, `RemovePermission`, and `SetTopicAttributes` actions in your IAM policy.

## Request Parameters
<a name="API_RemovePermission_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Label **
The unique label of the statement you want to remove.
Type: String
Required: Yes

 ** TopicArn **
The ARN of the topic whose access control policy you wish to modify.
Type: String
Required: Yes

## Errors
<a name="API_RemovePermission_Errors"></a>

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
<a name="API_RemovePermission_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_RemovePermission_Example_1"></a>

This example illustrates one usage of RemovePermission.

#### Sample Request
<a name="API_RemovePermission_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=RemovePermission
&TopicArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Test
&Label=NewPermission
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_RemovePermission_Example_1_Response"></a>

```
<RemovePermissionResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>d170b150-33a8-11df-995a-2d6fbe836cc1</RequestId>
    </ResponseMetadata>
</RemovePermissionResponse>
```

## See Also
<a name="API_RemovePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/RemovePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/RemovePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/RemovePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/RemovePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/RemovePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/RemovePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/RemovePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/RemovePermission)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/RemovePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/RemovePermission)
