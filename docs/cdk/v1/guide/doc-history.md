---
source_url: https://docs.aws.amazon.com/cdk/v1/guide/doc-history.html
---

This is the AWS CDK v1 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and will now only receive critical bug fixes and security patches. New features will be developed for CDK v2 exclusively. Support for CDK v1 will end entirely on June 1, 2023. [Migrate to CDK v2](work-with-cdk-v2.md) to have access to the latest features and fixes.

# AWS CDK Developer Guide history

See [Releases](https://github.com/awslabs/aws-cdk/releases) for information about AWS CDK releases. The AWS CDK is updated approximately once a week. Maintenance versions may be released between weekly releases to address critical issues. Each release includes a matched AWS CDK Toolkit (CDK CLI), AWS Construct Library, and API Reference. Updates to this Guide generally do not synchronize with AWS CDK releases.

**Note**
The table below represents significant documentation milestones. We fix errors and improve content on an ongoing basis.

| Change | Description | Date |
| --- |--- |--- |
| [Document `cdk.json`](doc-history.md) | Add documentation of `cdk.json` configuration values. | April 20, 2022 |
| [Dependency management](doc-history.md) | Add topic on managing dependencies with the AWS CDK. | April 7, 2022 |
| [Remove double-braces from Java examples](doc-history.md) | Replace this anti-pattern with Java 9 `Map.of` throughout. | March 9, 2022 |
| [AWS CDK v2 release](doc-history.md) | Improvements to CDK v1 Developer Guide to coincide with the release of CDK v2 and its documentation. | December 4, 2021 |
| [`cdk watch`](doc-history.md) | Add description of `cdk watch` command for incremental deployments. | November 19, 2021 |
| [Testing with `assertions`](doc-history.md) | Revise testing topic to use new `assertions` library. | November 17, 2021 |
| [Experimental modules](doc-history.md) | Explain how experimental modules work with CDK v2. | October 28, 2021 |
| [Faster local development](doc-history.md) | Add information on `--no-rollback` and `--hotswap` options for accelerated local development. | October 7, 2021 |
| [Add local tooling information](doc-history.md) | Update TypeScript and JavaScript topics with information on using locally-installed tools (`cdk`, `tsc`). | September 28, 2021 |
| [Update CDK Pipelines API](doc-history.md) | Update CDK Pipelines topic to use new API. | August 24, 2021 |
| [CloudFormation Public Registry](doc-history.md) | Add topic about using resource definitions from the CloudFormation Public Registry with the AWS CDK. | June 24, 2021 |
| [Best Practices topic](doc-history.md) | Add topic about best practices for developing CDK apps. | June 10, 2021 |
| [Go developer preview](doc-history.md) | Add information about Go language support (in developer preview) including a "Working with the CDK in Go" topic. | April 19, 2021 |
| [Import or migrate CloudFormation template](doc-history.md) | Add description of the new `cloudformation-include.CfnInclude` class, a powerful way to import and migrate CloudFormation templates, or to vend them as AWS CDK constructs. | October 15, 2020 |
| [Add construct tree section](doc-history.md) | Information about the construct tree and its relation to the constructs you define in your AWS CDK app. | October 5, 2020 |
| [Add Bootstrapping topic](doc-history.md) | A complete explanation of why and how to bootstrap AWS environments for the CDK, including a comprehensive discussion of how to customize the process. | September 8, 2020 |
| [Add CDK Pipelines how-to](doc-history.md) | CDK Pipelines let you easily automate the deployment of your AWS CDK apps from source control whenever they're updated.  | July 17, 2020 |
| [Improve CDK Toolkit topic](doc-history.md) | Include more information and examples around performing common tasks with the CLI (and the relevant flags) rather than just including a copy of the help. | July 9, 2020 |
| [Improve CodePipeline example](doc-history.md) | Update pipeline stack to build in proper language and add more material dealing with the CodeCommit repository. | July 6, 2020 |
| [Improve Getting Started](doc-history.md) | Remove extraneous material from Getting Started, use a more conversational tone, incorporate current best practices. Break out Hello World into its own topic. | June 17, 2020 |
| [Update stability index](doc-history.md) | Incorporate the latest definitions of the stability levels for AWS Construct Library modules. | June 11, 2020 |
| [CDK Toolkit versioning](doc-history.md) | Add information about cloud assembly versioning and compatibility of the CDK Toolkit (CLI) with the AWS Construct Library | April 22, 2020 |
| [Translating from TypeScript](doc-history.md) | Updated "CDK in Other Languages" topic to also include JavaScript, Java, and C\# and renamed it "Translating from TypeScript." | April 10, 2020 |
| [Parameters topic](doc-history.md) | Add Concepts topic on using parameters with the AWS CDK. | April 8, 2020 |
| [JavaScript code snippets](doc-history.md) | Reinstate JavaScript code snippets throughout (automated translation via Babel). | April 3, 2020 |
| [Working with the CDK](doc-history.md) | Add "Working with the CDK" articles for the five supported languages. Various other improvements and fixes. | February 4, 2020 |
| [Java code snippets](doc-history.md) | Add Java code snippets throughout. Designate Java and C\# bindings stable. | November 25, 2019 |
| [C\# code snippets](doc-history.md) | Add C\# code snippets throughout. | November 19, 2019 |
| [Python code snippets](doc-history.md) | Add Python code snippets throughout. Add Troubleshooting and Testing topics. | November 14, 2019 |
| [Troubleshooting topic](doc-history.md) | Add Troubleshooting topic to AWS CDK Developer Guide. | October 30, 2019 |
| [Improve Environments topic](doc-history.md) | Add Troubleshooting topic to AWS CDK Developer Guide. | October 10, 2019 |
| [ECS Patterns improvements](doc-history.md) | Updates to reflect improvements to ECS Patterns module. | September 17, 2019 |
| [New tagging API](doc-history.md) | Update tagging topic to use new API. | August 13, 2019 |
| [General availability](doc-history.md) | The AWS CDK Developer Guide is released. | July 11, 2019 |
