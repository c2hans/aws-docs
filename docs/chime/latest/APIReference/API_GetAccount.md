---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAccount.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# GetAccount
<a name="API_GetAccount"></a>

Retrieves details for the specified Amazon Chime account, such as account type and supported licenses.

## Request Syntax
<a name="API_GetAccount_RequestSyntax"></a>

```
GET /accounts/{{accountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_GetAccount_RequestSyntax) **   <a name="chime-GetAccount-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Account": {
      "AccountId": "string",
      "AccountStatus": "string",
      "AccountType": "string",
      "AwsAccountId": "string",
      "CreatedTimestamp": "string",
      "DefaultLicense": "string",
      "Name": "string",
      "SigninDelegateGroups": [
         {
            "GroupName": "string"
         }
      ],
      "SupportedLicenses": [ "string" ]
   }
}
```

## Response Elements
<a name="API_GetAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Account](#API_GetAccount_ResponseSyntax) **   <a name="chime-GetAccount-response-Account"></a>
The Amazon Chime account details.
Type: [Account](API_Account.md) object

## Errors
<a name="API_GetAccount_Errors"></a>

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

## Examples
<a name="API_GetAccount_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_GetAccount_Example_1"></a>

This example retrieves details for the specified Amazon Chime account.

#### Sample Request
<a name="API_GetAccount_Example_1_Request"></a>

```
GET /console/accounts/12a3456b-7c89-012d-3456-78901e23fg45 HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.83 Python/3.6.6 Windows/10 botocore/1.12.73 X-Amz-Date: 20190108T180420Z Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_GetAccount_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: bd51dac3-b142-405c-ab02-c9d0373ca476 Content-Type: application/json Content-Length: 544 Date: Tue, 08 Jan 2019 18:04:20 GMT Connection: keep-alive {"Account": {"AccountId": "12a3456b-7c89-012d-3456-78901e23fg45","AccountStatus": "Active","AccountType": "EnterpriseDirectory","Admins": null,"AwsAccountId": "111122223333","BillingType": "SeatBilling","CreatedTimestamp": "2018-12-20T18:38:02.181Z","DefaultLicense": "Pro","DelegationStatus": "NoDelegation","DirectoryId": "d-906717dc08","Domains": null,"Groups": [{"GroupId": "basic_users","License": "Basic"}, {"GroupId": "pro_users","License": "Pro"}],"Name": "EnterpriseDirectory","Owner": null,"SupportedLicenses": ["Basic", "Pro"],"UseProTrialLicense": false} }
```

## See Also
<a name="API_GetAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/GetAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/GetAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/GetAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/GetAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/GetAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/GetAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/GetAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/GetAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/GetAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/GetAccount)
