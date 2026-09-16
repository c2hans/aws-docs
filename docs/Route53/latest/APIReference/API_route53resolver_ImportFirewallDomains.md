---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ImportFirewallDomains.html
---

# ImportFirewallDomains
<a name="API_route53resolver_ImportFirewallDomains"></a>

Imports domain names from a file into a domain list, for use in a DNS firewall rule group.

Each domain specification in your domain list must satisfy the following requirements:
+ It can optionally start with `*` (asterisk).
+ With the exception of the optional starting asterisk, it must only contain the following characters: `A-Z`, `a-z`, `0-9`, `-` (hyphen).
+ It must be from 1-255 characters in length.

## Request Syntax
<a name="API_route53resolver_ImportFirewallDomains_RequestSyntax"></a>

```
{
   "DomainFileUrl": "{{string}}",
   "FirewallDomainListId": "{{string}}",
   "Operation": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ImportFirewallDomains_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainFileUrl](#API_route53resolver_ImportFirewallDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ImportFirewallDomains-request-DomainFileUrl"></a>
The fully qualified URL or URI of the file stored in Amazon Simple Storage Service (Amazon S3) that contains the list of domains to import.
The file must be in an S3 bucket that's in the same Region as your DNS Firewall. The file must be a text file and must contain a single domain per line.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [FirewallDomainListId](#API_route53resolver_ImportFirewallDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ImportFirewallDomains-request-FirewallDomainListId"></a>
The ID of the domain list that you want to modify with the import operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Operation](#API_route53resolver_ImportFirewallDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ImportFirewallDomains-request-Operation"></a>
What you want DNS Firewall to do with the domains that are listed in the file. This must be set to `REPLACE`, which updates the domain list to exactly match the list in the file.
Type: String
Valid Values: `REPLACE`
Required: Yes

## Response Syntax
<a name="API_route53resolver_ImportFirewallDomains_ResponseSyntax"></a>

```
{
   "Id": "string",
   "Name": "string",
   "Status": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_route53resolver_ImportFirewallDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_route53resolver_ImportFirewallDomains_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ImportFirewallDomains-response-Id"></a>
The Id of the firewall domain list that DNS Firewall just updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [Name](#API_route53resolver_ImportFirewallDomains_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ImportFirewallDomains-response-Name"></a>
The name of the domain list.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`

 ** [Status](#API_route53resolver_ImportFirewallDomains_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ImportFirewallDomains-response-Status"></a>
Status of the import request.
Type: String
Valid Values: `COMPLETE | COMPLETE_IMPORT_FAILED | IMPORTING | DELETING | UPDATING`

 ** [StatusMessage](#API_route53resolver_ImportFirewallDomains_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ImportFirewallDomains-response-StatusMessage"></a>
Additional information about the status of the list, if available.
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_route53resolver_ImportFirewallDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** ConflictException **
The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** LimitExceededException **
The request caused one or more limits to be exceeded.
 ** ResourceType **
For a `LimitExceededException` error, the type of resource that exceeded the current limit.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceType **
For a `ResourceNotFoundException` error, the type of resource that doesn't exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
You have provided an invalid command. If you ran the `UpdateFirewallDomains` request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
HTTP Status Code: 400

## See Also
<a name="API_route53resolver_ImportFirewallDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ImportFirewallDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ImportFirewallDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ImportFirewallDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ImportFirewallDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ImportFirewallDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ImportFirewallDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ImportFirewallDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ImportFirewallDomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ImportFirewallDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ImportFirewallDomains)
