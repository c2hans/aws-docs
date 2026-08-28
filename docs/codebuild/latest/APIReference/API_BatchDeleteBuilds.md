---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchDeleteBuilds.html
---

# BatchDeleteBuilds
<a name="API_BatchDeleteBuilds"></a>

Deletes one or more builds.

## Request Syntax
<a name="API_BatchDeleteBuilds_RequestSyntax"></a>

```
{
   "ids": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchDeleteBuilds_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ids](#API_BatchDeleteBuilds_RequestSyntax) **   <a name="CodeBuild-BatchDeleteBuilds-request-ids"></a>
The IDs of the builds to delete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_BatchDeleteBuilds_ResponseSyntax"></a>

```
{
   "buildsDeleted": [ "string" ],
   "buildsNotDeleted": [
      {
         "id": "string",
         "statusCode": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteBuilds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [buildsDeleted](#API_BatchDeleteBuilds_ResponseSyntax) **   <a name="CodeBuild-BatchDeleteBuilds-response-buildsDeleted"></a>
The IDs of the builds that were successfully deleted.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1.

 ** [buildsNotDeleted](#API_BatchDeleteBuilds_ResponseSyntax) **   <a name="CodeBuild-BatchDeleteBuilds-response-buildsNotDeleted"></a>
Information about any builds that could not be successfully deleted.
Type: Array of [BuildNotDeleted](API_BuildNotDeleted.md) objects

## Errors
<a name="API_BatchDeleteBuilds_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteBuilds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/BatchDeleteBuilds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/BatchDeleteBuilds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BatchDeleteBuilds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/BatchDeleteBuilds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BatchDeleteBuilds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/BatchDeleteBuilds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/BatchDeleteBuilds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/BatchDeleteBuilds)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/BatchDeleteBuilds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BatchDeleteBuilds)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
