---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateEntitlement.html
---

# UpdateEntitlement
<a name="API_UpdateEntitlement"></a>

Updates the specified entitlement.

## Request Syntax
<a name="API_UpdateEntitlement_RequestSyntax"></a>

```
{
   "AppVisibility": "{{string}}",
   "Attributes": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Description": "{{string}}",
   "Name": "{{string}}",
   "StackName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEntitlement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppVisibility](#API_UpdateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateEntitlement-request-AppVisibility"></a>
Specifies whether all or only selected apps are entitled.
Type: String
Valid Values: `ALL | ASSOCIATED`
Required: No

 ** [Attributes](#API_UpdateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateEntitlement-request-Attributes"></a>
The attributes of the entitlement.
Type: Array of [EntitlementAttribute](API_EntitlementAttribute.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [Description](#API_UpdateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateEntitlement-request-Description"></a>
The description of the entitlement.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Name](#API_UpdateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateEntitlement-request-Name"></a>
The name of the entitlement.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [StackName](#API_UpdateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateEntitlement-request-StackName"></a>
The name of the stack with which the entitlement is associated.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_UpdateEntitlement_ResponseSyntax"></a>

```
{
   "Entitlement": {
      "AppVisibility": "string",
      "Attributes": [
         {
            "Name": "string",
            "Value": "string"
         }
      ],
      "CreatedTime": number,
      "Description": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "StackName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateEntitlement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entitlement](#API_UpdateEntitlement_ResponseSyntax) **   <a name="WorkSpacesApplications-UpdateEntitlement-response-Entitlement"></a>
The entitlement.
Type: [Entitlement](API_Entitlement.md) object

## Errors
<a name="API_UpdateEntitlement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** EntitlementNotFoundException **
The entitlement can't be found.
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
<a name="API_UpdateEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/UpdateEntitlement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/UpdateEntitlement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UpdateEntitlement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/UpdateEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UpdateEntitlement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/UpdateEntitlement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/UpdateEntitlement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/UpdateEntitlement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/UpdateEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UpdateEntitlement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
