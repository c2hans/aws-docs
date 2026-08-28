---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListOperations.html
---

# ListOperations
<a name="API_domains_ListOperations"></a>

Returns information about all of the operations that return an operation ID and that have ever been performed on domains that were registered by the current account.

This command runs only in the us-east-1 Region.

## Request Syntax
<a name="API_domains_ListOperations_RequestSyntax"></a>

```
{
   "Marker": "{{string}}",
   "MaxItems": {{number}},
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "Status": [ "{{string}}" ],
   "SubmittedSince": {{number}},
   "Type": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_domains_ListOperations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_domains_ListOperations_RequestSyntax) **   <a name="Route53Domains-domains_ListOperations-request-Marker"></a>
For an initial request for a list of operations, omit this element. If the number of operations that are not yet complete is greater than the value that you specified for `MaxItems`, you can use `Marker` to return additional operations. Get the value of `NextPageMarker` from the previous response, and submit another request that includes the value of `NextPageMarker` in the `Marker` element.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [MaxItems](#API_domains_ListOperations_RequestSyntax) **   <a name="Route53Domains-domains_ListOperations-request-MaxItems"></a>
Number of domains to be returned.
Default: 20
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [SortBy](#API_domains_ListOperations_RequestSyntax) **   <a name="Route53Domains-domains_ListOperations-request-SortBy"></a>
 The sort type for returned values.
Type: String
Valid Values: `SubmittedDate`
Required: No

 ** [SortOrder](#API_domains_ListOperations_RequestSyntax) **   <a name="Route53Domains-domains_ListOperations-request-SortOrder"></a>
 The sort order for returned values, either ascending or descending.
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** [Status](#API_domains_ListOperations_RequestSyntax) **   <a name="Route53Domains-domains_ListOperations-request-Status"></a>
 The status of the operations.
Type: Array of strings
Array Members: Maximum number of 5 items.
Valid Values: `SUBMITTED | IN_PROGRESS | ERROR | SUCCESSFUL | FAILED`
Required: No

 ** [SubmittedSince](#API_domains_ListOperations_RequestSyntax) **   <a name="Route53Domains-domains_ListOperations-request-SubmittedSince"></a>
An optional parameter that lets you get information about all the operations that you submitted after a specified date and time. Specify the date and time in Unix time format and Coordinated Universal time (UTC).
Type: Timestamp
Required: No

 ** [Type](#API_domains_ListOperations_RequestSyntax) **   <a name="Route53Domains-domains_ListOperations-request-Type"></a>
 An arrays of the domains operation types.
Type: Array of strings
Array Members: Maximum number of 21 items.
Valid Values: `REGISTER_DOMAIN | DELETE_DOMAIN | TRANSFER_IN_DOMAIN | UPDATE_DOMAIN_CONTACT | UPDATE_NAMESERVER | CHANGE_PRIVACY_PROTECTION | DOMAIN_LOCK | ENABLE_AUTORENEW | DISABLE_AUTORENEW | ADD_DNSSEC | REMOVE_DNSSEC | EXPIRE_DOMAIN | TRANSFER_OUT_DOMAIN | CHANGE_DOMAIN_OWNER | RENEW_DOMAIN | PUSH_DOMAIN | INTERNAL_TRANSFER_OUT_DOMAIN | INTERNAL_TRANSFER_IN_DOMAIN | RELEASE_TO_GANDI | TRANSFER_ON_RENEW | RESTORE_DOMAIN`
Required: No

## Response Syntax
<a name="API_domains_ListOperations_ResponseSyntax"></a>

```
{
   "NextPageMarker": "string",
   "Operations": [
      {
         "DomainName": "string",
         "LastUpdatedDate": number,
         "Message": "string",
         "OperationId": "string",
         "Status": "string",
         "StatusFlag": "string",
         "SubmittedDate": number,
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_domains_ListOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageMarker](#API_domains_ListOperations_ResponseSyntax) **   <a name="Route53Domains-domains_ListOperations-response-NextPageMarker"></a>
If there are more operations than you specified for `MaxItems` in the request, submit another request and include the value of `NextPageMarker` in the value of `Marker`.
Type: String
Length Constraints: Maximum length of 4096.

 ** [Operations](#API_domains_ListOperations_ResponseSyntax) **   <a name="Route53Domains-domains_ListOperations-response-Operations"></a>
Lists summaries of the operations.
Type: Array of [OperationSummary](API_domains_OperationSummary.md) objects

## Errors
<a name="API_domains_ListOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

## Examples
<a name="API_domains_ListOperations_Examples"></a>

### ListOperations Example
<a name="API_domains_ListOperations_Example_1"></a>

This example illustrates one usage of ListOperations.

#### Sample Request
<a name="API_domains_ListOperations_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.ListOperations
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
   "MaxItems" : 2
}
```

#### Sample Response
<a name="API_domains_ListOperations_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
   "Operations":[
       {
         "OperationId":"4ced3d4a-e011-45ee-b94f-1e2d73477562",
         "Status":"WORKFLOW_IN_PROGRESS",
         "SubmittedDate":1403548979.088,
         "Type":"CHANGE_PRIVACY_PROTECTION"
      },
      {
         "OperationId":"2e3ac45b-89b3-47ea-a042-f56dcd1b6883",
         "Status":"WORKFLOW_IN_PROGRESS",
         "SubmittedDate":1403548986.429,
         "Type":"DOMAIN_LOCK"
      }
   ]
}
```

## See Also
<a name="API_domains_ListOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/ListOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/ListOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/ListOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/ListOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/ListOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/ListOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/ListOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/ListOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/ListOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/ListOperations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
