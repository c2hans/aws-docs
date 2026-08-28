---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListFrameworks.html
---

# ListFrameworks
<a name="API_ListFrameworks"></a>

Returns a list of all frameworks for an AWS account and AWS Region.

## Request Syntax
<a name="API_ListFrameworks_RequestSyntax"></a>

```
GET /audit/frameworks?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFrameworks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListFrameworks_RequestSyntax) **   <a name="Backup-ListFrameworks-request-uri-MaxResults"></a>
The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListFrameworks_RequestSyntax) **   <a name="Backup-ListFrameworks-request-uri-NextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

## Request Body
<a name="API_ListFrameworks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFrameworks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Frameworks": [
      {
         "CreationTime": number,
         "DeploymentStatus": "string",
         "FrameworkArn": "string",
         "FrameworkDescription": "string",
         "FrameworkName": "string",
         "NumberOfControls": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFrameworks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Frameworks](#API_ListFrameworks_ResponseSyntax) **   <a name="Backup-ListFrameworks-response-Frameworks"></a>
The frameworks with details for each framework, including the framework name, Amazon Resource Name (ARN), description, number of controls, creation time, and deployment status.
Type: Array of [Framework](API_Framework.md) objects

 ** [NextToken](#API_ListFrameworks_ResponseSyntax) **   <a name="Backup-ListFrameworks-response-NextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String

## Errors
<a name="API_ListFrameworks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_ListFrameworks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListFrameworks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListFrameworks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListFrameworks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListFrameworks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListFrameworks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListFrameworks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListFrameworks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListFrameworks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListFrameworks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListFrameworks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
