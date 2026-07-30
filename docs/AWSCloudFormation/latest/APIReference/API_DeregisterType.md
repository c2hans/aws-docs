---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html
---

# DeregisterType
<a name="API_DeregisterType"></a>

Marks an extension or extension version as `DEPRECATED` in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.

To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.

You can't deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.

To view the deprecation status of an extension or extension version, use [DescribeType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html).

For more information, see [Remove third-party private extensions from your account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-private-deregister-extension.html) in the * AWS CloudFormation User Guide*.

## Request Parameters
<a name="API_DeregisterType_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Arn **
The Amazon Resource Name (ARN) of the extension.
Conditional: You must specify either `TypeName` and `Type`, or `Arn`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:[0-9]{12}:type/.+`
Required: No

 ** Type **
The kind of extension.
Conditional: You must specify either `TypeName` and `Type`, or `Arn`.
Type: String
Valid Values: `RESOURCE | MODULE | HOOK`
Required: No

 ** TypeName **
The name of the extension.
Conditional: You must specify either `TypeName` and `Type`, or `Arn`.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 204.
Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`
Required: No

 ** VersionId **
The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-]+`
Required: No

## Errors
<a name="API_DeregisterType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CFNRegistry **
An error occurred during a CloudFormation registry operation.
 ** Message **
A message with details about the error that occurred.
HTTP Status Code: 400

 ** TypeNotFound **
The specified extension doesn't exist in the CloudFormation registry.
HTTP Status Code: 404

## Examples
<a name="API_DeregisterType_Examples"></a>

### Deregistering an extension version
<a name="API_DeregisterType_Example_1"></a>

The following example removes a specific version of the `My::Resource::Example` resource type from active use in the CloudFormation registry.

#### Sample Request
<a name="API_DeregisterType_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DeregisterType
 &Version=2010-05-15
 &TypeName=My::Resource::Example
 &Type=RESOURCE
 &VersionId=00000002
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20191204T181601Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_DeregisterType_Example_1_Response"></a>

```
<DeregisterTypeResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DeregisterTypeResult/>
  <ResponseMetadata>
    <RequestId>78c291d1-4463-4845-a600-29221example</RequestId>
  </ResponseMetadata>
</DeregisterTypeResponse>
```

## See Also
<a name="API_DeregisterType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeregisterType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/DeregisterType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeregisterType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeregisterType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeregisterType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeregisterType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeregisterType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeregisterType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeregisterType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeregisterType)
