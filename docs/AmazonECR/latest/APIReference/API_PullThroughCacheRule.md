---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PullThroughCacheRule.html
---

# PullThroughCacheRule
<a name="API_PullThroughCacheRule"></a>

The details of a pull through cache rule.

## Contents
<a name="API_PullThroughCacheRule_Contents"></a>

 ** createdAt **   <a name="ECR-Type-PullThroughCacheRule-createdAt"></a>
The date and time the pull through cache was created.
Type: Timestamp
Required: No

 ** credentialArn **   <a name="ECR-Type-PullThroughCacheRule-credentialArn"></a>
The ARN of the Secrets Manager secret associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 612.
Pattern: `^arn:aws(-\w+)*:secretsmanager:[a-zA-Z0-9-:]+:secret:ecr\-pullthroughcache\/[a-zA-Z0-9\/_+=.@-]+$`
Required: No

 ** customRoleArn **   <a name="ECR-Type-PullThroughCacheRule-customRoleArn"></a>
The ARN of the IAM role associated with the pull through cache rule.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** ecrRepositoryPrefix **   <a name="ECR-Type-PullThroughCacheRule-ecrRepositoryPrefix"></a>
The Amazon ECR repository prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: No

 ** registryId **   <a name="ECR-Type-PullThroughCacheRule-registryId"></a>
The AWS account ID associated with the registry the pull through cache rule is associated with.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** updatedAt **   <a name="ECR-Type-PullThroughCacheRule-updatedAt"></a>
The date and time, in JavaScript date format, when the pull through cache rule was last updated.
Type: Timestamp
Required: No

 ** upstreamRegistry **   <a name="ECR-Type-PullThroughCacheRule-upstreamRegistry"></a>
The name of the upstream source registry associated with the pull through cache rule.
Type: String
Valid Values: `ecr | ecr-public | quay | k8s | docker-hub | github-container-registry | azure-container-registry | gitlab-container-registry | chainguard`
Required: No

 ** upstreamRegistryUrl **   <a name="ECR-Type-PullThroughCacheRule-upstreamRegistryUrl"></a>
The upstream registry URL associated with the pull through cache rule.
Type: String
Required: No

 ** upstreamRepositoryPrefix **   <a name="ECR-Type-PullThroughCacheRule-upstreamRepositoryPrefix"></a>
The upstream repository prefix associated with the pull through cache rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: No

## See Also
<a name="API_PullThroughCacheRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/PullThroughCacheRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/PullThroughCacheRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/PullThroughCacheRule)
