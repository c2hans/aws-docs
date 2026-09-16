---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAccount.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# DeleteAccount
<a name="API_DeleteAccount"></a>

Deletes the specified Amazon Chime account. You must suspend all users before deleting `Team` account. You can use the [BatchSuspendUser](API_BatchSuspendUser.md) action to dodo.

For `EnterpriseLWA` and `EnterpriseAD` accounts, you must release the claimed domains for your Amazon Chime account before deletion. As soon as you release the domain, all users under that account are suspended.

Deleted accounts appear in your `Disabled` accounts list for 90 days. To restore deleted account from your `Disabled` accounts list, you must contact AWS Support.

After 90 days, deleted accounts are permanently removed from your `Disabled` accounts list.

## Request Syntax
<a name="API_DeleteAccount_RequestSyntax"></a>

```
DELETE /accounts/{{accountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_DeleteAccount_RequestSyntax) **   <a name="chime-DeleteAccount-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_DeleteAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAccount_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

 ** UnprocessableEntityException **
The request was well-formed but was unable to be followed due to semantic errors.
HTTP Status Code: 422

## Examples
<a name="API_DeleteAccount_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteAccount_Example_1"></a>

This example deletes the specified account.

#### Sample Request
<a name="API_DeleteAccount_Example_1_Request"></a>

```
DELETE /console/accounts/12a3456b-7c89-012d-3456-78901e23fg45 HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.83 Python/3.6.6 Windows/10 botocore/1.12.73 X-Amz-Date: 20190108T180112Z Authorization: AUTHPARAMS Content-Length: 0
```

#### Sample Response
<a name="API_DeleteAccount_Example_1_Response"></a>

```
HTTP/1.1 204 No Content x-amzn-RequestId: ac41c46f-e26f-4cc1-a9cf-c6056e743647 Content-Type: application/json Date: Tue, 08 Jan 2019 18:01:13 GMT Connection: keep-alive
```

## See Also
<a name="API_DeleteAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/DeleteAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/DeleteAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/DeleteAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/DeleteAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/DeleteAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/DeleteAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/DeleteAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/DeleteAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/DeleteAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/DeleteAccount)
