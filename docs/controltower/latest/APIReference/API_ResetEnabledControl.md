---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledControl.html
---

# ResetEnabledControl
<a name="API_ResetEnabledControl"></a>

Resets an enabled control. Does not work for controls implemented with SCPs.

## Request Syntax
<a name="API_ResetEnabledControl_RequestSyntax"></a>

```
POST /reset-enabled-control HTTP/1.1
Content-type: application/json

{
   "enabledControlIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ResetEnabledControl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ResetEnabledControl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [enabledControlIdentifier](#API_ResetEnabledControl_RequestSyntax) **   <a name="controltower-ResetEnabledControl-request-enabledControlIdentifier"></a>
The ARN of the enabled control to be reset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: Yes

## Response Syntax
<a name="API_ResetEnabledControl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "operationIdentifier": "string"
}
```

## Response Elements
<a name="API_ResetEnabledControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operationIdentifier](#API_ResetEnabledControl_ResponseSyntax) **   <a name="controltower-ResetEnabledControl-response-operationIdentifier"></a>
 The operation identifier for this `ResetEnabledControl` operation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_ResetEnabledControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting the resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded. See [Service quotas](https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html).
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ResetEnabledControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/ResetEnabledControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/ResetEnabledControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ResetEnabledControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/ResetEnabledControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ResetEnabledControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/ResetEnabledControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/ResetEnabledControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/ResetEnabledControl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ResetEnabledControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ResetEnabledControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
