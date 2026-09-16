---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_PutInvestigationGroupPolicy.html
---

# PutInvestigationGroupPolicy
<a name="API_PutInvestigationGroupPolicy"></a>

Creates an IAM resource policy and assigns it to the specified investigation group.

If you create your investigation group with `CreateInvestigationGroup` and you want to enable CloudWatch alarms to create investigations and add events to investigations, you must use this operation to create a policy similar to this example.

 ` { "Version": "2008-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "aiops.alarms.cloudwatch.amazonaws.com" }, "Action": [ "aiops:CreateInvestigation", "aiops:CreateInvestigationEvent" ], "Resource": "*", "Condition": { "StringEquals": { "aws:SourceAccount": "account-id" }, "ArnLike": { "aws:SourceArn": "arn:aws:cloudwatch::123456789012:alarm:*" } } } ] } `

## Request Syntax
<a name="API_PutInvestigationGroupPolicy_RequestSyntax"></a>

```
POST /investigationGroups/{{identifier}}/policy HTTP/1.1
Content-type: application/json

{
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutInvestigationGroupPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_PutInvestigationGroupPolicy_RequestSyntax) **   <a name="cloudwatchinvestigations-PutInvestigationGroupPolicy-request-uri-identifier"></a>
Specify either the name or the ARN of the investigation group that you want to assign the policy to.
Pattern: `(?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16})`
Required: Yes

## Request Body
<a name="API_PutInvestigationGroupPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policy](#API_PutInvestigationGroupPolicy_RequestSyntax) **   <a name="cloudwatchinvestigations-PutInvestigationGroupPolicy-request-policy"></a>
The policy, in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

## Response Syntax
<a name="API_PutInvestigationGroupPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "investigationGroupArn": "string"
}
```

## Response Elements
<a name="API_PutInvestigationGroupPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [investigationGroupArn](#API_PutInvestigationGroupPolicy_ResponseSyntax) **   <a name="cloudwatchinvestigations-PutInvestigationGroupPolicy-response-investigationGroupArn"></a>
The ARN of the investigation group that will use this policy.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}`

## Errors
<a name="API_PutInvestigationGroupPolicy_Errors"></a>

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
<a name="API_PutInvestigationGroupPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/aiops-2018-05-10/PutInvestigationGroupPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/aiops-2018-05-10/PutInvestigationGroupPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/PutInvestigationGroupPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/aiops-2018-05-10/PutInvestigationGroupPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/PutInvestigationGroupPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/aiops-2018-05-10/PutInvestigationGroupPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/aiops-2018-05-10/PutInvestigationGroupPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/aiops-2018-05-10/PutInvestigationGroupPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/aiops-2018-05-10/PutInvestigationGroupPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/PutInvestigationGroupPolicy)
