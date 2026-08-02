---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateEmailAddressAlias.html
---

# AssociateEmailAddressAlias
<a name="API_AssociateEmailAddressAlias"></a>

Associates an email address alias with an existing email address in an Connect Customer instance. This creates a forwarding relationship where emails sent to the alias email address are automatically forwarded to the primary email address.

 **Use cases**

Following are common uses cases for this API:
+  **Unified customer support**: Create multiple entry points (for example, support@example.com, help@example.com, customercare@example.com) that all forward to a single agent queue for streamlined management.
+  **Department consolidation**: Forward emails from legacy department addresses (for example, sales@example.com, info@example.com) to a centralized customer service email during organizational restructuring.
+  **Brand management**: Enable you to use familiar brand-specific email addresses that forward to the appropriate Connect Customer instance email address.

 **Important things to know**
+ Each email address can have a maximum of one alias. You cannot create multiple aliases for the same email address.
+ If the alias email address already receives direct emails, it continues to receive direct emails plus forwarded emails.
+ You cannot chain email aliases together (that is, create an alias of an alias).

 `AssociateEmailAddressAlias` does not return the following information:
+ A confirmation of the alias relationship details (you must call [DescribeEmailAddress](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeEmailAddress.html) to verify).
+ The timestamp of when the association occurred.
+ The status of the forwarding configuration.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

 **Related operations**
+  [DisassociateEmailAddressAlias](https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateEmailAddressAlias.html): Removes the alias association between two email addresses in an Connect Customer instance.
+  [DescribeEmailAddress](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeEmailAddress.html): View current alias configurations for an email address.
+  [SearchEmailAddresses](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchEmailAddresses.html): Find email addresses and their alias relationships across an instance.
+  [CreateEmailAddress](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateEmailAddress.html): Create new email addresses that can participate in alias relationships.
+  [DeleteEmailAddress](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteEmailAddress.html): Remove email addresses (automatically removes any alias relationships).
+  [UpdateEmailAddressMetadata](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateEmailAddressMetadata.html): Modify email address properties (does not affect alias relationships).

## Request Syntax
<a name="API_AssociateEmailAddressAlias_RequestSyntax"></a>

```
POST /email-addresses/{{InstanceId}}/{{EmailAddressId}}/associate-alias HTTP/1.1
Content-type: application/json

{
   "AliasConfiguration": {
      "EmailAddressId": "{{string}}"
   },
   "ClientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateEmailAddressAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailAddressId](#API_AssociateEmailAddressAlias_RequestSyntax) **   <a name="connect-AssociateEmailAddressAlias-request-uri-EmailAddressId"></a>
The identifier of the email address.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [InstanceId](#API_AssociateEmailAddressAlias_RequestSyntax) **   <a name="connect-AssociateEmailAddressAlias-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_AssociateEmailAddressAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AliasConfiguration](#API_AssociateEmailAddressAlias_RequestSyntax) **   <a name="connect-AssociateEmailAddressAlias-request-AliasConfiguration"></a>
Configuration object that specifies which email address will serve as the alias. The specified email address must already exist in the Connect Customer instance and cannot already be configured as an alias or have an alias of its own.
Type: [AliasConfiguration](API_AliasConfiguration.md) object
Required: Yes

 ** [ClientToken](#API_AssociateEmailAddressAlias_RequestSyntax) **   <a name="connect-AssociateEmailAddressAlias-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

## Response Syntax
<a name="API_AssociateEmailAddressAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateEmailAddressAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateEmailAddressAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## Examples
<a name="API_AssociateEmailAddressAlias_Examples"></a>

### Example 1: Basic alias association
<a name="API_AssociateEmailAddressAlias_Example_1"></a>

The following example creates a forwarding relationship where support@example.com (87654321-4321-4321-4321-210987654321) forwards to customerservice@example.com (11111111-2222-3333-4444-555555555555).

 **Request**

```
POST / HTTP/1.1
Host: connect.us-east-1.amazonaws.com
Content-Length: 152
X-Amz-Target: AmazonConnectService.AssociateEmailAddressAlias
X-Amz-Date: 20170705T211529Z
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20170705/us-east-1/connect/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=6bcb6a5ef9ee7585d83955e8a5c3f6d47cf581596208fc0e436fa1de26ef3f6a
Content-Type: application/x-amz-json-1.1
{
    "InstanceId": "12345678-1234-1234-1234-123456789012",
    "EmailAddressId": "87654321-4321-4321-4321-210987654321",
    "AliasConfiguration": {
        "EmailAddressId": "11111111-2222-3333-4444-555555555555"
    }
}
```

### Example 2: Alias association with client token for idempotency
<a name="API_AssociateEmailAddressAlias_Example_2"></a>

The following example response shows a safely created alias association with guaranteed idempotency for retry scenarios.

```
HTTP/1.1 200 OK
Date: Wed, 05 Jul 2017 21:15:29 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Connection: keep-alive
x-amzn-RequestId: 12345678-1234-1234-1234-123456789012
{}
```

## See Also
<a name="API_AssociateEmailAddressAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateEmailAddressAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateEmailAddressAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateEmailAddressAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateEmailAddressAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateEmailAddressAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateEmailAddressAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateEmailAddressAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateEmailAddressAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateEmailAddressAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateEmailAddressAlias)
