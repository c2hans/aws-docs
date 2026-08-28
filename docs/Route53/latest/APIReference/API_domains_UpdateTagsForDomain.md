---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateTagsForDomain.html
---

# UpdateTagsForDomain
<a name="API_domains_UpdateTagsForDomain"></a>

This operation adds or updates tags for a specified domain.

All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.

## Request Syntax
<a name="API_domains_UpdateTagsForDomain_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}",
   "TagsToUpdate": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_domains_UpdateTagsForDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_domains_UpdateTagsForDomain_RequestSyntax) **   <a name="Route53Domains-domains_UpdateTagsForDomain-request-DomainName"></a>
The domain for which you want to add or update tags.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [TagsToUpdate](#API_domains_UpdateTagsForDomain_RequestSyntax) **   <a name="Route53Domains-domains_UpdateTagsForDomain-request-TagsToUpdate"></a>
A list of the tag keys and values that you want to add or update. If you specify a key that already exists, the corresponding value will be replaced.
Type: Array of [Tag](API_domains_Tag.md) objects
Required: No

## Response Elements
<a name="API_domains_UpdateTagsForDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_domains_UpdateTagsForDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

 ** OperationLimitExceeded **
The number of operations or jobs running exceeded the allowed threshold for the account.
 ** message **
The number of operations or jobs running exceeded the allowed threshold for the account.
HTTP Status Code: 400

 ** UnsupportedTLD **
Amazon Route 53 does not support this top-level domain (TLD).
 ** message **
Amazon Route 53 does not support this top-level domain (TLD).
HTTP Status Code: 400

## Examples
<a name="API_domains_UpdateTagsForDomain_Examples"></a>

### UpdateTagsForDomain Example
<a name="API_domains_UpdateTagsForDomain_Example_1"></a>

This example illustrates one usage of UpdateTagsForDomain.

#### Sample Request
<a name="API_domains_UpdateTagsForDomain_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domain_v20140515.UpdateTagsForDomain
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
   "DomainName": "example.com",
   "TagsToUpdate":[
      {
         "Key": "foo",
         "Value": "bar"
      }, {
         "Key": "foo2",
         "Value": ""
      }
  ]
}
```

#### Sample Response
<a name="API_domains_UpdateTagsForDomain_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{}
```

## See Also
<a name="API_domains_UpdateTagsForDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/UpdateTagsForDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/UpdateTagsForDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/UpdateTagsForDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/UpdateTagsForDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/UpdateTagsForDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/UpdateTagsForDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/UpdateTagsForDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/UpdateTagsForDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/UpdateTagsForDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/UpdateTagsForDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
