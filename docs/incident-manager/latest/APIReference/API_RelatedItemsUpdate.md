---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_RelatedItemsUpdate.html
---

# RelatedItemsUpdate
<a name="API_RelatedItemsUpdate"></a>

Details about the related item you're adding.

## Contents
<a name="API_RelatedItemsUpdate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** itemToAdd **   <a name="IncidentManager-Type-RelatedItemsUpdate-itemToAdd"></a>
Details about the related item you're adding.
Type: [RelatedItem](API_RelatedItem.md) object
Required: No

 ** itemToRemove **   <a name="IncidentManager-Type-RelatedItemsUpdate-itemToRemove"></a>
Details about the related item you're deleting.
Type: [ItemIdentifier](API_ItemIdentifier.md) object
Required: No

## See Also
<a name="API_RelatedItemsUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/RelatedItemsUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/RelatedItemsUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/RelatedItemsUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
