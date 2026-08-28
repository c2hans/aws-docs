---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_AuthorizationData.html
---

# AuthorizationData
<a name="API_AuthorizationData"></a>

An authorization token data object that corresponds to a public registry.

## Contents
<a name="API_AuthorizationData_Contents"></a>

 ** authorizationToken **   <a name="ecrpublic-Type-AuthorizationData-authorizationToken"></a>
A base64-encoded string that contains authorization data for a public Amazon ECR registry. When the string is decoded, it's presented in the format `user:password` for public registry authentication using `docker login`.
Type: String
Pattern: `^\S+$`
Required: No

 ** expiresAt **   <a name="ecrpublic-Type-AuthorizationData-expiresAt"></a>
The Unix time in seconds and milliseconds when the authorization token expires. Authorization tokens are valid for 12 hours.
Type: Timestamp
Required: No

## See Also
<a name="API_AuthorizationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/AuthorizationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/AuthorizationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/AuthorizationData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
