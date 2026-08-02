---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteScheduledAction.html
---

# DeleteScheduledAction
<a name="API_DeleteScheduledAction"></a>

Deletes a scheduled action.

## Request Syntax
<a name="API_DeleteScheduledAction_RequestSyntax"></a>

```
{
   "scheduledActionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteScheduledAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [scheduledActionName](#API_DeleteScheduledAction_RequestSyntax) **   <a name="redshiftserverless-DeleteScheduledAction-request-scheduledActionName"></a>
The name of the scheduled action to delete.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 60.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteScheduledAction_ResponseSyntax"></a>

```
{
   "scheduledAction": {
      "endTime": number,
      "namespaceName": "string",
      "nextInvocations": [ number ],
      "roleArn": "string",
      "schedule": { ... },
      "scheduledActionDescription": "string",
      "scheduledActionName": "string",
      "scheduledActionUuid": "string",
      "startTime": number,
      "state": "string",
      "targetAction": { ... }
   }
}
```

## Response Elements
<a name="API_DeleteScheduledAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scheduledAction](#API_DeleteScheduledAction_ResponseSyntax) **   <a name="redshiftserverless-DeleteScheduledAction-response-scheduledAction"></a>
The deleted scheduled action object.
Type: [ScheduledActionResponse](API_ScheduledActionResponse.md) object

## Errors
<a name="API_DeleteScheduledAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/DeleteScheduledAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/DeleteScheduledAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/DeleteScheduledAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/DeleteScheduledAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/DeleteScheduledAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/DeleteScheduledAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/DeleteScheduledAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/DeleteScheduledAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/DeleteScheduledAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/DeleteScheduledAction)
