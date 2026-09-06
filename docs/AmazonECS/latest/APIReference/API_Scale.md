---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Scale.html
---

# Scale
<a name="API_Scale"></a>

A floating-point percentage of the desired number of tasks to place and keep running in the task set.

## Contents
<a name="API_Scale_Contents"></a>

 ** unit **   <a name="ECS-Type-Scale-unit"></a>
The unit of measure for the scale value.
Type: String
Valid Values: `PERCENT`
Required: No

 ** value **   <a name="ECS-Type-Scale-value"></a>
The value, specified as a percent total of a service's `desiredCount`, to scale the task set. Accepted values are numbers between 0 and 100.
Type: Double
Required: No

## See Also
<a name="API_Scale_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Scale)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Scale)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Scale)
