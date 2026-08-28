---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListAssociatedStacks.html
---

# ListAssociatedStacks
<a name="API_ListAssociatedStacks"></a>

Retrieves the name of the stack with which the specified fleet is associated.

## Request Syntax
<a name="API_ListAssociatedStacks_RequestSyntax"></a>

```
{
   "FleetName": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAssociatedStacks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FleetName](#API_ListAssociatedStacks_RequestSyntax) **   <a name="WorkSpacesApplications-ListAssociatedStacks-request-FleetName"></a>
The name of the fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [NextToken](#API_ListAssociatedStacks_RequestSyntax) **   <a name="WorkSpacesApplications-ListAssociatedStacks-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListAssociatedStacks_ResponseSyntax"></a>

```
{
   "Names": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssociatedStacks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Names](#API_ListAssociatedStacks_ResponseSyntax) **   <a name="WorkSpacesApplications-ListAssociatedStacks-response-Names"></a>
The name of the stack.
Type: Array of strings
Length Constraints: Minimum length of 1.

 ** [NextToken](#API_ListAssociatedStacks_ResponseSyntax) **   <a name="WorkSpacesApplications-ListAssociatedStacks-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListAssociatedStacks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListAssociatedStacks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/ListAssociatedStacks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/ListAssociatedStacks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ListAssociatedStacks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/ListAssociatedStacks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ListAssociatedStacks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/ListAssociatedStacks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/ListAssociatedStacks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/ListAssociatedStacks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/ListAssociatedStacks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ListAssociatedStacks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
