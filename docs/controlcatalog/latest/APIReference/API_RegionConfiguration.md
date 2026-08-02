---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_RegionConfiguration.html
---

# RegionConfiguration
<a name="API_RegionConfiguration"></a>

Returns information about the control, including the scope of the control, if enabled, and the Regions in which the control is available for deployment. For more information about scope, see [Global services](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html).

If you are applying controls through an AWS Control Tower landing zone environment, remember that the values returned in the `RegionConfiguration` API operation are not related to the governed Regions in your landing zone. For example, if you are governing Regions `A`,`B`,and `C` while the control is available in Regions `A`, `B`, C`,` and `D`, you'd see a response with `DeployableRegions` of `A`, `B`, `C`, and `D` for a control with `REGIONAL` scope, even though you may not intend to deploy the control in Region `D`, because you do not govern it through your landing zone.

## Contents
<a name="API_RegionConfiguration_Contents"></a>

 ** Scope **   <a name="controlcatalog-Type-RegionConfiguration-Scope"></a>
The coverage of the control, if deployed. Scope is an enumerated type, with value `Regional`, or `Global`. A control with Global scope is effective in all AWS Regions, regardless of the Region from which it is enabled, or to which it is deployed. A control implemented by an SCP is usually Global in scope. A control with Regional scope has operations that are restricted specifically to the Region from which it is enabled and to which it is deployed. Controls implemented by Config rules and CloudFormation hooks usually are Regional in scope. Security Hub controls usually are Regional in scope.
Type: String
Valid Values: `GLOBAL | REGIONAL`
Required: Yes

 ** DeployableRegions **   <a name="controlcatalog-Type-RegionConfiguration-DeployableRegions"></a>
Regions in which the control is available to be deployed.
Type: Array of strings
Pattern: `[a-zA-Z0-9-]{1,128}`
Required: No

## See Also
<a name="API_RegionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/RegionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/RegionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/RegionConfiguration)
