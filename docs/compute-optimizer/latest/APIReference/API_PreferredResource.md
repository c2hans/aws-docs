---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_PreferredResource.html
---

# PreferredResource
<a name="API_PreferredResource"></a>

 The preference to control which resource type values are considered when generating rightsizing recommendations. You can specify this preference as a combination of include and exclude lists. You must specify either an `includeList` or `excludeList`. If the preference is an empty set of resource type values, an error occurs. For more information, see [ Rightsizing recommendation preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences.html) in the * AWS Compute Optimizer User Guide*.

**Note**
This preference is only available for the Amazon EC2 instance and Auto Scaling group resource types.
Compute Optimizer only supports the customization of `Ec2InstanceTypes`.

## Contents
<a name="API_PreferredResource_Contents"></a>

 ** excludeList **   <a name="computeoptimizer-Type-PreferredResource-excludeList"></a>
 The preferred resource type values to exclude from the recommendation candidates. If this isn’t specified, all supported resources are included by default. You can specify up to 1000 values in this list.
Type: Array of strings
Required: No

 ** includeList **   <a name="computeoptimizer-Type-PreferredResource-includeList"></a>
 The preferred resource type values to include in the recommendation candidates. You can specify the exact resource type value, such as m5.large, or use wild card expressions, such as m5. If this isn’t specified, all supported resources are included by default. You can specify up to 1000 values in this list.
Type: Array of strings
Required: No

 ** name **   <a name="computeoptimizer-Type-PreferredResource-name"></a>
 The type of preferred resource to customize.
Compute Optimizer only supports the customization of `Ec2InstanceTypes`.
Type: String
Valid Values: `Ec2InstanceTypes`
Required: No

## See Also
<a name="API_PreferredResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/PreferredResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/PreferredResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/PreferredResource)
