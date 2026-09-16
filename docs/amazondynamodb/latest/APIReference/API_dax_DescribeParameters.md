---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameters.html
---

# DescribeParameters
<a name="API_dax_DescribeParameters"></a>

Returns the detailed parameter list for a particular parameter group.

## Request Syntax
<a name="API_dax_DescribeParameters_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ParameterGroupName": "{{string}}",
   "Source": "{{string}}"
}
```

## Request Parameters
<a name="API_dax_DescribeParameters_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ParameterGroupName](#API_dax_DescribeParameters_RequestSyntax) **   <a name="DDB-dax_DescribeParameters-request-ParameterGroupName"></a>
The name of the parameter group.
Type: String
Required: Yes

 ** [MaxResults](#API_dax_DescribeParameters_RequestSyntax) **   <a name="DDB-dax_DescribeParameters-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
The value for `MaxResults` must be between 20 and 100.
Type: Integer
Required: No

 ** [NextToken](#API_dax_DescribeParameters_RequestSyntax) **   <a name="DDB-dax_DescribeParameters-request-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by `MaxResults`.
Type: String
Required: No

 ** [Source](#API_dax_DescribeParameters_RequestSyntax) **   <a name="DDB-dax_DescribeParameters-request-Source"></a>
How the parameter is defined. For example, `system` denotes a system-defined parameter.
Type: String
Required: No

## Response Syntax
<a name="API_dax_DescribeParameters_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Parameters": [
      {
         "AllowedValues": "string",
         "ChangeType": "string",
         "DataType": "string",
         "Description": "string",
         "IsModifiable": "string",
         "NodeTypeSpecificValues": [
            {
               "NodeType": "string",
               "Value": "string"
            }
         ],
         "ParameterName": "string",
         "ParameterType": "string",
         "ParameterValue": "string",
         "Source": "string"
      }
   ]
}
```

## Response Elements
<a name="API_dax_DescribeParameters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_dax_DescribeParameters_ResponseSyntax) **   <a name="DDB-dax_DescribeParameters-response-NextToken"></a>
Provides an identifier to allow retrieval of paginated results.
Type: String

 ** [Parameters](#API_dax_DescribeParameters_ResponseSyntax) **   <a name="DDB-dax_DescribeParameters-response-Parameters"></a>
A list of parameters within a parameter group. Each element in the list represents one parameter.
Type: Array of [Parameter](API_dax_Parameter.md) objects

## Errors
<a name="API_dax_DescribeParameters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Two or more incompatible parameters were specified.
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
<a name="API_dax_DescribeParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/DescribeParameters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/DescribeParameters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/DescribeParameters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/DescribeParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/DescribeParameters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/DescribeParameters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/DescribeParameters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/DescribeParameters)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/DescribeParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/DescribeParameters)
