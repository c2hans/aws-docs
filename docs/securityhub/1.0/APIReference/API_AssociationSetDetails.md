---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AssociationSetDetails.html
---

# AssociationSetDetails
<a name="API_AssociationSetDetails"></a>

 The associations between a route table and one or more subnets or a gateway.

## Contents
<a name="API_AssociationSetDetails_Contents"></a>

 ** AssociationState **   <a name="securityhub-Type-AssociationSetDetails-AssociationState"></a>
 The state of the association between a route table and a subnet or gateway.
Type: [AssociationStateDetails](API_AssociationStateDetails.md) object
Required: No

 ** GatewayId **   <a name="securityhub-Type-AssociationSetDetails-GatewayId"></a>
 The ID of the internet gateway or virtual private gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Main **   <a name="securityhub-Type-AssociationSetDetails-Main"></a>
 Indicates whether this is the main route table.
Type: Boolean
Required: No

 ** RouteTableAssociationId **   <a name="securityhub-Type-AssociationSetDetails-RouteTableAssociationId"></a>
 The ID of the association.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RouteTableId **   <a name="securityhub-Type-AssociationSetDetails-RouteTableId"></a>
 The ID of the route table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SubnetId **   <a name="securityhub-Type-AssociationSetDetails-SubnetId"></a>
 The ID of the subnet. A subnet ID is not returned for an implicit association.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AssociationSetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AssociationSetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AssociationSetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AssociationSetDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
