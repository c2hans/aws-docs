---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetFromApiGatewayApiRequestDetails.html
---

# ImportAssetFromApiGatewayApiRequestDetails
<a name="API_ImportAssetFromApiGatewayApiRequestDetails"></a>

The request details.

## Contents
<a name="API_ImportAssetFromApiGatewayApiRequestDetails_Contents"></a>

 ** ApiId **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiRequestDetails-ApiId"></a>
The API Gateway API ID.
Type: String
Required: Yes

 ** ApiName **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiRequestDetails-ApiName"></a>
The API name.
Type: String
Required: Yes

 ** ApiSpecificationMd5Hash **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiRequestDetails-ApiSpecificationMd5Hash"></a>
The Base64-encoded MD5 hash of the OpenAPI 3.0 JSON API specification file. It is used to ensure the integrity of the file.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?`
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiRequestDetails-DataSetId"></a>
The data set ID.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** ProtocolType **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiRequestDetails-ProtocolType"></a>
The protocol type.
Type: String
Valid Values: `REST`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiRequestDetails-RevisionId"></a>
The revision ID.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Stage **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiRequestDetails-Stage"></a>
The API stage.
Type: String
Required: Yes

 ** ApiDescription **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiRequestDetails-ApiDescription"></a>
The API description. Markdown supported.
Type: String
Required: No

 ** ApiKey **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiRequestDetails-ApiKey"></a>
The API Gateway API key.
Type: String
Required: No

## See Also
<a name="API_ImportAssetFromApiGatewayApiRequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ImportAssetFromApiGatewayApiRequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ImportAssetFromApiGatewayApiRequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ImportAssetFromApiGatewayApiRequestDetails)
