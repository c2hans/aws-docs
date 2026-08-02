---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResourceTypeOption.html
---

# ResourceTypeOption
<a name="API_ResourceTypeOption"></a>

The options that affect the scope of the response.

## Contents
<a name="API_ResourceTypeOption_Contents"></a>

 ** OptionName **
The name of the option.
+ For `ec2:Instance`:

  Specify `state-name` - The current state of the EC2 instance.
+ For `ec2:LaunchTemplate`:

  Specify `version-depth` - The number of launch template versions to check, starting from the most recent version.
Type: String
Valid Values: `state-name | version-depth`
Required: No

 ** OptionValue.N **
A value for the specified option.
+ For `state-name`:
  + Valid values: `pending` \| `running` \| `shutting-down` \| `terminated` \| `stopping` \| `stopped`
  + Default: All states
+ For `version-depth`:
  + Valid values: Integers between `1` and `10000`
  + Default: `10`
Type: Array of strings
Required: No

## See Also
<a name="API_ResourceTypeOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ResourceTypeOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ResourceTypeOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ResourceTypeOption)
