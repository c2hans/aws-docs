---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeHub.html
---

# DescribeHub
<a name="API_DescribeHub"></a>

Returns details about the Hub resource in your account, including the `HubArn` and the time when you enabled Security Hub CSPM.

## Request Syntax
<a name="API_DescribeHub_RequestSyntax"></a>

```
GET /accounts?HubArn={{HubArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeHub_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HubArn](#API_DescribeHub_RequestSyntax) **   <a name="securityhub-DescribeHub-request-uri-HubArn"></a>
The ARN of the Hub resource to retrieve.
Pattern: `.*\S.*`

## Request Body
<a name="API_DescribeHub_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeHub_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AutoEnableControls": boolean,
   "ControlFindingGenerator": "string",
   "HubArn": "string",
   "SubscribedAt": "string"
}
```

## Response Elements
<a name="API_DescribeHub_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoEnableControls](#API_DescribeHub_ResponseSyntax) **   <a name="securityhub-DescribeHub-response-AutoEnableControls"></a>
Whether to automatically enable new controls when they are added to standards that are enabled.
If set to `true`, then new controls for enabled standards are enabled automatically. If set to `false`, then new controls are not enabled.
When you automatically enable new controls, you can interact with the controls in the console and programmatically immediately after release. However, automatically enabled controls have a temporary default status of `DISABLED`. It can take up to several days for Security Hub CSPM to process the control release and designate the control as `ENABLED` in your account. During the processing period, you can manually enable or disable a control, and Security Hub CSPM will maintain that designation regardless of whether you have `AutoEnableControls` set to `true`.
Type: Boolean

 ** [ControlFindingGenerator](#API_DescribeHub_ResponseSyntax) **   <a name="securityhub-DescribeHub-response-ControlFindingGenerator"></a>
Specifies whether the calling account has consolidated control findings turned on. If the value for this field is set to `SECURITY_CONTROL`, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.
If the value for this field is set to `STANDARD_CONTROL`, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.
The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is `SECURITY_CONTROL` if you enabled Security Hub CSPM on or after February 23, 2023.
Type: String
Valid Values: `STANDARD_CONTROL | SECURITY_CONTROL`

 ** [HubArn](#API_DescribeHub_ResponseSyntax) **   <a name="securityhub-DescribeHub-response-HubArn"></a>
The ARN of the Hub resource that was retrieved.
Type: String
Pattern: `.*\S.*`

 ** [SubscribedAt](#API_DescribeHub_ResponseSyntax) **   <a name="securityhub-DescribeHub-response-SubscribedAt"></a>
The date and time when Security Hub CSPM was enabled in the account.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_DescribeHub_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_DescribeHub_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DescribeHub)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DescribeHub)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DescribeHub)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DescribeHub)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DescribeHub)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DescribeHub)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DescribeHub)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DescribeHub)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DescribeHub)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DescribeHub)
