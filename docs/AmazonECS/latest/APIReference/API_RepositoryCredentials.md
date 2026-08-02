---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RepositoryCredentials.html
---

# RepositoryCredentials
<a name="API_RepositoryCredentials"></a>

The repository credentials for private registry authentication.

## Contents
<a name="API_RepositoryCredentials_Contents"></a>

 ** credentialsParameter **   <a name="ECS-Type-RepositoryCredentials-credentialsParameter"></a>
The Amazon Resource Name (ARN) of the secret containing the private repository credentials.
When you use the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same Region as the task that you're launching then you can use either the full ARN or the name of the secret. When you use the AWS Management Console, you must specify the full ARN of the secret.
Type: String
Required: Yes

## See Also
<a name="API_RepositoryCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/RepositoryCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/RepositoryCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/RepositoryCredentials)
