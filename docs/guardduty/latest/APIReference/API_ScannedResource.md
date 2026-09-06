---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ScannedResource.html
---

# ScannedResource
<a name="API_ScannedResource"></a>

Contains information about a resource that was scanned as part of the malware scan operation.

## Contents
<a name="API_ScannedResource_Contents"></a>

 ** resourceDetails **   <a name="guardduty-Type-ScannedResource-resourceDetails"></a>
Information about the scanned resource.
Type: [ScannedResourceDetails](API_ScannedResourceDetails.md) object
Required: No

 ** scannedResourceArn **   <a name="guardduty-Type-ScannedResource-scannedResourceArn"></a>
Amazon Resource Name (ARN) of the scanned resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** scannedResourceStatus **   <a name="guardduty-Type-ScannedResource-scannedResourceStatus"></a>
The status of the scanned resource.
Type: String
Valid Values: `RUNNING | COMPLETED | COMPLETED_WITH_ISSUES | FAILED | SKIPPED`
Required: No

 ** scannedResourceType **   <a name="guardduty-Type-ScannedResource-scannedResourceType"></a>
The resource type of the scanned resource.
Type: String
Valid Values: `EBS_RECOVERY_POINT | EBS_SNAPSHOT | EBS_VOLUME | EC2_AMI | EC2_INSTANCE | EC2_RECOVERY_POINT | S3_RECOVERY_POINT | S3_BUCKET | S3_POINT_IN_TIME_RECOVERY`
Required: No

 ** scanStatusReason **   <a name="guardduty-Type-ScannedResource-scanStatusReason"></a>
The reason for the scan status of this particular resource, if applicable.
Type: String
Valid Values: `ACCESS_DENIED | RESOURCE_NOT_FOUND | SNAPSHOT_SIZE_LIMIT_EXCEEDED | RESOURCE_UNAVAILABLE | INCONSISTENT_SOURCE | INCREMENTAL_NO_DIFFERENCE | NO_EBS_VOLUMES_FOUND | UNSUPPORTED_PRODUCT_CODE_TYPE | AMI_SNAPSHOT_LIMIT_EXCEEDED | UNRELATED_RESOURCES | BASE_RESOURCE_NOT_SCANNED | BASE_CREATED_AFTER_TARGET | UNSUPPORTED_FOR_INCREMENTAL | UNSUPPORTED_AMI | UNSUPPORTED_SNAPSHOT | UNSUPPORTED_COMPOSITE_RECOVERY_POINT | ALL_FILES_SKIPPED_OR_FAILED`
Required: No

## See Also
<a name="API_ScannedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ScannedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ScannedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ScannedResource)
