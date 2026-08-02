---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Secret.html
---

# Secret
<a name="API_Secret"></a>

An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
+ To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
+ To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_Secret_Contents"></a>

 ** name **   <a name="ECS-Type-Secret-name"></a>
The name of the secret.
Type: String
Required: Yes

 ** valueFrom **   <a name="ECS-Type-Secret-valueFrom"></a>
The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the SSM Parameter Store.
For information about the require AWS Identity and Access Management permissions, see [Required IAM permissions for Amazon ECS secrets](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-secrets.html#secrets-iam) (for Secrets Manager) or [Required IAM permissions for Amazon ECS secrets](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-parameters.html) (for Systems Manager Parameter store) in the *Amazon Elastic Container Service Developer Guide*.
If the SSM Parameter Store parameter exists in the same Region as the task you're launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
Type: String
Required: Yes

## See Also
<a name="API_Secret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Secret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Secret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Secret)
