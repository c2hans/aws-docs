---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProjectPolicy.html
---

# DeleteProjectPolicy
<a name="API_DeleteProjectPolicy"></a>

**Note**
This operation applies only to Amazon Rekognition Custom Labels.

Deletes an existing project policy.

To get a list of project policies attached to a project, call [ListProjectPolicies](API_ListProjectPolicies.md). To attach a project policy to a project, call [PutProjectPolicy](API_PutProjectPolicy.md).

This operation requires permissions to perform the `rekognition:DeleteProjectPolicy` action.

## Request Syntax
<a name="API_DeleteProjectPolicy_RequestSyntax"></a>

```
{
   "PolicyName": "{{string}}",
   "PolicyRevisionId": "{{string}}",
   "ProjectArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteProjectPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PolicyName](#API_DeleteProjectPolicy_RequestSyntax) **   <a name="rekognition-DeleteProjectPolicy-request-PolicyName"></a>
The name of the policy that you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [PolicyRevisionId](#API_DeleteProjectPolicy_RequestSyntax) **   <a name="rekognition-DeleteProjectPolicy-request-PolicyRevisionId"></a>
The ID of the project policy revision that you want to delete.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[0-9A-Fa-f]+`
Required: No

 ** [ProjectArn](#API_DeleteProjectPolicy_RequestSyntax) **   <a name="rekognition-DeleteProjectPolicy-request-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project that the project policy you want to delete is attached to.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: Yes

## Response Elements
<a name="API_DeleteProjectPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteProjectPolicy_Errors"></a>

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

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_DeleteProjectPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/DeleteProjectPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/DeleteProjectPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DeleteProjectPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/DeleteProjectPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DeleteProjectPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/DeleteProjectPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/DeleteProjectPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DeleteProjectPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DeleteProjectPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DeleteProjectPolicy)
