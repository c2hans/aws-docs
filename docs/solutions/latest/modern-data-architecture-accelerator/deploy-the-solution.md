---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

The solution is mainly deployed as an AWS CDK application. Customers can also use a CloudFormation template to deploy the solution based on some sample configurations.

Before you deploy, review the [cost](cost.md), [architecture](architecture-overview.md), and other considerations discussed earlier in this guide.

**Tip**
New to MDAA? We recommend starting with the [MDAA Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/6e7289c7-5662-494d-8b56-b8706412c3a6/en-US) for a guided, hands-on introduction.

## Terminology
<a name="terminology"></a>
+  **Deployment Account** - The AWS account where deployment activities will be occurring. This includes source control for MDAA, MDAA artifact building and publishing, and MDAA execution.
+  **Target Account** - The AWS account where Data Analytics Environment resources will ultimately be deployed by MDAA. Note that MDAA can execute in one account and deploy to another, or can execute and deploy to the same account.

## Prerequisites for CDK Deployment
<a name="prerequisites-for-cdk-deployment"></a>

### Manual Bootstrap (Single Deployment Source/Target Account)
<a name="manual-bootstrap-single-deployment-sourcetarget-account"></a>

1. Obtain AWS credentials for the account and place them into your credentials file or populate appropriate environment variables. These credentials should have sufficient permissions to create the following resources in the target account: \* IAM Roles \* SSM Parameters \* S3 Buckets

1. Run the CDK bootstrap command. Multiple regions can be specified simultaneously:

```
export CDK_NEW_BOOTSTRAP=1
cdk bootstrap aws://<AWS Account Number>/<Target Region>...
```

For example:

```
export CDK_NEW_BOOTSTRAP=1
cdk bootstrap aws://123456789012/ca-central-1 aws://123456789012/us-east-1
```

### Manual Bootstrap (Single Deployment Source Account and One or More Target Accounts)
<a name="manual-bootstrap-single-deployment-source-account-and-one-or-more-target-accounts"></a>

This procedure should be executed for each target account. This procedure bootstraps the target account while establishing trust with the source account (where deployments will be triggered)

Obtain AWS credentials for the target account and place them into your credentials file or populate appropriate environment variables.

These credentials should have sufficient permissions to create the following resources in the target account: \* IAM Roles \* SSM Parameters \* S3 Buckets

Run the CDK bootstrap command. Multiple regions can be specified simultaneously:

```
export CDK_NEW_BOOTSTRAP=1
cdk bootstrap --cloudformation-execution-policies <CDK Deployment IAM Policy Arns> --trust <Source Account Number> aws://<Target AWS Account Number>/<Target Region>...
```

Note that the permissions specified with cloudformation-execution-policies are granted to CloudFormation during deployment into the account. These permissions should be sufficient to deploy MDAA resources, but not overly permissive.

## Deployment
<a name="deployment"></a>

### Deployment Overview
<a name="deployment-overview"></a>

The following are procedures which can be executed in order to manually deploy MDAA to target accounts. These procedures assume that the appropriate preparations have been made within the organizations accounts.

### Deployment Patterns
<a name="deployment-patterns"></a>

MDAA may be deployed using a number of patterns:
+ Same Deployment Source and Target Account (Centralized Data Environment)
+ Single Deployment Source account, One or More Separate Target Accounts (Centralized deployment governance, decentralized Data Environments)

### Deployment Preparation
<a name="deployment-preparation"></a>

#### Node Installation
<a name="node-installation"></a>

Install a version of Node.js using a method appropriate to your system. MDAA requires nodejs 22.x and npm/npx version 10.x or greater.

As of MDAA 1.8.0, the CLI is cross-platform: the shell commands it generates internally are emitted in the correct syntax for both POSIX shells and Windows `cmd.exe`, so the CLI runs on Windows as well as macOS and Linux. Note that the example commands shown throughout this guide (for example the chained `git clone …​ && cd …​` steps) use POSIX shell syntax; adapt them to your shell when running on Windows.

#### Environment Setup
<a name="environment-setup"></a>

Verify your credentials are populated either in your environment or in your \~/.aws/credentials file. Also, verify your AWS region is specified either in your environment or in your \~/.aws/config file:

```
[default]
region=ca-central-1
```

#### Deployment from Locally Cloned Source Code
<a name="deployment-from-locally-cloned-source-code"></a>

As of MDAA 0.40, deployment from locally cloned MDAA source code is the preferred deployment mode, as it avoids requiring MDAA NPM packages to be published. As of 0.43, specification of the '-l' flag is no longer required to force local execution mode. Modules which are available in locally cloned MDAA source code will be used. Otherwise, the required packages will be installed via NPM.

1. Clone MDAA repo.

1. Run `<path_to_cloned_repo>/bin/mdaa -c <path_to_mdaa_yaml> <cdk action>`
   + MDAA will run npm install at the root of the cloned repo to install CDK and all necessary third-party dependencies.
   + MDAA will locate its own modules within the local source code repo Note that specifying specific MDAA versions in local\_mode will result in NPM packages being installed

Additional MDAA CLI commands:

Use the -h parameter to print a list of all MDAA CLI parameters

```
<path_to_cloned_repo>/bin/mdaa -h
```

Use the -c parameter to specify a config config file. Otherwise MDAA CLI will attempt to use mdaa.yaml from the local directory.

```
<path_to_cloned_repo>/bin/mdaa -c <optional-path-to-mdaa-config-file> <cdk action>
```

Specify a < cdk action >, which MDAA CLI will run against every configured module/CDK app:

```
<path_to_cloned_repo>/bin/mdaa <cdk action>
```

To list (Terraform validate) all stacks:

```
<path_to_cloned_repo>/bin/mdaa list
```

To synth (Terraform validate) all stacks:

```
<path_to_cloned_repo>/bin/mdaa synth
```

To diff (Terraform plan) all stacks:

```
<path_to_cloned_repo>/bin/mdaa diff
```

To deploy (Terraform deploy) all stacks:

```
<path_to_cloned_repo>/bin/mdaa deploy
```

To deploy only env=dev modules/stacks:

```
<path_to_cloned_repo>/bin/mdaa deploy -e dev
```

To deploy only domain1 and domain2 modules/stacks:

```
<path_to_cloned_repo>/bin/mdaa deploy -d domain1,domain2
```

To deploy only the test\_roles\_module and test\_datalake\_module modules/stacks:

```
<path_to_cloned_repo>/bin/mdaa deploy -m test_roles_module,test_datalake_module
```

Any CLI params not recognized by MDAA CLI will be pushed down to the CDK/Terraform CLI. In this example, --no-rollback will be pushed down to CDK:

```
<path_to_cloned_repo>/bin/mdaa deploy --no-rollback
```

#### Deployment from Published NPM Packages
<a name="deployment-from-published-npm-packages"></a>

MDAA can be installed from a private NPM package repo, and will also attempt to install MDAA modules from a private NPM repo. This is necessary if specific MDAA versions are specified in mdaa.yaml.

Verify that your private NPM repo is accessible and contains the appropriate MDAA NPM artifacts. If using a localhost based NPM repo (such as Verdaccio), verify it is running on localhost and updated with the latest MDAA packages from S3 (See [PREDEPLOYMENT](https://github.com/aws/modern-data-architecture-accelerator/blob/main/PREDEPLOYMENT.md)). When executed from its NPM package, MDAA will also attempt to NPM install each MDAA module from NPM repo.

Install MDAA from your private NPM repository using:

Global Installation:

```
npm install -g @aws-mdaa/cli
```

Then, MDAA can be executed globally:

```
mdaa -h
```

Optionally, both the MDAA CLI can be instead npm installed in a local directory:

```
npm install @aws-mdaa/cli
```

MDAA commands can then be run within the local directory using NPX.

```
npx mdaa -h
```

#### Deployment of MDAA Modules/CDK Apps using CDK CLI
<a name="deployment-of-mdaa-modulescdk-apps-using-cdk-cli"></a>

MDAA Modules are developed as independant CDK apps which can be directly executed using the CDK CLI. This is generally useful for development and troubleshooting directly against the MDAA codebase, but is not recommended for normal use.

To execute MDAA Modules/CDK apps using the CDK CLI:

1. Clone the MDAA source repo.

1. At the root of the repo, run npm install to install all packages required across all modules.

1. Change directory to the MDAA Modules/CDK apps source code directory (typically under packages/apps/< module category >/< module >)

1. Run the following CDK commands with the required context:

```
cdk synth -c org=<organization> -c env=<dev|test|prod> -c domain=<domain name> -c module_configs=<app_config_paths> -c tag_configs=<tag_config_paths> -c module_name=<module_name>
```

```
cdk synth -c org="sample-org" -c env="dev" -c domain="mdaa1" -c module_configs="warehouse.yaml" -c tag_configs="tags.yaml"  -c module_name="testing"
```

#### Required Context
<a name="required-context"></a>

The following context values are required for all modules. Note that additional context values may be required if context is referenced from within the module/app config.
+  **org** - Name of the organization
+  **env** - Name of the target environment (ie. dev/test/prod)
+  **domain** - Name of the deployment domain (allows multiple deployments in same org/env/account)
+  **module\_name** - Name of the MDAA module (allows multiple deployments of the same CDK app within same org/domain/env)
+  **module\_configs** - Comma separated list of paths to one or more app config files. Multiple config files will be merged, with later-listed config files taking precedence over earlier-listed config files.
+  **tag\_configs** - Comma separated list of paths to one or more tag config files. Multiple config files will be merged, with later-listed config files taking precedence over earlier-listed config files.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
