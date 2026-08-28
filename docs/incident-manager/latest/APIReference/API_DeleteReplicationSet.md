---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_DeleteReplicationSet.html
---

# DeleteReplicationSet
<a name="API_DeleteReplicationSet"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Deletes all Regions in your replication set. Deleting the replication set deletes all Incident Manager data.

## Request Syntax
<a name="API_DeleteReplicationSet_RequestSyntax"></a>

```
POST /deleteReplicationSet?arn={{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteReplicationSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_DeleteReplicationSet_RequestSyntax) **   <a name="IncidentManager-DeleteReplicationSet-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the replication set you're deleting.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Request Body
<a name="API_DeleteReplicationSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteReplicationSet_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteReplicationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteReplicationSet_Errors"></a>

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
<a name="API_DeleteReplicationSet_Examples"></a>

### Example
<a name="API_DeleteReplicationSet_Example_1"></a>

This example illustrates one usage of DeleteReplicationSet.

#### Sample Request
<a name="API_DeleteReplicationSet_Example_1_Request"></a>

```
POST /deleteReplicationSet?arn=arn%3Aaws%3Assm-incidents%3A%111122223333%3Areplication-set%2F40bd98f0-4110-2dee-b35e-b87006f9e172 HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.delete-replication-set
X-Amz-Date: 20210811T215946Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_DeleteReplicationSet_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteReplicationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/DeleteReplicationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/DeleteReplicationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/DeleteReplicationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/DeleteReplicationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/DeleteReplicationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/DeleteReplicationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/DeleteReplicationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/DeleteReplicationSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/DeleteReplicationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/DeleteReplicationSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
