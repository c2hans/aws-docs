---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_EnableOrganizationAdminAccount.html
---

# EnableOrganizationAdminAccount
<a name="API_EnableOrganizationAdminAccount"></a>

Designates the Detective administrator account for the organization in the current Region.

If the account does not have Detective enabled, then enables Detective for that account and creates a new behavior graph.

Can only be called by the organization management account.

If the organization has a delegated administrator account in Organizations, then the Detective administrator account must be either the delegated administrator account or the organization management account.

If the organization does not have a delegated administrator account in Organizations, then you can choose any account in the organization. If you choose an account other than the organization management account, Detective calls Organizations to make that account the delegated administrator account for Detective. The organization management account cannot be the delegated administrator account.

## Request Syntax
<a name="API_EnableOrganizationAdminAccount_RequestSyntax"></a>

```
POST /orgs/enableAdminAccount HTTP/1.1
Content-type: application/json

{
   "AccountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_EnableOrganizationAdminAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_EnableOrganizationAdminAccount_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_EnableOrganizationAdminAccount_RequestSyntax) **   <a name="detective-EnableOrganizationAdminAccount-request-AccountId"></a>
The AWS account identifier of the account to designate as the Detective administrator account for the organization.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: Yes

## Response Syntax
<a name="API_EnableOrganizationAdminAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_EnableOrganizationAdminAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableOrganizationAdminAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request cannot be completed because too many other requests are occurring at the same time.
HTTP Status Code: 429

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## Examples
<a name="API_EnableOrganizationAdminAccount_Examples"></a>

### Example
<a name="API_EnableOrganizationAdminAccount_Example_1"></a>

This example illustrates one usage of EnableOrganizationAdminAccount.

#### Sample Request
<a name="API_EnableOrganizationAdminAccount_Example_1_Request"></a>

```
POST /orgs/enableAdminAccount HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 28
Authorization: AUTHPARAMS
X-Amz-Date: 20210923T193018Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33

{
   "AccountId": "111122223333"
}
```

### Example
<a name="API_EnableOrganizationAdminAccount_Example_2"></a>

This example illustrates one usage of EnableOrganizationAdminAccount.

#### Sample Response
<a name="API_EnableOrganizationAdminAccount_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 0
Date: Thu, 23 Sep 2021 23:07:46 GMT
x-amzn-RequestId: 397d0549-0092-11e8-a0ee-a7f9aa6e7572
Connection: Keep-alive
```

## See Also
<a name="API_EnableOrganizationAdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/EnableOrganizationAdminAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/EnableOrganizationAdminAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/EnableOrganizationAdminAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/EnableOrganizationAdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/EnableOrganizationAdminAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/EnableOrganizationAdminAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/EnableOrganizationAdminAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/EnableOrganizationAdminAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/EnableOrganizationAdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/EnableOrganizationAdminAccount)
