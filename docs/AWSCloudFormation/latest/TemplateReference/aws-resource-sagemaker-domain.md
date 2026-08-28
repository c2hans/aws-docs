---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-domain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain
<a name="aws-resource-sagemaker-domain"></a>

Creates a `Domain`. A domain consists of an associated Amazon Elastic File System volume, a list of authorized users, and a variety of security, application, policy, and Amazon Virtual Private Cloud (VPC) configurations. Users within a domain can share notebook files and other artifacts with each other.

 **EFS storage**

When a domain is created, an EFS volume is created for use by all of the users within the domain. Each user receives a private home directory within the EFS volume for notebooks, Git repositories, and data files.

SageMaker AI uses the AWS Key Management Service (AWS KMS) to encrypt the EFS volume attached to the domain with an AWS managed key by default. For more control, you can specify a customer managed key. For more information, see [Protect Data at Rest Using Encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest.html).

 **VPC configuration**

All traffic between the domain and the Amazon EFS volume is through the specified VPC and subnets. For other traffic, you can specify the `AppNetworkAccessType` parameter. `AppNetworkAccessType` corresponds to the network access type that you choose when you onboard to the domain. The following options are available:
+ `PublicInternetOnly` - Non-EFS traffic goes through a VPC managed by Amazon SageMaker AI, which allows internet access. This is the default value.
+ `VpcOnly` - All traffic is through the specified VPC and subnets. Internet access is disabled by default. To allow internet access, you must specify a NAT gateway.

  When internet access is disabled, you won't be able to run a Amazon SageMaker AI Studio notebook or to train or host models unless your VPC has an interface endpoint to the SageMaker AI API and runtime or a NAT gateway and your security groups allow outbound connections.

**Important**
NFS traffic over TCP on port 2049 needs to be allowed in both inbound and outbound rules in order to launch a Amazon SageMaker AI Studio app successfully.

For more information, see [Connect Amazon SageMaker AI Studio Notebooks to Resources in a VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html).

## Syntax
<a name="aws-resource-sagemaker-domain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-domain-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Domain",
  "Properties" : {
      "[AppNetworkAccessType](#cfn-sagemaker-domain-appnetworkaccesstype)" : {{String}},
      "[AppSecurityGroupManagement](#cfn-sagemaker-domain-appsecuritygroupmanagement)" : {{String}},
      "[AuthMode](#cfn-sagemaker-domain-authmode)" : {{String}},
      "[DefaultSpaceSettings](#cfn-sagemaker-domain-defaultspacesettings)" : {{DefaultSpaceSettings}},
      "[DefaultUserSettings](#cfn-sagemaker-domain-defaultusersettings)" : {{UserSettings}},
      "[DomainName](#cfn-sagemaker-domain-domainname)" : {{String}},
      "[DomainSettings](#cfn-sagemaker-domain-domainsettings)" : {{DomainSettings}},
      "[HomeEfsFileSystemCreation](#cfn-sagemaker-domain-homeefsfilesystemcreation)" : {{String}},
      "[KmsKeyId](#cfn-sagemaker-domain-kmskeyid)" : {{String}},
      "[SubnetIds](#cfn-sagemaker-domain-subnetids)" : {{[ String, ... ]}},
      "[TagPropagation](#cfn-sagemaker-domain-tagpropagation)" : {{String}},
      "[Tags](#cfn-sagemaker-domain-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-sagemaker-domain-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-domain-syntax.yaml"></a>

```
Type: AWS::SageMaker::Domain
Properties:
  [AppNetworkAccessType](#cfn-sagemaker-domain-appnetworkaccesstype): {{String}}
  [AppSecurityGroupManagement](#cfn-sagemaker-domain-appsecuritygroupmanagement): {{String}}
  [AuthMode](#cfn-sagemaker-domain-authmode): {{String}}
  [DefaultSpaceSettings](#cfn-sagemaker-domain-defaultspacesettings): {{
    DefaultSpaceSettings}}
  [DefaultUserSettings](#cfn-sagemaker-domain-defaultusersettings): {{
    UserSettings}}
  [DomainName](#cfn-sagemaker-domain-domainname): {{String}}
  [DomainSettings](#cfn-sagemaker-domain-domainsettings): {{
    DomainSettings}}
  [HomeEfsFileSystemCreation](#cfn-sagemaker-domain-homeefsfilesystemcreation): {{String}}
  [KmsKeyId](#cfn-sagemaker-domain-kmskeyid): {{String}}
  [SubnetIds](#cfn-sagemaker-domain-subnetids): {{
    - String}}
  [TagPropagation](#cfn-sagemaker-domain-tagpropagation): {{String}}
  [Tags](#cfn-sagemaker-domain-tags): {{
    - Tag}}
  [VpcId](#cfn-sagemaker-domain-vpcid): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-domain-properties"></a>

`AppNetworkAccessType`  <a name="cfn-sagemaker-domain-appnetworkaccesstype"></a>
Specifies the VPC used for non-EFS traffic. The default value is `PublicInternetOnly`.
+ `PublicInternetOnly` - Non-EFS traffic is through a VPC managed by Amazon SageMaker AI, which allows direct internet access
+ `VpcOnly` - All Studio traffic is through the specified VPC and subnets
*Valid Values*: `PublicInternetOnly | VpcOnly`
*Required*: No
*Type*: String
*Allowed values*: `PublicInternetOnly | VpcOnly`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppSecurityGroupManagement`  <a name="cfn-sagemaker-domain-appsecuritygroupmanagement"></a>
The entity that creates and manages the required security groups for inter-app communication in `VpcOnly` mode. Required when `CreateDomain.AppNetworkAccessType` is `VpcOnly` and `DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn` is provided. If setting up the domain for use with RStudio, this value must be set to `Service`.
*Allowed Values*: `Service` \| `Customer`
*Required*: No
*Type*: String
*Allowed values*: `Service | Customer`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthMode`  <a name="cfn-sagemaker-domain-authmode"></a>
The mode of authentication that members use to access the Domain.
*Valid Values*: `SSO | IAM`
*Required*: Yes
*Type*: String
*Allowed values*: `SSO | IAM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultSpaceSettings`  <a name="cfn-sagemaker-domain-defaultspacesettings"></a>
The default settings for shared spaces that users create in the domain.
SageMaker applies these settings only to shared spaces. It doesn't apply them to private spaces.
*Required*: No
*Type*: [DefaultSpaceSettings](aws-properties-sagemaker-domain-defaultspacesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultUserSettings`  <a name="cfn-sagemaker-domain-defaultusersettings"></a>
The default user settings.
*Required*: Yes
*Type*: [UserSettings](aws-properties-sagemaker-domain-usersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-sagemaker-domain-domainname"></a>
The domain name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainSettings`  <a name="cfn-sagemaker-domain-domainsettings"></a>
A collection of settings that apply to the `SageMaker Domain`. These settings are specified through the `CreateDomain` API call.
*Required*: No
*Type*: [DomainSettings](aws-properties-sagemaker-domain-domainsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HomeEfsFileSystemCreation`  <a name="cfn-sagemaker-domain-homeefsfilesystemcreation"></a>
Indicates whether a home EFS file system is created for the domain.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-sagemaker-domain-kmskeyid"></a>
SageMaker uses AWS KMS to encrypt the EFS volume attached to the Domain with an AWS managed customer master key (CMK) by default. For more control, specify a customer managed CMK.
*Length Constraints*: Maximum length of 2048.
*Pattern*: `.*`
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-sagemaker-domain-subnetids"></a>
The VPC subnets that Studio uses for communication.
*Length Constraints*: Maximum length of 32.
*Array members*: Minimum number of 1 item. Maximum number of 16 items.
*Pattern*: `[-0-9a-zA-Z]+`
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `32 | 16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagPropagation`  <a name="cfn-sagemaker-domain-tagpropagation"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-domain-tags"></a>
Tags to associated with the Domain. Each tag consists of a key and an optional value. Tag keys must be unique per resource. Tags are searchable using the Search API.
Tags that you specify for the Domain are also added to all apps that are launched in the Domain.
*Array members*: Minimum number of 0 items. Maximum number of 50 items.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-domain-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-sagemaker-domain-vpcid"></a>
The ID of the Amazon Virtual Private Cloud (Amazon VPC) that Studio uses for communication.
*Length Constraints*: Maximum length of 32.
*Pattern*: `[-0-9a-zA-Z]+`
*Required*: No
*Type*: String
*Pattern*: `[-0-9a-zA-Z]+`
*Maximum*: `32`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## Return values
<a name="aws-resource-sagemaker-domain-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-domain-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Domain ID, such as `d-xxxxxxxxxxxx`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-domain-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-domain-return-values-fn--getatt-fn--getatt"></a>

`DomainArn`  <a name="DomainArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Domain, such as `arn:aws:sagemaker:us-west-2:account-id:domain/my-domain-name`.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The Domain ID.

`HomeEfsFileSystemId`  <a name="HomeEfsFileSystemId-fn::getatt"></a>
The ID of the Amazon Elastic File System (EFS) managed by this Domain.

`SecurityGroupIdForDomainBoundary`  <a name="SecurityGroupIdForDomainBoundary-fn::getatt"></a>
The ID of the security group that authorizes traffic between the `RSessionGateway` apps and the `RStudioServerPro` app.

`SingleSignOnApplicationArn`  <a name="SingleSignOnApplicationArn-fn::getatt"></a>
The ARN of the application managed by SageMaker in IAM Identity Center. This value is only returned for domains created after October 1, 2023.

`SingleSignOnManagedApplicationInstanceId`  <a name="SingleSignOnManagedApplicationInstanceId-fn::getatt"></a>
The IAM Identity Center managed application instance ID.

`Url`  <a name="Url-fn::getatt"></a>
The URL for the Domain.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
