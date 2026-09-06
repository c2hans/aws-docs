---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Patch.html
---

# Patch
<a name="API_Patch"></a>

Represents metadata about a patch.

## Contents
<a name="API_Patch_Contents"></a>

 ** AdvisoryIds **   <a name="systemsmanager-Type-Patch-AdvisoryIds"></a>
The Advisory ID of the patch. For example, `RHSA-2020:3779`. Applies to Linux-based managed nodes only.
Type: Array of strings
Required: No

 ** Arch **   <a name="systemsmanager-Type-Patch-Arch"></a>
The architecture of the patch. For example, in `example-pkg-0.710.10-2.7.abcd.x86_64`, the architecture is indicated by `x86_64`. Applies to Linux-based managed nodes only.
Type: String
Required: No

 ** BugzillaIds **   <a name="systemsmanager-Type-Patch-BugzillaIds"></a>
The Bugzilla ID of the patch. For example, `1600646`. Applies to Linux-based managed nodes only.
Type: Array of strings
Required: No

 ** Classification **   <a name="systemsmanager-Type-Patch-Classification"></a>
The classification of the patch. For example, `SecurityUpdates`, `Updates`, or `CriticalUpdates`.
Type: String
Required: No

 ** ContentUrl **   <a name="systemsmanager-Type-Patch-ContentUrl"></a>
The URL where more information can be obtained about the patch.
Type: String
Required: No

 ** CVEIds **   <a name="systemsmanager-Type-Patch-CVEIds"></a>
The Common Vulnerabilities and Exposures (CVE) ID of the patch. For example, `CVE-2011-3192`. Applies to Linux-based managed nodes only.
Type: Array of strings
Required: No

 ** Description **   <a name="systemsmanager-Type-Patch-Description"></a>
The description of the patch.
Type: String
Required: No

 ** Epoch **   <a name="systemsmanager-Type-Patch-Epoch"></a>
The epoch of the patch. For example in `pkg-example-EE-20180914-2.2.amzn1.noarch`, the epoch value is `20180914-2`. Applies to Linux-based managed nodes only.
Type: Integer
Required: No

 ** Id **   <a name="systemsmanager-Type-Patch-Id"></a>
The ID of the patch. Applies to Windows patches only.
This ID isn't the same as the Microsoft Knowledge Base ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** KbNumber **   <a name="systemsmanager-Type-Patch-KbNumber"></a>
The Microsoft Knowledge Base ID of the patch. Applies to Windows patches only.
Type: String
Required: No

 ** Language **   <a name="systemsmanager-Type-Patch-Language"></a>
The language of the patch if it's language-specific.
Type: String
Required: No

 ** MsrcNumber **   <a name="systemsmanager-Type-Patch-MsrcNumber"></a>
The ID of the Microsoft Security Response Center (MSRC) bulletin the patch is related to. For example, `MS14-045`. Applies to Windows patches only.
Type: String
Required: No

 ** MsrcSeverity **   <a name="systemsmanager-Type-Patch-MsrcSeverity"></a>
The severity of the patch, such as `Critical`, `Important`, or `Moderate`. Applies to Windows patches only.
Type: String
Required: No

 ** Name **   <a name="systemsmanager-Type-Patch-Name"></a>
The name of the patch. Applies to Linux-based managed nodes only.
Type: String
Required: No

 ** Product **   <a name="systemsmanager-Type-Patch-Product"></a>
The specific product the patch is applicable for. For example, `WindowsServer2016` or `AmazonLinux2018.03`.
Type: String
Required: No

 ** ProductFamily **   <a name="systemsmanager-Type-Patch-ProductFamily"></a>
The product family the patch is applicable for. For example, `Windows` or `Amazon Linux 2`.
Type: String
Required: No

 ** Release **   <a name="systemsmanager-Type-Patch-Release"></a>
The particular release of a patch. For example, in `pkg-example-EE-20180914-2.2.amzn1.noarch`, the release is `2.amaz1`. Applies to Linux-based managed nodes only.
Type: String
Required: No

 ** ReleaseDate **   <a name="systemsmanager-Type-Patch-ReleaseDate"></a>
The date the patch was released.
Type: Timestamp
Required: No

 ** Repository **   <a name="systemsmanager-Type-Patch-Repository"></a>
The source patch repository for the operating system and version, such as `trusty-security` for Ubuntu Server 14.04 LTE and `focal-security` for Ubuntu Server 20.04 LTE. Applies to Linux-based managed nodes only.
Type: String
Required: No

 ** Severity **   <a name="systemsmanager-Type-Patch-Severity"></a>
The severity level of the patch. For example, `CRITICAL` or `MODERATE`.
Type: String
Required: No

 ** Title **   <a name="systemsmanager-Type-Patch-Title"></a>
The title of the patch.
Type: String
Required: No

 ** Vendor **   <a name="systemsmanager-Type-Patch-Vendor"></a>
The name of the vendor providing the patch.
Type: String
Required: No

 ** Version **   <a name="systemsmanager-Type-Patch-Version"></a>
The version number of the patch. For example, in `example-pkg-1.710.10-2.7.abcd.x86_64`, the version number is indicated by `-1`. Applies to Linux-based managed nodes only.
Type: String
Required: No

## See Also
<a name="API_Patch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Patch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Patch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Patch)
