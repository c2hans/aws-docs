---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxVolume.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxVolume
<a name="API_KxVolume"></a>

 The structure that contains the metadata of the volume.

## Contents
<a name="API_KxVolume_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** availabilityZoneIds **   <a name="finspace-Type-KxVolume-availabilityZoneIds"></a>
The identifier of the availability zones.
Type: Array of strings
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** azMode **   <a name="finspace-Type-KxVolume-azMode"></a>
The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.
Type: String
Valid Values: `SINGLE | MULTI`
Required: No

 ** createdTimestamp **   <a name="finspace-Type-KxVolume-createdTimestamp"></a>
 The timestamp at which the volume was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** description **   <a name="finspace-Type-KxVolume-description"></a>
 A description of the volume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** lastModifiedTimestamp **   <a name="finspace-Type-KxVolume-lastModifiedTimestamp"></a>
The last time that the volume was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** status **   <a name="finspace-Type-KxVolume-status"></a>
The status of volume.
+ CREATING – The volume creation is in progress.
+ CREATE\_FAILED – The volume creation has failed.
+ ACTIVE – The volume is active.
+ UPDATING – The volume is in the process of being updated.
+ UPDATE\_FAILED – The update action failed.
+ UPDATED – The volume is successfully updated.
+ DELETING – The volume is in the process of being deleted.
+ DELETE\_FAILED – The system failed to delete the volume.
+ DELETED – The volume is successfully deleted.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | UPDATING | UPDATED | UPDATE_FAILED | DELETING | DELETED | DELETE_FAILED`
Required: No

 ** statusReason **   <a name="finspace-Type-KxVolume-statusReason"></a>
The error message when a failed state occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`
Required: No

 ** volumeName **   <a name="finspace-Type-KxVolume-volumeName"></a>
A unique identifier for the volume.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** volumeType **   <a name="finspace-Type-KxVolume-volumeType"></a>
 The type of file system volume. Currently, FinSpace only supports `NAS_1` volume type.
Type: String
Valid Values: `NAS_1`
Required: No

## See Also
<a name="API_KxVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxVolume)
