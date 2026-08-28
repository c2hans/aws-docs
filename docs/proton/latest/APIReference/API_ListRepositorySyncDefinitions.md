---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListRepositorySyncDefinitions.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListRepositorySyncDefinitions
<a name="API_ListRepositorySyncDefinitions"></a>

List repository sync definitions with detail data.

## Request Syntax
<a name="API_ListRepositorySyncDefinitions_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}",
   "repositoryName": "{{string}}",
   "repositoryProvider": "{{string}}",
   "syncType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRepositorySyncDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListRepositorySyncDefinitions_RequestSyntax) **   <a name="proton-ListRepositorySyncDefinitions-request-nextToken"></a>
A token that indicates the location of the next repository sync definition in the array of repository sync definitions, after the list of repository sync definitions previously requested.
Type: String
Length Constraints: Fixed length of 0.
Required: No

 ** [repositoryName](#API_ListRepositorySyncDefinitions_RequestSyntax) **   <a name="proton-ListRepositorySyncDefinitions-request-repositoryName"></a>
The repository name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[A-Za-z0-9_.-].*/[A-Za-z0-9_.-].*`
Required: Yes

 ** [repositoryProvider](#API_ListRepositorySyncDefinitions_RequestSyntax) **   <a name="proton-ListRepositorySyncDefinitions-request-repositoryProvider"></a>
The repository provider.
Type: String
Valid Values: `GITHUB | GITHUB_ENTERPRISE | BITBUCKET`
Required: Yes

 ** [syncType](#API_ListRepositorySyncDefinitions_RequestSyntax) **   <a name="proton-ListRepositorySyncDefinitions-request-syncType"></a>
The sync type. The only supported value is `TEMPLATE_SYNC`.
Type: String
Valid Values: `TEMPLATE_SYNC | SERVICE_SYNC`
Required: Yes

## Response Syntax
<a name="API_ListRepositorySyncDefinitions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "syncDefinitions": [
      {
         "branch": "string",
         "directory": "string",
         "parent": "string",
         "target": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRepositorySyncDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRepositorySyncDefinitions_ResponseSyntax) **   <a name="proton-ListRepositorySyncDefinitions-response-nextToken"></a>
A token that indicates the location of the next repository sync definition in the array of repository sync definitions, after the current requested list of repository sync definitions.
Type: String
Length Constraints: Fixed length of 0.

 ** [syncDefinitions](#API_ListRepositorySyncDefinitions_ResponseSyntax) **   <a name="proton-ListRepositorySyncDefinitions-response-syncDefinitions"></a>
An array of repository sync definitions.
Type: Array of [RepositorySyncDefinition](API_RepositorySyncDefinition.md) objects

## Errors
<a name="API_ListRepositorySyncDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ListRepositorySyncDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListRepositorySyncDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListRepositorySyncDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListRepositorySyncDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListRepositorySyncDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListRepositorySyncDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListRepositorySyncDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListRepositorySyncDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListRepositorySyncDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListRepositorySyncDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListRepositorySyncDefinitions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
