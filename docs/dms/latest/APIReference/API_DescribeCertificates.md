---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeCertificates.html
---

# DescribeCertificates
<a name="API_DescribeCertificates"></a>

Provides a description of the certificate.

## Request Syntax
<a name="API_DescribeCertificates_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeCertificates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeCertificates_RequestSyntax) **   <a name="DMS-DescribeCertificates-request-Filters"></a>
Filters applied to the certificates described in the form of key-value pairs. Valid values are `certificate-arn` and `certificate-id`.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeCertificates_RequestSyntax) **   <a name="DMS-DescribeCertificates-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeCertificates_RequestSyntax) **   <a name="DMS-DescribeCertificates-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 10
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeCertificates_ResponseSyntax"></a>

```
{
   "Certificates": [
      {
         "CertificateArn": "string",
         "CertificateCreationDate": number,
         "CertificateIdentifier": "string",
         "CertificateOwner": "string",
         "CertificatePem": "string",
         "CertificateWallet": blob,
         "KeyLength": number,
         "KmsKeyId": "string",
         "SigningAlgorithm": "string",
         "ValidFromDate": number,
         "ValidToDate": number
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeCertificates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificates](#API_DescribeCertificates_ResponseSyntax) **   <a name="DMS-DescribeCertificates-response-Certificates"></a>
The Secure Sockets Layer (SSL) certificates associated with the replication instance.
Type: Array of [Certificate](API_Certificate.md) objects

 ** [Marker](#API_DescribeCertificates_ResponseSyntax) **   <a name="DMS-DescribeCertificates-response-Marker"></a>
The pagination token.
Type: String

## Errors
<a name="API_DescribeCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribeCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeCertificates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeCertificates)
