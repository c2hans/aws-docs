---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_RelatedItem.html
---

# RelatedItem
<a name="API_RelatedItem"></a>

Resources that responders use to triage and mitigate the incident.

## Contents
<a name="API_RelatedItem_Contents"></a>

 ** identifier **   <a name="IncidentManager-Type-RelatedItem-identifier"></a>
Details about the related item.
Type: [ItemIdentifier](API_ItemIdentifier.md) object
Required: Yes

 ** generatedId **   <a name="IncidentManager-Type-RelatedItem-generatedId"></a>
A unique ID for a `RelatedItem`.
Don't specify this parameter when you add a `RelatedItem` by using the [UpdateRelatedItems](API_UpdateRelatedItems.md) API action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `related-item/(ANALYSIS|INCIDENT|METRIC|PARENT|ATTACHMENT|OTHER|AUTOMATION|INVOLVED_RESOURCE|TASK)/([0-9]|[A-F]){32}`
Required: No

 ** title **   <a name="IncidentManager-Type-RelatedItem-title"></a>
The title of the related item.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

## See Also
<a name="API_RelatedItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/RelatedItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/RelatedItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/RelatedItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
