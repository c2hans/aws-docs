---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="Route53-Type-Tag-Key"></a>
The value of `Key` depends on the operation that you want to perform:
+  **Add a tag to a health check or hosted zone**: `Key` is the name that you want to give the new tag.
+  **Edit a tag**: `Key` is the name of the tag that you want to change the `Value` for.
+  ** Delete a key**: `Key` is the name of the tag you want to remove.
+  **Give a name to a health check**: Edit the default `Name` tag. In the Amazon Route 53 console, the list of your health checks includes a **Name** column that lets you see the name that you've given to each health check.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** Value **   <a name="Route53-Type-Tag-Value"></a>
The value of `Value` depends on the operation that you want to perform:
+  **Add a tag to a health check or hosted zone**: `Value` is the value that you want to give the new tag.
+  **Edit a tag**: `Value` is the new value that you want to assign the tag.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/Tag)
