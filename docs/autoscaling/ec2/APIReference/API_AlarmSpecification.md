---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AlarmSpecification.html
---

# AlarmSpecification
<a name="API_AlarmSpecification"></a>

Specifies the CloudWatch alarm specification to use in an instance refresh.

## Contents
<a name="API_AlarmSpecification_Contents"></a>

 ** Alarms.member.N **
The names of one or more CloudWatch alarms to monitor for the instance refresh. You can specify up to 10 alarms.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_AlarmSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/AlarmSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/AlarmSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/AlarmSpecification)
