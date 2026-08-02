---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListEntitledApplications.html
---

# ListEntitledApplications
<a name="API_ListEntitledApplications"></a>

Retrieves a list of entitled applications.

## Request Syntax
<a name="API_ListEntitledApplications_RequestSyntax"></a>

```
{
   "EntitlementName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StackName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEntitledApplications_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EntitlementName](#API_ListEntitledApplications_RequestSyntax) **   <a name="WorkSpacesApplications-ListEntitledApplications-request-EntitlementName"></a>
The name of the entitlement.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [MaxResults](#API_ListEntitledApplications_RequestSyntax) **   <a name="WorkSpacesApplications-ListEntitledApplications-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Required: No

 ** [NextToken](#API_ListEntitledApplications_RequestSyntax) **   <a name="WorkSpacesApplications-ListEntitledApplications-request-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [StackName](#API_ListEntitledApplications_RequestSyntax) **   <a name="WorkSpacesApplications-ListEntitledApplications-request-StackName"></a>
The name of the stack with which the entitlement is associated.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_ListEntitledApplications_ResponseSyntax"></a>

```
{
   "EntitledApplications": [
      {
         "ApplicationIdentifier": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEntitledApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EntitledApplications](#API_ListEntitledApplications_ResponseSyntax) **   <a name="WorkSpacesApplications-ListEntitledApplications-response-EntitledApplications"></a>
The entitled applications.
Type: Array of [EntitledApplication](API_EntitledApplication.md) objects

 ** [NextToken](#API_ListEntitledApplications_ResponseSyntax) **   <a name="WorkSpacesApplications-ListEntitledApplications-response-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListEntitledApplications_Errors"></a>

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
<a name="API_ListEntitledApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/ListEntitledApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/ListEntitledApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ListEntitledApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/ListEntitledApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ListEntitledApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/ListEntitledApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/ListEntitledApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/ListEntitledApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/ListEntitledApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ListEntitledApplications)
