---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_RestApi.html
---

# RestApi
<a name="API_RestApi"></a>

Represents a REST API.

## Contents
<a name="API_RestApi_Contents"></a>

 ** apiKeySource **   <a name="apigw-Type-RestApi-apiKeySource"></a>
The source of the API key for metering requests according to a usage plan. Valid values are: >`HEADER` to read the API key from the `X-API-Key` header of a request. `AUTHORIZER` to read the API key from the `UsageIdentifierKey` from a custom authorizer.
Type: String
Valid Values: `HEADER | AUTHORIZER`
Required: No

 ** apiStatus **   <a name="apigw-Type-RestApi-apiStatus"></a>
The ApiStatus of the RestApi.
Type: String
Valid Values: `UPDATING | AVAILABLE | PENDING | FAILED`
Required: No

 ** apiStatusMessage **   <a name="apigw-Type-RestApi-apiStatusMessage"></a>
 The status message of the RestApi. When the status message is `UPDATING` you can still invoke it.
Type: String
Required: No

 ** binaryMediaTypes **   <a name="apigw-Type-RestApi-binaryMediaTypes"></a>
The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.
Type: Array of strings
Required: No

 ** createdDate **   <a name="apigw-Type-RestApi-createdDate"></a>
The timestamp when the API was created.
Type: Timestamp
Required: No

 ** description **   <a name="apigw-Type-RestApi-description"></a>
The API's description.
Type: String
Required: No

 ** disableExecuteApiEndpoint **   <a name="apigw-Type-RestApi-disableExecuteApiEndpoint"></a>
Specifies whether clients can invoke your API by using the default `execute-api` endpoint. By default, clients can invoke your API with the default `https://{api_id}.execute-api.{region}.amazonaws.com` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.
Type: Boolean
Required: No

 ** endpointAccessMode **   <a name="apigw-Type-RestApi-endpointAccessMode"></a>
 The endpoint access mode of the RestApi.
Type: String
Valid Values: `BASIC | STRICT`
Required: No

 ** endpointConfiguration **   <a name="apigw-Type-RestApi-endpointConfiguration"></a>
The endpoint configuration of this RestApi showing the endpoint types and IP address types of the API.
Type: [EndpointConfiguration](API_EndpointConfiguration.md) object
Required: No

 ** id **   <a name="apigw-Type-RestApi-id"></a>
The API's identifier. This identifier is unique across all of your APIs in API Gateway.
Type: String
Required: No

 ** minimumCompressionSize **   <a name="apigw-Type-RestApi-minimumCompressionSize"></a>
A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.
Type: Integer
Required: No

 ** name **   <a name="apigw-Type-RestApi-name"></a>
The API's name.
Type: String
Required: No

 ** policy **   <a name="apigw-Type-RestApi-policy"></a>
A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.
Type: String
Required: No

 ** rootResourceId **   <a name="apigw-Type-RestApi-rootResourceId"></a>
The API's root resource ID.
Type: String
Required: No

 ** securityPolicy **   <a name="apigw-Type-RestApi-securityPolicy"></a>
 The Transport Layer Security (TLS) version \+ cipher suite for this RestApi.
Type: String
Valid Values: `TLS_1_0 | TLS_1_2 | SecurityPolicy_TLS13_1_3_2025_09 | SecurityPolicy_TLS13_1_3_FIPS_2025_09 | SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_PQ_2025_09 | SecurityPolicy_TLS13_1_2_2021_06 | SecurityPolicy_TLS13_2025_EDGE | SecurityPolicy_TLS12_PFS_2025_EDGE | SecurityPolicy_TLS12_2018_EDGE`
Required: No

 ** tags **   <a name="apigw-Type-RestApi-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map
Required: No

 ** version **   <a name="apigw-Type-RestApi-version"></a>
A version identifier for the API.
Type: String
Required: No

 ** warnings **   <a name="apigw-Type-RestApi-warnings"></a>
The warning messages reported when `failonwarnings` is turned on during API import.
Type: Array of strings
Required: No

## See Also
<a name="API_RestApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/RestApi)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/RestApi)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/RestApi)
