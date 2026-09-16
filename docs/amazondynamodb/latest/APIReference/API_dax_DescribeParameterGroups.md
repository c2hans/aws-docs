---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeParameterGroups.html
---

# DescribeParameterGroups
<a name="API_dax_DescribeParameterGroups"></a>

Returns a list of parameter group descriptions. If a parameter group name is specified, the list will contain only the descriptions for that group.

## Request Syntax
<a name="API_dax_DescribeParameterGroups_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ParameterGroupNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_dax_DescribeParameterGroups_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [MaxResults](#API_dax_DescribeParameterGroups_RequestSyntax) **   <a name="DDB-dax_DescribeParameterGroups-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
The value for `MaxResults` must be between 20 and 100.
Type: Integer
Required: No

 ** [NextToken](#API_dax_DescribeParameterGroups_RequestSyntax) **   <a name="DDB-dax_DescribeParameterGroups-request-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by `MaxResults`.
Type: String
Required: No

 ** [ParameterGroupNames](#API_dax_DescribeParameterGroups_RequestSyntax) **   <a name="DDB-dax_DescribeParameterGroups-request-ParameterGroupNames"></a>
The names of the parameter groups.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_dax_DescribeParameterGroups_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ParameterGroups": [
      {
         "Description": "string",
         "ParameterGroupName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_dax_DescribeParameterGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_dax_DescribeParameterGroups_ResponseSyntax) **   <a name="DDB-dax_DescribeParameterGroups-response-NextToken"></a>
Provides an identifier to allow retrieval of paginated results.
Type: String

 ** [ParameterGroups](#API_dax_DescribeParameterGroups_ResponseSyntax) **   <a name="DDB-dax_DescribeParameterGroups-response-ParameterGroups"></a>
An array of parameter groups. Each element in the array represents one parameter group.
Type: Array of [ParameterGroup](API_dax_ParameterGroup.md) objects

## Errors
<a name="API_dax_DescribeParameterGroups_Errors"></a>

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
<a name="API_dax_DescribeParameterGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/DescribeParameterGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/DescribeParameterGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/DescribeParameterGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/DescribeParameterGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/DescribeParameterGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/DescribeParameterGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/DescribeParameterGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/DescribeParameterGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/DescribeParameterGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/DescribeParameterGroups)
