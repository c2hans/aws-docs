---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSAMLProvider.html
---

# GetSAMLProvider
<a name="API_GetSAMLProvider"></a>

Returns the SAML provider metadocument that was uploaded when the IAM SAML provider resource object was created or updated.

**Note**
This operation requires [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Request Parameters
<a name="API_GetSAMLProvider_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SAMLProviderArn **
The Amazon Resource Name (ARN) of the SAML provider resource object in IAM to get information about.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## Response Elements
<a name="API_GetSAMLProvider_ResponseElements"></a>

The following elements are returned by the service.

 ** AssertionEncryptionMode **
Specifies the encryption setting for the SAML provider.
Type: String
Valid Values: `Required | Allowed`

 ** CreateDate **
The date and time when the SAML provider was created.
Type: Timestamp

 **PrivateKeyList.member.N**
The private key metadata for the SAML provider.
Type: Array of [SAMLPrivateKey](API_SAMLPrivateKey.md) objects
Array Members: Maximum number of 2 items.

 ** SAMLMetadataDocument **
The XML metadata document that includes information about an identity provider.
Type: String
Length Constraints: Minimum length of 1000. Maximum length of 10000000.

 ** SAMLProviderUUID **
The unique identifier assigned to the SAML provider.
Type: String
Length Constraints: Minimum length of 22. Maximum length of 64.
Pattern: `[A-Z0-9]+`

 **Tags.member.N**
A list of tags that are attached to the specified IAM SAML provider. The returned list of tags is sorted by tag key. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.

 ** ValidUntil **
The expiration date and time for the SAML provider.
Type: Timestamp

## Errors
<a name="API_GetSAMLProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetSAMLProvider_Examples"></a>

### Example
<a name="API_GetSAMLProvider_Example_1"></a>

This example illustrates one usage of GetSAMLProvider.

#### Sample Request
<a name="API_GetSAMLProvider_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetSAMLProvider
&Name=arn:aws:iam::123456789012:saml-provider/MyUniversity
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetSAMLProvider_Example_1_Response"></a>

```
<GetSAMLProviderResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<GetSAMLProviderResult>
  <AssertionEncryptionMode>Allowed</AssertionEncryptionMode>
  <CreateDate>2012-05-09T16:27:11Z</CreateDate>
  <ValidUntil>2015-12-31T211:59:59Z</ValidUntil>
  <SAMLMetadataDocument>Pd9fexDssTkRgGNqs...DxptfEs==</SAMLMetadataDocument>
  <PrivateKeyList>
   <member>
        <KeyId>SAMLPKOQIX75IETFBAK8F6</KeyId>
        <Timestamp>2024-06-02T17:01:44Z</Timestamp>
    </member>
    <member>
        <KeyId>SAMLNLPRIX13IASBCAW4F3</KeyId>
        <Timestamp>2024-07-03T18:03:44Z</Timestamp>
    </member>
  </PrivateKeyList>
</GetSAMLProviderResult>
<ResponseMetadata>
  <RequestId>29f47818-99f5-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</GetSAMLProviderResponse>
```

## See Also
<a name="API_GetSAMLProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetSAMLProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetSAMLProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetSAMLProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetSAMLProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetSAMLProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetSAMLProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetSAMLProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetSAMLProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetSAMLProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetSAMLProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
