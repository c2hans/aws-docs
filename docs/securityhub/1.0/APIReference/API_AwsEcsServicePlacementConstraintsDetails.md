---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServicePlacementConstraintsDetails.html
---

# AwsEcsServicePlacementConstraintsDetails
<a name="API_AwsEcsServicePlacementConstraintsDetails"></a>

A placement constraint for the tasks in the service.

## Contents
<a name="API_AwsEcsServicePlacementConstraintsDetails_Contents"></a>

 ** Expression **   <a name="securityhub-Type-AwsEcsServicePlacementConstraintsDetails-Expression"></a>
A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is `distinctInstance`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsEcsServicePlacementConstraintsDetails-Type"></a>
The type of constraint. Use `distinctInstance` to run each task in a particular group on a different container instance. Use `memberOf` to restrict the selection to a group of valid candidates.
Valid values: `distinctInstance` \| `memberOf`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsServicePlacementConstraintsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServicePlacementConstraintsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServicePlacementConstraintsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServicePlacementConstraintsDetails)
