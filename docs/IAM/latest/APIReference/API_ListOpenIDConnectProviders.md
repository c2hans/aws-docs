---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListOpenIDConnectProviders.html
---

# ListOpenIDConnectProviders
<a name="API_ListOpenIDConnectProviders"></a>

Lists information about the IAM OpenID Connect (OIDC) provider resource objects defined in the AWS account.

**Note**
IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for an OIDC provider, see [GetOpenIDConnectProvider](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOpenIDConnectProvider.html).

## Response Elements
<a name="API_ListOpenIDConnectProviders_ResponseElements"></a>

The following element is returned by the service.

 **OpenIDConnectProviderList.member.N**
The list of IAM OIDC provider resource objects defined in the AWS account.
Type: Array of [OpenIDConnectProviderListEntry](API_OpenIDConnectProviderListEntry.md) objects

## Errors
<a name="API_ListOpenIDConnectProviders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ListOpenIDConnectProviders_Examples"></a>

### Example
<a name="API_ListOpenIDConnectProviders_Example_1"></a>

This example illustrates one usage of ListOpenIDConnectProviders.

#### Sample Request
<a name="API_ListOpenIDConnectProviders_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListOpenIDConnectProviders
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListOpenIDConnectProviders_Example_1_Response"></a>

```
<ListOpenIDConnectProvidersResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListOpenIDConnectProvidersResult>
    <OpenIDConnectProviderList>
      <member>
        <Arn>arn:aws:iam::123456789012:oidc-provider/server.example.com</Arn>
      </member>
      <member>
        <Arn>arn:aws:iam::123456789012:oidc-provider/server.example.org</Arn>
      </member>
    </OpenIDConnectProviderList>
  </ListOpenIDConnectProvidersResult>
  <ResponseMetadata>
    <RequestId>de2c0228-4f63-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</ListOpenIDConnectProvidersResponse>
```

## See Also
<a name="API_ListOpenIDConnectProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListOpenIDConnectProviders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListOpenIDConnectProviders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListOpenIDConnectProviders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListOpenIDConnectProviders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListOpenIDConnectProviders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListOpenIDConnectProviders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListOpenIDConnectProviders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListOpenIDConnectProviders)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListOpenIDConnectProviders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListOpenIDConnectProviders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
