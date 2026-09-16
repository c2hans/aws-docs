---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ListServers.html
---

# ListServers
<a name="API_ListServers"></a>

Lists the file transfer protocol-enabled servers that are associated with your AWS account.

## Request Syntax
<a name="API_ListServers_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListServers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListServers_RequestSyntax) **   <a name="TransferFamily-ListServers-request-MaxResults"></a>
Specifies the number of servers to return as a response to the `ListServers` query.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListServers_RequestSyntax) **   <a name="TransferFamily-ListServers-request-NextToken"></a>
When additional results are obtained from the `ListServers` command, a `NextToken` parameter is returned in the output. You can then pass the `NextToken` parameter in a subsequent command to continue listing additional servers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: No

## Response Syntax
<a name="API_ListServers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Servers": [
      {
         "Arn": "string",
         "Domain": "string",
         "EndpointType": "string",
         "IdentityProviderType": "string",
         "LoggingRole": "string",
         "ServerId": "string",
         "State": "string",
         "UserCount": number
      }
   ]
}
```

## Response Elements
<a name="API_ListServers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListServers_ResponseSyntax) **   <a name="TransferFamily-ListServers-response-NextToken"></a>
When you can get additional results from the `ListServers` operation, a `NextToken` parameter is returned in the output. In a following command, you can pass in the `NextToken` parameter to continue listing additional servers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [Servers](#API_ListServers_ResponseSyntax) **   <a name="TransferFamily-ListServers-response-Servers"></a>
An array of servers that were listed.
Type: Array of [ListedServer](API_ListedServer.md) objects

## Errors
<a name="API_ListServers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidNextTokenException **
The `NextToken` parameter that was passed is invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed because the AWSTransfer Family service is not available.
HTTP Status Code: 500

## Examples
<a name="API_ListServers_Examples"></a>

### Example
<a name="API_ListServers_Example_1"></a>

The following example lists the servers that exist in your AWS account.

Note that the example `NextToken` values are not real: they are meant to indicate how to use the parameter.

#### Sample Request
<a name="API_ListServers_Example_1_Request"></a>

```
{
   "MaxResults": 1,
   "NextToken": "token-from-previous-API-call"
}
```

#### Sample Response
<a name="API_ListServers_Example_1_Response"></a>

```
{
   "NextToken": "another-token-to-continue-listing",
   "Servers": [
      {
         "Arn": "arn:aws:transfer:us-east-1:111112222222:server/s-01234567890abcdef",
         "Domain": "S3",
         "IdentityProviderType": "SERVICE_MANAGED",
         "EndpointType": "PUBLIC",
         "LoggingRole": "arn:aws:iam::111112222222:role/my-role",
         "ServerId": "s-01234567890abcdef",
         "State": "ONLINE",
         "UserCount": 3
      }
   ]
}
```

## See Also
<a name="API_ListServers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/ListServers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/ListServers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ListServers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/ListServers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ListServers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/ListServers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/ListServers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/ListServers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/ListServers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ListServers)
