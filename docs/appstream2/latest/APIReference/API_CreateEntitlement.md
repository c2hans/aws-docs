---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateEntitlement.html
---

# CreateEntitlement
<a name="API_CreateEntitlement"></a>

Creates a new entitlement. Entitlements control access to specific applications within a stack, based on user attributes. Entitlements apply to SAML 2.0 federated user identities. WorkSpaces Applications user pool and streaming URL users are entitled to all applications in a stack. Entitlements don't apply to the desktop stream view application, or to applications managed by a dynamic app provider using the Dynamic Application Framework.

## Request Syntax
<a name="API_CreateEntitlement_RequestSyntax"></a>

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
<a name="API_CreateEntitlement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppVisibility](#API_CreateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-CreateEntitlement-request-AppVisibility"></a>
Specifies whether all or selected apps are entitled.
Type: String
Valid Values: `ALL | ASSOCIATED`
Required: Yes

 ** [Attributes](#API_CreateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-CreateEntitlement-request-Attributes"></a>
The attributes of the entitlement.
Type: Array of [EntitlementAttribute](API_EntitlementAttribute.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [Description](#API_CreateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-CreateEntitlement-request-Description"></a>
The description of the entitlement.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Name](#API_CreateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-CreateEntitlement-request-Name"></a>
The name of the entitlement.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [StackName](#API_CreateEntitlement_RequestSyntax) **   <a name="WorkSpacesApplications-CreateEntitlement-request-StackName"></a>
The name of the stack with which the entitlement is associated.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_CreateEntitlement_ResponseSyntax"></a>

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
<a name="API_CreateEntitlement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entitlement](#API_CreateEntitlement_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateEntitlement-response-Entitlement"></a>
The entitlement.
Type: [Entitlement](API_Entitlement.md) object

## Errors
<a name="API_CreateEntitlement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntitlementAlreadyExistsException **
The entitlement already exists.
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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateEntitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateEntitlement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateEntitlement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateEntitlement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateEntitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateEntitlement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateEntitlement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateEntitlement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateEntitlement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateEntitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateEntitlement)
