---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteExperimentDefinition.html
---

# DeleteExperimentDefinition
<a name="API_DeleteExperimentDefinition"></a>

Deletes an experiment definition. You can archive the definition to hide it from the active list while preserving it for future reference, or permanently delete it along with all associated run history.

## Request Syntax
<a name="API_DeleteExperimentDefinition_RequestSyntax"></a>

```
DELETE /applications/{{ApplicationIdentifier}}/experimentdefinitions/{{ExperimentDefinitionIdentifier}}?delete_type={{DeleteType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteExperimentDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_DeleteExperimentDefinition_RequestSyntax) **   <a name="appconfig-DeleteExperimentDefinition-request-uri-ApplicationIdentifier"></a>
The application ID or name.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [DeleteType](#API_DeleteExperimentDefinition_RequestSyntax) **   <a name="appconfig-DeleteExperimentDefinition-request-uri-DeleteType"></a>
The type of deletion to perform. Valid values include archive (hide but preserve) and permanent (delete permanently).
Valid Values: `ARCHIVE | DESTROY`

 ** [ExperimentDefinitionIdentifier](#API_DeleteExperimentDefinition_RequestSyntax) **   <a name="appconfig-DeleteExperimentDefinition-request-uri-ExperimentDefinitionIdentifier"></a>
The experiment definition ID or name.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_DeleteExperimentDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteExperimentDefinition_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteExperimentDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteExperimentDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_DeleteExperimentDefinition_Examples"></a>

### Example
<a name="API_DeleteExperimentDefinition_Example_1"></a>

This example illustrates one usage of DeleteExperimentDefinition.

#### Sample Request
<a name="API_DeleteExperimentDefinition_Example_1_Request"></a>

```
DELETE /applications/abc1234/experimentdefinitions/bsxyd7k HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
User-Agent: aws-cli
X-Amz-Date: 20210916T175455Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210916/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_DeleteExperimentDefinition_Example_1_Response"></a>

```
HTTP/1.1 204 No Content
```

## See Also
<a name="API_DeleteExperimentDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/DeleteExperimentDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/DeleteExperimentDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeleteExperimentDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/DeleteExperimentDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeleteExperimentDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/DeleteExperimentDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/DeleteExperimentDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/DeleteExperimentDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/DeleteExperimentDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeleteExperimentDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
