---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DeleteServiceLevelObjective.html
---

# DeleteServiceLevelObjective
<a name="API_DeleteServiceLevelObjective"></a>

Deletes the specified service level objective.

## Request Syntax
<a name="API_DeleteServiceLevelObjective_RequestSyntax"></a>

```
DELETE /slo/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteServiceLevelObjective_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-DeleteServiceLevelObjective-request-uri-Id"></a>
The ARN or name of the service level objective to delete.
Pattern: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]$|^arn:(aws|aws-us-gov):application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

## Request Body
<a name="API_DeleteServiceLevelObjective_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteServiceLevelObjective_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteServiceLevelObjective_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteServiceLevelObjective_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found.
 ** ResourceId **
Can't find the resource id.
 ** ResourceType **
The resource type is not valid.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteServiceLevelObjective_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/DeleteServiceLevelObjective)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/DeleteServiceLevelObjective)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/DeleteServiceLevelObjective)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/DeleteServiceLevelObjective)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/DeleteServiceLevelObjective)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/DeleteServiceLevelObjective)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/DeleteServiceLevelObjective)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/DeleteServiceLevelObjective)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/DeleteServiceLevelObjective)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/DeleteServiceLevelObjective)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
