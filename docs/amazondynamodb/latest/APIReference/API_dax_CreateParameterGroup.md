---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_CreateParameterGroup.html
---

# CreateParameterGroup
<a name="API_dax_CreateParameterGroup"></a>

Creates a new parameter group. A parameter group is a collection of parameters that you apply to all of the nodes in a DAX cluster.

## Request Syntax
<a name="API_dax_CreateParameterGroup_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "ParameterGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_dax_CreateParameterGroup_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ParameterGroupName](#API_dax_CreateParameterGroup_RequestSyntax) **   <a name="DDB-dax_CreateParameterGroup-request-ParameterGroupName"></a>
The name of the parameter group to apply to all of the clusters in this replication group.
Type: String
Required: Yes

 ** [Description](#API_dax_CreateParameterGroup_RequestSyntax) **   <a name="DDB-dax_CreateParameterGroup-request-Description"></a>
A description of the parameter group.
Type: String
Required: No

## Response Syntax
<a name="API_dax_CreateParameterGroup_ResponseSyntax"></a>

```
{
   "ParameterGroup": {
      "Description": "string",
      "ParameterGroupName": "string"
   }
}
```

## Response Elements
<a name="API_dax_CreateParameterGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ParameterGroup](#API_dax_CreateParameterGroup_ResponseSyntax) **   <a name="DDB-dax_CreateParameterGroup-response-ParameterGroup"></a>
Represents the output of a *CreateParameterGroup* action.
Type: [ParameterGroup](API_dax_ParameterGroup.md) object

## Errors
<a name="API_dax_CreateParameterGroup_Errors"></a>

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

 ** ParameterGroupAlreadyExistsFault **
The specified parameter group already exists.
HTTP Status Code: 400

 ** ParameterGroupQuotaExceededFault **
You have attempted to exceed the maximum number of parameter groups.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## See Also
<a name="API_dax_CreateParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/CreateParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/CreateParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/CreateParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/CreateParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/CreateParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/CreateParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/CreateParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/CreateParameterGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/CreateParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/CreateParameterGroup)
