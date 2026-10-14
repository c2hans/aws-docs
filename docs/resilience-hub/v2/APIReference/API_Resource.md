---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

Represents an AWS resource discovered by Resilience Hub.

## Contents
<a name="API_Resource_Contents"></a>

 ** identifier **   <a name="ngresiliencehub-Type-Resource-identifier"></a>
The identifier of the resource.
Type: String
Required: Yes

 ** availabilityZoneId **   <a name="ngresiliencehub-Type-Resource-availabilityZoneId"></a>
The Availability Zone ID of the Availability Zone that hosts the resource, such as use1-az1. The Availability Zone ID is consistent across Amazon Web Services (AWS) accounts, unlike the Availability Zone name.
Type: String
Required: No

 ** availabilityZoneName **   <a name="ngresiliencehub-Type-Resource-availabilityZoneName"></a>
The name of the Availability Zone that hosts the resource, such as us-west-2a.
Type: String
Required: No

 ** awsAccountId **   <a name="ngresiliencehub-Type-Resource-awsAccountId"></a>
The AWS account ID that owns the resource.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** awsRegion **   <a name="ngresiliencehub-Type-Resource-awsRegion"></a>
The AWS Region where the resource is located.
Type: String
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

 ** containmentParentId **   <a name="ngresiliencehub-Type-Resource-containmentParentId"></a>
The identifier of the single parent resource that contains this resource, used to represent containment relationships in the resource topology. A resource has at most one containment parent.
Type: String
Required: No

 ** logicalResourceGroupId **   <a name="ngresiliencehub-Type-Resource-logicalResourceGroupId"></a>
The identifier of the logical resource group that this resource belongs to. Resources that share this identifier are managed as a single unit.
Type: String
Required: No

 ** resourceType **   <a name="ngresiliencehub-Type-Resource-resourceType"></a>
The type of the resource.
Type: String
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/Resource)
