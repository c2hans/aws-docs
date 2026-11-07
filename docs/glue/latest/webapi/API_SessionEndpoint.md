---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SessionEndpoint.html
---

# SessionEndpoint
<a name="API_SessionEndpoint"></a>

Contains the Spark Connect endpoint details for an interactive session, including the URL and authentication credentials.

## Contents
<a name="API_SessionEndpoint_Contents"></a>

 ** AuthToken **   <a name="Glue-Type-SessionEndpoint-AuthToken"></a>
The authentication token to include in requests to the Spark Connect endpoint.
Type: String
Length Constraints: Maximum length of 16384.
Required: Yes

 ** AuthTokenExpirationTime **   <a name="Glue-Type-SessionEndpoint-AuthTokenExpirationTime"></a>
The time at which the authentication token expires.
Type: Timestamp
Required: Yes

 ** Url **   <a name="Glue-Type-SessionEndpoint-Url"></a>
The Spark Connect endpoint URL for the session.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^sc://.*$`
Required: Yes

## See Also
<a name="API_SessionEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SessionEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SessionEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SessionEndpoint)
