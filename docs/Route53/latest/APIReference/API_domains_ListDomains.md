---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListDomains.html
---

# ListDomains
<a name="API_domains_ListDomains"></a>

This operation returns all the domain names registered with Amazon Route 53 for the current AWS account if no filtering conditions are used.

## Request Syntax
<a name="API_domains_ListDomains_RequestSyntax"></a>

```
{
   "FilterConditions": [
      {
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxItems": {{number}},
   "SortCondition": {
      "Name": "{{string}}",
      "SortOrder": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_domains_ListDomains_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FilterConditions](#API_domains_ListDomains_RequestSyntax) **   <a name="Route53Domains-domains_ListDomains-request-FilterConditions"></a>
A complex type that contains information about the filters applied during the `ListDomains` request. The filter conditions can include domain name and domain expiration.
Type: Array of [FilterCondition](API_domains_FilterCondition.md) objects
Required: No

 ** [Marker](#API_domains_ListDomains_RequestSyntax) **   <a name="Route53Domains-domains_ListDomains-request-Marker"></a>
For an initial request for a list of domains, omit this element. If the number of domains that are associated with the current AWS account is greater than the value that you specified for `MaxItems`, you can use `Marker` to return additional domains. Get the value of `NextPageMarker` from the previous response, and submit another request that includes the value of `NextPageMarker` in the `Marker` element.
Constraints: The marker must match the value specified in the previous request.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [MaxItems](#API_domains_ListDomains_RequestSyntax) **   <a name="Route53Domains-domains_ListDomains-request-MaxItems"></a>
Number of domains to be returned.
Default: 20
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [SortCondition](#API_domains_ListDomains_RequestSyntax) **   <a name="Route53Domains-domains_ListDomains-request-SortCondition"></a>
A complex type that contains information about the requested ordering of domains in the returned list.
Type: [SortCondition](API_domains_SortCondition.md) object
Required: No

## Response Syntax
<a name="API_domains_ListDomains_ResponseSyntax"></a>

```
{
   "Domains": [
      {
         "AutoRenew": boolean,
         "DomainName": "string",
         "Expiry": number,
         "TransferLock": boolean
      }
   ],
   "NextPageMarker": "string"
}
```

## Response Elements
<a name="API_domains_ListDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Domains](#API_domains_ListDomains_ResponseSyntax) **   <a name="Route53Domains-domains_ListDomains-response-Domains"></a>
A list of domains.
Type: Array of [DomainSummary](API_domains_DomainSummary.md) objects

 ** [NextPageMarker](#API_domains_ListDomains_ResponseSyntax) **   <a name="Route53Domains-domains_ListDomains-response-NextPageMarker"></a>
If there are more domains than you specified for `MaxItems` in the request, submit another request and include the value of `NextPageMarker` in the value of `Marker`.
Type: String
Length Constraints: Maximum length of 4096.

## Errors
<a name="API_domains_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

## Examples
<a name="API_domains_ListDomains_Examples"></a>

### ListDomains Example
<a name="API_domains_ListDomains_Example_1"></a>

This example illustrates one usage of ListDomains.

#### Sample Request
<a name="API_domains_ListDomains_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.ListDomains
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
   "Marker":"AxDAClaROQAXasf29GHWAIKPLA=",
   "MaxItems":20
}
```

#### Sample Response
<a name="API_domains_ListDomains_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
   "Domains":[
      {
         "AutoRenew":false,
         "DomainName":"example.com",
         "Expiry":1431203765,
         "TransferLock":false
      },
      {
         "AutoRenew":false,
         "DomainName":"example.net",
         "Expiry":1431539260,
         "TransferLock":false
      },
      {
         "AutoRenew":false,
         "DomainName":"example.org",
         "Expiry":1431240024,
         "TransferLock":false
      },
      {
         "AutoRenew":false,
         "DomainName":"example.test",
         "Expiry":1431539259,
         "TransferLock":false
      }
   ]
}
```

## See Also
<a name="API_domains_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/ListDomains)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/ListDomains)
