---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainSuggestions.html
---

# GetDomainSuggestions
<a name="API_domains_GetDomainSuggestions"></a>

The GetDomainSuggestions operation returns a list of suggested domain names.

## Request Syntax
<a name="API_domains_GetDomainSuggestions_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}",
   "OnlyAvailable": {{boolean}},
   "SuggestionCount": {{number}}
}
```

## Request Parameters
<a name="API_domains_GetDomainSuggestions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_domains_GetDomainSuggestions_RequestSyntax) **   <a name="Route53Domains-domains_GetDomainSuggestions-request-DomainName"></a>
A domain name that you want to use as the basis for a list of possible domain names. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*.
The domain name can contain only the following characters:
+ Letters a through z. Domain names are not case sensitive.
+ Numbers 0 through 9.
+ Hyphen (-). You can't specify a hyphen at the beginning or end of a label.
+ Period (.) to separate the labels in the name, such as the `.` in `example.com`.
Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [OnlyAvailable](#API_domains_GetDomainSuggestions_RequestSyntax) **   <a name="Route53Domains-domains_GetDomainSuggestions-request-OnlyAvailable"></a>
If `OnlyAvailable` is `true`, Route 53 returns only domain names that are available. If `OnlyAvailable` is `false`, Route 53 returns domain names without checking whether they're available to be registered. To determine whether the domain is available, you can call `checkDomainAvailability` for each suggestion.
Type: Boolean
Required: Yes

 ** [SuggestionCount](#API_domains_GetDomainSuggestions_RequestSyntax) **   <a name="Route53Domains-domains_GetDomainSuggestions-request-SuggestionCount"></a>
The number of suggested domain names that you want Route 53 to return. Specify a value between 1 and 50. Note that fewer than the requested number might be returned.
Type: Integer
Required: Yes

## Response Syntax
<a name="API_domains_GetDomainSuggestions_ResponseSyntax"></a>

```
{
   "SuggestionsList": [
      {
         "Availability": "string",
         "DomainName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_domains_GetDomainSuggestions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SuggestionsList](#API_domains_GetDomainSuggestions_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainSuggestions-response-SuggestionsList"></a>
A list of possible domain names. If you specified `true` for `OnlyAvailable` in the request, the list contains only domains that are available for registration.
Type: Array of [DomainSuggestion](API_domains_DomainSuggestion.md) objects

## Errors
<a name="API_domains_GetDomainSuggestions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

 ** UnsupportedTLD **
Amazon Route 53 does not support this top-level domain (TLD).
 ** message **
Amazon Route 53 does not support this top-level domain (TLD).
HTTP Status Code: 400

## Examples
<a name="API_domains_GetDomainSuggestions_Examples"></a>

### GetDomainSuggestions Example
<a name="API_domains_GetDomainSuggestions_Example_1"></a>

This example illustrates one usage of GetDomainSuggestions.

#### Sample Request
<a name="API_domains_GetDomainSuggestions_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.GetDomainSuggestions
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
    "DomainName": "example.com",
    "SuggestionCount": 8,
    "OnlyAvailable": false
}
```

#### Sample Response
<a name="API_domains_GetDomainSuggestions_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
    "SuggestionsList":[
        {"DomainName": "example.net"},
        {"DomainName": "example.org"},
        {"DomainName": "example.io"},
        {"DomainName": "example.com.au"},
        {"DomainName": "example.co.uk"},
        {"DomainName": "example.de"},
        {"DomainName": "example.co"},
        {"DomainName": "example.info"}
    ]
}
```

## See Also
<a name="API_domains_GetDomainSuggestions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/GetDomainSuggestions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/GetDomainSuggestions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/GetDomainSuggestions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/GetDomainSuggestions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/GetDomainSuggestions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/GetDomainSuggestions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/GetDomainSuggestions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/GetDomainSuggestions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/GetDomainSuggestions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/GetDomainSuggestions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
