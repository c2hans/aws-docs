---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationResource.html
---

# RemediationResource
<a name="API_RemediationResource"></a>

Provides comprehensive details about a resource.

## Contents
<a name="API_RemediationResource_Contents"></a>

 ** AccountId **   <a name="securityhub-Type-RemediationResource-AccountId"></a>
The AWS account that recorded the resource data in Security Hub.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** CloudProvider **   <a name="securityhub-Type-RemediationResource-CloudProvider"></a>
The cloud provider where the resource exists.
+  `AWS` specifies that the resource exists in AWS.
+  `Azure` specifies that the resource exists in Microsoft Azure.
Type: String
Valid Values: `Azure | AWS`
Required: Yes

 ** Id **   <a name="securityhub-Type-RemediationResource-Id"></a>
The unique identifier for a resource.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Region **   <a name="securityhub-Type-RemediationResource-Region"></a>
The AWS Region in which Security Hub recorded the resource data.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResourceRegion **   <a name="securityhub-Type-RemediationResource-ResourceRegion"></a>
The native cloud region where the resource is located. For AWS, this is an AWS Region (for example, `us-east-1`). For Azure resources, this is the Azure region (for example, `westus2`). This field is always included.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Type **   <a name="securityhub-Type-RemediationResource-Type"></a>
The type of the resource.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="securityhub-Type-RemediationResource-Name"></a>
The name of the resource.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceGuid **   <a name="securityhub-Type-RemediationResource-ResourceGuid"></a>
The global identifier used to identify a resource.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceOwnerAccountId **   <a name="securityhub-Type-RemediationResource-ResourceOwnerAccountId"></a>
The identifier of the cloud account that owns the resource. For AWS resources, this is the AWS account ID. For Azure resources, this is the Azure subscription ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourceOwnerOrgId **   <a name="securityhub-Type-RemediationResource-ResourceOwnerOrgId"></a>
The identifier of the cloud organization that owns the resource. For AWS resources, this is the AWS Organizations ID. For Azure resources, this is the Azure tenant ID.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RemediationResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationResource)
