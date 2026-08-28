---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateUpload.html
---

# UpdateUpload
<a name="API_UpdateUpload"></a>

Updates an uploaded test spec.

## Request Syntax
<a name="API_UpdateUpload_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "contentType": "{{string}}",
   "editContent": {{boolean}},
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateUpload_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateUpload_RequestSyntax) **   <a name="devicefarm-UpdateUpload-request-arn"></a>
The Amazon Resource Name (ARN) of the uploaded test spec.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [contentType](#API_UpdateUpload_RequestSyntax) **   <a name="devicefarm-UpdateUpload-request-contentType"></a>
The upload's content type (for example, `application/x-yaml`).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [editContent](#API_UpdateUpload_RequestSyntax) **   <a name="devicefarm-UpdateUpload-request-editContent"></a>
Set to true if the YAML file has changed and must be updated. Otherwise, set to false.
Type: Boolean
Required: No

 ** [name](#API_UpdateUpload_RequestSyntax) **   <a name="devicefarm-UpdateUpload-request-name"></a>
The upload's test spec file name. The name must not contain any forward slashes (/). The test spec file name must end with the `.yaml` or `.yml` file extension.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_UpdateUpload_ResponseSyntax"></a>

```
{
   "upload": {
      "arn": "string",
      "category": "string",
      "contentType": "string",
      "created": number,
      "message": "string",
      "metadata": "string",
      "name": "string",
      "status": "string",
      "type": "string",
      "url": "string"
   }
}
```

## Response Elements
<a name="API_UpdateUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [upload](#API_UpdateUpload_ResponseSyntax) **   <a name="devicefarm-UpdateUpload-response-upload"></a>
A test spec uploaded to Device Farm.
Type: [Upload](API_Upload.md) object

## Errors
<a name="API_UpdateUpload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/UpdateUpload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/UpdateUpload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/UpdateUpload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/UpdateUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/UpdateUpload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/UpdateUpload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/UpdateUpload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/UpdateUpload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/UpdateUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/UpdateUpload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
