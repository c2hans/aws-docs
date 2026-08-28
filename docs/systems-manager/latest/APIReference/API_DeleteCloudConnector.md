---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteCloudConnector.html
---

# DeleteCloudConnector
<a name="API_DeleteCloudConnector"></a>

Deletes a cloud connector.

## Request Syntax
<a name="API_DeleteCloudConnector_RequestSyntax"></a>

```
{
   "CloudConnectorId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCloudConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CloudConnectorId](#API_DeleteCloudConnector_RequestSyntax) **   <a name="systemsmanager-DeleteCloudConnector-request-CloudConnectorId"></a>
The ID of the cloud connector to delete.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Response Syntax
<a name="API_DeleteCloudConnector_ResponseSyntax"></a>

```
{
   "CloudConnectorId": "string"
}
```

## Response Elements
<a name="API_DeleteCloudConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudConnectorId](#API_DeleteCloudConnector_ResponseSyntax) **   <a name="systemsmanager-DeleteCloudConnector-response-CloudConnectorId"></a>
The ID of the cloud connector that was deleted.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_DeleteCloudConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
An error occurred because of a conflict with a concurrent request or the current state of the resource. Retry your request.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified parameter to be shared could not be found.
HTTP Status Code: 400

## Examples
<a name="API_DeleteCloudConnector_Examples"></a>

### Example
<a name="API_DeleteCloudConnector_Example_1"></a>

This example illustrates one usage of DeleteCloudConnector.

#### Sample Request
<a name="API_DeleteCloudConnector_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DeleteCloudConnector
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240220T232503Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240220/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 62

{
    "CloudConnectorId": "8077bdca-72e6-4cda-8fd9-09bae51454f6"
}
```

#### Sample Response
<a name="API_DeleteCloudConnector_Example_1_Response"></a>

```
{
    "CloudConnectorId": "8077bdca-72e6-4cda-8fd9-09bae51454f6"
}
```

## See Also
<a name="API_DeleteCloudConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteCloudConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteCloudConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteCloudConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteCloudConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteCloudConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteCloudConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteCloudConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteCloudConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteCloudConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteCloudConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
