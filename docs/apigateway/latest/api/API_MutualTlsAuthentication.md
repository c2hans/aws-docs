---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_MutualTlsAuthentication.html
---

# MutualTlsAuthentication
<a name="API_MutualTlsAuthentication"></a>

The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.

## Contents
<a name="API_MutualTlsAuthentication_Contents"></a>

 ** truststoreUri **   <a name="apigw-Type-MutualTlsAuthentication-truststoreUri"></a>
An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example `s3://bucket-name/key-name`. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.
Type: String
Required: No

 ** truststoreVersion **   <a name="apigw-Type-MutualTlsAuthentication-truststoreVersion"></a>
The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.
Type: String
Required: No

 ** truststoreWarnings **   <a name="apigw-Type-MutualTlsAuthentication-truststoreWarnings"></a>
A list of warnings that API Gateway returns while processing your truststore. Invalid certificates produce warnings. Mutual TLS is still enabled, but some clients might not be able to access your API. To resolve warnings, upload a new truststore to S3, and then update you domain name to use the new version.
Type: Array of strings
Required: No

## See Also
<a name="API_MutualTlsAuthentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/MutualTlsAuthentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/MutualTlsAuthentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/MutualTlsAuthentication)
