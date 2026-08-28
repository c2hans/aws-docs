---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuthorizerDescription.html
---

# AuthorizerDescription
<a name="API_AuthorizerDescription"></a>

The authorizer description.

## Contents
<a name="API_AuthorizerDescription_Contents"></a>

 ** authorizerArn **   <a name="iot-Type-AuthorizerDescription-authorizerArn"></a>
The authorizer ARN.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** authorizerFunctionArn **   <a name="iot-Type-AuthorizerDescription-authorizerFunctionArn"></a>
The authorizer's Lambda function ARN.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

 ** authorizerName **   <a name="iot-Type-AuthorizerDescription-authorizerName"></a>
The authorizer name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`
Required: No

 ** creationDate **   <a name="iot-Type-AuthorizerDescription-creationDate"></a>
The UNIX timestamp of when the authorizer was created.
Type: Timestamp
Required: No

 ** enableCachingForHttp **   <a name="iot-Type-AuthorizerDescription-enableCachingForHttp"></a>
When `true`, the result from the authorizer’s Lambda function is cached for the time specified in `refreshAfterInSeconds`. The cached result is used while the device reuses the same HTTP connection.
Type: Boolean
Required: No

 ** lastModifiedDate **   <a name="iot-Type-AuthorizerDescription-lastModifiedDate"></a>
The UNIX timestamp of when the authorizer was last updated.
Type: Timestamp
Required: No

 ** signingDisabled **   <a name="iot-Type-AuthorizerDescription-signingDisabled"></a>
Specifies whether AWS IoT validates the token signature in an authorization request.
Type: Boolean
Required: No

 ** status **   <a name="iot-Type-AuthorizerDescription-status"></a>
The status of the authorizer.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** tokenKeyName **   <a name="iot-Type-AuthorizerDescription-tokenKeyName"></a>
The key used to extract the token from the HTTP headers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** tokenSigningPublicKeys **   <a name="iot-Type-AuthorizerDescription-tokenSigningPublicKeys"></a>
The public keys used to validate the token signature returned by your custom authentication service.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9:_-]+`
Value Length Constraints: Maximum length of 5120.
Value Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_AuthorizerDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuthorizerDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuthorizerDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuthorizerDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
