---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_FailedOrganizationalUnit.html
---

# FailedOrganizationalUnit
<a name="API_FailedOrganizationalUnit"></a>

**Important**
This is not available during the preview release.

An organizational unit that was requested in an Organizational Report's filters but could not be expanded into its member accounts. A failed OU means the report is missing the accounts it contained.

## Contents
<a name="API_FailedOrganizationalUnit_Contents"></a>

 ** organizationalUnitId **   <a name="wellarchitected-Type-FailedOrganizationalUnit-organizationalUnitId"></a>
The AWS Organizations OU ID that could not be expanded.
Type: String
Pattern: `ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`
Required: Yes

 ** reason **   <a name="wellarchitected-Type-FailedOrganizationalUnit-reason"></a>
A human-readable explanation of why the organizational unit could not be expanded.
Type: String
Required: Yes

## See Also
<a name="API_FailedOrganizationalUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/FailedOrganizationalUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/FailedOrganizationalUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/FailedOrganizationalUnit)
