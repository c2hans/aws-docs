---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxConnectionString.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# GetKxConnectionString
<a name="API_GetKxConnectionString"></a>

Retrieves a connection string for a user to connect to a kdb cluster. You must call this API using the same role that you have defined while creating a user.

## Request Syntax
<a name="API_GetKxConnectionString_RequestSyntax"></a>

```
GET /kx/environments/{{environmentId}}/connectionString?clusterName={{clusterName}}&userArn={{userArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetKxConnectionString_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clusterName](#API_GetKxConnectionString_RequestSyntax) **   <a name="finspace-GetKxConnectionString-request-uri-clusterName"></a>
A name of the kdb cluster.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [environmentId](#API_GetKxConnectionString_RequestSyntax) **   <a name="finspace-GetKxConnectionString-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: Yes

 ** [userArn](#API_GetKxConnectionString_RequestSyntax) **   <a name="finspace-GetKxConnectionString-request-uri-userArn"></a>
 The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:kxEnvironment/[0-9A-Za-z_-]{1,128}/kxUser/[0-9A-Za-z_-]{1,128}$`
Required: Yes

## Request Body
<a name="API_GetKxConnectionString_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetKxConnectionString_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "signedConnectionString": "string"
}
```

## Response Elements
<a name="API_GetKxConnectionString_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [signedConnectionString](#API_GetKxConnectionString_ResponseSyntax) **   <a name="finspace-GetKxConnectionString-response-signedConnectionString"></a>
The signed connection string that you can use to connect to clusters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(:|:tcps:\/\/)[a-zA-Z0-9-\.\_]+:\d+:[a-zA-Z0-9-\.\_]+:\S+$`

## Errors
<a name="API_GetKxConnectionString_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetKxConnectionString_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/GetKxConnectionString)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/GetKxConnectionString)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/GetKxConnectionString)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/GetKxConnectionString)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/GetKxConnectionString)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/GetKxConnectionString)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/GetKxConnectionString)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/GetKxConnectionString)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/GetKxConnectionString)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/GetKxConnectionString)
