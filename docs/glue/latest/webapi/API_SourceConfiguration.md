---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SourceConfiguration.html
---

# SourceConfiguration
<a name="API_SourceConfiguration"></a>

Configuration that defines how to make requests to endpoints, including request methods, paths, parameters, and response handling.

## Contents
<a name="API_SourceConfiguration_Contents"></a>

 ** PaginationConfiguration **   <a name="Glue-Type-SourceConfiguration-PaginationConfiguration"></a>
Configuration for handling paginated responses from the REST API, supporting both cursor-based and offset-based pagination strategies.
Type: [PaginationConfiguration](API_PaginationConfiguration.md) object
Required: No

 ** RequestMethod **   <a name="Glue-Type-SourceConfiguration-RequestMethod"></a>
The HTTP method to use for requests to this endpoint, such as GET, POST.
Type: String
Valid Values: `GET | POST`
Required: No

 ** RequestParameters **   <a name="Glue-Type-SourceConfiguration-RequestParameters"></a>
Configuration for request parameters that should be included in API calls, such as query parameters, headers, or body content.
Type: Array of [ConnectorProperty](API_ConnectorProperty.md) objects
Required: No

 ** RequestPath **   <a name="Glue-Type-SourceConfiguration-RequestPath"></a>
The URL path for the REST endpoint, which may include parameter placeholders that will be replaced with actual values during requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `/[a-zA-Z0-9._~:/?#\[\]@!$&'()*+,;={}-]*`
Required: No

 ** ResponseConfiguration **   <a name="Glue-Type-SourceConfiguration-ResponseConfiguration"></a>
Configuration that defines how to parse and extract data from API responses, including success and error handling.
Type: [ResponseConfiguration](API_ResponseConfiguration.md) object
Required: No

## See Also
<a name="API_SourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SourceConfiguration)
