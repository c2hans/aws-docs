---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListAssociatedFleets.html
---

# ListAssociatedFleets
<a name="API_ListAssociatedFleets"></a>

Retrieves the name of the fleet that is associated with the specified stack.

## Request Syntax
<a name="API_ListAssociatedFleets_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "StackName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAssociatedFleets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListAssociatedFleets_RequestSyntax) **   <a name="WorkSpacesApplications-ListAssociatedFleets-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [StackName](#API_ListAssociatedFleets_RequestSyntax) **   <a name="WorkSpacesApplications-ListAssociatedFleets-request-StackName"></a>
The name of the stack.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_ListAssociatedFleets_ResponseSyntax"></a>

```
{
   "Names": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssociatedFleets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Names](#API_ListAssociatedFleets_ResponseSyntax) **   <a name="WorkSpacesApplications-ListAssociatedFleets-response-Names"></a>
The name of the fleet.
Type: Array of strings
Length Constraints: Minimum length of 1.

 ** [NextToken](#API_ListAssociatedFleets_ResponseSyntax) **   <a name="WorkSpacesApplications-ListAssociatedFleets-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListAssociatedFleets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListAssociatedFleets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/ListAssociatedFleets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/ListAssociatedFleets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ListAssociatedFleets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/ListAssociatedFleets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ListAssociatedFleets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/ListAssociatedFleets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/ListAssociatedFleets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/ListAssociatedFleets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/ListAssociatedFleets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ListAssociatedFleets)
