---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_auth_Credentials.html
---

# Credentials
<a name="API_auth_Credentials"></a>

The * AWS Signature Version 4* type of temporary credentials.

## Contents
<a name="API_auth_Credentials_Contents"></a>

 ** accessKeyId **   <a name="AmazonEKS-Type-auth_Credentials-accessKeyId"></a>
The access key ID that identifies the temporary security credentials.
Type: String
Required: Yes

 ** expiration **   <a name="AmazonEKS-Type-auth_Credentials-expiration"></a>
The Unix epoch timestamp in seconds when the current credentials expire.
Type: Timestamp
Required: Yes

 ** secretAccessKey **   <a name="AmazonEKS-Type-auth_Credentials-secretAccessKey"></a>
The secret access key that applications inside the pods use to sign requests.
Type: String
Required: Yes

 ** sessionToken **   <a name="AmazonEKS-Type-auth_Credentials-sessionToken"></a>
The token that applications inside the pods must pass to any service API to use the temporary credentials.
Type: String
Required: Yes

## See Also
<a name="API_auth_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-auth-2023-11-26/Credentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-auth-2023-11-26/Credentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-auth-2023-11-26/Credentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
