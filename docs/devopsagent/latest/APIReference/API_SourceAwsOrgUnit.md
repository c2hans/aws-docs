---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SourceAwsOrgUnit.html
---

# SourceAwsOrgUnit

Identifies an AWS Organizations organizational unit and its member accounts that are targeted for source monitoring.

## Contents
<a name="API_SourceAwsOrgUnit_Contents"></a>

 ** organizationalUnitId **   <a name="devopsagent-Type-SourceAwsOrgUnit-organizationalUnitId"></a>
The identifier of the AWS Organizations organizational unit.
Type: String
Pattern: `(r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: Yes

 ** accountIds **   <a name="devopsagent-Type-SourceAwsOrgUnit-accountIds"></a>
The AWS account IDs that belong to this organizational unit and are targeted for source monitoring.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_SourceAwsOrgUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SourceAwsOrgUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SourceAwsOrgUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SourceAwsOrgUnit)
