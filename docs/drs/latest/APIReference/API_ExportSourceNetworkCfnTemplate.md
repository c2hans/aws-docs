---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ExportSourceNetworkCfnTemplate.html
---

# ExportSourceNetworkCfnTemplate
<a name="API_ExportSourceNetworkCfnTemplate"></a>

Export the Source Network CloudFormation template to an S3 bucket.

## Request Syntax
<a name="API_ExportSourceNetworkCfnTemplate_RequestSyntax"></a>

```
POST /ExportSourceNetworkCfnTemplate HTTP/1.1
Content-type: application/json

{
   "sourceNetworkID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ExportSourceNetworkCfnTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ExportSourceNetworkCfnTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sourceNetworkID](#API_ExportSourceNetworkCfnTemplate_RequestSyntax) **   <a name="drs-ExportSourceNetworkCfnTemplate-request-sourceNetworkID"></a>
The Source Network ID to export its CloudFormation template to an S3 bucket.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_ExportSourceNetworkCfnTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "s3DestinationUrl": "string"
}
```

## Response Elements
<a name="API_ExportSourceNetworkCfnTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [s3DestinationUrl](#API_ExportSourceNetworkCfnTemplate_ResponseSyntax) **   <a name="drs-ExportSourceNetworkCfnTemplate-response-s3DestinationUrl"></a>
S3 bucket URL where the Source Network CloudFormation template was exported to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.

## Errors
<a name="API_ExportSourceNetworkCfnTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_ExportSourceNetworkCfnTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/ExportSourceNetworkCfnTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/ExportSourceNetworkCfnTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ExportSourceNetworkCfnTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/ExportSourceNetworkCfnTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ExportSourceNetworkCfnTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/ExportSourceNetworkCfnTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/ExportSourceNetworkCfnTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/ExportSourceNetworkCfnTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/ExportSourceNetworkCfnTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ExportSourceNetworkCfnTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
