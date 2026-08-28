---
source_url: https://docs.aws.amazon.com/cloud9/latest/APIReference/API_ListEnvironments.html
---

# ListEnvironments
<a name="API_ListEnvironments"></a>

Gets a list of AWS Cloud9 development environment identifiers.

**Important**
 AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

**Important**
 AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

## Request Syntax
<a name="API_ListEnvironments_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEnvironments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListEnvironments_RequestSyntax) **   <a name="cloud9-ListEnvironments-request-maxResults"></a>
The maximum number of environments to get identifiers for.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListEnvironments_RequestSyntax) **   <a name="cloud9-ListEnvironments-request-nextToken"></a>
During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a *next token*. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
Type: String
Required: No

## Response Syntax
<a name="API_ListEnvironments_ResponseSyntax"></a>

```
{
   "environmentIds": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentIds](#API_ListEnvironments_ResponseSyntax) **   <a name="cloud9-ListEnvironments-response-environmentIds"></a>
The list of environment identifiers.
Type: Array of strings
Pattern: `^[a-zA-Z0-9]{8,32}$`

 ** [nextToken](#API_ListEnvironments_ResponseSyntax) **   <a name="cloud9-ListEnvironments-response-nextToken"></a>
If there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a *next token*. To get the next batch of items in the list, call this operation again, adding the next token to the call.
Type: String

## Errors
<a name="API_ListEnvironments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The target request is invalid.
HTTP Status Code: 400

 ** ConflictException **
A conflict occurred.
HTTP Status Code: 400

 ** ForbiddenException **
An access permissions issue occurred.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error occurred.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit was exceeded.
HTTP Status Code: 400

 ** NotFoundException **
The target resource cannot be found.
HTTP Status Code: 400

 ** TooManyRequestsException **
Too many service requests were made over the given time period.
HTTP Status Code: 400

## Examples
<a name="API_ListEnvironments_Examples"></a>

### Example
<a name="API_ListEnvironments_Example_1"></a>

The following example gets the IDs of available AWS Cloud9 development environments.

#### Sample Request
<a name="API_ListEnvironments_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AWSCloud9WorkspaceManagementService.ListEnvironments
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>

{}
```

#### Sample Response
<a name="API_ListEnvironments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <Date>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
x-amzn-RequestId: <RequestId>
Connection: Keep-alive

{
  "environmentIds": [
    "349c86d4579e4e7298d500ff57a6b2EX",
    "45a3da47af0840f2b0c0824f5ee232EX"
  ]
}
```

## See Also
<a name="API_ListEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/ListEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloud9-2017-09-23/ListEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/ListEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/ListEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/ListEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/ListEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/ListEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/ListEnvironments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/ListEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/ListEnvironments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud9. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud9` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
