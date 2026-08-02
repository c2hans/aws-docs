---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/sample-configs.html
---

# Sample configurations
<a name="sample-configs"></a>

Modern Data Architecture Accelerator (MDAA) on AWS includes example sample configurations that allow you to quickly deploy analytics workloads and data platforms across your organisation. The repository includes sample configurations and detailed documentation that provide guidance for implementing various modules including analytics platform, ML workloads and data architectures across different AWS Regions.

MDAA is designed to deploy data environments across multiple domains and environments. Each domain/environment is constituted by one or more configured MDAA modules. Each MDAA module references a CDK app and corresponding configuration. During deployment, MDAA executes a module’s underlying CDK application, providing all necessary configuration details as CDK context.

We built these sample configurations based on AWS best practices and common analytics use cases across industries. This solution provides automated deployment of analytics infrastructure while maintaining flexibility to customise based on your specific data requirements, security needs, and compliance standards

These sample MDAA configurations (starter kits) are provided as a starting point for common data platform architectures. They live under the `starter_kits/` directory of the MDAA repository.
+  [Minimal](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/minimal) - Foundational governance layer (IAM roles, Glue Catalog encryption, Lake Formation settings) for building custom architectures
+  [Basic Data Lake](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/basic_datalake) - Secure S3 data lake with Glue Data Catalog, Athena, and CloudTrail audit
+  [AI/ML Platform (Basic Data Science)](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/basic_datascience_platform) - Team-based SageMaker Studio platform with an integrated data lake
+  [Lakehouse Analytics](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/lakehouse_analytics) - End-to-end lakehouse spanning S3 storage, Glue ETL, data quality, Athena, Redshift, and QuickSight
+  [DataZone Governed Lakehouse](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/datazone_governed_lakehouse) - Enterprise lakehouse with fine-grained governance via DataZone and Lake Formation
+  [SMUS Research Environment](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/smus_research_environment) - Multi-team research environment on SageMaker Unified Studio in a single account
+  [SMUS Data Mesh](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/smus_data_mesh) - Multi-account SageMaker Unified Studio deployment with cross-account data sharing and custom blueprints
+  [MLOps Platform](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/mlops_platform) - End-to-end ML lifecycle: training, deployment, and monitoring with CI/CD
+  [GenAI Foundation](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/genai_foundation) - Bedrock-based customer support agent with RAG, knowledge bases, and guardrails
+  [GAIA Chatbot](https://github.com/aws/modern-data-architecture-accelerator/tree/main/starter_kits/genai_gaia_chatbot) - Production-ready GenAI chatbot backend with Cognito auth, AppSync streaming, and CloudFront

Additional customization of the baselines will likely be required to align with your organization’s specific analytics needs and compliance requirements. Example configurations are also available in the external [sample configurations repository](https://github.com/aws-samples/sample-config-modern-data-architecture-accelerator).

## MDAA Configuration Structure
<a name="config-structure"></a>

MDAA is designed to deploy data environments across multiple domains and environments. Each domain/environment is constituted by one or more configured MDAA modules. Each MDAA module references a CDK app and corresponding configuration. During deployment, MDAA executes a module’s underlying CDK application, providing all necessary configuration details as CDK context.
+ Domain - A data environment can be organized into one or more domains, which may align to organizational units such as line of business, directorate, etc. Domains may be spread across one or more accounts. When spread across multiple accounts, each domain becomes a potential node in a data mesh architecture.
+ Environment - An domain can be deployed across multiple environments (such as DEV/TEST/PROD). Each environment may deployed in a separate account.
+ Module - A module specifies which CDK App and corresponding configuration will be deployed within an data environment domain/environment. During deployment, modules will be deployed in stages according to dependencies between modules.
+ CDK App - A CDK App is built, executed, and deployed using the AWS CDK framework. The CDK app will be forked from the MDAA orchestrator and executed as a regular CDK application. Each CDK produces one or more CloudFormation stacks, which in turn deploy the cloud resources which will constitute the data environment. Alternatively, instead of deploying resources directly to the environment, they can instead be published as Service Catalog products, to be deployed on a self-service basis by users within the accounts.

MDAA Config File/Folder Layouts MDAA is configured using a set of YAML configuration files. The main CLI configuration file (typically 'mdaa.yaml') specifies the global, domain, environment, and modules to be deployed. Module (CDK App) configurations are specified in separate YAML files, or can be configured inline in the CLI config itself. Module (CDK App) configurations are documented in detail in their respective READMEs. Terraform modules are configured directly using HCL configurations next to mdaa.yaml. MDAA configuration layouts are very flexible. Configurations for an entire org can be concentrated into a single MDAA config file, or can be spread out across multiple config files by domain, line of business, environment, etc.

 **Single Domain, Shared CDK Apps Configs Across Envs**

In this scenario, a MDAA config contains a single domain, with CDK App configs shared across dev/test/prod. In this case, the shared configs likely make heavy use of SSM parameters to achieve portability across environments.

 **Single Domain, Separate CDK Apps Configs Across Envs**

In this scenario, a MDAA config contains a single domain, with separate CDK App configs across dev/test/prod.

 **Multiple domains, single MDAA config**

In this scenario, multiple domains are in the same MDAA Config/

 **Multiple domains, Multiple MDAA config**

In this scenario, each domain is in its own MDAA config.

## Module Configurations
<a name="mod-config"></a>

Each MDAA Module/CDK App has its own configuration schema, which is documented in their respective READMEs. There are some common configuration behaviours and capabilities, however, which can be used across all MDAA Module configs.

 **Dynamic References**

MDAA allows use of Dynamic References in configuration files. These build on the concept of CloudFormation Dynamic References.

```
# Example Config File w/Dynamic References

# Will be passed through to CloudFormation as a CFN Dynamic Reference and will be resolved at deployment time
vpcId: "{{resolve:ssm:/path/to/ssm/param}}"
sensitive_value: "{{resolve:ssm-secure:parameter-name:version}}"
db_username: "{{resolve:secretsmanager:MyRDSSecret:SecretString:username}}",
db_password: "{{resolve:secretsmanager:MyRDSSecret:SecretString:password}}"

# Will be resolved at synth time to the CDK context value passed from the MDAA CLI config or directly in CDK context
subnetId: "{{context:some_context_key}}"

# Will be resolved at synth time to environment variable values
subnetId: "{{env_var:some_env_variable_name}}"

# Will be resolved at synth time to the values passed for org/domain/env/account/region from the MDAA CLI config via CDK context
# Identical to org: "{{context:org}}"
org: "{{org}}"
domain: "{{domain}}"
env: "{{env}}"
module_name: "{{module_name}}"
partition: "{{partition}}"
account: "{{account}}"
region: "{{region}}"

# Dynamic references can also be embedded inline in config values:
key_arn: arn:{{partition}}:kms:{{region}}:{{account}}:key/{{context:key_id}}
```

 **Configuration Sharing Across Domains, Envs, Modules**

MDAA modules may share identical config files across multiple domains, envs, and modules. Because MDAA automatically injects the domain/env/module names into resource naming, each resulting deployment will result in uniquely named resources but with otherwise identical behaviours.

```
# Example MDAA Config With Shared Configs
domains:
  domain1:
    environments:
      dev:
        modules:
          test_datalake:
            module_path: "@aws-mdaa/datalake"
            module_configs:
              - ./shared/datalake.yaml
  domain2:
    environments:
      dev:
        modules:
          test_datalake:
            module_path: "@aws-mdaa/datalake"
            module_configs:
              - ./shared/datalake.yaml
```

Both datalakes will have identical configurations, but named according to their domain.

 **Configuration Composition**

Each MDAA module accepts one or more configuration files, which are merged into an effective config, which is then validated and parsed by the app. This allows for configs to be composed of common base configs shared across multiple modules, environments, or domains, with only the differentiating config values to be applied on top. In general, config files will be merged according to the following rules:
+ Lists on same config key will be merged across config files
+ Objects on same config key will be concatenated
+ Scalar values will be overridden, with config files higher on list taking precedence

```
# Example MDAA CLI Module Specification With Multiple Configs
domains:
  domain1:
    environments:
      dev:
        modules:
          roles1:
            module_path: "@aws-mdaa/roles"
            module_configs:
              - ./domain1/roles1.yaml
              - ./shared/roles_base.yaml
  domain2:
    environments:
      dev:
        modules:
          roles2:
            module_path: "@aws-mdaa/roles"
            module_configs:
              - ./domain2/roles2.yaml
              - ./shared/roles_base.yaml
```
