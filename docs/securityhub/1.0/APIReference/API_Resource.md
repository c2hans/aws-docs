---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

A resource related to a finding.

## Contents
<a name="API_Resource_Contents"></a>

 ** Id **   <a name="securityhub-Type-Resource-Id"></a>
The canonical identifier for the given resource type.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Type **   <a name="securityhub-Type-Resource-Type"></a>
The type of the resource that details are provided for. If possible, set `Type` to one of the supported resource types. For example, if the resource is an EC2 instance, then set `Type` to `AwsEc2Instance`.
If the resource does not match any of the provided types, then set `Type` to `Other`.
Length Constraints: Minimum length of 1. Maximum length of 256.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ApplicationArn **   <a name="securityhub-Type-Resource-ApplicationArn"></a>
 The Amazon Resource Name (ARN) of the application that is related to a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ApplicationName **   <a name="securityhub-Type-Resource-ApplicationName"></a>
 The name of the application that is related to a finding.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DataClassification **   <a name="securityhub-Type-Resource-DataClassification"></a>
Contains information about sensitive data that was detected on the resource.
Type: [DataClassificationDetails](API_DataClassificationDetails.md) object
Required: No

 ** Details **   <a name="securityhub-Type-Resource-Details"></a>
Additional details about the resource related to a finding.
Type: [ResourceDetails](API_ResourceDetails.md) object
Required: No

 ** Owner **   <a name="securityhub-Type-Resource-Owner"></a>
Information about the account and organization that own the resource.
Type: [ResourceOwner](API_ResourceOwner.md) object
Required: No

 ** Partition **   <a name="securityhub-Type-Resource-Partition"></a>
The canonical AWS partition name that the Region is assigned to.
Type: String
Valid Values: `aws | aws-cn | aws-us-gov | aws-us-iso | aws-us-iso-b | AzureCloud`
Required: No

 ** Provider **   <a name="securityhub-Type-Resource-Provider"></a>
The cloud provider that the resource belongs to. Valid values are `AWS` and `Azure`.
Type: String
Valid Values: `Azure | AWS`
Required: No

 ** Region **   <a name="securityhub-Type-Resource-Region"></a>
The canonical AWS external Region name where this resource is located.
Length Constraints: Minimum length of 1. Maximum length of 16.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceRole **   <a name="securityhub-Type-Resource-ResourceRole"></a>
Identifies the role of the resource in the finding. A resource is either the actor or target of the finding activity,
Type: String
Pattern: `.*\S.*`
Required: No

 ** Tags **   <a name="securityhub-Type-Resource-Tags"></a>
A list of AWS tags associated with a resource at the time the finding was processed. Tags must follow [AWS tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Resource)
