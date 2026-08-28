---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Use this operation to assign a resource-based policy to a CloudWatch RUM app monitor to control access to it. Each app monitor can have one resource-based policy. The maximum size of the policy is 4 KB. To learn more about using resource policies with RUM, see [Using resource-based policies with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html).

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
PUT /appmonitor/{{Name}}/policy HTTP/1.1
Content-type: application/json

{
   "PolicyDocument": "{{string}}",
   "PolicyRevisionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_PutResourcePolicy_RequestSyntax) **   <a name="cloudwatchrum-PutResourcePolicy-request-uri-Name"></a>
The name of the app monitor that you want to apply this resource-based policy to. To find the names of your app monitors, you can use the [ListAppMonitors](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListAppMonitors.html) operation.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PolicyDocument](#API_PutResourcePolicy_RequestSyntax) **   <a name="cloudwatchrum-PutResourcePolicy-request-PolicyDocument"></a>
The JSON to use as the resource policy. The document can be up to 4 KB in size. For more information about the contents and syntax for this policy, see [Using resource-based policies with CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html).
Type: String
Required: Yes

 ** [PolicyRevisionId](#API_PutResourcePolicy_RequestSyntax) **   <a name="cloudwatchrum-PutResourcePolicy-request-PolicyRevisionId"></a>
A string value that you can use to conditionally update your policy. You can provide the revision ID of your existing policy to make mutating requests against that policy.
When you assign a policy revision ID, then later requests about that policy will be rejected with an `InvalidPolicyRevisionIdException` error if they don't provide the correct current revision ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PolicyDocument": "string",
   "PolicyRevisionId": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyDocument](#API_PutResourcePolicy_ResponseSyntax) **   <a name="cloudwatchrum-PutResourcePolicy-response-PolicyDocument"></a>
The JSON policy document that you specified.
Type: String

 ** [PolicyRevisionId](#API_PutResourcePolicy_ResponseSyntax) **   <a name="cloudwatchrum-PutResourcePolicy-response-PolicyRevisionId"></a>
The policy revision ID information that you specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation attempted to create a resource that already exists.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 409

 ** InternalServerException **
Internal service exception.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
HTTP Status Code: 500

 ** InvalidPolicyRevisionIdException **
The policy revision ID that you provided doeesn't match the latest policy revision ID.
HTTP Status Code: 400

 ** MalformedPolicyDocumentException **
The policy document that you specified is not formatted correctly.
HTTP Status Code: 400

 ** PolicySizeLimitExceededException **
The policy document is too large. The limit is 4 KB.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Resource not found.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
One of the arguments for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/PutResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/PutResourcePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
