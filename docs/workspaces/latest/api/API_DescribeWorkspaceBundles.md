---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceBundles.html
---

# DescribeWorkspaceBundles
<a name="API_DescribeWorkspaceBundles"></a>

Retrieves a list that describes the available WorkSpace bundles.

You can filter the results using either bundle ID or owner, but not both.

## Request Syntax
<a name="API_DescribeWorkspaceBundles_RequestSyntax"></a>

```
{
   "BundleIds": [ "{{string}}" ],
   "NextToken": "{{string}}",
   "Owner": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWorkspaceBundles_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [BundleIds](#API_DescribeWorkspaceBundles_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceBundles-request-BundleIds"></a>
The identifiers of the bundles. You cannot combine this parameter with any other filter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: No

 ** [NextToken](#API_DescribeWorkspaceBundles_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceBundles-request-NextToken"></a>
The token for the next set of results. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Owner](#API_DescribeWorkspaceBundles_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceBundles-request-Owner"></a>
The owner of the bundles. You cannot combine this parameter with any other filter.
To describe the bundles provided by AWS, specify `AMAZON`. To describe the bundles that belong to your account, don't specify a value.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeWorkspaceBundles_ResponseSyntax"></a>

```
{
   "Bundles": [
      {
         "BundleId": "string",
         "BundleType": "string",
         "ComputeType": {
            "Name": "string"
         },
         "CreationTime": number,
         "Description": "string",
         "ImageId": "string",
         "LastUpdatedTime": number,
         "Name": "string",
         "Owner": "string",
         "RootStorage": {
            "Capacity": "string"
         },
         "State": "string",
         "UserStorage": {
            "Capacity": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeWorkspaceBundles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Bundles](#API_DescribeWorkspaceBundles_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceBundles-response-Bundles"></a>
Information about the bundles.
Type: Array of [WorkspaceBundle](API_WorkspaceBundle.md) objects

 ** [NextToken](#API_DescribeWorkspaceBundles_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceBundles-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return. This token is valid for one day and must be used within that time frame.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DescribeWorkspaceBundles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeWorkspaceBundles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeWorkspaceBundles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeWorkspaceBundles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspaceBundles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeWorkspaceBundles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspaceBundles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeWorkspaceBundles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeWorkspaceBundles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeWorkspaceBundles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeWorkspaceBundles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspaceBundles)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
