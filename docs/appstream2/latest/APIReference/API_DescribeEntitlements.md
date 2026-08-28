---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeEntitlements.html
---

# DescribeEntitlements
<a name="API_DescribeEntitlements"></a>

Retrieves a list that describes one of more entitlements.

## Request Syntax
<a name="API_DescribeEntitlements_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "Name": "{{string}}",
   "NextToken": "{{string}}",
   "StackName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEntitlements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeEntitlements_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeEntitlements-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Required: No

 ** [Name](#API_DescribeEntitlements_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeEntitlements-request-Name"></a>
The name of the entitlement.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: No

 ** [NextToken](#API_DescribeEntitlements_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeEntitlements-request-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [StackName](#API_DescribeEntitlements_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeEntitlements-request-StackName"></a>
The name of the stack with which the entitlement is associated.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_DescribeEntitlements_ResponseSyntax"></a>

```
{
   "Entitlements": [
      {
         "AppVisibility": "string",
         "Attributes": [
            {
               "Name": "string",
               "Value": "string"
            }
         ],
         "CreatedTime": number,
         "Description": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "StackName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeEntitlements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entitlements](#API_DescribeEntitlements_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeEntitlements-response-Entitlements"></a>
The entitlements.
Type: Array of [Entitlement](API_Entitlement.md) objects

 ** [NextToken](#API_DescribeEntitlements_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeEntitlements-response-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeEntitlements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntitlementNotFoundException **
The entitlement can't be found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEntitlements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeEntitlements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeEntitlements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeEntitlements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeEntitlements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeEntitlements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeEntitlements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeEntitlements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeEntitlements)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeEntitlements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeEntitlements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
