---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ChangeLog.html
---

# ChangeLog
<a name="API_ChangeLog"></a>

 The record of a change within AWS Audit Manager. For example, this could be the status change of an assessment or the delegation of a control set.

## Contents
<a name="API_ChangeLog_Contents"></a>

 ** action **   <a name="auditmanager-Type-ChangeLog-action"></a>
 The action that was performed.
Type: String
Valid Values: `CREATE | UPDATE_METADATA | ACTIVE | INACTIVE | DELETE | UNDER_REVIEW | REVIEWED | IMPORT_EVIDENCE`
Required: No

 ** createdAt **   <a name="auditmanager-Type-ChangeLog-createdAt"></a>
 The time when the action was performed and the changelog record was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="auditmanager-Type-ChangeLog-createdBy"></a>
 The user or role that performed the action.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:iam:.*`
Required: No

 ** objectName **   <a name="auditmanager-Type-ChangeLog-objectName"></a>
 The name of the object that changed. This could be the name of an assessment, control, or control set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** objectType **   <a name="auditmanager-Type-ChangeLog-objectType"></a>
 The object that was changed, such as an assessment, control, or control set.
Type: String
Valid Values: `ASSESSMENT | CONTROL_SET | CONTROL | DELEGATION | ASSESSMENT_REPORT`
Required: No

## See Also
<a name="API_ChangeLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ChangeLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ChangeLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ChangeLog)
