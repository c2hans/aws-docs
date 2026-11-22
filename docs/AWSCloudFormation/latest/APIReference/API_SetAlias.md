---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetAlias.html
---

# SetAlias

Assigns an alias to an existing stack. An alias is an alternative name for a stack that can be used in place of the stack name in any CloudFormation API call that accepts the `StackName` parameter. This enables you to effectively rename a stack without recreating it.

After setting an alias, both the original stack name and the alias resolve to the same stack. Setting an alias does not change the stack's ARN, physical resource IDs, or any deployed resources.

**Note**
Each stack can have at most one alias. To change a stack's alias, first remove the existing alias using [RemoveAlias](API_RemoveAlias.md), then set a new one.

## Request Parameters
<a name="API_SetAlias_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AliasName **
The alias to assign to the stack. The alias can then be used in place of the stack name in any API call that accepts `StackName`.
The name must be unique within the same account and Region. It cannot match an existing stack name or another active alias.
An alias name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** StackName **
The name or unique stack ID of the stack to assign an alias to.
Type: String
Required: Yes

## Errors
<a name="API_SetAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExists **
The resource with the name requested already exists.
HTTP Status Code: 400

 ** LimitExceeded **
The quota for the resource has already been reached.
For information about resource and stack limitations, see [CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the * AWS CloudFormation User Guide*.
HTTP Status Code: 400

## Examples
<a name="API_SetAlias_Examples"></a>

### SetAlias
<a name="API_SetAlias_Example_1"></a>

This example illustrates one usage of SetAlias.

#### Sample Request
<a name="API_SetAlias_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=SetAlias
 &StackName=MyStack
 &AliasName=MyAlias
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response
<a name="API_SetAlias_Example_1_Response"></a>

```
<SetAliasResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ResponseMetadata>
    <RequestId>a1b2c3d4-5678-90ab-cdef-example11111</RequestId>
  </ResponseMetadata>
</SetAliasResponse>
```

## See Also
<a name="API_SetAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/SetAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/SetAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/SetAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/SetAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/SetAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/SetAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/SetAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/SetAlias)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/SetAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/SetAlias)
