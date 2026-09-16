---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UpdateParameterGroup.html
---

# UpdateParameterGroup
<a name="API_dax_UpdateParameterGroup"></a>

Modifies the parameters of a parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.

## Request Syntax
<a name="API_dax_UpdateParameterGroup_RequestSyntax"></a>

```
{
   "ParameterGroupName": "{{string}}",
   "ParameterNameValues": [
      {
         "ParameterName": "{{string}}",
         "ParameterValue": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_dax_UpdateParameterGroup_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ParameterGroupName](#API_dax_UpdateParameterGroup_RequestSyntax) **   <a name="DDB-dax_UpdateParameterGroup-request-ParameterGroupName"></a>
The name of the parameter group.
Type: String
Required: Yes

 ** [ParameterNameValues](#API_dax_UpdateParameterGroup_RequestSyntax) **   <a name="DDB-dax_UpdateParameterGroup-request-ParameterNameValues"></a>
An array of name-value pairs for the parameters in the group. Each element in the array represents a single parameter.
 `record-ttl-millis` and `query-ttl-millis` are the only supported parameter names. For more details, see [Configuring TTL Settings](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings.ttl).
Type: Array of [ParameterNameValue](API_dax_ParameterNameValue.md) objects
Required: Yes

## Response Syntax
<a name="API_dax_UpdateParameterGroup_ResponseSyntax"></a>

```
{
   "ParameterGroup": {
      "Description": "string",
      "ParameterGroupName": "string"
   }
}
```

## Response Elements
<a name="API_dax_UpdateParameterGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ParameterGroup](#API_dax_UpdateParameterGroup_ResponseSyntax) **   <a name="DDB-dax_UpdateParameterGroup-response-ParameterGroup"></a>
The parameter group that has been modified.
Type: [ParameterGroup](API_dax_ParameterGroup.md) object

## Errors
<a name="API_dax_UpdateParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Two or more incompatible parameters were specified.
HTTP Status Code: 400

 ** InvalidParameterGroupStateFault **
One or more parameters in a parameter group are in an invalid state.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value for a parameter is invalid.
HTTP Status Code: 400

 ** ParameterGroupNotFoundFault **
The specified parameter group does not exist.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## See Also
<a name="API_dax_UpdateParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/UpdateParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/UpdateParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/UpdateParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/UpdateParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/UpdateParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/UpdateParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/UpdateParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/UpdateParameterGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/UpdateParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/UpdateParameterGroup)
