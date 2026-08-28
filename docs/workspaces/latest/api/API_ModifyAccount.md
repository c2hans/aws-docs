---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyAccount.html
---

# ModifyAccount
<a name="API_ModifyAccount"></a>

Modifies the configuration of Bring Your Own License (BYOL) for the specified account.

## Request Syntax
<a name="API_ModifyAccount_RequestSyntax"></a>

```
{
   "DedicatedTenancyManagementCidrRange": "{{string}}",
   "DedicatedTenancySupport": "{{string}}"
}
```

## Request Parameters
<a name="API_ModifyAccount_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DedicatedTenancyManagementCidrRange](#API_ModifyAccount_RequestSyntax) **   <a name="WorkSpaces-ModifyAccount-request-DedicatedTenancyManagementCidrRange"></a>
The IP address range, specified as an IPv4 CIDR block, for the management network interface. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block). The CIDR block size must be /16 (for example, 203.0.113.25/16). It must also be specified as available by the `ListAvailableManagementCidrRanges` operation.
Type: String
Pattern: `(^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.0\.0)(\/(16$))$`
Required: No

 ** [DedicatedTenancySupport](#API_ModifyAccount_RequestSyntax) **   <a name="WorkSpaces-ModifyAccount-request-DedicatedTenancySupport"></a>
The status of BYOL.
Type: String
Valid Values: `ENABLED`
Required: No

## Response Syntax
<a name="API_ModifyAccount_ResponseSyntax"></a>

```
{
   "Message": "string"
}
```

## Response Elements
<a name="API_ModifyAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Message](#API_ModifyAccount_ResponseSyntax) **   <a name="WorkSpaces-ModifyAccount-response-Message"></a>
The text message to describe the status of BYOL modification.
Type: String

## Errors
<a name="API_ModifyAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InvalidResourceStateException **
The state of the resource is not valid for this operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

 ** ResourceUnavailableException **
The specified resource is not available.
 ** message **
The exception error message.
 ** ResourceId **
The identifier of the resource that is not available.
HTTP Status Code: 400

## See Also
<a name="API_ModifyAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/ModifyAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/ModifyAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModifyAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/ModifyAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModifyAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/ModifyAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/ModifyAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/ModifyAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/ModifyAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModifyAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
