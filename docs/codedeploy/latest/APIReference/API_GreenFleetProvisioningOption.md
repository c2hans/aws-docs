---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GreenFleetProvisioningOption.html
---

# GreenFleetProvisioningOption
<a name="API_GreenFleetProvisioningOption"></a>

Information about the instances that belong to the replacement environment in a blue/green deployment.

## Contents
<a name="API_GreenFleetProvisioningOption_Contents"></a>

 ** action **   <a name="CodeDeploy-Type-GreenFleetProvisioningOption-action"></a>
The method used to add instances to a replacement environment.
+  `DISCOVER_EXISTING`: Use instances that already exist or will be created manually.
+  `COPY_AUTO_SCALING_GROUP`: Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.
Type: String
Valid Values: `DISCOVER_EXISTING | COPY_AUTO_SCALING_GROUP`
Required: No

## See Also
<a name="API_GreenFleetProvisioningOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GreenFleetProvisioningOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GreenFleetProvisioningOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GreenFleetProvisioningOption)
