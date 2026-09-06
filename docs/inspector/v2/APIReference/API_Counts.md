---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Counts.html
---

# Counts
<a name="API_Counts"></a>

a structure that contains information on the count of resources within a group.

## Contents
<a name="API_Counts_Contents"></a>

 ** count **   <a name="inspector2-Type-Counts-count"></a>
The number of resources.
Type: Long
Required: No

 ** groupKey **   <a name="inspector2-Type-Counts-groupKey"></a>
The key associated with this group
Type: String
Valid Values: `SCAN_STATUS_CODE | SCAN_STATUS_REASON | ACCOUNT_ID | RESOURCE_TYPE | ECR_REPOSITORY_NAME | PROVIDER | PROVIDER_ACCOUNT_ID | PROVIDER_REGION | PROVIDER_ORG_ID`
Required: No

## See Also
<a name="API_Counts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Counts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Counts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Counts)
