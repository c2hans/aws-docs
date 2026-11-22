---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateOpenIDConnectProvider.html
---

# UpdateOpenIDConnectProvider

Updates the configuration of an existing IAM OpenID Connect (OIDC) identity provider resource object. Use this operation to set, change, or remove the trusted identity propagation context provider, and to associate or disassociate an IAM Identity Center instance with the provider.

**Note**
This operation does not update the OIDC provider's server certificate thumbprints. Thumbprints are managed only by the [UpdateOpenIDConnectProviderThumbprint](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateOpenIDConnectProviderThumbprint.html) operation. To change a provider's thumbprints, call that operation instead.

To remove a configuration rather than replace it, use the `RemoveContextProvider` and `RemoveIdentityCenterInstance` parameters. For each configuration, provide either the new value or the corresponding `Remove` flag in a single request, but not both. For example, specifying both `ContextProvider` and `RemoveContextProvider` in the same request is not allowed.

A single request can change either the context provider or the IAM Identity Center association, but not both. To change both, make separate `UpdateOpenIDConnectProvider` requests. To remove the context provider, first remove the IAM Identity Center association in a separate request.

To control who can configure trusted identity propagation on an OIDC provider, use the [iam:EnableIdentityPropagation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_EnableIdentityPropagation), [iam:EnableIdentityCenterAssociation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_EnableIdentityCenterAssociation), [iam:ResourceIdentityProviderIssuers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_ResourceIdentityProviderIssuers), [iam:RequestIdentityCenterInstanceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_RequestIdentityCenterInstanceArn), and [iam:ResourceIdentityCenterInstanceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_ResourceIdentityCenterInstanceArn) condition keys in IAM policies. The `Request` keys contain the values in the request. The `Resource` keys contain the values stored on the provider.

## Request Parameters
<a name="API_UpdateOpenIDConnectProvider_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ContextProvider **
The trusted identity propagation context provider configuration to set on the OIDC provider. This configuration defines the subject mapping and the source-to-target key mappings that are used when trusted context is injected. For more information, see [ContextProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ContextProvider.html).
To remove the existing context provider instead of replacing it, use `RemoveContextProvider`. Do not specify both `ContextProvider` and `RemoveContextProvider` in the same request.
Type: [ContextProvider](API_ContextProvider.md) object
Required: No

 ** IdentityCenterInstanceArn **
The Amazon Resource Name (ARN) of the IAM Identity Center instance to associate with the OIDC provider.
For the format, see [InstanceMetadata](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_InstanceMetadata.html) in the *IAM Identity Center API Reference*.
To disassociate the currently associated instance instead of changing it, use `RemoveIdentityCenterInstance`. Do not specify both `IdentityCenterInstanceArn` and `RemoveIdentityCenterInstance` in the same request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Required: No

 ** OpenIDConnectProviderArn **
The Amazon Resource Name (ARN) of the IAM OIDC provider resource object to update. You can get a list of OIDC provider resource ARNs by using the [ListOpenIDConnectProviders](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html) operation.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** RemoveContextProvider **
Specifies whether to remove the existing context provider configuration from the OIDC provider. Set this value to `true` to remove the context provider.
This parameter is mutually exclusive with `ContextProvider`. In a single request, specify either a new `ContextProvider` value or `RemoveContextProvider`, but not both.
Type: Boolean
Required: No

 ** RemoveIdentityCenterInstance **
Specifies whether to disassociate the IAM Identity Center instance from the OIDC provider. Set this value to `true` to remove the association.
This parameter is mutually exclusive with `IdentityCenterInstanceArn`. In a single request, specify either a new `IdentityCenterInstanceArn` value or `RemoveIdentityCenterInstance`, but not both.
Type: Boolean
Required: No

## Errors
<a name="API_UpdateOpenIDConnectProvider_Errors"></a>

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
<a name="API_UpdateOpenIDConnectProvider_Examples"></a>

### Update the context provider configuration
<a name="API_UpdateOpenIDConnectProvider_Example_1"></a>

This example illustrates one usage of UpdateOpenIDConnectProvider.

#### Sample Request
<a name="API_UpdateOpenIDConnectProvider_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=UpdateOpenIDConnectProvider
&OpenIDConnectProviderArn=arn:aws:iam::123456789012:oidc-provider/server.example.com
&ContextProvider.SubjectSourceKey=sub
&ContextProvider.SubjectTypeValue=user
&ContextProvider.KeyDefinitionList.member.1.SourceKey=department
&ContextProvider.KeyDefinitionList.member.1.TargetKey=department
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateOpenIDConnectProvider_Example_1_Response"></a>

```
<UpdateOpenIDConnectProviderResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>29b6031c-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</UpdateOpenIDConnectProviderResponse>
```

### Associate an IAM Identity Center instance
<a name="API_UpdateOpenIDConnectProvider_Example_2"></a>

This example illustrates one usage of UpdateOpenIDConnectProvider.

#### Sample Request
<a name="API_UpdateOpenIDConnectProvider_Example_2_Request"></a>

```
https://iam.amazonaws.com/?Action=UpdateOpenIDConnectProvider
&OpenIDConnectProviderArn=arn:aws:iam::123456789012:oidc-provider/server.example.com
&IdentityCenterInstanceArn=arn:aws:sso:::instance/ssoins-1234567890abcdef
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateOpenIDConnectProvider_Example_2_Response"></a>

```
<UpdateOpenIDConnectProviderResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>3a7c142d-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</UpdateOpenIDConnectProviderResponse>
```

## See Also
<a name="API_UpdateOpenIDConnectProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UpdateOpenIDConnectProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UpdateOpenIDConnectProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UpdateOpenIDConnectProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UpdateOpenIDConnectProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UpdateOpenIDConnectProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UpdateOpenIDConnectProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UpdateOpenIDConnectProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UpdateOpenIDConnectProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UpdateOpenIDConnectProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UpdateOpenIDConnectProvider)
