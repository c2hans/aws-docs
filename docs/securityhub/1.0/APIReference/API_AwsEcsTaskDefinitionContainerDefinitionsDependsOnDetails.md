---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails"></a>

A dependency that is defined for container startup and shutdown.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails_Contents"></a>

 ** Condition **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails-Condition"></a>
The dependency condition of the dependent container. Indicates the required status of the dependent container before the current container can start. Valid values are as follows:
+  `COMPLETE`
+  `HEALTHY`
+  `SUCCESS`
+  `START`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ContainerName **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails-ContainerName"></a>
The name of the dependent container.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails)
