---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TagFilter.html
---

# TagFilter
<a name="API_TagFilter"></a>

Information about an on-premises instance tag filter.

## Contents
<a name="API_TagFilter_Contents"></a>

 ** Key **   <a name="CodeDeploy-Type-TagFilter-Key"></a>
The on-premises instance tag filter key.
Type: String
Required: No

 ** Type **   <a name="CodeDeploy-Type-TagFilter-Type"></a>
The on-premises instance tag filter type:
+ KEY\_ONLY: Key only.
+ VALUE\_ONLY: Value only.
+ KEY\_AND\_VALUE: Key and value.
Type: String
Valid Values: `KEY_ONLY | VALUE_ONLY | KEY_AND_VALUE`
Required: No

 ** Value **   <a name="CodeDeploy-Type-TagFilter-Value"></a>
The on-premises instance tag filter value.
Type: String
Required: No

## See Also
<a name="API_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/TagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/TagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/TagFilter)
