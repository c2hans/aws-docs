---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Template.html
---

# Template
<a name="API_Template"></a>

An Active Directory compatible certificate template. Connectors issue certificates against these templates based on the requestor's Active Directory group membership.

## Contents
<a name="API_Template_Contents"></a>

 ** Arn **   <a name="PcaConnectorAd-Type-Template-Arn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/template\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** ConnectorArn **   <a name="PcaConnectorAd-Type-Template-ConnectorArn"></a>
 The Amazon Resource Name (ARN) that was returned when you called [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CreatedAt **   <a name="PcaConnectorAd-Type-Template-CreatedAt"></a>
The date and time that the template was created.
Type: Timestamp
Required: No

 ** Definition **   <a name="PcaConnectorAd-Type-Template-Definition"></a>
Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.
Type: [TemplateDefinition](API_TemplateDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Name **   <a name="PcaConnectorAd-Type-Template-Name"></a>
Name of the templates. Template names must be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^\s+$)((?![\x5c'\x2b,;<=>#\x22])([\x20-\x7E]))+`
Required: No

 ** ObjectIdentifier **   <a name="PcaConnectorAd-Type-Template-ObjectIdentifier"></a>
Object identifier of a template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([0-2])\.([0-9]|([0-3][0-9]))(\.([0-9]+)){0,126}`
Required: No

 ** PolicySchema **   <a name="PcaConnectorAd-Type-Template-PolicySchema"></a>
The template schema version. Template schema versions can be v2, v3, or v4. The template configuration options change based on the template schema version.
Type: Integer
Required: No

 ** Revision **   <a name="PcaConnectorAd-Type-Template-Revision"></a>
The version of the template. Template updates will increment the minor revision. Re-enrolling all certificate holders will increment the major revision.
Type: [TemplateRevision](API_TemplateRevision.md) object
Required: No

 ** Status **   <a name="PcaConnectorAd-Type-Template-Status"></a>
Status of the template. Status can be creating, active, deleting, or failed.
Type: String
Valid Values: `ACTIVE | DELETING`
Required: No

 ** UpdatedAt **   <a name="PcaConnectorAd-Type-Template-UpdatedAt"></a>
The date and time that the template was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Template_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/Template)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/Template)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/Template)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
