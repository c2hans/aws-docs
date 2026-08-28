---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html
---

# GetAuthorizationToken
<a name="API_GetAuthorizationToken"></a>

Retrieves an authorization token. An authorization token represents your IAM authentication credentials and can be used to access any Amazon ECR registry that your IAM principal has access to. The authorization token is valid for 12 hours.

The `authorizationToken` returned is a base64 encoded string that can be decoded and used in a `docker login` command to authenticate to a registry. The AWS CLI offers an `get-login-password` command that simplifies the login process. For more information, see [Registry authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth) in the *Amazon Elastic Container Registry User Guide*.

## Request Syntax
<a name="API_GetAuthorizationToken_RequestSyntax"></a>

```
{
   "registryIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetAuthorizationToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [registryIds](#API_GetAuthorizationToken_RequestSyntax) **   <a name="ECR-GetAuthorizationToken-request-registryIds"></a>
 *This parameter has been deprecated.*
A list of AWS account IDs that are associated with the registries for which to get AuthorizationData objects. If you do not specify a registry, the default registry is assumed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_GetAuthorizationToken_ResponseSyntax"></a>

```
{
   "authorizationData": [
      {
         "authorizationToken": "string",
         "expiresAt": number,
         "proxyEndpoint": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetAuthorizationToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizationData](#API_GetAuthorizationToken_ResponseSyntax) **   <a name="ECR-GetAuthorizationToken-response-authorizationData"></a>
A list of authorization token data objects that correspond to the `registryIds` values in the request.
The size of the authorization token returned by Amazon ECR is not fixed. We recommend that you don't make assumptions about the maximum size.
Type: Array of [AuthorizationData](API_AuthorizationData.md) objects

## Errors
<a name="API_GetAuthorizationToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

## Examples
<a name="API_GetAuthorizationToken_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_GetAuthorizationToken_Example_1"></a>

This example gets an authorization token for your default registry.

#### Sample Request
<a name="API_GetAuthorizationToken_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.GetAuthorizationToken
X-Amz-Date: 20220516T185613Z
User-Agent: aws-cli/1.9.9 Python/2.7.10 Darwin/14.5.0 botocore/1.3.9
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{}
```

#### Sample Response
<a name="API_GetAuthorizationToken_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Sun, 17 May 2022 06:56:13 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 1590
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "authorizationData": [
    {
      "authorizationToken": "QVdTOkNpQzErSHF1ZXZPcUR...",
      "expiresAt": "2022-05-17T06:56:13.652000+00:00",
      "proxyEndpoint": "https://012345678910.dkr.ecr.us-east-1.amazonaws.com"
    }
  ]
}
```

## See Also
<a name="API_GetAuthorizationToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/GetAuthorizationToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/GetAuthorizationToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/GetAuthorizationToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/GetAuthorizationToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/GetAuthorizationToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/GetAuthorizationToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/GetAuthorizationToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/GetAuthorizationToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/GetAuthorizationToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/GetAuthorizationToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
