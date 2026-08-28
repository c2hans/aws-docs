---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/configuration-management.html
---

# Configuration management
<a name="configuration-management"></a>

 In a microservices architecture, each service interacts with various resources like databases, queues, and other services. A consistent way to configure each service's connections and operating environment is vital. Ideally, an application should adapt to new configurations without needing a restart. This approach is part of the Twelve-Factor App principles, which recommend storing configurations in environment variables.

 A different approach is to use [AWS App Config](https://aws.amazon.com/systems-manager/features/appconfig/). It’s a feature of AWS Systems Manager which makes it easy for customers to quickly and safely configure, validate, and deploy feature flags and application configuration. Your feature flag and configurations data can be validated syntactically or semantically in the pre-deployment phase, and can be monitored and automatically rolled back if an alarm that you have configured is triggered. AppConfig can be integrated with Amazon ECS and Amazon EKS by using the AWS AppConfig agent. The agent functions as a sidecar container running alongside your Amazon ECS and Amazon EKS container applications. If you use AWS AppConfig feature flags or other dynamic configuration data in a Lambda function, then we recommend that you add the AWS AppConfig Lambda extension as a layer to your Lambda function.

 [GitOps](https://github.com/weaveworks/weave-gitops) is an innovative approach to configuration management that uses Git as the source of truth for all configuration changes. This means that any changes made to your configuration files are automatically tracked, versioned, and audited through Git.

## Secrets management
<a name="secrets-management"></a>

 Security is paramount, so credentials should not be passed in plain text. AWS offers secure services for this, like AWS Systems Manager Parameter Store and AWS Secrets Manager. These tools can send secrets to containers in Amazon EKS as volumes, or to Amazon ECS as environment variables. In AWS Lambda, environment variables are made available to your code automatically. For Kubernetes workflows, the [External Secrets Operator](https://external-secrets.io/v0.8.5/) fetches secrets directly from services like AWS Secrets Manager, creating corresponding Kubernetes Secrets. This enables a seamless integration with Kubernetes-native configurations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
