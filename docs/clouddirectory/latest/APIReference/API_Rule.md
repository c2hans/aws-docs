---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_Rule.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# Rule
<a name="API_Rule"></a>

Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

## Contents
<a name="API_Rule_Contents"></a>

 ** Parameters **   <a name="amazoncds-Type-Rule-Parameters"></a>
The minimum and maximum parameters that are associated with the rule.
Type: String to string map
Required: No

 ** Type **   <a name="amazoncds-Type-Rule-Type"></a>
The type of attribute validation rule.
Type: String
Valid Values: `BINARY_LENGTH | NUMBER_COMPARISON | STRING_FROM_SET | STRING_LENGTH`
Required: No

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/Rule)
