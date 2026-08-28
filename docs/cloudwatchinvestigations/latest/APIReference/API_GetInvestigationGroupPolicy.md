---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_GetInvestigationGroupPolicy.html
---

# GetInvestigationGroupPolicy
<a name="API_GetInvestigationGroupPolicy"></a>

Returns the JSON of the IAM resource policy associated with the specified investigation group in a string. For example, `{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"aiops.alarms.cloudwatch.amazonaws.com\"},\"Action\":[\"aiops:CreateInvestigation\",\"aiops:CreateInvestigationEvent\"],\"Resource\":\"*\",\"Condition\":{\"StringEquals\":{\"aws:SourceAccount\":\"111122223333\"},\"ArnLike\":{\"aws:SourceArn\":\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\"}}}]}`.

## Request Syntax
<a name="API_GetInvestigationGroupPolicy_RequestSyntax"></a>

```
GET /investigationGroups/{{identifier}}/policy HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInvestigationGroupPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_GetInvestigationGroupPolicy_RequestSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroupPolicy-request-uri-identifier"></a>
Specify either the name or the ARN of the investigation group that you want to view the policy of.
Pattern: `(?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16})`
Required: Yes

## Request Body
<a name="API_GetInvestigationGroupPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInvestigationGroupPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "investigationGroupArn": "string",
   "policy": "string"
}
```

## Response Elements
<a name="API_GetInvestigationGroupPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [investigationGroupArn](#API_GetInvestigationGroupPolicy_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroupPolicy-response-investigationGroupArn"></a>
The Amazon Resource Name (ARN) of the investigation group that you want to view the policy of.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}`

 ** [policy](#API_GetInvestigationGroupPolicy_ResponseSyntax) **   <a name="cloudwatchinvestigations-GetInvestigationGroupPolicy-response-policy"></a>
The policy, in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

## Errors
<a name="API_GetInvestigationGroupPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation couldn't be completed because of a conflict in resource states.
HTTP Status Code: 409

 ** ForbiddenException **
Access id denied for this operation, or this operation is not valid for the specified resource.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. You can try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits. You can try again later.
HTTP Status Code: 429

 ** ValidationException **
This operation or its parameters aren't formatted correctly.
HTTP Status Code: 400

## See Also
<a name="API_GetInvestigationGroupPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/aiops-2018-05-10/GetInvestigationGroupPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/aiops-2018-05-10/GetInvestigationGroupPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/GetInvestigationGroupPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/aiops-2018-05-10/GetInvestigationGroupPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/GetInvestigationGroupPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/aiops-2018-05-10/GetInvestigationGroupPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/aiops-2018-05-10/GetInvestigationGroupPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/aiops-2018-05-10/GetInvestigationGroupPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/aiops-2018-05-10/GetInvestigationGroupPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/GetInvestigationGroupPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch investigations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchinvestigations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
