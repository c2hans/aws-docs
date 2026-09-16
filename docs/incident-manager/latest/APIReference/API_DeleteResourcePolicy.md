---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DeleteResourcePolicy.html
---

# DeleteResourcePolicy
<a name="API_DeleteResourcePolicy"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Deletes the resource policy that AWS Resource Access Manager uses to share your Incident Manager resource.

## Request Syntax
<a name="API_DeleteResourcePolicy_RequestSyntax"></a>

```
POST /deleteResourcePolicy HTTP/1.1
Content-type: application/json

{
   "policyId": "{{string}}",
   "resourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policyId](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="IncidentManager-DeleteResourcePolicy-request-policyId"></a>
The ID of the resource policy you're deleting.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [resourceArn](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="IncidentManager-DeleteResourcePolicy-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource you're deleting the policy from.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Response Syntax
<a name="API_DeleteResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_DeleteResourcePolicy_Examples"></a>

### Example
<a name="API_DeleteResourcePolicy_Example_1"></a>

This example illustrates one usage of DeleteResourcePolicy.

#### Sample Request
<a name="API_DeleteResourcePolicy_Example_1_Request"></a>

```
POST /deleteResourcePolicy HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.delete-resource-policy
X-Amz-Date: 20210811T204449Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 133

{
	"policyId": "72f95d0502d05ebf6e7d2c30ee0445cf",
	"resourceArn": "arn:aws:ssm-incidents::111122223333:response-plan/example-response"
}
```

#### Sample Response
<a name="API_DeleteResourcePolicy_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/DeleteResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/DeleteResourcePolicy)
