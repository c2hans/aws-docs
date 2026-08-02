---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SigningRule.html
---

# SigningRule
<a name="API_SigningRule"></a>

A signing rule that specifies a signing profile and optional repository filters. When an image is pushed to a matching repository, a signing job is created using the specified profile.

## Contents
<a name="API_SigningRule_Contents"></a>

 ** signingProfileArn **   <a name="ECR-Type-SigningRule-signingProfileArn"></a>
The ARN of the AWS Signer signing profile to use for signing images that match this rule. For more information about signing profiles, see [Signing profiles](https://docs.aws.amazon.com/signer/latest/developerguide/signing-profiles.html) in the * AWS Signer Developer Guide*.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^arn:aws(-[a-z]+)*:signer:[a-z0-9-]+:[0-9]{12}:\/signing-profiles\/[a-zA-Z0-9_]{2,}$`
Required: Yes

 ** repositoryFilters **   <a name="ECR-Type-SigningRule-repositoryFilters"></a>
A list of repository filters that determine which repositories have their images signed on push. If no filters are specified, all images pushed to the registry are signed using the rule's signing profile. Maximum of 100 filters per rule.
Type: Array of [SigningRepositoryFilter](API_SigningRepositoryFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_SigningRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/SigningRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/SigningRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/SigningRule)
