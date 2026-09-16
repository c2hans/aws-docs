---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ListGroupResources.html
---

# ListGroupResources
<a name="API_ListGroupResources"></a>

This operation returns a list of the ARNs of the canaries that are associated with the specified group.

## Request Syntax
<a name="API_ListGroupResources_RequestSyntax"></a>

```
POST /group/{{groupIdentifier}}/resources HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListGroupResources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [groupIdentifier](#API_ListGroupResources_RequestSyntax) **   <a name="synthetics-ListGroupResources-request-uri-GroupIdentifier"></a>
Specifies the group to return information for. You can specify the group name, the ARN, or the group ID as the `GroupIdentifier`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_ListGroupResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListGroupResources_RequestSyntax) **   <a name="synthetics-ListGroupResources-request-MaxResults"></a>
Specify this parameter to limit how many canary ARNs are returned each time you use the `ListGroupResources` operation. If you omit this parameter, the default of 20 is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextToken](#API_ListGroupResources_RequestSyntax) **   <a name="synthetics-ListGroupResources-request-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^.+$`
Required: No

## Response Syntax
<a name="API_ListGroupResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Resources": [ "string" ]
}
```

## Response Elements
<a name="API_ListGroupResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListGroupResources_ResponseSyntax) **   <a name="synthetics-ListGroupResources-response-NextToken"></a>
A token that indicates that there is more data available. You can use this token in a subsequent `ListGroupResources` operation to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^.+$`

 ** [Resources](#API_ListGroupResources_ResponseSyntax) **   <a name="synthetics-ListGroupResources-response-Resources"></a>
An array of ARNs. These ARNs are for the canaries that are associated with the group.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListGroupResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A conflicting operation is already in progress.
HTTP Status Code: 409

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One of the specified resources was not found.
HTTP Status Code: 404

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_ListGroupResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/ListGroupResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/ListGroupResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/ListGroupResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/ListGroupResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/ListGroupResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/ListGroupResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/ListGroupResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/ListGroupResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/ListGroupResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/ListGroupResources)
