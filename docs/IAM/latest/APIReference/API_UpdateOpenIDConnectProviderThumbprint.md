---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateOpenIDConnectProviderThumbprint.html
---

# UpdateOpenIDConnectProviderThumbprint
<a name="API_UpdateOpenIDConnectProviderThumbprint"></a>

Replaces the existing list of server certificate thumbprints associated with an OpenID Connect (OIDC) provider resource object with a new list of thumbprints.

The list that you pass with this operation completely replaces the existing list of thumbprints. (The lists are not merged.)

Typically, you need to update a thumbprint only when the identity provider certificate changes, which occurs rarely. However, if the provider's certificate *does* change, any attempt to assume an IAM role that specifies the OIDC provider as a principal fails until the certificate thumbprint is updated.

**Note**
 AWS secures communication with OIDC identity providers (IdPs) using our library of trusted root certificate authorities (CAs) to verify the JSON Web Key Set (JWKS) endpoint's TLS certificate. If your OIDC IdP relies on a certificate that is not signed by one of these trusted CAs, only then we secure communication using the thumbprints set in the IdP's configuration.

**Note**
Trust for the OIDC provider is derived from the provider certificate and is validated by the thumbprint. Therefore, it is best to limit access to the `UpdateOpenIDConnectProviderThumbprint` operation to highly privileged users.

## Request Parameters
<a name="API_UpdateOpenIDConnectProviderThumbprint_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** OpenIDConnectProviderArn **
The Amazon Resource Name (ARN) of the IAM OIDC provider resource object for which you want to update the thumbprint. You can get a list of OIDC provider ARNs by using the [ListOpenIDConnectProviders](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html) operation.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 **ThumbprintList.member.N**
A list of certificate thumbprints that are associated with the specified IAM OpenID Connect provider. For more information, see [CreateOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html).
Type: Array of strings
Length Constraints: Fixed length of 40.
Required: Yes

## Errors
<a name="API_UpdateOpenIDConnectProviderThumbprint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_UpdateOpenIDConnectProviderThumbprint_Examples"></a>

### Example
<a name="API_UpdateOpenIDConnectProviderThumbprint_Example_1"></a>

This example illustrates one usage of UpdateOpenIDConnectProviderThumbprint.

#### Sample Request
<a name="API_UpdateOpenIDConnectProviderThumbprint_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=UpdateOpenIDConnectProviderThumbprint
&ThumbprintList.list.1=c3768084dfb3d2b68b7897bf5f565da8eEXAMPLE
&OpenIDConnectProviderArn=arn:aws:iam::123456789012:oidc-provider/server.example.com
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateOpenIDConnectProviderThumbprint_Example_1_Response"></a>

```
<UpdateOpenIDConnectProviderThumbprintResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>29b6031c-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</UpdateOpenIDConnectProviderThumbprintResponse>
```

## See Also
<a name="API_UpdateOpenIDConnectProviderThumbprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UpdateOpenIDConnectProviderThumbprint)
