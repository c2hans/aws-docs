---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveClientIDFromOpenIDConnectProvider.html
---

# RemoveClientIDFromOpenIDConnectProvider
<a name="API_RemoveClientIDFromOpenIDConnectProvider"></a>

Removes the specified client ID (also known as audience) from the list of client IDs registered for the specified IAM OpenID Connect (OIDC) provider resource object.

This operation is idempotent; it does not fail or return an error if you try to remove a client ID that does not exist.

## Request Parameters
<a name="API_RemoveClientIDFromOpenIDConnectProvider_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClientID **
The client ID (also known as audience) to remove from the IAM OIDC provider resource. For more information about client IDs, see [CreateOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** OpenIDConnectProviderArn **
The Amazon Resource Name (ARN) of the IAM OIDC provider resource to remove the client ID from. You can get a list of OIDC provider ARNs by using the [ListOpenIDConnectProviders](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html) operation.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## Errors
<a name="API_RemoveClientIDFromOpenIDConnectProvider_Errors"></a>

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
<a name="API_RemoveClientIDFromOpenIDConnectProvider_Examples"></a>

### Example
<a name="API_RemoveClientIDFromOpenIDConnectProvider_Example_1"></a>

This example illustrates one usage of RemoveClientIDFromOpenIDConnectProvider.

#### Sample Request
<a name="API_RemoveClientIDFromOpenIDConnectProvider_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=RemoveClientIDFromOpenIDConnectProvider
&ClientID=my-application-ID
&OpenIDConnectProviderArn=arn:aws:iam::123456789012:oidc-provider/server.example.com
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_RemoveClientIDFromOpenIDConnectProvider_Example_1_Response"></a>

```
<RemoveClientIDFromOpenIDConnectProviderResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>1a5214df-4f67-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</RemoveClientIDFromOpenIDConnectProviderResponse>
```

## See Also
<a name="API_RemoveClientIDFromOpenIDConnectProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/RemoveClientIDFromOpenIDConnectProvider)
