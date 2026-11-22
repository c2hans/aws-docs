---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RemoveAlias.html
---

# RemoveAlias

Removes an alias from a stack. After the alias is removed successfully, it can no longer be used to reference the stack in API calls.

## Request Parameters
<a name="API_RemoveAlias_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AliasName **
The alias name to remove.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Errors
<a name="API_RemoveAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RemoveAlias_Examples"></a>

### RemoveAlias
<a name="API_RemoveAlias_Example_1"></a>

This example illustrates one usage of RemoveAlias.

#### Sample Request
<a name="API_RemoveAlias_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=RemoveAlias
 &AliasName=prod-api
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response
<a name="API_RemoveAlias_Example_1_Response"></a>

```
<RemoveAliasResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ResponseMetadata>
    <RequestId>a1b2c3d4-5678-90ab-cdef-example22222</RequestId>
  </ResponseMetadata>
</RemoveAliasResponse>
```

## See Also
<a name="API_RemoveAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/RemoveAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/RemoveAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RemoveAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/RemoveAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RemoveAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/RemoveAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/RemoveAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/RemoveAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/RemoveAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RemoveAlias)
