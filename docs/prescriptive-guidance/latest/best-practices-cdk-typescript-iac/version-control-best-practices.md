---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/version-control-best-practices.html
---

# Use release and version control for constructs
<a name="version-control-best-practices"></a>

## Version control for the AWS CDK
<a name="version-control-for-the-9999999999999999cdk-.e875239c-5911-50c7-9b5e-05b22db76def"></a>

AWS CDK common constructs can be created by multiple teams and shared across an organization for consumption. Typically, developers release new features or bug fixes in their common AWS CDK constructs. These constructs are used by AWS CDK applications or any other existing AWS CDK constructs as part of a dependency. For this reason, it's crucial that developers update and release their construct with proper semantic versions independently. Downstream AWS CDK applications or other AWS CDK constructs can update their dependency to use the newly released AWS CDK construct version.

Semantic versioning (Semver) is a set of rules, or method, for providing unique software numbers to computer software. Versions are defined as follows:
+ A MAJOR version consists of incompatible API changes or a breaking change.
+ A MINOR version consists of functionality that's added in a backwards-compatible manner.
+ A PATCH version consists of backwards-compatible bug fixes.

For more information on semantic versioning, see [Semantic Versioning Specification (SemVer)](https://semver.org/) in the Semantic Versioning documentation.

## Repository and packaging for AWS CDK constructs
<a name="repository-and-packaging-for-9999999999999999cdk--constructs.c5358614-8e24-5c53-8a29-9e30ee3fdc1a"></a>

As AWS CDK constructs are developed by different teams and are used by multiple AWS CDK applications, you can use a separate repository for each AWS CDK construct. This also can help you enforce access control. Each repository could contain all the source code related to the same AWS CDK construct along with all of its dependencies. By keeping a single application (that is, an AWS CDK construct) in a single repository, you can decrease the scope of impact of changes during deployment.

The AWS CDK not only generates CloudFormation templates for deploying infrastructure, but it also bundles runtime assets like Lambda functions and Docker images and deploys them alongside your infrastructure. It's not only possible to combine the code that defines your infrastructure and the code that implements your runtime logic into a single construct—it's a best practice. These two kinds of code don't need to live in separate repositories or even in separate packages.

To consume packages across repository boundaries, you must have a private package repository—similar to npm, PyPi, or Maven Central, but internal to your organization. You must also have a release process that builds, tests, and publishes the package to the private package repository. You can create private repositories, such as PyPi server, by using a local virtual machine (VM) or Amazon S3. When you design or create a private package registry, it's crucial to consider the risk of service disruption due to high availability and scalability. A serverless managed service that's hosted in the cloud to store packages can greatly decrease the maintenance overhead. For example, you can use [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/) to host packages for most popular programming languages. You can also use CodeArtifact to set external repository connections and replicate them within CodeArtifact.

Dependencies on packages in the package repository are managed by your language's package manager (for example, npm for TypeScript or JavaScript applications). Your package manager makes sure that builds are repeatable by recording the specific versions of every package your application depends on and then lets you upgrade those dependencies in a controlled manner, as the following diagram shows.

![Dependencies](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/images/guide-img/b7d5d887-7172-4d47-9f1f-1cf7ae181482/images/5a85d0ba-77f0-4553-be4e-711b03e14933.png)

## Construct releasing for the AWS CDK
<a name="construct-releasing-for-the-9999999999999999cdk-.390fdd6d-098a-59bd-805a-98b29b1e7509"></a>

We recommend that you create your own automated pipeline to build and release new AWS CDK construct versions. If you put a proper pull request approval process in place, then once you commit and push your source code into the main branch of the repository, the pipeline can build and create a release candidate version. That version can be pushed to CodeArtifact and tested before releasing the production-ready version. Optionally, you can test your new AWS CDK construct version locally before merging the code with the main branch. This causes the pipeline to release the production-ready version. Take into consideration that shared constructs and packages must be tested independently of the consuming application, as if they were being released to the public.

The following diagram shows a sample AWS CDK version release pipeline.

![Release pipeline](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/images/guide-img/b7d5d887-7172-4d47-9f1f-1cf7ae181482/images/774bf06e-57df-424d-81fe-9ec8317aaa1f.png)

You can use the following sample commands to build, test, and publish npm packages. First, sign in to the artifact repository by running the following command.

```
aws codeartifact login --tool npm --domain <Domain Name> --domain-owner $(aws sts get-caller-identity --output text --query 'Account')  \
--repository <Repository Name> --region <AWS Region Name>
```

Then, complete the following steps:

1. Install the required packages based on the `package.json`** **file: `npm install`

1. Create the release candidate version: `npm version prerelease --preid rc`

1. Build the npm package: `npm run build`

1. Test the npm package: `npm run test`

1. Publish the npm package: `npm publish`
