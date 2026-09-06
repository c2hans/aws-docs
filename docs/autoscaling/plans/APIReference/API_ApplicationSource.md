---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ApplicationSource.html
---

# ApplicationSource
<a name="API_ApplicationSource"></a>

Represents an application source.

## Contents
<a name="API_ApplicationSource_Contents"></a>

 ** CloudFormationStackARN **   <a name="autoscaling-Type-ApplicationSource-CloudFormationStackARN"></a>
The Amazon Resource Name (ARN) of a CloudFormation stack.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** TagFilters **   <a name="autoscaling-Type-ApplicationSource-TagFilters"></a>
A set of tags (up to 50).
Type: Array of [TagFilter](API_TagFilter.md) objects
Required: No

## See Also
<a name="API_ApplicationSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/ApplicationSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/ApplicationSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/ApplicationSource)
