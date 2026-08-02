---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_AuthorizationData.html
---

# AuthorizationData
<a name="API_AuthorizationData"></a>

An object representing authorization data for an Amazon ECR registry.

## Contents
<a name="API_AuthorizationData_Contents"></a>

 ** authorizationToken **   <a name="ECR-Type-AuthorizationData-authorizationToken"></a>
A base64-encoded string that contains authorization data for the specified Amazon ECR registry. When the string is decoded, it is presented in the format `user:password` for private registry authentication using `docker login`.
Type: String
Pattern: `^\S+$`
Required: No

 ** expiresAt **   <a name="ECR-Type-AuthorizationData-expiresAt"></a>
The Unix time in seconds and milliseconds when the authorization token expires. Authorization tokens are valid for 12 hours.
Type: Timestamp
Required: No

 ** proxyEndpoint **   <a name="ECR-Type-AuthorizationData-proxyEndpoint"></a>
The registry URL to use for this authorization token in a `docker login` command. The Amazon ECR registry URL format is `https://aws_account_id.dkr.ecr.region.amazonaws.com`. For example, `https://012345678910.dkr.ecr.us-east-1.amazonaws.com`..
Type: String
Required: No

## See Also
<a name="API_AuthorizationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/AuthorizationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/AuthorizationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/AuthorizationData)
