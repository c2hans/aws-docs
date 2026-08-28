---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanResultDetails.html
---

# CisScanResultDetails
<a name="API_CisScanResultDetails"></a>

The CIS scan result details.

## Contents
<a name="API_CisScanResultDetails_Contents"></a>

 ** scanArn **   <a name="inspector2-Type-CisScanResultDetails-scanArn"></a>
The CIS scan result details' scan ARN.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/cis-scan/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** accountId **   <a name="inspector2-Type-CisScanResultDetails-accountId"></a>
The CIS scan result details' account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** checkDescription **   <a name="inspector2-Type-CisScanResultDetails-checkDescription"></a>
The account ID that's associated with the CIS scan result details.
Type: String
Required: No

 ** checkId **   <a name="inspector2-Type-CisScanResultDetails-checkId"></a>
The CIS scan result details' check ID.
Type: String
Required: No

 ** findingArn **   <a name="inspector2-Type-CisScanResultDetails-findingArn"></a>
The CIS scan result details' finding ARN.
Type: String
Pattern: `arn:aws(-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/\d{12}/cis-finding/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** level **   <a name="inspector2-Type-CisScanResultDetails-level"></a>
The CIS scan result details' level.
Type: String
Valid Values: `LEVEL_1 | LEVEL_2`
Required: No

 ** platform **   <a name="inspector2-Type-CisScanResultDetails-platform"></a>
The CIS scan result details' platform.
Type: String
Required: No

 ** remediation **   <a name="inspector2-Type-CisScanResultDetails-remediation"></a>
The CIS scan result details' remediation.
Type: String
Required: No

 ** status **   <a name="inspector2-Type-CisScanResultDetails-status"></a>
The CIS scan result details' status.
Type: String
Valid Values: `PASSED | FAILED | SKIPPED`
Required: No

 ** statusReason **   <a name="inspector2-Type-CisScanResultDetails-statusReason"></a>
The CIS scan result details' status reason.
Type: String
Required: No

 ** targetResourceId **   <a name="inspector2-Type-CisScanResultDetails-targetResourceId"></a>
The CIS scan result details' target resource ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `.*(^arn:.*:ecr:.*:\d{12}:repository\/[a-zA-Z0-9._\/-]+(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$)|(^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}\/project-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$))|(^\/subscriptions\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\/resourcegroups\/[a-z0-9_\-\.()]+\/providers\/(microsoft\.compute\/virtualmachines\/[a-z0-9_\-]+|microsoft\.web\/sites\/[a-z0-9_\-]+|microsoft\.containerregistry\/registries\/[a-z0-9_\-]+(\/repositories\/[a-z0-9_\-\/]+\/images?\/sha256:[a-f0-9]{64})?)$).*`
Required: No

 ** title **   <a name="inspector2-Type-CisScanResultDetails-title"></a>
The CIS scan result details' title.
Type: String
Required: No

## See Also
<a name="API_CisScanResultDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisScanResultDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisScanResultDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisScanResultDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
