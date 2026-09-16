---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UnregisterConnector.html
---

# UnregisterConnector
<a name="API_UnregisterConnector"></a>

Unregisters the custom connector registered in your account that matches the connector label provided in the request.

## Request Syntax
<a name="API_UnregisterConnector_RequestSyntax"></a>

```
POST /unregister-connector HTTP/1.1
Content-type: application/json

{
   "connectorLabel": "{{string}}",
   "forceDelete": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UnregisterConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UnregisterConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [connectorLabel](#API_UnregisterConnector_RequestSyntax) **   <a name="appflow-UnregisterConnector-request-connectorLabel"></a>
The label of the connector. The label is unique for each `ConnectorRegistration` in your AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: Yes

 ** [forceDelete](#API_UnregisterConnector_RequestSyntax) **   <a name="appflow-UnregisterConnector-request-forceDelete"></a>
Indicates whether Amazon AppFlow should unregister the connector, even if it is currently in use in one or more connector profiles. The default value is false.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UnregisterConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UnregisterConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UnregisterConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
 There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again.
HTTP Status Code: 409

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

## Examples
<a name="API_UnregisterConnector_Examples"></a>

### Unregister connectors
<a name="API_UnregisterConnector_Example_1"></a>

This example shows a sample request for the `UnregisterConnector` API and a sample response.

#### Sample Request
<a name="API_UnregisterConnector_Example_1_Request"></a>

```
{
  "connectorLabel": "MySampleCustomConnector",
  "forceDelete": true
}
```

```
{
  "message": "Conflict executing request: Connector: MySampleCustomConnector is associated with one or more connector profiles. If you still want to *delete* it, *then* make *delete* request *with* forceDelete flag *as* true. *Some* of the associated connector profiles are: [myTestProfile1, myTestProfile2]"
}
```

## See Also
<a name="API_UnregisterConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/UnregisterConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/UnregisterConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/UnregisterConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/UnregisterConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/UnregisterConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/UnregisterConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/UnregisterConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/UnregisterConnector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/UnregisterConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/UnregisterConnector)
