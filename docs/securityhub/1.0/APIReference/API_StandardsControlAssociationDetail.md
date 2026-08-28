---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StandardsControlAssociationDetail.html
---

# StandardsControlAssociationDetail
<a name="API_StandardsControlAssociationDetail"></a>

 Provides details about a control's enablement status in a specified standard.

## Contents
<a name="API_StandardsControlAssociationDetail_Contents"></a>

 ** AssociationStatus **   <a name="securityhub-Type-StandardsControlAssociationDetail-AssociationStatus"></a>
 Specifies whether a control is enabled or disabled in a specified standard.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** SecurityControlArn **   <a name="securityhub-Type-StandardsControlAssociationDetail-SecurityControlArn"></a>
 The ARN of a security control across standards, such as `arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1`. This parameter doesn't mention a specific standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** SecurityControlId **   <a name="securityhub-Type-StandardsControlAssociationDetail-SecurityControlId"></a>
 The unique identifier of a security control across standards. Values for this field typically consist of an AWS service name and a number, such as APIGateway.3.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** StandardsArn **   <a name="securityhub-Type-StandardsControlAssociationDetail-StandardsArn"></a>
 The Amazon Resource Name (ARN) of a security standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** RelatedRequirements **   <a name="securityhub-Type-StandardsControlAssociationDetail-RelatedRequirements"></a>
 The requirement that underlies a control in the compliance framework related to the standard.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** StandardsControlArns **   <a name="securityhub-Type-StandardsControlAssociationDetail-StandardsControlArns"></a>
 Provides the input parameter that Security Hub CSPM uses to call the [UpdateStandardsControl](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html) API. This API can be used to enable or disable a control in a specified standard.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** StandardsControlDescription **   <a name="securityhub-Type-StandardsControlAssociationDetail-StandardsControlDescription"></a>
 The description of a control. This typically summarizes how Security Hub CSPM evaluates the control and the conditions under which it produces a failed finding. This parameter may reference a specific standard.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StandardsControlTitle **   <a name="securityhub-Type-StandardsControlAssociationDetail-StandardsControlTitle"></a>
 The title of a control. This field may reference a specific standard.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-StandardsControlAssociationDetail-UpdatedAt"></a>
 The time at which the enablement status of the control in the specified standard was last updated.
Type: Timestamp
Required: No

 ** UpdatedReason **   <a name="securityhub-Type-StandardsControlAssociationDetail-UpdatedReason"></a>
 The reason for updating the enablement status of a control in a specified standard.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_StandardsControlAssociationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StandardsControlAssociationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StandardsControlAssociationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StandardsControlAssociationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
