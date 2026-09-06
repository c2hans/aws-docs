---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsApiGatewayRestApiDetails.html
---

# AwsApiGatewayRestApiDetails
<a name="API_AwsApiGatewayRestApiDetails"></a>

Contains information about a REST API in version 1 of Amazon API Gateway.

## Contents
<a name="API_AwsApiGatewayRestApiDetails_Contents"></a>

 ** ApiKeySource **   <a name="securityhub-Type-AwsApiGatewayRestApiDetails-ApiKeySource"></a>
The source of the API key for metering requests according to a usage plan.
 `HEADER` indicates whether to read the API key from the X-API-Key header of a request.
 `AUTHORIZER` indicates whether to read the API key from the `UsageIdentifierKey` from a custom authorizer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** BinaryMediaTypes **   <a name="securityhub-Type-AwsApiGatewayRestApiDetails-BinaryMediaTypes"></a>
The list of binary media types supported by the REST API.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** CreatedDate **   <a name="securityhub-Type-AwsApiGatewayRestApiDetails-CreatedDate"></a>
Indicates when the API was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsApiGatewayRestApiDetails-Description"></a>
A description of the REST API.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EndpointConfiguration **   <a name="securityhub-Type-AwsApiGatewayRestApiDetails-EndpointConfiguration"></a>
The endpoint configuration of the REST API.
Type: [AwsApiGatewayEndpointConfiguration](API_AwsApiGatewayEndpointConfiguration.md) object
Required: No

 ** Id **   <a name="securityhub-Type-AwsApiGatewayRestApiDetails-Id"></a>
The identifier of the REST API.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MinimumCompressionSize **   <a name="securityhub-Type-AwsApiGatewayRestApiDetails-MinimumCompressionSize"></a>
The minimum size in bytes of a payload before compression is enabled.
If `null`, then compression is disabled.
If 0, then all payloads are compressed.
Type: Integer
Required: No

 ** Name **   <a name="securityhub-Type-AwsApiGatewayRestApiDetails-Name"></a>
The name of the REST API.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Version **   <a name="securityhub-Type-AwsApiGatewayRestApiDetails-Version"></a>
The version identifier for the REST API.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsApiGatewayRestApiDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsApiGatewayRestApiDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsApiGatewayRestApiDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsApiGatewayRestApiDetails)
