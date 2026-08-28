---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListResources.html
---

# ListResources
<a name="API_ListResources"></a>

Lists the resources registered to be managed by the Data Catalog.

## Request Syntax
<a name="API_ListResources_RequestSyntax"></a>

```
POST /ListResources HTTP/1.1
Content-type: application/json

{
   "FilterConditionList": [
      {
         "ComparisonOperator": "{{string}}",
         "Field": "{{string}}",
         "StringValueList": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FilterConditionList](#API_ListResources_RequestSyntax) **   <a name="lakeformation-ListResources-request-FilterConditionList"></a>
Any applicable row-level and/or column-level filtering conditions for the resources.
Type: Array of [FilterCondition](API_FilterCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_ListResources_RequestSyntax) **   <a name="lakeformation-ListResources-request-MaxResults"></a>
The maximum number of resource results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListResources_RequestSyntax) **   <a name="lakeformation-ListResources-request-NextToken"></a>
A continuation token, if this is not the first call to retrieve these resources.
Type: String
Required: No

## Response Syntax
<a name="API_ListResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ResourceInfoList": [
      {
         "ExpectedResourceOwnerAccount": "string",
         "HybridAccessEnabled": boolean,
         "LastModified": number,
         "ResourceArn": "string",
         "RoleArn": "string",
         "VerificationStatus": "string",
         "WithFederation": boolean,
         "WithPrivilegedAccess": boolean
      }
   ]
}
```

## Response Elements
<a name="API_ListResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResources_ResponseSyntax) **   <a name="lakeformation-ListResources-response-NextToken"></a>
A continuation token, if this is not the first call to retrieve these resources.
Type: String

 ** [ResourceInfoList](#API_ListResources_ResponseSyntax) **   <a name="lakeformation-ListResources-response-ResourceInfoList"></a>
A summary of the data lake resources.
Type: Array of [ResourceInfo](API_ResourceInfo.md) objects

## Errors
<a name="API_ListResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ListResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ListResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ListResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ListResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ListResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ListResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ListResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ListResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ListResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ListResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
