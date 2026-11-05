---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SoftwareResourceResult.html
---

# SoftwareResourceResult
<a name="API_SoftwareResourceResult"></a>

Provides information about a resource that contains a software package.

## Contents
<a name="API_SoftwareResourceResult_Contents"></a>

 ** AccountId **   <a name="securityhub-Type-SoftwareResourceResult-AccountId"></a>
The AWS account that recorded the resource data in Security Hub.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Region **   <a name="securityhub-Type-SoftwareResourceResult-Region"></a>
The AWS Region that recorded the resource data in Security Hub.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResourceId **   <a name="securityhub-Type-SoftwareResourceResult-ResourceId"></a>
The unique identifier for a resource.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResourceType **   <a name="securityhub-Type-SoftwareResourceResult-ResourceType"></a>
The type of resource, for example `AWS::EC2::Instance` or `AWS::Lambda::Function`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResourceCloudPartition **   <a name="securityhub-Type-SoftwareResourceResult-ResourceCloudPartition"></a>
The cloud partition where the resource exists. For AWS, valid values include `aws`, `aws-cn`, and `aws-us-gov`. This field isn't returned for cloud providers that don't use partitions.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceOwnerAccountId **   <a name="securityhub-Type-SoftwareResourceResult-ResourceOwnerAccountId"></a>
The identifier of the cloud account that owns the resource. For AWS resources, this is the AWS account ID. For Azure resources, this is the Azure subscription ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceOwnerOrgId **   <a name="securityhub-Type-SoftwareResourceResult-ResourceOwnerOrgId"></a>
The identifier of the cloud organization that owns the resource. For AWS resources, this is the AWS Organizations ID. For Azure resources, this is the Azure tenant ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceProvider **   <a name="securityhub-Type-SoftwareResourceResult-ResourceProvider"></a>
The cloud provider where the resource exists. Valid values are `AWS` and `Azure`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceRegion **   <a name="securityhub-Type-SoftwareResourceResult-ResourceRegion"></a>
The native cloud region where the resource is located. For AWS, this is an AWS Region (for example, `us-east-1`). For Azure resources, this is the Azure region (for example, `westus2`).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SoftwareResourceResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SoftwareResourceResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SoftwareResourceResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SoftwareResourceResult)
