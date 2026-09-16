---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_InfrastructureConfiguration.html
---

# InfrastructureConfiguration
<a name="API_InfrastructureConfiguration"></a>

Details of the infrastructure configuration.

## Contents
<a name="API_InfrastructureConfiguration_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-InfrastructureConfiguration-arn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-InfrastructureConfiguration-dateCreated"></a>
The date on which the infrastructure configuration was created.
Type: String
Required: No

 ** dateUpdated **   <a name="imagebuilder-Type-InfrastructureConfiguration-dateUpdated"></a>
The date on which the infrastructure configuration was last updated.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-InfrastructureConfiguration-description"></a>
The description of the infrastructure configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** instanceMetadataOptions **   <a name="imagebuilder-Type-InfrastructureConfiguration-instanceMetadataOptions"></a>
The instance metadata option settings for the infrastructure configuration.
Type: [InstanceMetadataOptions](API_InstanceMetadataOptions.md) object
Required: No

 ** instanceProfileName **   <a name="imagebuilder-Type-InfrastructureConfiguration-instanceProfileName"></a>
The instance profile of the infrastructure configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=,.@-]+$`
Required: No

 ** instanceTypes **   <a name="imagebuilder-Type-InfrastructureConfiguration-instanceTypes"></a>
The instance types of the infrastructure configuration.
Type: Array of strings
Required: No

 ** keyPair **   <a name="imagebuilder-Type-InfrastructureConfiguration-keyPair"></a>
The Amazon EC2 key pair of the infrastructure configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** logging **   <a name="imagebuilder-Type-InfrastructureConfiguration-logging"></a>
The logging configuration of the infrastructure configuration.
Type: [Logging](API_Logging.md) object
Required: No

 ** name **   <a name="imagebuilder-Type-InfrastructureConfiguration-name"></a>
The name of the infrastructure configuration.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** placement **   <a name="imagebuilder-Type-InfrastructureConfiguration-placement"></a>
The instance placement settings that define where the instances that are launched from your image run.
Type: [Placement](API_Placement.md) object
Required: No

 ** resourceTags **   <a name="imagebuilder-Type-InfrastructureConfiguration-resourceTags"></a>
The tags attached to the resource created by Image Builder.
Type: String to string map
Map Entries: Maximum number of 30 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** securityGroupIds **   <a name="imagebuilder-Type-InfrastructureConfiguration-securityGroupIds"></a>
The security group IDs of the infrastructure configuration.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** snsTopicArn **   <a name="imagebuilder-Type-InfrastructureConfiguration-snsTopicArn"></a>
The Amazon Resource Name (ARN) of the SNS topic to which Image Builder sends image build event notifications.
EC2 Image Builder is unable to send notifications to SNS topics that are encrypted using keys from other accounts. The key that is used to encrypt the SNS topic must reside in the account that the Image Builder service runs under.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** subnetId **   <a name="imagebuilder-Type-InfrastructureConfiguration-subnetId"></a>
The subnet ID of the infrastructure configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** tags **   <a name="imagebuilder-Type-InfrastructureConfiguration-tags"></a>
The tags of the infrastructure configuration.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** terminateInstanceOnFailure **   <a name="imagebuilder-Type-InfrastructureConfiguration-terminateInstanceOnFailure"></a>
The terminate instance on failure configuration of the infrastructure configuration.
Type: Boolean
Required: No

## See Also
<a name="API_InfrastructureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/InfrastructureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/InfrastructureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/InfrastructureConfiguration)
