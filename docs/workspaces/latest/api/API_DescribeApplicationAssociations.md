---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeApplicationAssociations.html
---

# DescribeApplicationAssociations
<a name="API_DescribeApplicationAssociations"></a>

Describes the associations between the application and the specified associated resources.

## Request Syntax
<a name="API_DescribeApplicationAssociations_RequestSyntax"></a>

```
{
   "ApplicationId": "{{string}}",
   "AssociatedResourceTypes": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApplicationAssociations_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_DescribeApplicationAssociations_RequestSyntax) **   <a name="WorkSpaces-DescribeApplicationAssociations-request-ApplicationId"></a>
The identifier of the specified application.
Type: String
Pattern: `^wsa-[0-9a-z]{8,63}$`
Required: Yes

 ** [AssociatedResourceTypes](#API_DescribeApplicationAssociations_RequestSyntax) **   <a name="WorkSpaces-DescribeApplicationAssociations-request-AssociatedResourceTypes"></a>
The resource type of the associated resources.
Type: Array of strings
Valid Values: `WORKSPACE | BUNDLE | IMAGE`
Required: Yes

 ** [MaxResults](#API_DescribeApplicationAssociations_RequestSyntax) **   <a name="WorkSpaces-DescribeApplicationAssociations-request-MaxResults"></a>
The maximum number of associations to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeApplicationAssociations_RequestSyntax) **   <a name="WorkSpaces-DescribeApplicationAssociations-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeApplicationAssociations_ResponseSyntax"></a>

```
{
   "Associations": [
      {
         "ApplicationId": "string",
         "AssociatedResourceId": "string",
         "AssociatedResourceType": "string",
         "Created": number,
         "LastUpdatedTime": number,
         "State": "string",
         "StateReason": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeApplicationAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Associations](#API_DescribeApplicationAssociations_ResponseSyntax) **   <a name="WorkSpaces-DescribeApplicationAssociations-response-Associations"></a>
List of associations and information about them.
Type: Array of [ApplicationResourceAssociation](API_ApplicationResourceAssociation.md) objects

 ** [NextToken](#API_DescribeApplicationAssociations_ResponseSyntax) **   <a name="WorkSpaces-DescribeApplicationAssociations-response-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DescribeApplicationAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** OperationNotSupportedException **
This operation is not supported.
 ** message **
The exception error message.
 ** reason **
The exception error reason.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApplicationAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeApplicationAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeApplicationAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeApplicationAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeApplicationAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeApplicationAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeApplicationAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeApplicationAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeApplicationAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeApplicationAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeApplicationAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
