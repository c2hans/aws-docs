---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html
---

# GetOperationDetail
<a name="API_domains_GetOperationDetail"></a>

This operation returns the current status of an operation that is not completed.

## Request Syntax
<a name="API_domains_GetOperationDetail_RequestSyntax"></a>

```
{
   "OperationId": "{{string}}"
}
```

## Request Parameters
<a name="API_domains_GetOperationDetail_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OperationId](#API_domains_GetOperationDetail_RequestSyntax) **   <a name="Route53Domains-domains_GetOperationDetail-request-OperationId"></a>
The identifier for the operation for which you want to get the status. Route 53 returned the identifier in the response to the original request.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_domains_GetOperationDetail_ResponseSyntax"></a>

```
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
```

## Response Elements
<a name="API_domains_GetOperationDetail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainName](#API_domains_GetOperationDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetOperationDetail-response-DomainName"></a>
The name of a domain.
Type: String
Length Constraints: Maximum length of 255.

 ** [LastUpdatedDate](#API_domains_GetOperationDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetOperationDetail-response-LastUpdatedDate"></a>
 The date when the operation was last updated.
Type: Timestamp

 ** [Message](#API_domains_GetOperationDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetOperationDetail-response-Message"></a>
Detailed information on the status including possible errors.
Type: String

 ** [OperationId](#API_domains_GetOperationDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetOperationDetail-response-OperationId"></a>
The identifier for the operation.
Type: String
Length Constraints: Maximum length of 255.

 ** [Status](#API_domains_GetOperationDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetOperationDetail-response-Status"></a>
The current status of the requested operation in the system.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | ERROR | SUCCESSFUL | FAILED`

 ** [StatusFlag](#API_domains_GetOperationDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetOperationDetail-response-StatusFlag"></a>
 Lists any outstanding operations that require customer action. Valid values are:
+  `PENDING_ACCEPTANCE`: The operation is waiting for acceptance from the account that is receiving the domain.
+  `PENDING_CUSTOMER_ACTION`: The operation is waiting for customer action, for example, returning an email.
+  `PENDING_AUTHORIZATION`: The operation is waiting for the form of authorization. For more information, see [ResendOperationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendOperationAuthorization.html).
+  `PENDING_PAYMENT_VERIFICATION`: The operation is waiting for the payment method to validate.
+  `PENDING_SUPPORT_CASE`: The operation includes a support case and is waiting for its resolution.
Type: String
Valid Values: `PENDING_ACCEPTANCE | PENDING_CUSTOMER_ACTION | PENDING_AUTHORIZATION | PENDING_PAYMENT_VERIFICATION | PENDING_SUPPORT_CASE`

 ** [SubmittedDate](#API_domains_GetOperationDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetOperationDetail-response-SubmittedDate"></a>
The date when the request was submitted.
Type: Timestamp

 ** [Type](#API_domains_GetOperationDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetOperationDetail-response-Type"></a>
The type of operation that was requested.
Type: String
Valid Values: `REGISTER_DOMAIN | DELETE_DOMAIN | TRANSFER_IN_DOMAIN | UPDATE_DOMAIN_CONTACT | UPDATE_NAMESERVER | CHANGE_PRIVACY_PROTECTION | DOMAIN_LOCK | ENABLE_AUTORENEW | DISABLE_AUTORENEW | ADD_DNSSEC | REMOVE_DNSSEC | EXPIRE_DOMAIN | TRANSFER_OUT_DOMAIN | CHANGE_DOMAIN_OWNER | RENEW_DOMAIN | PUSH_DOMAIN | INTERNAL_TRANSFER_OUT_DOMAIN | INTERNAL_TRANSFER_IN_DOMAIN | RELEASE_TO_GANDI | TRANSFER_ON_RENEW | RESTORE_DOMAIN`

## Errors
<a name="API_domains_GetOperationDetail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

## Examples
<a name="API_domains_GetOperationDetail_Examples"></a>

### GetOperationDetail Example
<a name="API_domains_GetOperationDetail_Example_1"></a>

This example illustrates one usage of GetOperationDetail.

#### Sample Request
<a name="API_domains_GetOperationDetail_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.GetOperationDetail
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
   "OperationId":"43884ce5-e30a-4801-858f-7aa86356c127"
}
```

#### Sample Response
<a name="API_domains_GetOperationDetail_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
   "DomainName":"happierdomain.ca",
   "OperationId":"43884ce5-e30a-4801-858f-7aa86356c127",
   "Status":"WORKFLOW_IN_PROGRESS",
   "SubmittedDate" : 1402630939.057,
   "Type" : "REGISTER_DOMAIN"
}
```

## See Also
<a name="API_domains_GetOperationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/GetOperationDetail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/GetOperationDetail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/GetOperationDetail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/GetOperationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/GetOperationDetail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/GetOperationDetail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/GetOperationDetail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/GetOperationDetail)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/GetOperationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/GetOperationDetail)
