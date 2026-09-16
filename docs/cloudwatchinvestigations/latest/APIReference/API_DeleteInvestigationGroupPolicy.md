---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_DeleteInvestigationGroupPolicy.html
---

# DeleteInvestigationGroupPolicy
<a name="API_DeleteInvestigationGroupPolicy"></a>

Removes the IAM resource policy from being associated with the investigation group that you specify.

## Request Syntax
<a name="API_DeleteInvestigationGroupPolicy_RequestSyntax"></a>

```
DELETE /investigationGroups/{{identifier}}/policy HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteInvestigationGroupPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_DeleteInvestigationGroupPolicy_RequestSyntax) **   <a name="cloudwatchinvestigations-DeleteInvestigationGroupPolicy-request-uri-identifier"></a>
Specify either the name or the ARN of the investigation group that you want to remove the policy from.
Pattern: `(?:[\-_A-Za-z0-9]{1,512}|arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16})`
Required: Yes

## Request Body
<a name="API_DeleteInvestigationGroupPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteInvestigationGroupPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteInvestigationGroupPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteInvestigationGroupPolicy_Errors"></a>

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
<a name="API_DeleteInvestigationGroupPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/DeleteInvestigationGroupPolicy)
