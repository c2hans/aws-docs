---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateApplicationToEntitlement.html
---

# AssociateApplicationToEntitlement
<a name="API_AssociateApplicationToEntitlement"></a>

Associates an application to entitle.

## Request Syntax
<a name="API_AssociateApplicationToEntitlement_RequestSyntax"></a>

```
{
   "ApplicationIdentifier": "{{string}}",
   "EntitlementName": "{{string}}",
   "StackName": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateApplicationToEntitlement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationIdentifier](#API_AssociateApplicationToEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-AssociateApplicationToEntitlement-request-ApplicationIdentifier"></a>
The identifier of the application.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [EntitlementName](#API_AssociateApplicationToEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-AssociateApplicationToEntitlement-request-EntitlementName"></a>
The name of the entitlement.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [StackName](#API_AssociateApplicationToEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-AssociateApplicationToEntitlement-request-StackName"></a>
The name of the stack.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Elements
<a name="API_AssociateApplicationToEntitlement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateApplicationToEntitlement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntitlementNotFoundException **
The entitlement can't be found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_AssociateApplicationToEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/AssociateApplicationToEntitlement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/AssociateApplicationToEntitlement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AssociateApplicationToEntitlement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/AssociateApplicationToEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AssociateApplicationToEntitlement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/AssociateApplicationToEntitlement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/AssociateApplicationToEntitlement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/AssociateApplicationToEntitlement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/AssociateApplicationToEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AssociateApplicationToEntitlement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
