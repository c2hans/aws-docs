---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ResourcePolicy.html
---

# ResourcePolicy
<a name="API_ResourcePolicy"></a>

 An AWS CodeArtifact resource policy that contains a resource ARN, document details, and a revision.

## Contents
<a name="API_ResourcePolicy_Contents"></a>

 ** document **   <a name="codeartifact-Type-ResourcePolicy-document"></a>
 The resource policy formatted in JSON.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7168.
Pattern: `[\P{C}\s]+`
Required: No

 ** resourceArn **   <a name="codeartifact-Type-ResourcePolicy-resourceArn"></a>
 The ARN of the resource associated with the resource policy
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** revision **   <a name="codeartifact-Type-ResourcePolicy-revision"></a>
 The current revision of the resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `\S+`
Required: No

## See Also
<a name="API_ResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/ResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/ResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/ResourcePolicy)
