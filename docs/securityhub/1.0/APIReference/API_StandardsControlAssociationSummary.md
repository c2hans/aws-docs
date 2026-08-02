---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StandardsControlAssociationSummary.html
---

# StandardsControlAssociationSummary
<a name="API_StandardsControlAssociationSummary"></a>

 An array that provides the enablement status and other details for each control that applies to each enabled standard.

## Contents
<a name="API_StandardsControlAssociationSummary_Contents"></a>

 ** AssociationStatus **   <a name="securityhub-Type-StandardsControlAssociationSummary-AssociationStatus"></a>
 The enablement status of a control in a specific standard.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** SecurityControlArn **   <a name="securityhub-Type-StandardsControlAssociationSummary-SecurityControlArn"></a>
 The ARN of a control, such as `arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1`. This parameter doesn't mention a specific standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** SecurityControlId **   <a name="securityhub-Type-StandardsControlAssociationSummary-SecurityControlId"></a>
 A unique standard-agnostic identifier for a control. Values for this field typically consist of an AWS service and a number, such as APIGateway.5. This field doesn't reference a specific standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** StandardsArn **   <a name="securityhub-Type-StandardsControlAssociationSummary-StandardsArn"></a>
 The Amazon Resource Name (ARN) of a standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** RelatedRequirements **   <a name="securityhub-Type-StandardsControlAssociationSummary-RelatedRequirements"></a>
 The requirement that underlies this control in the compliance framework related to the standard.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** StandardsControlDescription **   <a name="securityhub-Type-StandardsControlAssociationSummary-StandardsControlDescription"></a>
 The description of a control. This typically summarizes how Security Hub CSPM evaluates the control and the conditions under which it produces a failed finding. The parameter may reference a specific standard.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StandardsControlTitle **   <a name="securityhub-Type-StandardsControlAssociationSummary-StandardsControlTitle"></a>
 The title of a control.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-StandardsControlAssociationSummary-UpdatedAt"></a>
The last time that a control's enablement status in a specified standard was updated.
Type: Timestamp
Required: No

 ** UpdatedReason **   <a name="securityhub-Type-StandardsControlAssociationSummary-UpdatedReason"></a>
The reason for updating a control's enablement status in a specified standard.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_StandardsControlAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StandardsControlAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StandardsControlAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StandardsControlAssociationSummary)
