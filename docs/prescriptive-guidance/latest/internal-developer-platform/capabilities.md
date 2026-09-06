---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/capabilities.html
---

# Capabilities of an internal developer platform
<a name="capabilities"></a>

The internal developer platform should provide the following capabilities.

|
|
| Capability | Recommended service or tool |
| --- |--- |
| Templating to ensure the delivery of a packaged and functional set of tools | [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html), [GitHub](https://github.com/) or [GitLab](https://about.gitlab.com/) |
| Code repository for collaboration between developers and storage of golden path templates | [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), or [Bitbucket Cloud](https://www.atlassian.com/software/bitbucket) |
| Configuration repository as a canonical data store for application configuration | [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) or [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) |
| Artifact registries that preserve a signed, accessible, and traceable list of packaged components | [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) or [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html) |
| Secret management to provide secure long-term storage for sensitive data | [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) |
| Cryptographic signing and validation of artifacts to allow for verification of the consistency and integrity of the data they contain | [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) |
| Developer portal as a software catalog of all components, systems, and domains | [Backstage](https://backstage.io/docs/overview/what-is-backstage) |
| Identity and access management to authenticate and authorize in a well-defined manner | [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) or [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) |
| Infrastructure as code (IaC) tool to set up infrastructure resources for the application | [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) |
| Continuous delivery for both infrastructure and application deployment | [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) |
| Workflow orchestration to prepare resources for delivery | [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html), [GitHub](https://github.com/) or [GitLab](https://about.gitlab.com/) |
| Service discovery for dynamic lookup of service details | [AWS Cloud Map](https://docs.aws.amazon.com/cloud-map/latest/dg/what-is-cloud-map.html) or [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) |
| Observability that provides workload monitoring, logging, tracing, and alerting | [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html), [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html), or [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) |
| Compute platform that hosts the platform capabilities and its integration points | [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) |

Although this is not a comprehensive list of all the capabilities that the internal developer platform can provide, these are the essential capabilities to support the developer experience from development to production. These capabilities can be automated by creating a golden path that the developers use. For more information about these capabilities, see [Technology Capabilities](https://cnoe.io/docs/capabilities) on the Cloud Native Operational Excellence (CNOE) website.

As mentioned previously, golden paths for infrastructure and workload deployment should be aligned with your organization's security standards. The following table describes the security capabilities that golden paths should provide.

|
|
| Golden path type | Security capability | Recommended tool |
| --- |--- |--- |
| Infrastructure deployment | Linting | [cfn-lint](https://github.com/aws-cloudformation/cfn-lint) |
| Infrastructure deployment | Security checks | [cfn-nag](https://github.com/stelligent/cfn_nag) or [cdk-nag](https://github.com/cdklabs/cdk-nag) |
| Infrastructure deployment | Policy checks | [AWS CloudFormation Guard](https://github.com/aws-cloudformation/cloudformation-guard) |
| Workload deployment | Software composition analysis (SCA) and static application security testing (SAST) | [Anchore](https://anchore.com/opensource/) or [Snyk Open Source](https://snyk.io/product/open-source-security-management/) |
| Workload deployment | Artifact registries | [Continuous image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) in Amazon ECR |
| Workload deployment | Secrets scanning | [git-secrets](https://github.com/awslabs/git-secrets) |
| Workload deployment | Dynamic application security testing (DAST) | [Zed Attack Proxy (ZAP)](https://www.zaproxy.org/) |
| Workload deployment | Runtime application self-protection (RASP) | [Sysdig Falco](https://sysdig.com/opensource/falco/) |
