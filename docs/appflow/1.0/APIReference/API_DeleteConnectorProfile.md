---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DeleteConnectorProfile.html
---

# DeleteConnectorProfile
<a name="API_DeleteConnectorProfile"></a>

 Enables you to delete an existing connector profile.

## Request Syntax
<a name="API_DeleteConnectorProfile_RequestSyntax"></a>

```
POST /delete-connector-profile HTTP/1.1
Content-type: application/json

{
   "connectorProfileName": "{{string}}",
   "forceDelete": {{boolean}}
}
```

## URI Request Parameters
<a name="API_DeleteConnectorProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteConnectorProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [connectorProfileName](#API_DeleteConnectorProfile_RequestSyntax) **   <a name="appflow-DeleteConnectorProfile-request-connectorProfileName"></a>
 The name of the connector profile. The name is unique for each `ConnectorProfile` in your account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: Yes

 ** [forceDelete](#API_DeleteConnectorProfile_RequestSyntax) **   <a name="appflow-DeleteConnectorProfile-request-forceDelete"></a>
 Indicates whether Amazon AppFlow should delete the profile, even if it is currently in use in one or more flows.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DeleteConnectorProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteConnectorProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteConnectorProfile_Errors"></a>

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
<a name="API_DeleteConnectorProfile_Examples"></a>

### Marketo
<a name="API_DeleteConnectorProfile_Example_1"></a>

This example shows a sample request and response for the `CreateConnectorProfile` API using Marketo. If `forceDelete` is false, and there are flows associated, you will see a message similar to that shown in the third sample.

#### Sample Request
<a name="API_DeleteConnectorProfile_Example_1_Request"></a>

```
{
  "connectorProfileName": "testMarketoProfile",
  "forceDelete": "true"
}
```

#### Sample Response
<a name="API_DeleteConnectorProfile_Example_1_Response"></a>

```
{
  "deleted": true,
  "flowNames": null
}
```

```
{
  "message": "Conflict executing request: Connector profile: testMarketoProfile is associated with one or more flows. If you still want to *delete* it, *then* make *delete* request *with* forceDelete flag *as* true. *Some* of the associated flows are: [myTestFlow1]"
}
```

## See Also
<a name="API_DeleteConnectorProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/DeleteConnectorProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/DeleteConnectorProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/DeleteConnectorProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/DeleteConnectorProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/DeleteConnectorProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/DeleteConnectorProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/DeleteConnectorProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/DeleteConnectorProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/DeleteConnectorProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/DeleteConnectorProfile)
