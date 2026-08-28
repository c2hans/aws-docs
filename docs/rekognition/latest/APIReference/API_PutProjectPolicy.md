---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PutProjectPolicy.html
---

# PutProjectPolicy
<a name="API_PutProjectPolicy"></a>

**Note**
This operation applies only to Amazon Rekognition Custom Labels.

Attaches a project policy to a Amazon Rekognition Custom Labels project in a trusting AWS account. A project policy specifies that a trusted AWS account can copy a model version from a trusting AWS account to a project in the trusted AWS account. To copy a model version you use the [CopyProjectVersion](API_CopyProjectVersion.md) operation. Only applies to Custom Labels projects.

For more information about the format of a project policy document, see [Attaching a project policy (SDK)](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-attach-project-policy.html).

The response from `PutProjectPolicy` is a revision ID for the project policy. You can attach multiple project policies to a project. You can also update an existing project policy by specifying the policy revision ID of the existing policy.

To remove a project policy from a project, call [DeleteProjectPolicy](API_DeleteProjectPolicy.md). To get a list of project policies attached to a project, call [ListProjectPolicies](API_ListProjectPolicies.md).

You copy a model version by calling [CopyProjectVersion](API_CopyProjectVersion.md).

This operation requires permissions to perform the `rekognition:PutProjectPolicy` action.

## Request Syntax
<a name="API_PutProjectPolicy_RequestSyntax"></a>

```
{
   "PolicyDocument": "{{string}}",
   "PolicyName": "{{string}}",
   "PolicyRevisionId": "{{string}}",
   "ProjectArn": "{{string}}"
}
```

## Request Parameters
<a name="API_PutProjectPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PolicyDocument](#API_PutProjectPolicy_RequestSyntax) **   <a name="rekognition-PutProjectPolicy-request-PolicyDocument"></a>
A resource policy to add to the model. The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow the IAM syntax. For more information about the contents of a JSON policy document, see [IAM JSON policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 ** [PolicyName](#API_PutProjectPolicy_RequestSyntax) **   <a name="rekognition-PutProjectPolicy-request-PolicyName"></a>
A name for the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [PolicyRevisionId](#API_PutProjectPolicy_RequestSyntax) **   <a name="rekognition-PutProjectPolicy-request-PolicyRevisionId"></a>
The revision ID for the Project Policy. Each time you modify a policy, Amazon Rekognition Custom Labels generates and assigns a new `PolicyRevisionId` and then deletes the previous version of the policy.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[0-9A-Fa-f]+`
Required: No

 ** [ProjectArn](#API_PutProjectPolicy_RequestSyntax) **   <a name="rekognition-PutProjectPolicy-request-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project that the project policy is attached to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: Yes

## Response Syntax
<a name="API_PutProjectPolicy_ResponseSyntax"></a>

```
{
   "PolicyRevisionId": "string"
}
```

## Response Elements
<a name="API_PutProjectPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyRevisionId](#API_PutProjectPolicy_ResponseSyntax) **   <a name="rekognition-PutProjectPolicy-response-PolicyRevisionId"></a>
The ID of the project policy.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[0-9A-Fa-f]+`

## Errors
<a name="API_PutProjectPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** InvalidPolicyRevisionIdException **
The supplied revision id for the project policy is invalid.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: `StartLabelDetection`) will raise a `LimitExceededException` exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit.
HTTP Status Code: 400

 ** MalformedPolicyDocumentException **
The format of the project policy document that you supplied to `PutProjectPolicy` is incorrect.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
A resource with the specified ID already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

The size of the resource exceeds the allowed limit. For more information, see [Guidelines and quotas in Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html).
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_PutProjectPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/PutProjectPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/PutProjectPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/PutProjectPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/PutProjectPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/PutProjectPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/PutProjectPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/PutProjectPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/PutProjectPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/PutProjectPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/PutProjectPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
