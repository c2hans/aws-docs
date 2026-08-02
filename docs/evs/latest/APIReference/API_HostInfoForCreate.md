---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_HostInfoForCreate.html
---

# HostInfoForCreate
<a name="API_HostInfoForCreate"></a>

An object that represents a host.

**Note**
You cannot use `dedicatedHostId` and `placementGroupId` together in the same `HostInfoForCreate`object. This results in a `ValidationException` response.

## Contents
<a name="API_HostInfoForCreate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** hostName **   <a name="evs-Type-HostInfoForCreate-hostName"></a>
The DNS hostname of the host. DNS hostnames for hosts must be unique across Amazon EVS environments and within VCF.
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** instanceType **   <a name="evs-Type-HostInfoForCreate-instanceType"></a>
The EC2 instance type that represents the host.
Type: String
Valid Values: `i4i.metal | i7i.metal-24xl`
Required: Yes

 ** keyName **   <a name="evs-Type-HostInfoForCreate-keyName"></a>
The name of the SSH key that is used to access the host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** dedicatedHostId **   <a name="evs-Type-HostInfoForCreate-dedicatedHostId"></a>
The unique ID of the Amazon EC2 Dedicated Host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `h-[a-f0-9]{8}([a-f0-9]{9})?`
Required: No

 ** placementGroupId **   <a name="evs-Type-HostInfoForCreate-placementGroupId"></a>
The unique ID of the placement group where the host is placed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `pg-[a-f0-9]{8}([a-f0-9]{9})?`
Required: No

## See Also
<a name="API_HostInfoForCreate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/HostInfoForCreate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/HostInfoForCreate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/HostInfoForCreate)
