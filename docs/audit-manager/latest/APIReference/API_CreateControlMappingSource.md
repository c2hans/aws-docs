---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateControlMappingSource.html
---

# CreateControlMappingSource
<a name="API_CreateControlMappingSource"></a>

The mapping attributes that determine the evidence source for a given control, along with related parameters and metadata. This doesn't contain `mappingID`.

## Contents
<a name="API_CreateControlMappingSource_Contents"></a>

 ** sourceDescription **   <a name="auditmanager-Type-CreateControlMappingSource-sourceDescription"></a>
 The description of the data source that determines where Audit Manager collects evidence from for the control.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** sourceFrequency **   <a name="auditmanager-Type-CreateControlMappingSource-sourceFrequency"></a>
Specifies how often evidence is collected from the control mapping source.
Type: String
Valid Values: `DAILY | WEEKLY | MONTHLY`
Required: No

 ** sourceKeyword **   <a name="auditmanager-Type-CreateControlMappingSource-sourceKeyword"></a>
A keyword that relates to the control data source.
For manual evidence, this keyword indicates if the manual evidence is a file or text.
For automated evidence, this keyword identifies a specific CloudTrail event, AWS Config rule, Security Hub CSPM control, or AWS API name.
 To learn more about the supported keywords that you can use when mapping a control data source, see the following pages in the * AWS Audit Manager User Guide*:
+  [AWS Config rules supported by AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html)
+  [AWS Security Hub CSPM controls supported by AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-ash.html)
+  [API calls supported by AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-api.html)
+  [AWS CloudTrail event names supported by AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-cloudtrail.html)
Type: [SourceKeyword](API_SourceKeyword.md) object
Required: No

 ** sourceName **   <a name="auditmanager-Type-CreateControlMappingSource-sourceName"></a>
 The name of the control mapping data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** sourceSetUpOption **   <a name="auditmanager-Type-CreateControlMappingSource-sourceSetUpOption"></a>
The setup option for the data source. This option reflects if the evidence collection method is automated or manual. If you don’t provide a value for `sourceSetUpOption`, AWS Audit Manager automatically infers and populates the correct value based on the `sourceType` that you specify.
Type: String
Valid Values: `System_Controls_Mapping | Procedural_Controls_Mapping`
Required: No

 ** sourceType **   <a name="auditmanager-Type-CreateControlMappingSource-sourceType"></a>
 Specifies which type of data source is used to collect evidence.
+ The source can be an individual data source type, such as `AWS_Cloudtrail`, `AWS_Config`, `AWS_Security_Hub`, `AWS_API_Call`, or `MANUAL`.
+ The source can also be a managed grouping of data sources, such as a `Core_Control` or a `Common_Control`.
Type: String
Valid Values: `AWS_Cloudtrail | AWS_Config | AWS_Security_Hub | AWS_API_Call | MANUAL | Common_Control | Core_Control`
Required: No

 ** troubleshootingText **   <a name="auditmanager-Type-CreateControlMappingSource-troubleshootingText"></a>
 The instructions for troubleshooting the control.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^[\w\W\s\S]*$`
Required: No

## See Also
<a name="API_CreateControlMappingSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/CreateControlMappingSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/CreateControlMappingSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/CreateControlMappingSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
