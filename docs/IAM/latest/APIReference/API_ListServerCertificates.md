---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServerCertificates.html
---

# ListServerCertificates
<a name="API_ListServerCertificates"></a>

Lists the server certificates stored in IAM that have the specified path prefix. If none exist, the operation returns an empty list.

 You can paginate the results using the `MaxItems` and `Marker` parameters.

For more information about working with server certificates, see [Working with server certificates](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html) in the *IAM User Guide*. This topic also includes a list of AWS services that can use the server certificates that you manage with IAM.

**Note**
IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for a servercertificate, see [GetServerCertificate](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServerCertificate.html).

## Request Parameters
<a name="API_ListServerCertificates_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **
Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the `Marker` element in the response that you received to indicate where the next call should start.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** MaxItems **
Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the `IsTruncated` response element is `true`.
If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the `IsTruncated` response element returns `true`, and `Marker` contains a value to include in the subsequent call that tells the service where to continue from.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** PathPrefix **
 The path prefix for filtering the results. For example: `/company/servercerts` would get all server certificates for which the path starts with `/company/servercerts`.
This parameter is optional. If it is not included, it defaults to a slash (/), listing all server certificates. This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the \! (`\u0021`) through the DEL character (`\u007F`), including most punctuation characters, digits, and upper and lowercased letters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `\u002F[\u0021-\u007F]*`
Required: No

## Response Elements
<a name="API_ListServerCertificates_ResponseElements"></a>

The following elements are returned by the service.

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

 **ServerCertificateMetadataList.member.N**
A list of server certificates.
Type: Array of [ServerCertificateMetadata](API_ServerCertificateMetadata.md) objects

## Errors
<a name="API_ListServerCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ListServerCertificates_Examples"></a>

### Example
<a name="API_ListServerCertificates_Example_1"></a>

This example illustrates one usage of ListServerCertificates.

#### Sample Request
<a name="API_ListServerCertificates_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListServerCertificates
&PathPrefix=/company/servercerts
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListServerCertificates_Example_1_Response"></a>

```
<ListServerCertificatesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<ListServerCertificatesResult>
  <IsTruncated>false</IsTruncated>
  <ServerCertificateMetadataList>
    <member>
      <ServerCertificateName>ProdServerCert</ServerCertificateName>
      <Path>/company/servercerts/</Path>
      <Arn>arn:aws:iam::123456789012:server-certificate/company/servercerts/ProdServerCert</Arn>
      <UploadDate>2010-05-08T01:02:03.004Z</UploadDate>
      <ServerCertificateId>ASCACKCEVSQ6CEXAMPLE1</ServerCertificateId>
      <Expiration>2012-05-08T01:02:03.004Z</Expiration>
    </member>
    <member>
      <ServerCertificateName>BetaServerCert</ServerCertificateName>
      <Path>/company/servercerts/</Path>
      <Arn>arn:aws:iam::123456789012:server-certificate/company/servercerts/BetaServerCert</Arn>
      <UploadDate>2010-05-08T02:03:01.004Z</UploadDate>
      <ServerCertificateId>ASCACKCEVSQ6CEXAMPLE2</ServerCertificateId>
      <Expiration>2012-05-08T02:03:01.004Z</Expiration>
    </member>
    <member>
      <ServerCertificateName>TestServerCert</ServerCertificateName>
      <Path>/company/servercerts/</Path>
      <Arn>arn:aws:iam::123456789012:server-certificate/company/servercerts/TestServerCert</Arn>
      <UploadDate>2010-05-08T03:01:02.004Z</UploadDate>
      <ServerCertificateId>ASCACKCEVSQ6CEXAMPLE3</ServerCertificateId>
      <Expiration>2012-05-08T03:01:02.004Z</Expiration>
    </member>
  </ServerCertificateMetadataList>
</ListServerCertificatesResult>
<ResponseMetadata>
  <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
</ResponseMetadata>
</ListServerCertificatesResponse>
```

## See Also
<a name="API_ListServerCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListServerCertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListServerCertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListServerCertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListServerCertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListServerCertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListServerCertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListServerCertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListServerCertificates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListServerCertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListServerCertificates)
