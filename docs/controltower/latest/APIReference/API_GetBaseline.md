---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaseline.html
---

# GetBaseline
<a name="API_GetBaseline"></a>

Retrieve details about an existing `Baseline` resource by specifying its identifier. For usage examples, see [*the AWS Control Tower User Guide*](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html).

## Request Syntax
<a name="API_GetBaseline_RequestSyntax"></a>

```
POST /get-baseline HTTP/1.1
Content-type: application/json

{
   "baselineIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetBaseline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetBaseline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [baselineIdentifier](#API_GetBaseline_RequestSyntax) **   <a name="controltower-GetBaseline-request-baselineIdentifier"></a>
The ARN of the `Baseline` resource to be retrieved.
Type: String
Pattern: `arn:[a-z-]+:controltower:[a-z0-9-]*:[0-9]{0,12}:baseline/[A-Z0-9]{16}`
Required: Yes

## Response Syntax
<a name="API_GetBaseline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "description": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_GetBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetBaseline_ResponseSyntax) **   <a name="controltower-GetBaseline-response-arn"></a>
The baseline ARN.
Type: String
Pattern: `arn:[a-z-]+:controltower:[a-z0-9-]*:[0-9]{0,12}:baseline/[A-Z0-9]{16}`

 ** [description](#API_GetBaseline_ResponseSyntax) **   <a name="controltower-GetBaseline-response-description"></a>
A description of the baseline.
Type: String

 ** [name](#API_GetBaseline_ResponseSyntax) **   <a name="controltower-GetBaseline-response-name"></a>
A user-friendly name for the baseline.
Type: String

## Errors
<a name="API_GetBaseline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/GetBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/GetBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/GetBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/GetBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/GetBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/GetBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/GetBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/GetBaseline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/GetBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/GetBaseline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
