---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html
---

# UpdateStandardsControl
<a name="API_UpdateStandardsControl"></a>

Used to control whether an individual security standard control is enabled or disabled.

Calls to this operation return a `RESOURCE_NOT_FOUND_EXCEPTION` error when the standard subscription for the control has `StandardsControlsUpdatable` value `NOT_READY_FOR_UPDATES`.

## Request Syntax
<a name="API_UpdateStandardsControl_RequestSyntax"></a>

```
PATCH /standards/control/{{StandardsControlArn+}} HTTP/1.1
Content-type: application/json

{
   "ControlStatus": "{{string}}",
   "DisabledReason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateStandardsControl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [StandardsControlArn](#API_UpdateStandardsControl_RequestSyntax) **   <a name="securityhub-UpdateStandardsControl-request-uri-StandardsControlArn"></a>
The ARN of the security standard control to enable or disable.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdateStandardsControl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ControlStatus](#API_UpdateStandardsControl_RequestSyntax) **   <a name="securityhub-UpdateStandardsControl-request-ControlStatus"></a>
The updated status of the security standard control.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [DisabledReason](#API_UpdateStandardsControl_RequestSyntax) **   <a name="securityhub-UpdateStandardsControl-request-DisabledReason"></a>
A description of the reason why you are disabling a security standard control. If you are disabling a control, then this is required.
Type: String
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_UpdateStandardsControl_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateStandardsControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateStandardsControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_UpdateStandardsControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateStandardsControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateStandardsControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateStandardsControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateStandardsControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateStandardsControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateStandardsControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateStandardsControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateStandardsControl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateStandardsControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateStandardsControl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
