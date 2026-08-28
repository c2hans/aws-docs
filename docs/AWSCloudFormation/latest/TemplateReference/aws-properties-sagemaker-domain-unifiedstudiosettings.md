---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-unifiedstudiosettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain UnifiedStudioSettings
<a name="aws-properties-sagemaker-domain-unifiedstudiosettings"></a>

The settings that apply to an Amazon SageMaker AI domain when you use it in Amazon SageMaker Unified Studio.

## Syntax
<a name="aws-properties-sagemaker-domain-unifiedstudiosettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-unifiedstudiosettings-syntax.json"></a>

```
{
  "[DomainAccountId](#cfn-sagemaker-domain-unifiedstudiosettings-domainaccountid)" : {{String}},
  "[DomainId](#cfn-sagemaker-domain-unifiedstudiosettings-domainid)" : {{String}},
  "[DomainRegion](#cfn-sagemaker-domain-unifiedstudiosettings-domainregion)" : {{String}},
  "[EnvironmentId](#cfn-sagemaker-domain-unifiedstudiosettings-environmentid)" : {{String}},
  "[ProjectId](#cfn-sagemaker-domain-unifiedstudiosettings-projectid)" : {{String}},
  "[ProjectS3Path](#cfn-sagemaker-domain-unifiedstudiosettings-projects3path)" : {{String}},
  "[StudioWebPortalAccess](#cfn-sagemaker-domain-unifiedstudiosettings-studiowebportalaccess)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-unifiedstudiosettings-syntax.yaml"></a>

```
  [DomainAccountId](#cfn-sagemaker-domain-unifiedstudiosettings-domainaccountid): {{String}}
  [DomainId](#cfn-sagemaker-domain-unifiedstudiosettings-domainid): {{String}}
  [DomainRegion](#cfn-sagemaker-domain-unifiedstudiosettings-domainregion): {{String}}
  [EnvironmentId](#cfn-sagemaker-domain-unifiedstudiosettings-environmentid): {{String}}
  [ProjectId](#cfn-sagemaker-domain-unifiedstudiosettings-projectid): {{String}}
  [ProjectS3Path](#cfn-sagemaker-domain-unifiedstudiosettings-projects3path): {{String}}
  [StudioWebPortalAccess](#cfn-sagemaker-domain-unifiedstudiosettings-studiowebportalaccess): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-unifiedstudiosettings-properties"></a>

`DomainAccountId`  <a name="cfn-sagemaker-domain-unifiedstudiosettings-domainaccountid"></a>
The ID of the AWS account that has the Amazon SageMaker Unified Studio domain. The default value, if you don't specify an ID, is the ID of the account that has the Amazon SageMaker AI domain.
*Required*: No
*Type*: String
*Pattern*: `^\d+$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainId`  <a name="cfn-sagemaker-domain-unifiedstudiosettings-domainid"></a>
The ID of the Amazon SageMaker Unified Studio domain associated with this domain.
*Required*: No
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainRegion`  <a name="cfn-sagemaker-domain-unifiedstudiosettings-domainregion"></a>
The AWS Region where the domain is located in Amazon SageMaker Unified Studio. The default value, if you don't specify a Region, is the Region where the Amazon SageMaker AI domain is located.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z]{2}-[a-zA-Z\-]+-\d+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentId`  <a name="cfn-sagemaker-domain-unifiedstudiosettings-environmentid"></a>
The ID of the environment that Amazon SageMaker Unified Studio associates with the domain.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectId`  <a name="cfn-sagemaker-domain-unifiedstudiosettings-projectid"></a>
The ID of the Amazon SageMaker Unified Studio project that corresponds to the domain.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectS3Path`  <a name="cfn-sagemaker-domain-unifiedstudiosettings-projects3path"></a>
The location where Amazon S3 stores temporary execution data and other artifacts for the project that corresponds to the domain.
*Required*: No
*Type*: String
*Pattern*: `[\w\.-]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StudioWebPortalAccess`  <a name="cfn-sagemaker-domain-unifiedstudiosettings-studiowebportalaccess"></a>
Sets whether you can access the domain in Amazon SageMaker Studio:
ENABLED
You can access the domain in Amazon SageMaker Studio. If you migrate the domain to Amazon SageMaker Unified Studio, you can access it in both studio interfaces.
DISABLED
You can't access the domain in Amazon SageMaker Studio. If you migrate the domain to Amazon SageMaker Unified Studio, you can access it only in that studio interface.
To migrate a domain to Amazon SageMaker Unified Studio, you specify the UnifiedStudioSettings data type when you use the UpdateDomain action.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
