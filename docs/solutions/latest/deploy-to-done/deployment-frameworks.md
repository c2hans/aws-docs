---
source_url: https://docs.aws.amazon.com/solutions/latest/deploy-to-done/deployment-frameworks.html
---

# Deployment Frameworks
<a name="deployment-frameworks"></a>

Once your application runs on Elastic Beanstalk, integrate deployment into your existing engineering workflows.

## Console Deployment
<a name="console-deployment"></a>

The Elastic Beanstalk console provides a step-by-step visual interface for deployment. Upload a source bundle or container image, then monitor deployment progress showing environment health transitions, instance-level status, and real-time event logging via the Deployments tab. View full deployment history with one-click rollback options for any previous version.

## AWS CLI and SDKs
<a name="aws-cli-and-sdks"></a>

The AWS CLI and AWS SDKs let you script environment creation and deployment from your own tooling. Use `aws elasticbeanstalk create-application`, `create-application-version`, and `create-environment` to provision and deploy applications, including registering pre-built container images from Amazon ECR for multi-service architectures.

## Infrastructure as Code (Terraform)
<a name="infrastructure-as-code-terraform"></a>

For teams managing infrastructure declaratively, the AWS provider for Terraform includes Elastic Beanstalk resources for applications, application versions, and environments, so you can version-control your environment definitions alongside the rest of your infrastructure.

## GitHub Actions
<a name="github-actions"></a>

The [official GitHub Action for Elastic Beanstalk](https://github.com/aws-actions/aws-elastic-beanstalk-deploy) enables push-to-deploy workflows:

1. Application code merges to your main branch

1. GitHub Actions builds and packages the deployment artifact

1. The action uploads to S3 and triggers an Elastic Beanstalk deployment

1. Elastic Beanstalk manages rolling updates automatically, health checks, and automatic rollback

This eliminates custom deployment scripts while keeping your CI/CD pipeline in GitHub.

## Deployment Strategies
<a name="deployment-strategies"></a>

Elastic Beanstalk supports multiple deployment strategies, selectable per environment. The strategies available differ by deployment mode: Standard Mode offers all-at-once, rolling, rolling with additional batch, and immutable; Cluster Mode offers all-at-once, rolling, immutable, and traffic-splitting deployments. Confirm the strategies available for your mode in the deployment strategy documentation linked below.

**Deployment Strategies**

| Strategy | Behavior | Available In | Best For |
| --- | --- | --- | --- |
| All at once | Deploys to all instances simultaneously | Standard, Cluster | Development environments, fast iteration |
| Rolling | Deploys in batches, maintaining capacity | Standard, Cluster | Production with tolerance for brief reduced capacity |
| Rolling with additional batch | Launches new instances before retiring old | Standard | Production where full capacity must be maintained |
| Immutable | Launches entirely new instances, swaps on health | Standard, Cluster | Production where deployment failure cannot impact running instances |
| Traffic splitting | Routes a percentage of traffic to new version | Cluster | When you need to validate a new version with a subset of real production traffic before full rollout |

All strategies include automatic rollback on health check failure. If a deployment causes health degradation, Elastic Beanstalk reverts to the previous version without manual intervention.

## Go Deeper
<a name="deployment-frameworks-go-deeper"></a>

**Go Deeper**
[Deploy to Elastic Beanstalk with GitHub Actions](https://aws.amazon.com/blogs/dotnet/deploy-to-elastic-beanstalk-environment-with-github-actions/) - CI/CD pipeline setup
[AWS Elastic Beanstalk Now Supports GitHub Actions (What's New)](https://aws.amazon.com/about-aws/whats-new/2026/02/aws-elastic-beanstalk-github-action/) - Feature announcement
[Elastic Beanstalk Deployment Strategies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.deploy-existing-version.html) - All-at-once, rolling, immutable, and traffic-splitting deployments
[Elastic Beanstalk Deployments Tab (What's New)](https://aws.amazon.com/about-aws/whats-new/2026/03/elastic-beanstalk-deployments-tab/) - Real-time deployment monitoring
[Deploy Containers by Using Elastic Beanstalk (Prescriptive Guidance)](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containers-by-using-elastic-beanstalk.html) - Docker deployment pattern
