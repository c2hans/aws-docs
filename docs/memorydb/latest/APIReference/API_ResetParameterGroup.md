---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ResetParameterGroup.html
---

# ResetParameterGroup
<a name="API_ResetParameterGroup"></a>

Modifies the parameters of a parameter group to the engine or system default value. You can reset specific parameters by submitting a list of parameter names. To reset the entire parameter group, specify the AllParameters and ParameterGroupName parameters.

## Request Syntax
<a name="API_ResetParameterGroup_RequestSyntax"></a>

```
{
   "AllParameters": {{boolean}},
   "ParameterGroupName": "{{string}}",
   "ParameterNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ResetParameterGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllParameters](#API_ResetParameterGroup_RequestSyntax) **   <a name="MemoryDB-ResetParameterGroup-request-AllParameters"></a>
If true, all parameters in the parameter group are reset to their default values. If false, only the parameters listed by ParameterNames are reset to their default values.
Type: Boolean
Required: No

 ** [ParameterGroupName](#API_ResetParameterGroup_RequestSyntax) **   <a name="MemoryDB-ResetParameterGroup-request-ParameterGroupName"></a>
The name of the parameter group to reset.
Type: String
Required: Yes

 ** [ParameterNames](#API_ResetParameterGroup_RequestSyntax) **   <a name="MemoryDB-ResetParameterGroup-request-ParameterNames"></a>
An array of parameter names to reset to their default values. If AllParameters is true, do not use ParameterNames. If AllParameters is false, you must specify the name of at least one parameter to reset.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_ResetParameterGroup_ResponseSyntax"></a>

```
{
   "ParameterGroup": {
      "ARN": "string",
      "Description": "string",
      "Family": "string",
      "Name": "string"
   }
}
```

## Response Elements
<a name="API_ResetParameterGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ParameterGroup](#API_ResetParameterGroup_ResponseSyntax) **   <a name="MemoryDB-ResetParameterGroup-response-ParameterGroup"></a>
The parameter group being reset.
Type: [ParameterGroup](API_ParameterGroup.md) object

## Errors
<a name="API_ResetParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **

HTTP Status Code: 400

 ** InvalidParameterGroupStateFault **

HTTP Status Code: 400

 ** InvalidParameterValueException **

HTTP Status Code: 400

 ** ParameterGroupNotFoundFault **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_ResetParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/ResetParameterGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/ResetParameterGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/ResetParameterGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/ResetParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/ResetParameterGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/ResetParameterGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/ResetParameterGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/ResetParameterGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/ResetParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/ResetParameterGroup)
