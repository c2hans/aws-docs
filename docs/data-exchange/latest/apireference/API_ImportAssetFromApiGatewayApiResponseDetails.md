---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetFromApiGatewayApiResponseDetails.html
---

# ImportAssetFromApiGatewayApiResponseDetails
<a name="API_ImportAssetFromApiGatewayApiResponseDetails"></a>

The response details.

## Contents
<a name="API_ImportAssetFromApiGatewayApiResponseDetails_Contents"></a>

 ** ApiId **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-ApiId"></a>
The API ID.
Type: String
Required: Yes

 ** ApiName **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-ApiName"></a>
The API name.
Type: String
Required: Yes

 ** ApiSpecificationMd5Hash **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-ApiSpecificationMd5Hash"></a>
The Base64-encoded Md5 hash for the API asset, used to ensure the integrity of the API at that location.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?`
Required: Yes

 ** ApiSpecificationUploadUrl **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-ApiSpecificationUploadUrl"></a>
The upload URL of the API specification.
Type: String
Required: Yes

 ** ApiSpecificationUploadUrlExpiresAt **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-ApiSpecificationUploadUrlExpiresAt"></a>
The date and time that the upload URL expires, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-DataSetId"></a>
The data set ID.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** ProtocolType **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-ProtocolType"></a>
The protocol type.
Type: String
Valid Values: `REST`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-RevisionId"></a>
The revision ID.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Stage **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-Stage"></a>
The API stage.
Type: String
Required: Yes

 ** ApiDescription **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-ApiDescription"></a>
The API description.
Type: String
Required: No

 ** ApiKey **   <a name="dataexchange-Type-ImportAssetFromApiGatewayApiResponseDetails-ApiKey"></a>
The API key.
Type: String
Required: No

## See Also
<a name="API_ImportAssetFromApiGatewayApiResponseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ImportAssetFromApiGatewayApiResponseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ImportAssetFromApiGatewayApiResponseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ImportAssetFromApiGatewayApiResponseDetails)
