---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ScanStatus.html
---

# ScanStatus
<a name="API_ScanStatus"></a>

The status of the scan.

## Contents
<a name="API_ScanStatus_Contents"></a>

 ** reason **   <a name="inspector2-Type-ScanStatus-reason"></a>
The scan status. Possible return values and descriptions are:
 `ACCESS_DENIED` - Resource access policy restricting Amazon Inspector access. Please update the IAM policy.
 `ACCESS_DENIED_TO_ENCRYPTION_KEY` - The KMS key policy doesn't allow Amazon Inspector access. Update the key policy.
 `DEEP_INSPECTION_COLLECTION_TIME_LIMIT_EXCEEDED` - Amazon Inspector failed to extract the package inventory because the package collection time exceeding the maximum threshold of 15 minutes.
 `DEEP_INSPECTION_DAILY_SSM_INVENTORY_LIMIT_EXCEEDED` - The SSM agent couldn't send inventory to Amazon Inspector because the SSM quota for Inventory data collected per instance per day has already been reached for this instance.
 `DEEP_INSPECTION_NO_INVENTORY` - The Amazon Inspector plugin hasn't yet been able to collect an inventory of packages for this instance. This is usually the result of a pending scan, however, if this status persists after 6 hours, use SSM to ensure that the required Amazon Inspector associations exist and are running for the instance.
 `DEEP_INSPECTION_PACKAGE_COLLECTION_LIMIT_EXCEEDED` - The instance has exceeded the 5000 package limit for Amazon Inspector Deep inspection. To resume Deep inspection for this instance you can try to adjust the custom paths associated with the account.
 `EC2_INSTANCE_STOPPED` - This EC2 instance is in a stopped state, therefore, Amazon Inspector will pause scanning. The existing findings will continue to exist until the instance is terminated. Once the instance is re-started, Inspector will automatically start scanning the instance again. Please note that you will not be charged for this instance while it's in a stopped state.
 `EXCLUDED_BY_TAG` - This resource was not scanned because it has been excluded by a tag.
 `IMAGE_SIZE_EXCEEDED` - Reserved for future use.
 `INTEGRATION_CONNNECTION_LOST` - Amazon Inspector couldn't communicate with the source code management platform.
 `INTERNAL_ERROR` - Amazon Inspector has encountered an internal error for this resource. Amazon Inspector service will automatically resolve the issue and resume the scanning. No action required from the user.
 `NO_INVENTORY` - Amazon Inspector couldn't find software application inventory to scan for vulnerabilities. This might be caused due to required Amazon Inspector associations being deleted or failing to run on your resource. Please verify the status of `InspectorInventoryCollection-do-not-delete` association in the SSM console for the resource. Additionally, you can verify the instance's inventory in the SSM Fleet Manager console.
 `NO_RESOURCES_FOUND` - Reserved for future use.
 `NO_SCAN_CONFIGURATION_ASSOCIATED` - The code repository resource doesn't have an associated scan configuration.
 `PENDING_DISABLE` - This resource is pending cleanup during disablement. The customer will not be billed while a resource is in the pending disable status.
 `PENDING_INITIAL_SCAN` - This resource has been identified for scanning, results will be available soon.
 `RESOURCE_TERMINATED` - This resource has been terminated. The findings and coverage associated with this resource are in the process of being cleaned up.
 `SCAN_ELIGIBILITY_EXPIRED` - The configured scan duration has lapsed for this image.
 `SCAN_FREQUENCY_MANUAL` - This image will not be covered by Amazon Inspector due to the repository scan frequency configuration.
 `SCAN_FREQUENCY_SCAN_ON_PUSH` - This image will be scanned one time and will not new findings because of the scan frequency configuration.
 `SCAN_IN_PROGRESS` - The resource is currently being scanned.
 `STALE_INVENTORY` - Amazon Inspector wasn't able to collect an updated software application inventory in the last 7 days. Please confirm the required Amazon Inspector associations still exist and you can still see an updated inventory in the SSM console.
 `SUCCESSFUL` - The scan was successful.
 `UNMANAGED_EC2_INSTANCE` - The EC2 instance is not managed by SSM, please use the following SSM automation to remediate the issue: [https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-managed-instance.html](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-managed-instance.html). Once the instance becomes managed by SSM, Inspector will automatically begin scanning this instance.
 `UNSUPPORTED_CODE_ARTIFACTS ` - The function was not scanned because it has an unsupported code artifacts.
 `UNSUPPORTED_CONFIG_FILE` - Reserved for future use.
 `UNSUPPORTED_LANGUAGE` - The scan was unsuccessful because the repository contains files in an unsupported programming language.
 `UNSUPPORTED_MEDIA_TYPE `- The ECR image has an unsupported media type.
 `UNSUPPORTED_OS` - Amazon Inspector does not support this OS, architecture, or image manifest type at this time. To see a complete list of supported operating systems see: [https://docs.aws.amazon.com/inspector/latest/user/supported.html]( https://docs.aws.amazon.com/inspector/latest/user/supported.html).
 `UNSUPPORTED_RUNTIME` - The function was not scanned because it has an unsupported runtime. To see a complete list of supported runtimes see: [https://docs.aws.amazon.com/inspector/latest/user/supported.html]( https://docs.aws.amazon.com/inspector/latest/user/supported.html).
 `IMAGE_ARCHIVED` - This image has been archived in Amazon ECR and is no longer available for scanning in Amazon Inspector.
Type: String
Valid Values: `PENDING_INITIAL_SCAN | ACCESS_DENIED | INTERNAL_ERROR | UNMANAGED_EC2_INSTANCE | UNSUPPORTED_OS | SCAN_ELIGIBILITY_EXPIRED | RESOURCE_TERMINATED | SUCCESSFUL | NO_RESOURCES_FOUND | IMAGE_SIZE_EXCEEDED | SCAN_FREQUENCY_MANUAL | SCAN_FREQUENCY_SCAN_ON_PUSH | EC2_INSTANCE_STOPPED | PENDING_DISABLE | NO_INVENTORY | STALE_INVENTORY | EXCLUDED_BY_TAG | UNSUPPORTED_RUNTIME | UNSUPPORTED_MEDIA_TYPE | UNSUPPORTED_CONFIG_FILE | DEEP_INSPECTION_PACKAGE_COLLECTION_LIMIT_EXCEEDED | DEEP_INSPECTION_DAILY_SSM_INVENTORY_LIMIT_EXCEEDED | DEEP_INSPECTION_COLLECTION_TIME_LIMIT_EXCEEDED | DEEP_INSPECTION_NO_INVENTORY | AGENTLESS_INSTANCE_STORAGE_LIMIT_EXCEEDED | AGENTLESS_INSTANCE_COLLECTION_TIME_LIMIT_EXCEEDED | PENDING_REVIVAL_SCAN | INTEGRATION_CONNECTION_LOST | ACCESS_DENIED_TO_ENCRYPTION_KEY | UNSUPPORTED_LANGUAGE | NO_SCAN_CONFIGURATION_ASSOCIATED | SCAN_IN_PROGRESS | IMAGE_ARCHIVED | UNSUPPORTED_CODE_ARTIFACTS | RESOURCE_UNMANAGED | RESOURCE_STOPPED`
Required: Yes

 ** statusCode **   <a name="inspector2-Type-ScanStatus-statusCode"></a>
The status code of the scan.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

## See Also
<a name="API_ScanStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ScanStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ScanStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ScanStatus)
