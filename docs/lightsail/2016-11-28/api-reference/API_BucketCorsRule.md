---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_BucketCorsRule.html
---

# BucketCorsRule
<a name="API_BucketCorsRule"></a>

Describes a cross-origin resource sharing (CORS) rule for a Lightsail bucket. CORS rules specify which origins are allowed to access the bucket, which HTTP methods are allowed, and other access control information. For more information, see [Configuring cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html).

## Contents
<a name="API_BucketCorsRule_Contents"></a>

 ** allowedMethods **   <a name="Lightsail-Type-BucketCorsRule-allowedMethods"></a>
The HTTP methods that are allowed when accessing the bucket from the specified origin. Each CORS rule must identify at least one origin and one method.
You can use the following HTTP methods:
+  `GET` - Retrieves data from the server, such as downloading files or viewing content.
+  `PUT` - Uploads or replaces data on the server, such as uploading new files.
+  `POST` - Sends data to the server for processing, such as submitting forms or creating new resources.
+  `DELETE` - Removes data from the server, such as deleting files or resources.
+  `HEAD` - Retrieves only the headers from the server without the actual content, useful for checking if a resource exists.
Type: Array of strings
Pattern: `^(DELETE|GET|HEAD|POST|PUT)$`
Required: Yes

 ** allowedOrigins **   <a name="Lightsail-Type-BucketCorsRule-allowedOrigins"></a>
One or more origins you want customers to be able to access the bucket from. Each CORS rule must identify at least one origin and one method.
Type: Array of strings
Required: Yes

 ** allowedHeaders **   <a name="Lightsail-Type-BucketCorsRule-allowedHeaders"></a>
Headers that are specified in the `Access-Control-Request-Headers` header. These headers are allowed in a preflight `OPTIONS` request. In response to any preflight `OPTIONS` request, Amazon S3 returns any requested headers that are allowed.
Type: Array of strings
Required: No

 ** exposeHeaders **   <a name="Lightsail-Type-BucketCorsRule-exposeHeaders"></a>
One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript `XMLHttpRequest` object).
Type: Array of strings
Required: No

 ** id **   <a name="Lightsail-Type-BucketCorsRule-id"></a>
A unique identifier for the CORS rule. The ID value can be up to 255 characters long. The IDs help you find a rule in the configuration.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** maxAgeSeconds **   <a name="Lightsail-Type-BucketCorsRule-maxAgeSeconds"></a>
The time in seconds that your browser is to cache the preflight response for the specified resource. A CORS rule can have only one `maxAgeSeconds` element.
Type: Integer
Required: No

## See Also
<a name="API_BucketCorsRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/BucketCorsRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/BucketCorsRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/BucketCorsRule)
