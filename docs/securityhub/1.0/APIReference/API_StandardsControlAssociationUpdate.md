---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StandardsControlAssociationUpdate.html
---

# StandardsControlAssociationUpdate
<a name="API_StandardsControlAssociationUpdate"></a>

An array of requested updates to the enablement status of controls in specified standards. The objects in the array include a security control ID, the Amazon Resource Name (ARN) of the standard, the requested enablement status, and the reason for updating the enablement status.

## Contents
<a name="API_StandardsControlAssociationUpdate_Contents"></a>

 ** AssociationStatus **   <a name="securityhub-Type-StandardsControlAssociationUpdate-AssociationStatus"></a>
The desired enablement status of the control in the standard.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** SecurityControlId **   <a name="securityhub-Type-StandardsControlAssociationUpdate-SecurityControlId"></a>
The unique identifier for the security control whose enablement status you want to update.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** StandardsArn **   <a name="securityhub-Type-StandardsControlAssociationUpdate-StandardsArn"></a>
The Amazon Resource Name (ARN) of the standard in which you want to update the control's enablement status.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** UpdatedReason **   <a name="securityhub-Type-StandardsControlAssociationUpdate-UpdatedReason"></a>
The reason for updating the control's enablement status in the standard.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_StandardsControlAssociationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StandardsControlAssociationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StandardsControlAssociationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StandardsControlAssociationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
