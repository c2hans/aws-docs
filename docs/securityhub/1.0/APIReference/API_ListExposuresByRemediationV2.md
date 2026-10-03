---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListExposuresByRemediationV2.html
---

# ListExposuresByRemediationV2
<a name="API_ListExposuresByRemediationV2"></a>

Retrieves the exposure findings tied to a specific remediation target. Results are sorted by previous severity, highest first, and are paginated.

## Request Syntax
<a name="API_ListExposuresByRemediationV2_RequestSyntax"></a>

```
POST /ListExposuresByRemediationV2 HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TargetUid": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListExposuresByRemediationV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListExposuresByRemediationV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListExposuresByRemediationV2_RequestSyntax) **   <a name="securityhub-ListExposuresByRemediationV2-request-MaxResults"></a>
The maximum number of results to return. Valid range is 1-100. If you don't specify a value, the operation returns up to 25 results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListExposuresByRemediationV2_RequestSyntax) **   <a name="securityhub-ListExposuresByRemediationV2-request-NextToken"></a>
The token used to paginate the exposures list returned. On your first call to `ListExposuresByRemediationV2`, omit this parameter or set it to `NULL`. For subsequent calls, use the `NextToken` value returned in the previous response to retrieve the next page of results.
Type: String
Required: No

 ** [TargetUid](#API_ListExposuresByRemediationV2_RequestSyntax) **   <a name="securityhub-ListExposuresByRemediationV2-request-TargetUid"></a>
The unique identifier (ID) of an existing remediation target to list exposure findings for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_ListExposuresByRemediationV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Impact": "string",
         "MetadataUid": "string",
         "PreviousSeverity": "string",
         "ProjectedSeverity": "string",
         "Title": "string"
      }
   ],
   "NextToken": "string",
   "Resource": {
      "AccountId": "string",
      "CloudProvider": "string",
      "Id": "string",
      "Name": "string",
      "Region": "string",
      "ResourceGuid": "string",
      "ResourceOwnerAccountId": "string",
      "ResourceOwnerOrgId": "string",
      "ResourceRegion": "string",
      "Type": "string"
   },
   "TargetUid": "string",
   "TotalCount": number,
   "Trait": {
      "Title": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_ListExposuresByRemediationV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListExposuresByRemediationV2_ResponseSyntax) **   <a name="securityhub-ListExposuresByRemediationV2-response-Items"></a>
An array of exposure findings returned by the operation.
Type: Array of [ExposureFinding](API_ExposureFinding.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

 ** [NextToken](#API_ListExposuresByRemediationV2_ResponseSyntax) **   <a name="securityhub-ListExposuresByRemediationV2-response-NextToken"></a>
The pagination token to use to request the next page of results. Otherwise, this parameter is null.
Type: String

 ** [Resource](#API_ListExposuresByRemediationV2_ResponseSyntax) **   <a name="securityhub-ListExposuresByRemediationV2-response-Resource"></a>
Provides comprehensive details about a resource.
Type: [RemediationResource](API_RemediationResource.md) object

 ** [TargetUid](#API_ListExposuresByRemediationV2_ResponseSyntax) **   <a name="securityhub-ListExposuresByRemediationV2-response-TargetUid"></a>
The unique identifier (ID) of the remediation target that the exposure findings are associated with.
Type: String
Pattern: `.*\S.*`

 ** [TotalCount](#API_ListExposuresByRemediationV2_ResponseSyntax) **   <a name="securityhub-ListExposuresByRemediationV2-response-TotalCount"></a>
The total count of exposure findings associated with the remediation target.
Type: Integer

 ** [Trait](#API_ListExposuresByRemediationV2_ResponseSyntax) **   <a name="securityhub-ListExposuresByRemediationV2-response-Trait"></a>
The specific trait associated with the remediation target.
Type: [RemediationTrait](API_RemediationTrait.md) object

## Errors
<a name="API_ListExposuresByRemediationV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_ListExposuresByRemediationV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListExposuresByRemediationV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListExposuresByRemediationV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListExposuresByRemediationV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListExposuresByRemediationV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListExposuresByRemediationV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListExposuresByRemediationV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListExposuresByRemediationV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListExposuresByRemediationV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListExposuresByRemediationV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListExposuresByRemediationV2)
