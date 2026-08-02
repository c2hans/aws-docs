---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSAMLProviders.html
---

# ListSAMLProviders
<a name="API_ListSAMLProviders"></a>

Lists the SAML provider resource objects defined in IAM in the account. IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for a SAML provider, see [GetSAMLProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSAMLProvider.html).

**Important**
 This operation requires [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Response Elements
<a name="API_ListSAMLProviders_ResponseElements"></a>

The following element is returned by the service.

 **SAMLProviderList.member.N**
The list of SAML provider resource objects defined in IAM for this AWS account.
Type: Array of [SAMLProviderListEntry](API_SAMLProviderListEntry.md) objects

## Errors
<a name="API_ListSAMLProviders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ListSAMLProviders_Examples"></a>

### Example
<a name="API_ListSAMLProviders_Example_1"></a>

This example illustrates one usage of ListSAMLProviders.

#### Sample Request
<a name="API_ListSAMLProviders_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListSAMLProviders
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListSAMLProviders_Example_1_Response"></a>

```
<ListSAMLProvidersResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<ListSAMLProvidersResult>
  <SAMLProviderList>
    <member>
      <Arn>arn:aws:iam::123456789012:saml-provider/MyUniversity</Arn>
      <ValidUntil>2032-05-09T16:27:11Z</ValidUntil>
      <CreateDate>2012-05-09T16:27:03Z</CreateDate>
    </member>
    <member>
      <Arn>arn:aws:iam::123456789012:saml-provider/MyUniversity</Arn>
      <ValidUntil>2015-03-11T13:11:02Z</ValidUntil>
      <CreateDate>2012-05-09T16:27:11Z</CreateDate>
    </member>
  </SAMLProviderList>
</ListSAMLProvidersResult>
<ResponseMetadata>
  <RequestId>fd74fa8d-99f3-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</ListSAMLProvidersResponse>
```

## See Also
<a name="API_ListSAMLProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListSAMLProviders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListSAMLProviders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListSAMLProviders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListSAMLProviders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListSAMLProviders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListSAMLProviders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListSAMLProviders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListSAMLProviders)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListSAMLProviders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListSAMLProviders)
