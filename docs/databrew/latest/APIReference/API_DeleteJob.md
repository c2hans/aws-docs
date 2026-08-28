---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DeleteJob.html
---

# DeleteJob
<a name="API_DeleteJob"></a>

Deletes the specified DataBrew job.

## Request Syntax
<a name="API_DeleteJob_RequestSyntax"></a>

```
DELETE /jobs/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DeleteJob_RequestSyntax) **   <a name="databrew-DeleteJob-request-uri-Name"></a>
The name of the job to be deleted.
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: Yes

## Request Body
<a name="API_DeleteJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_DeleteJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_DeleteJob_ResponseSyntax) **   <a name="databrew-DeleteJob-response-Name"></a>
The name of the job that you deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 240.

## Errors
<a name="API_DeleteJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DeleteJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/DeleteJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/DeleteJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DeleteJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/DeleteJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DeleteJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/DeleteJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/DeleteJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/DeleteJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/DeleteJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DeleteJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
