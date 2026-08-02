---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveUserFromGroup.html
---

# RemoveUserFromGroup
<a name="API_RemoveUserFromGroup"></a>

Removes the specified user from the specified group.

## Request Parameters
<a name="API_RemoveUserFromGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GroupName **
The name of the group to update.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** UserName **
The name of the user to remove.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Errors
<a name="API_RemoveUserFromGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_RemoveUserFromGroup_Examples"></a>

### Example
<a name="API_RemoveUserFromGroup_Example_1"></a>

This example illustrates one usage of RemoveUserFromGroup.

#### Sample Request
<a name="API_RemoveUserFromGroup_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=RemoveUserFromGroup
&GroupName=Managers
&UserName=Bob
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_RemoveUserFromGroup_Example_1_Response"></a>

```
<RemoveUserFromGroupResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</RemoveUserFromGroupResponse>
```

## See Also
<a name="API_RemoveUserFromGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/RemoveUserFromGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/RemoveUserFromGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/RemoveUserFromGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/RemoveUserFromGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/RemoveUserFromGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/RemoveUserFromGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/RemoveUserFromGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/RemoveUserFromGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/RemoveUserFromGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/RemoveUserFromGroup)
