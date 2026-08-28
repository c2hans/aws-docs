---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/enterprise-blueprint-factory/using-factory.html
---

# Using the Enterprise Blueprint Factory
<a name="using-factory"></a>

This section helps you create, update, or delete blueprints in your environment. It provides detailed instructions for managing a blueprint throughout its [life cycle](architecture-blueprint-lifecycle.md).

To create or update custom blueprints, you must have an understanding of how to create IaC templates, such as AWS CloudFormation [templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) or AWS Cloud Development Kit (AWS CDK) [constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html). This guide does not include information or instructions about how to define the blueprints that you release through the Enterprise Blueprint Factory.

## Prerequisites
<a name="using-factory-prereqs"></a>

The following are the prerequisites for using the Enterprise Blueprint Factory in your AWS environment:
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ Permissions to assume the `ServiceCatalogEndUserRole` AWS Identity and Access Management (IAM) role
+ An CloudFormation template or AWS CDK construct

## Creating a blueprint
<a name="using-factory-create"></a>

The Enterprise Blueprint Factory pipelines deploy the blueprints that you define in the configuration file. The developer initiates the configuration pipeline by merging the configuration file into the configuration repository. Then, the Enterprise Blueprint Factory uses the `ServiceCatalogLaunchConstraintRole` to deploy the blueprint as a product in Service Catalog. For more information about the actions that the configuration pipeline and release pipeline perform when you create a blueprint, see [Blueprint creation](architecture-blueprint-lifecycle.md#architecture-blueprint-lifecycle-create) in this guide.

**To add the blueprint to the product repository**

1. Make sure that you have set up your Enterprise Blueprint Factory according to the instructions in [Setting up the Enterprise Blueprint Factory](setup.md) in this guide.

1. Confirm that the policy for the `ServiceCataloglogLaunchConstraintRole` role allows you to provision the resources defined in the blueprint.

1. In the product repository (`ServiceCatalog-BlueprintProductRepo`), create a folder for the new blueprint.

1. Paste the IaC template (CloudFormation template or AWS CDK construct) into the folder that you created.

1. Create a file named **product\_config.json** in the folder that you created.

1. Open the** product\_config.json** file, and paste the following into the file:

   ```
   {
       "SchemaVersion": "1.0",
       "ProductVersionName": "1.0.1",
       "Deprecated_Versions" : [],
       "ProductVersionDescription": "<description>",
       "ProductType": "CLOUD_FORMATION_TEMPLATE",
       "Properties": {
           "TemplateFilePath": "./<folder name>/<file name>"
       }
   }
   ```

   Where:
   + `<description>` is a brief description of the blueprint version
   + `<folder name>` is the name of the folder you created in the product repository
   + `<file name>` is the name of the IaC template
**Note**
You can update the schema version or product version names to match your organization's policies.

1. Save and close the **product\_config.json** file.

1. Enter the following commands to merge the changes into the product repository:

   ```
   cd ServiceCatalog-BlueprintProductRepo
   git add <folder name>/<file name> <folder name>\product_config.json
   git commit -m "The first version of <file name> blueprint"
   git push origin main
   ```

**To update the configuration file**

1. In the configuration repository (`ServiceCatalog-ConfigRepo`), open the **config.yml** file.

1. Edit the `portfolios` section and `products` section as needed for the new blueprint. For more information, see [Configuration file](architecture-components.md#architecture-config-file) in this guide.

1. Save and close the **config.yml** file.

1. Enter the following commands to merge the changes into the configuration repository:

   ```
   cd ServiceCatalog-ConfigRepo
   git add config.yml
   git commit -m "<description of change>"
   git push origin main
   ```

   Approval of this pull request initiates the configuration pipeline. The configuration pipeline creates a release pipeline for the product.

**To review the deployment logs**

1. Sign in to the Enterprise Blueprint Factory administrative account.

1. Open the [AWS CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home).

1. In **Name**, choose the release pipeline for the product. By default, the pipeline name is `BluePrint_<Product-Name>-<CloudFormation-Stack-Name>`.

1. Choose **View history**.

1. View the status of the pipeline and stage execution. For more information about the status, see [View execution status](https://docs.aws.amazon.com/codepipeline/latest/userguide/executions-view.html#pipelines-executions-status-console) in the CodePipeline documentation.

1. If the pipeline fails, review the cause of the failure. For instructions about how to configure monitoring for your pipelines, see [Monitoring pipelines](https://docs.aws.amazon.com/codepipeline/latest/userguide/monitoring.html) in the CodePipeline documentation. If the release pipeline failed due to a cfn-lint or cfn\_nag check, correct the error in the template. Submit another pull request to the product repo. This restarts the release pipeline. For more information about correcting template errors, see the [Troubleshooting](#using-factory-troubleshooting) section in this guide.

1.  Wait until the release pipeline status is `Succeeded`.

**To validate the deployment**

1. Sign in to a consumer account in the organization.

1. Assume the `ServiceCatalogEndUserRole` IAM role.

1. Open the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/).

1. In the navigation pane, choose **Products**.

1. Confirm that the new product is available in the list of products.

## Updating a blueprint
<a name="using-factory-update"></a>

For more information about the actions that the configuration pipeline and release pipeline perform when you create a blueprint, see [Blueprint update](architecture-blueprint-lifecycle.md#architecture-blueprint-lifecycle-update) in this guide.

**To update a blueprint**

1. In the product repository, navigate into the folder for the product.

1. Paste the updated IaC template. Make sure that the file name is the same as the previous version.

1. Open the **product\_config.json** file.

1. For `ProductVersionName`, update the version number.

1. If you want to prevent the previous product version from being deployed in future, for `Deprecated_Versions`, enter the previous version numbers in a comma-separated list.

1. Enter the following commands to merge the changes into the product repository:

   ```
   cd ServiceCatalog-BlueprintProductRepo
   git add <folder name>/<file name> <folder name>\product_config.json
   git commit -m "Version <number> of <file name> blueprint"
   git push origin main
   ```

   Approval of this pull request initiates the release pipeline for the product.

**To review the deployment logs**

1. Sign in to the Enterprise Blueprint Factory administrative account.

1. Open the [AWS CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home).

1. In **Name**, choose the release pipeline. By default, the pipeline name is `BluePrint_<Product-Name>-<CloudFormation-Stack-Name>`.

1. Choose **View history**.

1. View the status of the pipeline and stage execution. For more information about the status, see [View execution status](https://docs.aws.amazon.com/codepipeline/latest/userguide/executions-view.html#pipelines-executions-status-console) in the CodePipeline documentation.

1. If the pipeline fails, review the cause of the failure. For instructions about how to configure monitoring for your pipelines, see [Monitoring pipelines](https://docs.aws.amazon.com/codepipeline/latest/userguide/monitoring.html) in the CodePipeline documentation. If the release pipeline failed due to a cfn-lint or cfn\_nag check, correct the error in the template. Submit another pull request to the product repo. This restarts the release pipeline. For more information about correcting template errors, see the [Troubleshooting](#using-factory-troubleshooting) section in this guide.

1.  Wait until the release pipeline status is `Succeeded`.

**To validate the update**

1. Sign in to a consumer account in the organization.

1. Assume the `ServiceCatalogEndUserRole` IAM role.

1. Open the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/).

1. In the navigation pane, choose **Products**.

1. Confirm that the new product version is available in the list of products.

## Deleting a blueprint
<a name="using-factory-delete"></a>

When you delete a product, Service Catalog removes all of product versions from every portfolio that contains the product. For more information, see [Deleting products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/productmgmt-delete.html) in the Service Catalog documentation. For more information about the actions that the configuration pipeline and release pipeline perform when you create a blueprint, see [Blueprint deletion](architecture-blueprint-lifecycle.md#architecture-blueprint-lifecycle-delete) in this guide.

**To delete a blueprint**

1. In the configuration repository, open the **config.yml** file.

1. Edit the products section, remove or comment out the product you want to delete.

1. Save and close the **config.yml** file.

1. Enter the following commands to merge the changes into the configuration repository:

   ```
   cd ServiceCatalog-ConfigRepo
   git add config.yml
   git commit -m "<description of change>"
   git push origin main
   ```

   Approval of this pull request initiates the configuration pipeline. The configuration pipeline deletes the product and its release pipeline.

1. In the product repository, delete the folder for the product, including its contents.

1. Enter the following commands to merge the changes into the product repository:

   ```
   cd ServiceCatalog-BlueprintProductRepo
   git add .
   git commit -m "Delete <file name> blueprint"
   git push origin main
   ```

**To validate the deletion**

1. Sign in to a consumer account in the organization.

1. Assume the `ServiceCatalogEndUserRole` IAM role.

1. Open the [Service Catalog console](https://console.aws.amazon.com/servicecatalog/).

1. In the navigation pane, choose **Products**.

1. Confirm that the deleted product is no longer available.

## Troubleshooting
<a name="using-factory-troubleshooting"></a>

When you create or update a blueprint, the cfn-lint and cfn-nag tools validate the blueprint. For more information about validation in the release pipeline, see [Release pipeline](architecture-components.md#architecture-release-pipeline) in this guide. Any reported syntax or security errors cause the pipeline to fail. To successfully deploy the blueprint through the release pipeline, you must correct the errors in the blueprint.

The following is an example output that shows two security-related errors, a failure and a warning.

```
BP-SNS.yml
---------------------------------------------------
BP-SNS.yml
---------------------------------------------------
| WARN W47
|
| Resource: ["ExampleTopic"]
| Line numbers: [5]
|
| SNS Topic should specify KmsMasterKeyId property
---------------------------------------------------
| FAIL F18
|
| Resource: ["ExampleTopicPolicy"]
| Line numbers: [10]
|
| SNS topic policy should not allow * principal

Failures count: 1
Warnings count: 1
```

To correct these errors, in the blueprint file, you would replace the `*` principal in the Amazon Simple Notification Service (Amazon SNS) topic policy and associate an AWS Key Management Service (AWS KMS) key with the topic. The following code example demonstrates these updates.

```
ExampleTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: ExampleTopic
  ExampleTopicPolicy:
    Type: AWS::SNS::TopicPolicy
    Properties:
      KmsMasterKeyId: alias/aws/sns  # Added KMS key
      PolicyDocument:
        Id: Id1
        Version: '2012-10-17'
        Statement:
        - Sid: Sid2
          Effect: Allow
          Principal:
            "Service" : "s3.amazonaws.com"  # Replaced "AWS": '*'
          Action: 'sns:Publish'
          Resource: !Ref ExampleTopic
      Topics:
        - !Ref ExampleTopic
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
