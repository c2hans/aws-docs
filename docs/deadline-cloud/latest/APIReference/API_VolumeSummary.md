---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_VolumeSummary.html
---

# VolumeSummary
<a name="API_VolumeSummary"></a>

The summary of a persistent volume.

## Contents
<a name="API_VolumeSummary_Contents"></a>

 ** availabilityZoneId **   <a name="deadlinecloud-Type-VolumeSummary-availabilityZoneId"></a>
The Availability Zone ID of the volume.
Type: String
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-VolumeSummary-farmId"></a>
The farm ID of the farm that contains the fleet.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** fleetId **   <a name="deadlinecloud-Type-VolumeSummary-fleetId"></a>
The fleet ID of the fleet that contains the volume.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** sizeGiB **   <a name="deadlinecloud-Type-VolumeSummary-sizeGiB"></a>
The volume size in GiB.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65536.
Required: Yes

 ** state **   <a name="deadlinecloud-Type-VolumeSummary-state"></a>
The state of the volume.
Type: String
Valid Values: `PENDING_CREATION | PENDING_ATTACHMENT | IN_USE | AVAILABLE | PENDING_DELETION`
Required: Yes

 ** volumeId **   <a name="deadlinecloud-Type-VolumeSummary-volumeId"></a>
The volume ID.
Type: String
Pattern: `volume-[0-9a-f]{32}`
Required: Yes

 ** attachedWorkerId **   <a name="deadlinecloud-Type-VolumeSummary-attachedWorkerId"></a>
The worker ID of the worker the volume is attached to.
Type: String
Pattern: `worker-[0-9a-f]{32}`
Required: No

## See Also
<a name="API_VolumeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/VolumeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/VolumeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/VolumeSummary)
