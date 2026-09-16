---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeCustomerMetadata.html
---

# DescribeCustomerMetadata
<a name="API_DescribeCustomerMetadata"></a>

Get and view a list of customer agreements, along with their signed status and whether the customer is an NNIPartner, NNIPartnerV2, or a nonPartner.

## Response Syntax
<a name="API_DescribeCustomerMetadata_ResponseSyntax"></a>

```
{
   "agreements": [
      {
         "agreementName": "string",
         "status": "string"
      }
   ],
   "nniPartnerType": "string"
}
```

## Response Elements
<a name="API_DescribeCustomerMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreements](#API_DescribeCustomerMetadata_ResponseSyntax) **   <a name="DX-DescribeCustomerMetadata-response-agreements"></a>
The list of customer agreements.
Type: Array of [CustomerAgreement](API_CustomerAgreement.md) objects

 ** [nniPartnerType](#API_DescribeCustomerMetadata_ResponseSyntax) **   <a name="DX-DescribeCustomerMetadata-response-nniPartnerType"></a>
The type of network-to-network interface (NNI) partner. The partner type will be one of the following:
+ V1: This partner can only allocate 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, or 500Mbps subgigabit connections.
+ V2: This partner can only allocate 1GB, 2GB, 5GB, or 10GB hosted connections.
+ nonPartner: The customer is not a partner.
Type: String
Valid Values: `v1 | v2 | nonPartner`

## Errors
<a name="API_DescribeCustomerMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCustomerMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeCustomerMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeCustomerMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeCustomerMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeCustomerMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeCustomerMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeCustomerMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeCustomerMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeCustomerMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeCustomerMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeCustomerMetadata)
