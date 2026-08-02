---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResetServiceSpecificCredential.html
---

# ResetServiceSpecificCredential
<a name="API_ResetServiceSpecificCredential"></a>

Resets the password for a service-specific credential. The new password is AWS generated and cryptographically strong. It cannot be configured by the user. Resetting the password immediately invalidates the previous password associated with this user.

## Request Parameters
<a name="API_ResetServiceSpecificCredential_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ServiceSpecificCredentialId **
The unique identifier of the service-specific credential.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters that can consist of any upper or lowercased letter or digit.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** UserName **
The name of the IAM user associated with the service-specific credential. If this value is not specified, then the operation assumes the user whose credentials are used to call the operation.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

## Response Elements
<a name="API_ResetServiceSpecificCredential_ResponseElements"></a>

The following element is returned by the service.

 ** ServiceSpecificCredential **
A structure with details about the updated service-specific credential, including the new password.
This is the **only** time that you can access the password. You cannot recover the password later, but you can reset it again.
Type: [ServiceSpecificCredential](API_ServiceSpecificCredential.md) object

## Errors
<a name="API_ResetServiceSpecificCredential_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

## Examples
<a name="API_ResetServiceSpecificCredential_Examples"></a>

### Example
<a name="API_ResetServiceSpecificCredential_Example_1"></a>

The following example shows how to request a new password for an existing service-specific credential that is associated with a specific IAM user.

#### Sample Request
<a name="API_ResetServiceSpecificCredential_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ResetServiceSpecificCredential
&UserName=Jane
&ServiceSpecificCredentialId=ACCA12345ABCDEXAMPLE
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ResetServiceSpecificCredential_Example_1_Response"></a>

```
<ResetServiceSpecificCredentialResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResetServiceSpecificCredentialResult>
    <ServiceSpecificCredential>
      <CreateDate>2016-10-15T20:56:46.012Z</CreateDate>
      <ServiceName>codecommit.amazonaws.com</ServiceName>
      <ServiceUserName>Jane-123456789012</ServiceUserName>
      <ServicePassword>wJalrXUtnFEMI/K7MDENGPxRfiCYzEXAMPLE</ServicePassword>
      <ServiceSpecificCredentialId>ACCA12345ABCDEXAMPLE</ServiceSpecificCredentialId>
      <Status>Active</Status>
      <UserName>Jane</UserName>
    </ServiceSpecificCredential>
  </ResetServiceSpecificCredentialResult>
  <ResponseMetadata>
    <RequestId>EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE</RequestId>
  </ResponseMetadata>
</ResetServiceSpecificCredentialResponse>
```

## See Also
<a name="API_ResetServiceSpecificCredential_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ResetServiceSpecificCredential)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ResetServiceSpecificCredential)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ResetServiceSpecificCredential)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ResetServiceSpecificCredential)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ResetServiceSpecificCredential)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ResetServiceSpecificCredential)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ResetServiceSpecificCredential)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ResetServiceSpecificCredential)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ResetServiceSpecificCredential)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ResetServiceSpecificCredential)
