---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxScalingGroup.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxScalingGroup
<a name="API_KxScalingGroup"></a>

 A structure for storing metadata of scaling group.

## Contents
<a name="API_KxScalingGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** availabilityZoneId **   <a name="finspace-Type-KxScalingGroup-availabilityZoneId"></a>
The identifier of the availability zones.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** clusters **   <a name="finspace-Type-KxScalingGroup-clusters"></a>
 The list of clusters currently active in a given scaling group.
Type: Array of strings
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** createdTimestamp **   <a name="finspace-Type-KxScalingGroup-createdTimestamp"></a>
 The timestamp at which the scaling group was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** hostType **   <a name="finspace-Type-KxScalingGroup-hostType"></a>
 The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.
You can add one of the following values:
+  `kx.sg.large` – The host type with a configuration of 16 GiB memory and 2 vCPUs.
+  `kx.sg.xlarge` – The host type with a configuration of 32 GiB memory and 4 vCPUs.
+  `kx.sg.2xlarge` – The host type with a configuration of 64 GiB memory and 8 vCPUs.
+  `kx.sg.4xlarge` – The host type with a configuration of 108 GiB memory and 16 vCPUs.
+  `kx.sg.8xlarge` – The host type with a configuration of 216 GiB memory and 32 vCPUs.
+  `kx.sg.16xlarge` – The host type with a configuration of 432 GiB memory and 64 vCPUs.
+  `kx.sg.32xlarge` – The host type with a configuration of 864 GiB memory and 128 vCPUs.
+  `kx.sg1.16xlarge` – The host type with a configuration of 1949 GiB memory and 64 vCPUs.
+  `kx.sg1.24xlarge` – The host type with a configuration of 2948 GiB memory and 96 vCPUs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-zA-Z0-9._]+`
Required: No

 ** lastModifiedTimestamp **   <a name="finspace-Type-KxScalingGroup-lastModifiedTimestamp"></a>
 The last time that the scaling group was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** scalingGroupName **   <a name="finspace-Type-KxScalingGroup-scalingGroupName"></a>
A unique identifier for the kdb scaling group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** status **   <a name="finspace-Type-KxScalingGroup-status"></a>
 The status of scaling groups.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DELETING | DELETED | DELETE_FAILED`
Required: No

 ** statusReason **   <a name="finspace-Type-KxScalingGroup-statusReason"></a>
 The error message when a failed state occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`
Required: No

## See Also
<a name="API_KxScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxScalingGroup)
