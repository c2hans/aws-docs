---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResourceDataSyncDestinationDataSharing.html
---

# ResourceDataSyncDestinationDataSharing
<a name="API_ResourceDataSyncDestinationDataSharing"></a>

Synchronize AWS Systems Manager Inventory data from multiple AWS accounts defined in AWS Organizations to a centralized Amazon S3 bucket. Data is synchronized to individual key prefixes in the central bucket. Each key prefix represents a different AWS account ID.

## Contents
<a name="API_ResourceDataSyncDestinationDataSharing_Contents"></a>

 ** DestinationDataSharingType **   <a name="systemsmanager-Type-ResourceDataSyncDestinationDataSharing-DestinationDataSharingType"></a>
The sharing data type. Only `Organization` is supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ResourceDataSyncDestinationDataSharing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ResourceDataSyncDestinationDataSharing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ResourceDataSyncDestinationDataSharing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ResourceDataSyncDestinationDataSharing)
