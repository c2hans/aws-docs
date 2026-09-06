---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageUsageResourceTypeOptionRequest.html
---

# ImageUsageResourceTypeOptionRequest
<a name="API_ImageUsageResourceTypeOptionRequest"></a>

The options that affect the scope of the report.

## Contents
<a name="API_ImageUsageResourceTypeOptionRequest_Contents"></a>

 ** OptionName **
The name of the option.
Valid value: `version-depth` - The number of launch template versions to check.
Type: String
Required: No

 ** OptionValue.N **
A value for the specified option.
Valid values: Integers between `1` and `10000`
Default: `20`
Type: Array of strings
Required: No

## See Also
<a name="API_ImageUsageResourceTypeOptionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageUsageResourceTypeOptionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageUsageResourceTypeOptionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageUsageResourceTypeOptionRequest)
