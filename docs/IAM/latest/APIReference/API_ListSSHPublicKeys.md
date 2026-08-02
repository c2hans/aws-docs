---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSSHPublicKeys.html
---

# ListSSHPublicKeys
<a name="API_ListSSHPublicKeys"></a>

Returns information about the SSH public keys associated with the specified IAM user. If none exists, the operation returns an empty list.

The SSH public keys returned by this operation are used only for authenticating the IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see [Set up CodeCommit for SSH connections](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-credentials-ssh.html) in the *CodeCommit User Guide*.

Although each user is limited to a small number of keys, you can still paginate the results using the `MaxItems` and `Marker` parameters.

## Request Parameters
<a name="API_ListSSHPublicKeys_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **
Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the `Marker` element in the response that you received to indicate where the next call should start.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** MaxItems **
Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the `IsTruncated` response element is `true`.
If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the `IsTruncated` response element returns `true`, and `Marker` contains a value to include in the subsequent call that tells the service where to continue from.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** UserName **
The name of the IAM user to list SSH public keys for. If none is specified, the `UserName` field is determined implicitly based on the AWS access key used to sign the request.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

## Response Elements
<a name="API_ListSSHPublicKeys_ResponseElements"></a>

The following elements are returned by the service.

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

 **SSHPublicKeys.member.N**
A list of the SSH public keys assigned to IAM user.
Type: Array of [SSHPublicKeyMetadata](API_SSHPublicKeyMetadata.md) objects

## Errors
<a name="API_ListSSHPublicKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

## Examples
<a name="API_ListSSHPublicKeys_Examples"></a>

### Example
<a name="API_ListSSHPublicKeys_Example_1"></a>

This example illustrates one usage of ListSSHPublicKeys.

#### Sample Request
<a name="API_ListSSHPublicKeys_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListSSHPublicKeys
&UserName=Jane
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListSSHPublicKeys_Example_1_Response"></a>

```
<ListSSHPublicKeysResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListSSHPublicKeysResult>
    <IsTruncated>false</IsTruncated>
    <SSHPublicKeys>
      <member>
        <UploadDate>2015-06-05T20:56:46Z</UploadDate>
        <UserName>Jane</UserName>
        <SSHPublicKeyId>APKAEIVFHP46CEXAMPLE</SSHPublicKeyId>
        <Status>Active</Status>
      </member>
    </SSHPublicKeys>
  </ListSSHPublicKeysResult>
  <ResponseMetadata>
    <RequestId>9f8e2d77-f36c-11e4-97db-33c4eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListSSHPublicKeysResponse>
```

## See Also
<a name="API_ListSSHPublicKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListSSHPublicKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListSSHPublicKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListSSHPublicKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListSSHPublicKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListSSHPublicKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListSSHPublicKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListSSHPublicKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListSSHPublicKeys)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListSSHPublicKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListSSHPublicKeys)
