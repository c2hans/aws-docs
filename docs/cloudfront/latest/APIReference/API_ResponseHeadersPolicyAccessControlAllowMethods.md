---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyAccessControlAllowMethods.html
---

# ResponseHeadersPolicyAccessControlAllowMethods
<a name="API_ResponseHeadersPolicyAccessControlAllowMethods"></a>

A list of HTTP methods that CloudFront includes as values for the `Access-Control-Allow-Methods` HTTP response header.

For more information about the `Access-Control-Allow-Methods` HTTP response header, see [Access-Control-Allow-Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods) in the MDN Web Docs.

## Contents
<a name="API_ResponseHeadersPolicyAccessControlAllowMethods_Contents"></a>

 ** Items **   <a name="cloudfront-Type-ResponseHeadersPolicyAccessControlAllowMethods-Items"></a>
The list of HTTP methods. Valid values are:
+  `GET`
+  `DELETE`
+  `HEAD`
+  `OPTIONS`
+  `PATCH`
+  `POST`
+  `PUT`
+  `ALL`
 `ALL` is a special value that includes all of the listed HTTP methods.
Type: Array of strings
Valid Values: `GET | POST | OPTIONS | PUT | DELETE | PATCH | HEAD | ALL`
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-ResponseHeadersPolicyAccessControlAllowMethods-Quantity"></a>
The number of HTTP methods in the list.
Type: Integer
Required: Yes

## See Also
<a name="API_ResponseHeadersPolicyAccessControlAllowMethods_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlAllowMethods)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlAllowMethods)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyAccessControlAllowMethods)
