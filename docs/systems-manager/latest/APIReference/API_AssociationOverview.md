---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AssociationOverview.html
---

# AssociationOverview
<a name="API_AssociationOverview"></a>

Information about the association.

## Contents
<a name="API_AssociationOverview_Contents"></a>

 ** AssociationStatusAggregatedCount **   <a name="systemsmanager-Type-AssociationOverview-AssociationStatusAggregatedCount"></a>
Returns the number of targets for the association status. For example, if you created an association with two managed nodes, and one of them was successful, this would return the count of managed nodes by status.
Type: String to integer map
Required: No

 ** DetailedStatus **   <a name="systemsmanager-Type-AssociationOverview-DetailedStatus"></a>
A detailed status of the association.
Type: String
Required: No

 ** Status **   <a name="systemsmanager-Type-AssociationOverview-Status"></a>
The status of the association. Status can be: Pending, Success, or Failed.
Type: String
Required: No

## See Also
<a name="API_AssociationOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AssociationOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AssociationOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AssociationOverview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
