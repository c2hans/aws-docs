---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ControlSet.html
---

# ControlSet
<a name="API_ControlSet"></a>

 A set of controls in AWS Audit Manager.

## Contents
<a name="API_ControlSet_Contents"></a>

 ** controls **   <a name="auditmanager-Type-ControlSet-controls"></a>
 The list of controls within the control set.
Type: Array of [Control](API_Control.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** id **   <a name="auditmanager-Type-ControlSet-id"></a>
 The identifier of the control set in the assessment. This is the control set name in a plain string format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** name **   <a name="auditmanager-Type-ControlSet-name"></a>
 The name of the control set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\\_]*$`
Required: No

## See Also
<a name="API_ControlSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ControlSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ControlSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ControlSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
