---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_DeleteConfigurationManager.html
---

# DeleteConfigurationManager
<a name="API_DeleteConfigurationManager"></a>

Deletes a configuration manager.

## Request Syntax
<a name="API_DeleteConfigurationManager_RequestSyntax"></a>

```
DELETE /configurationManager/{{ManagerArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteConfigurationManager_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ManagerArn](#API_DeleteConfigurationManager_RequestSyntax) **   <a name="quicksetup-DeleteConfigurationManager-request-uri-ManagerArn"></a>
The ID of the configuration manager.
Pattern: `arn:aws(-cn|-us-gov)?:ssm-quicksetup:([^:]+):(\d{12}):configuration-manager/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}`
Required: Yes

## Request Body
<a name="API_DeleteConfigurationManager_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteConfigurationManager_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteConfigurationManager_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteConfigurationManager_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requester has insufficient permissions to perform the operation.
HTTP Status Code: 403

 ** ConflictException **
Another request is being processed. Wait a few minutes and try again.
HTTP Status Code: 409

 ** InternalServerException **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found. Check the ID or name and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request or operation exceeds the maximum allowed request rate per AWS account and AWS Region.
HTTP Status Code: 429

 ** ValidationException **
The request is invalid. Verify the values provided for the request parameters are accurate.
HTTP Status Code: 400

## See Also
<a name="API_DeleteConfigurationManager_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/DeleteConfigurationManager)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quick Setup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick-setup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
