---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartImportTask.html
---

# StartImportTask
<a name="API_StartImportTask"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Starts an import task, which allows you to import details of your on-premises environment directly into AWS Migration Hub without having to use the AWS Application Discovery Service (Application Discovery Service) tools such as the AWS Application Discovery Service Agentless Collector or Application Discovery Agent. This gives you the option to perform migration assessment and planning directly from your imported data, including the ability to group your devices as applications and track their migration status.

To start an import request, do this:

1. Download the specially formatted comma separated value (CSV) import template, which you can find here: [https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import\_template.csv](https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv).

1. Fill out the template with your server and application data.

1. Upload your import file to an Amazon S3 bucket, and make a note of it's Object URL. Your import file must be in the CSV format.

1. Use the console or the `StartImportTask` command with the AWS CLI or one of the AWS SDKs to import the records from your file.

For more information, including step-by-step procedures, see [Migration Hub Import](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html) in the * AWS Application Discovery Service User Guide*.

**Note**
There are limits to the number of import tasks you can create (and delete) in an AWS account. For more information, see [AWS Application Discovery Service Limits](https://docs.aws.amazon.com/application-discovery/latest/userguide/ads_service_limits.html) in the * AWS Application Discovery Service User Guide*.

## Request Syntax
<a name="API_StartImportTask_RequestSyntax"></a>

```
{
   "clientRequestToken": "{{string}}",
   "importUrl": "{{string}}",
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_StartImportTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_StartImportTask_RequestSyntax) **   <a name="DiscServ-StartImportTask-request-clientRequestToken"></a>
Optional. A unique token that you can provide to prevent the same import request from occurring more than once. If you don't provide a token, a token is automatically generated.
Sending more than one `StartImportTask` request with the same client request token will return information about the original import task with that client request token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [importUrl](#API_StartImportTask_RequestSyntax) **   <a name="DiscServ-StartImportTask-request-importUrl"></a>
The URL for your import file that you've uploaded to Amazon S3.
If you're using the AWS CLI, this URL is structured as follows: `s3://BucketName/ImportFileName.CSV`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `\S+://\S+/[\s\S]*\S[\s\S]*`
Required: Yes

 ** [name](#API_StartImportTask_RequestSyntax) **   <a name="DiscServ-StartImportTask-request-name"></a>
A descriptive name for this request. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task. We recommend that you use a meaningful name for each import task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_StartImportTask_ResponseSyntax"></a>

```
{
   "task": {
      "applicationImportFailure": number,
      "applicationImportSuccess": number,
      "clientRequestToken": "string",
      "errorsAndFailedEntriesZip": "string",
      "fileClassification": "string",
      "importCompletionTime": number,
      "importDeletedTime": number,
      "importRequestTime": number,
      "importTaskId": "string",
      "importUrl": "string",
      "name": "string",
      "serverImportFailure": number,
      "serverImportSuccess": number,
      "status": "string"
   }
}
```

## Response Elements
<a name="API_StartImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [task](#API_StartImportTask_ResponseSyntax) **   <a name="DiscServ-StartImportTask-response-task"></a>
An array of information related to the import task request including status information, times, IDs, the Amazon S3 Object URL for the import file, and more.
Type: [ImportTask](API_ImportTask.md) object

## Errors
<a name="API_StartImportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** ResourceInUseException **
This issue occurs when the same `clientRequestToken` is used with the `StartImportTask` action, but with different parameters. For example, you use the same request token but have two different import URLs, you can encounter this issue. If the import tasks are meant to be different, use a different `clientRequestToken`, and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_StartImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/StartImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/StartImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/StartImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/StartImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/StartImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/StartImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/StartImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/StartImportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/StartImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/StartImportTask)
