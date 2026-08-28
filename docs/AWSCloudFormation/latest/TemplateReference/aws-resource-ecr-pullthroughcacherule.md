---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecr-pullthroughcacherule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::PullThroughCacheRule
<a name="aws-resource-ecr-pullthroughcacherule"></a>

The `AWS::ECR::PullThroughCacheRule` resource creates or updates a pull through cache rule. A pull through cache rule provides a way to cache images from an upstream registry in your Amazon ECR private registry.

## Syntax
<a name="aws-resource-ecr-pullthroughcacherule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecr-pullthroughcacherule-syntax.json"></a>

```
{
  "Type" : "AWS::ECR::PullThroughCacheRule",
  "Properties" : {
      "[CredentialArn](#cfn-ecr-pullthroughcacherule-credentialarn)" : {{String}},
      "[CustomRoleArn](#cfn-ecr-pullthroughcacherule-customrolearn)" : {{String}},
      "[EcrRepositoryPrefix](#cfn-ecr-pullthroughcacherule-ecrrepositoryprefix)" : {{String}},
      "[UpstreamRegistry](#cfn-ecr-pullthroughcacherule-upstreamregistry)" : {{String}},
      "[UpstreamRegistryUrl](#cfn-ecr-pullthroughcacherule-upstreamregistryurl)" : {{String}},
      "[UpstreamRepositoryPrefix](#cfn-ecr-pullthroughcacherule-upstreamrepositoryprefix)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ecr-pullthroughcacherule-syntax.yaml"></a>

```
Type: AWS::ECR::PullThroughCacheRule
Properties:
  [CredentialArn](#cfn-ecr-pullthroughcacherule-credentialarn): {{String}}
  [CustomRoleArn](#cfn-ecr-pullthroughcacherule-customrolearn): {{String}}
  [EcrRepositoryPrefix](#cfn-ecr-pullthroughcacherule-ecrrepositoryprefix): {{String}}
  [UpstreamRegistry](#cfn-ecr-pullthroughcacherule-upstreamregistry): {{String}}
  [UpstreamRegistryUrl](#cfn-ecr-pullthroughcacherule-upstreamregistryurl): {{String}}
  [UpstreamRepositoryPrefix](#cfn-ecr-pullthroughcacherule-upstreamrepositoryprefix): {{String}}
```

## Properties
<a name="aws-resource-ecr-pullthroughcacherule-properties"></a>

`CredentialArn`  <a name="cfn-ecr-pullthroughcacherule-credentialarn"></a>
The ARN of the Secrets Manager secret associated with the pull through cache rule.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-zA-Z-]+:secretsmanager:[a-zA-Z0-9-:]+:secret:ecr\-pullthroughcache\/[a-zA-Z0-9\/_+=.@-]+$`
*Minimum*: `50`
*Maximum*: `612`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomRoleArn`  <a name="cfn-ecr-pullthroughcacherule-customrolearn"></a>
The ARN of the IAM role associated with the pull through cache rule.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EcrRepositoryPrefix`  <a name="cfn-ecr-pullthroughcacherule-ecrrepositoryprefix"></a>
The Amazon ECR repository prefix associated with the pull through cache rule.
*Required*: No
*Type*: String
*Pattern*: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
*Minimum*: `2`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UpstreamRegistry`  <a name="cfn-ecr-pullthroughcacherule-upstreamregistry"></a>
The name of the upstream source registry associated with the pull through cache rule.
*Required*: No
*Type*: String
*Allowed values*: `ecr | ecr-public | quay | k8s | docker-hub | github-container-registry | azure-container-registry | gitlab-container-registry | chainguard`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UpstreamRegistryUrl`  <a name="cfn-ecr-pullthroughcacherule-upstreamregistryurl"></a>
The upstream registry URL associated with the pull through cache rule.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UpstreamRepositoryPrefix`  <a name="cfn-ecr-pullthroughcacherule-upstreamrepositoryprefix"></a>
The upstream repository prefix associated with the pull through cache rule.
*Required*: No
*Type*: String
*Pattern*: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
*Minimum*: `2`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-resource-ecr-pullthroughcacherule--examples"></a>

The following resource examples show how to create a pull through cache rule for a private registry.

**Topics**
+ [Create a pull through cache rule for an upstream registry that requires authentication](#aws-resource-ecr-pullthroughcacherule--examples--Create_a_pull_through_cache_rule_for_an_upstream_registry_that_requires_authentication)
+ [Create a pull through cache rule for an upstream registry that does not require authentication](#aws-resource-ecr-pullthroughcacherule--examples--Create_a_pull_through_cache_rule_for_an_upstream_registry_that_does_not_require_authentication)

### Create a pull through cache rule for an upstream registry that requires authentication
<a name="aws-resource-ecr-pullthroughcacherule--examples--Create_a_pull_through_cache_rule_for_an_upstream_registry_that_requires_authentication"></a>

The following example creates a pull through cache rule for the upstream registry Docker Hub, which requires authentication. The authentication credentials for the upstream registry must be stored in a Secrets Manager secret with a secret name with a `ecr-pullthroughcache/` prefix. You specify the full Amazon Resource Name (ARN) of the secret. When the pull through cache rule is used to pull images from the upstream registry, Amazon ECR will create repositories in your private registry on your behalf with the `docker-hub` prefix.

#### JSON
<a name="aws-resource-ecr-pullthroughcacherule--examples--Create_a_pull_through_cache_rule_for_an_upstream_registry_that_requires_authentication--json"></a>

```
{
    "Resources": {
        "MyECRPullThroughCacheRule": {
            "Type": "AWS::ECR::PullThroughCacheRule",
            "Properties": {
                "EcrRepositoryPrefix": "docker-hub",
                "UpstreamRegistryUrl": "registry-1.docker.io",
                "CredentialArn": "arn:aws:secretsmanager:us-east-2:111122223333:secret:ecr-pullthroughcache/example1234"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ecr-pullthroughcacherule--examples--Create_a_pull_through_cache_rule_for_an_upstream_registry_that_requires_authentication--yaml"></a>

```
Resources:
  MyECRPullThroughCacheRule:
    Type: 'AWS::ECR::PullThroughCacheRule'
    Properties:
      EcrRepositoryPrefix: 'docker-hub'
      UpstreamRegistryUrl: 'registry-1.docker.io'
      CredentialArn: 'arn:aws:secretsmanager:us-east-2:111122223333:secret:ecr-pullthroughcache/example1234'
      UpstreamRegistry: 'docker-hub'
```

### Create a pull through cache rule for an upstream registry that does not require authentication
<a name="aws-resource-ecr-pullthroughcacherule--examples--Create_a_pull_through_cache_rule_for_an_upstream_registry_that_does_not_require_authentication"></a>

The following example creates a pull through cache rule that caches repositories with the name prefix `ecr-public` from the Amazon ECR Public registry into your private registry.

#### JSON
<a name="aws-resource-ecr-pullthroughcacherule--examples--Create_a_pull_through_cache_rule_for_an_upstream_registry_that_does_not_require_authentication--json"></a>

```
{
    "Resources": {
        "MyECRPullThroughCacheRule": {
            "Type": "AWS::ECR::PullThroughCacheRule",
            "Properties": {
                "EcrRepositoryPrefix": "ecr-public",
                "UpstreamRegistryUrl": "public.ecr.aws"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ecr-pullthroughcacherule--examples--Create_a_pull_through_cache_rule_for_an_upstream_registry_that_does_not_require_authentication--yaml"></a>

```
Resources:
  MyECRPullThroughCacheRule:
    Type: 'AWS::ECR::PullThroughCacheRule'
    Properties:
      EcrRepositoryPrefix: 'ecr-public'
      UpstreamRegistryUrl: 'public.ecr.aws'
      UpstreamRegistry: 'ecr-public'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
