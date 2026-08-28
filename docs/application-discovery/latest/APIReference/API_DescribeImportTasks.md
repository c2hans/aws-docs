---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeImportTasks.html
---

# DescribeImportTasks
<a name="API_DescribeImportTasks"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Returns an array of import tasks for your account, including status information, times, IDs, the Amazon S3 Object URL for the import file, and more.

## Request Syntax
<a name="API_DescribeImportTasks_RequestSyntax"></a>

```
{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeImportTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeImportTasks_RequestSyntax) **   <a name="DiscServ-DescribeImportTasks-request-filters"></a>
An array of name-value pairs that you provide to filter the results for the `DescribeImportTask` request to a specific subset of results. Currently, wildcard values aren't supported for filters.
Type: Array of [ImportTaskFilter](API_ImportTaskFilter.md) objects
Required: No

 ** [maxResults](#API_DescribeImportTasks_RequestSyntax) **   <a name="DiscServ-DescribeImportTasks-request-maxResults"></a>
The maximum number of results that you want this request to return, up to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeImportTasks_RequestSyntax) **   <a name="DiscServ-DescribeImportTasks-request-nextToken"></a>
The token to request a specific page of results.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeImportTasks_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tasks": [
      {
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
   ]
}
```

## Response Elements
<a name="API_DescribeImportTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeImportTasks_ResponseSyntax) **   <a name="DiscServ-DescribeImportTasks-response-nextToken"></a>
The token to request the next page of results.
Type: String

 ** [tasks](#API_DescribeImportTasks_ResponseSyntax) **   <a name="DiscServ-DescribeImportTasks-response-tasks"></a>
A returned array of import tasks that match any applied filters, up to the specified number of maximum results.
Type: Array of [ImportTask](API_ImportTask.md) objects

## Errors
<a name="API_DescribeImportTasks_Errors"></a>

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

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_DescribeImportTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/DescribeImportTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/DescribeImportTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/DescribeImportTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/DescribeImportTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/DescribeImportTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/DescribeImportTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/DescribeImportTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/DescribeImportTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/DescribeImportTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/DescribeImportTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
