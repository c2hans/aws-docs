---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AssociationStatus.html
---

# AssociationStatus
<a name="API_AssociationStatus"></a>

Describes an association status.

## Contents
<a name="API_AssociationStatus_Contents"></a>

 ** Date **   <a name="systemsmanager-Type-AssociationStatus-Date"></a>
The date when the status changed.
Type: Timestamp
Required: Yes

 ** Message **   <a name="systemsmanager-Type-AssociationStatus-Message"></a>
The reason for the status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** Name **   <a name="systemsmanager-Type-AssociationStatus-Name"></a>
The status.
Type: String
Valid Values: `Pending | Success | Failed`
Required: Yes

 ** AdditionalInfo **   <a name="systemsmanager-Type-AssociationStatus-AdditionalInfo"></a>
A user-defined string.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_AssociationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AssociationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AssociationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AssociationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
