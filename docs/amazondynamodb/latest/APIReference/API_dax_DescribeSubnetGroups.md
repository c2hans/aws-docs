---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DescribeSubnetGroups.html
---

# DescribeSubnetGroups
<a name="API_dax_DescribeSubnetGroups"></a>

Returns a list of subnet group descriptions. If a subnet group name is specified, the list will contain only the description of that group.

## Request Syntax
<a name="API_dax_DescribeSubnetGroups_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SubnetGroupNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_dax_DescribeSubnetGroups_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [MaxResults](#API_dax_DescribeSubnetGroups_RequestSyntax) **   <a name="DDB-dax_DescribeSubnetGroups-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
The value for `MaxResults` must be between 20 and 100.
Type: Integer
Required: No

 ** [NextToken](#API_dax_DescribeSubnetGroups_RequestSyntax) **   <a name="DDB-dax_DescribeSubnetGroups-request-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by `MaxResults`.
Type: String
Required: No

 ** [SubnetGroupNames](#API_dax_DescribeSubnetGroups_RequestSyntax) **   <a name="DDB-dax_DescribeSubnetGroups-request-SubnetGroupNames"></a>
The name of the subnet group.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_dax_DescribeSubnetGroups_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SubnetGroups": [
      {
         "Description": "string",
         "SubnetGroupName": "string",
         "Subnets": [
            {
               "SubnetAvailabilityZone": "string",
               "SubnetIdentifier": "string",
               "SupportedNetworkTypes": [ "string" ]
            }
         ],
         "SupportedNetworkTypes": [ "string" ],
         "VpcId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_dax_DescribeSubnetGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_dax_DescribeSubnetGroups_ResponseSyntax) **   <a name="DDB-dax_DescribeSubnetGroups-response-NextToken"></a>
Provides an identifier to allow retrieval of paginated results.
Type: String

 ** [SubnetGroups](#API_dax_DescribeSubnetGroups_ResponseSyntax) **   <a name="DDB-dax_DescribeSubnetGroups-response-SubnetGroups"></a>
An array of subnet groups. Each element in the array represents a single subnet group.
Type: Array of [SubnetGroup](API_dax_SubnetGroup.md) objects

## Errors
<a name="API_dax_DescribeSubnetGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

 ** SubnetGroupNotFoundFault **
The requested subnet group name does not refer to an existing subnet group.
HTTP Status Code: 400

## See Also
<a name="API_dax_DescribeSubnetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/DescribeSubnetGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/DescribeSubnetGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/DescribeSubnetGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/DescribeSubnetGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/DescribeSubnetGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/DescribeSubnetGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/DescribeSubnetGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/DescribeSubnetGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/DescribeSubnetGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/DescribeSubnetGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
