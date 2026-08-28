---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WeightPerAxleGroup.html
---

# WeightPerAxleGroup
<a name="API_WeightPerAxleGroup"></a>

Specifies the total weight for different axle group configurations. Used in regions where regulations set different weight limits based on axle group types.

 **Unit**: `kilograms`

## Contents
<a name="API_WeightPerAxleGroup_Contents"></a>

 ** Quad **   <a name="location-Type-WeightPerAxleGroup-Quad"></a>
Total weight in kilograms for quad (four adjacent) axle configurations.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Quint **   <a name="location-Type-WeightPerAxleGroup-Quint"></a>
Total weight in kilograms for quint (five adjacent) axle configurations.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Single **   <a name="location-Type-WeightPerAxleGroup-Single"></a>
Total weight in kilograms for single axle configurations.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Tandem **   <a name="location-Type-WeightPerAxleGroup-Tandem"></a>
Total weight in kilograms for tandem (two adjacent) axle configurations.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Triple **   <a name="location-Type-WeightPerAxleGroup-Triple"></a>
Total weight in kilograms for triple (three adjacent) axle configurations.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_WeightPerAxleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WeightPerAxleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WeightPerAxleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WeightPerAxleGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
