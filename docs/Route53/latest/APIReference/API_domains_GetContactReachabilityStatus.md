---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetContactReachabilityStatus.html
---

# GetContactReachabilityStatus
<a name="API_domains_GetContactReachabilityStatus"></a>

For operations that require confirmation that the email address for the registrant contact is valid, such as registering a new domain, this operation returns information about whether the registrant contact has responded.

If you want us to resend the email, use the `ResendContactReachabilityEmail` operation.

## Request Syntax
<a name="API_domains_GetContactReachabilityStatus_RequestSyntax"></a>

```
{
   "domainName": "{{string}}"
}
```

## Request Parameters
<a name="API_domains_GetContactReachabilityStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domainName](#API_domains_GetContactReachabilityStatus_RequestSyntax) **   <a name="Route53Domains-domains_GetContactReachabilityStatus-request-domainName"></a>
The name of the domain for which you want to know whether the registrant contact has confirmed that the email address is valid.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## Response Syntax
<a name="API_domains_GetContactReachabilityStatus_ResponseSyntax"></a>

```
{
   "domainName": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_domains_GetContactReachabilityStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainName](#API_domains_GetContactReachabilityStatus_ResponseSyntax) **   <a name="Route53Domains-domains_GetContactReachabilityStatus-response-domainName"></a>
The domain name for which you requested the reachability status.
Type: String
Length Constraints: Maximum length of 255.

 ** [status](#API_domains_GetContactReachabilityStatus_ResponseSyntax) **   <a name="Route53Domains-domains_GetContactReachabilityStatus-response-status"></a>
Whether the registrant contact has responded. Values include the following:
PENDING
We sent the confirmation email and haven't received a response yet.
DONE
We sent the email and got confirmation from the registrant contact.
EXPIRED
The time limit expired before the registrant contact responded.
Type: String
Valid Values: `PENDING | DONE | EXPIRED`

## Errors
<a name="API_domains_GetContactReachabilityStatus_Errors"></a>

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
<a name="API_domains_GetContactReachabilityStatus_Examples"></a>

### GetContactReachabilityStatus Example
<a name="API_domains_GetContactReachabilityStatus_Example_1"></a>

This example illustrates one usage of GetContactReachabilityStatus.

#### Sample Request
<a name="API_domains_GetContactReachabilityStatus_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205225Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.GetContactReachabilityStatus
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
connections:Keep-Alive
{
   "domainName":"example.com"
}
```

#### Sample Response
<a name="API_domains_GetContactReachabilityStatus_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
   "domainName":"example.com",
   "status":"PENDING"
}
```

## See Also
<a name="API_domains_GetContactReachabilityStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/GetContactReachabilityStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/GetContactReachabilityStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/GetContactReachabilityStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/GetContactReachabilityStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/GetContactReachabilityStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/GetContactReachabilityStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/GetContactReachabilityStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/GetContactReachabilityStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/GetContactReachabilityStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/GetContactReachabilityStatus)
