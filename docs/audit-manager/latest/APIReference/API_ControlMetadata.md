---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ControlMetadata.html
---

# ControlMetadata
<a name="API_ControlMetadata"></a>

 The metadata that's associated with the standard control or custom control.

## Contents
<a name="API_ControlMetadata_Contents"></a>

 ** arn **   <a name="auditmanager-Type-ControlMetadata-arn"></a>
 The Amazon Resource Name (ARN) of the control.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:.*:auditmanager:.*`
Required: No

 ** controlSources **   <a name="auditmanager-Type-ControlMetadata-controlSources"></a>
 The data source that determines where Audit Manager collects evidence from for the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z_0-9-\s.,]+$`
Required: No

 ** createdAt **   <a name="auditmanager-Type-ControlMetadata-createdAt"></a>
 The time when the control was created.
Type: Timestamp
Required: No

 ** id **   <a name="auditmanager-Type-ControlMetadata-id"></a>
 The unique identifier for the control.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** lastUpdatedAt **   <a name="auditmanager-Type-ControlMetadata-lastUpdatedAt"></a>
 The time when the control was most recently updated.
Type: Timestamp
Required: No

 ** name **   <a name="auditmanager-Type-ControlMetadata-name"></a>
 The name of the control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\]*$`
Required: No

## See Also
<a name="API_ControlMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ControlMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ControlMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ControlMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
