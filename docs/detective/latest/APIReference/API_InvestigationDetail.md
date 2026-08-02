---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_InvestigationDetail.html
---

# InvestigationDetail
<a name="API_InvestigationDetail"></a>

Details about the investigation related to a potential security event identified by Detective.

## Contents
<a name="API_InvestigationDetail_Contents"></a>

 ** CreatedTime **   <a name="detective-Type-InvestigationDetail-CreatedTime"></a>
The time stamp of the creation time of the investigation report. The value is an UTC ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: No

 ** EntityArn **   <a name="detective-Type-InvestigationDetail-EntityArn"></a>
The unique Amazon Resource Name (ARN) of the IAM user and IAM role.
Type: String
Pattern: `^arn:.*`
Required: No

 ** EntityType **   <a name="detective-Type-InvestigationDetail-EntityType"></a>
Type of entity. For example, AWS accounts, such as IAM user and role.
Type: String
Valid Values: `IAM_ROLE | IAM_USER`
Required: No

 ** InvestigationId **   <a name="detective-Type-InvestigationDetail-InvestigationId"></a>
The investigation ID of the investigation report.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^[0-9]+$`
Required: No

 ** Severity **   <a name="detective-Type-InvestigationDetail-Severity"></a>
Severity based on the likelihood and impact of the indicators of compromise discovered in the investigation.
Type: String
Valid Values: `INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** State **   <a name="detective-Type-InvestigationDetail-State"></a>
The current state of the investigation. An archived investigation indicates you have completed reviewing the investigation.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: No

 ** Status **   <a name="detective-Type-InvestigationDetail-Status"></a>
Status based on the completion status of the investigation.
Type: String
Valid Values: `RUNNING | FAILED | SUCCESSFUL`
Required: No

## See Also
<a name="API_InvestigationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/InvestigationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/InvestigationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/InvestigationDetail)
