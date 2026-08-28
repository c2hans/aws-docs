---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListSecurityControlDefinitions.html
---

# ListSecurityControlDefinitions
<a name="API_ListSecurityControlDefinitions"></a>

 Lists all of the security controls that apply to a specified standard.

## Request Syntax
<a name="API_ListSecurityControlDefinitions_RequestSyntax"></a>

```
GET /securityControls/definitions?MaxResults={{MaxResults}}&NextToken={{NextToken}}&Providers={{Providers}}&StandardsArn={{StandardsArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSecurityControlDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListSecurityControlDefinitions_RequestSyntax) **   <a name="securityhub-ListSecurityControlDefinitions-request-uri-MaxResults"></a>
 An optional parameter that limits the total results of the API response to the specified number. If this parameter isn't provided in the request, the results include the first 25 security controls that apply to the specified standard. The results also include a `NextToken` parameter that you can use in a subsequent API call to get the next 25 controls. This repeats until all controls for the standard are returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListSecurityControlDefinitions_RequestSyntax) **   <a name="securityhub-ListSecurityControlDefinitions-request-uri-NextToken"></a>
 Optional pagination parameter.

 ** [Providers](#API_ListSecurityControlDefinitions_RequestSyntax) **   <a name="securityhub-ListSecurityControlDefinitions-request-uri-Providers"></a>
A list of cloud providers to filter the security control definitions by. For example, specify `Azure` to return only controls that evaluate Azure resources.
Valid Values: `AWS | Azure`

 ** [StandardsArn](#API_ListSecurityControlDefinitions_RequestSyntax) **   <a name="securityhub-ListSecurityControlDefinitions-request-uri-StandardsArn"></a>
 The Amazon Resource Name (ARN) of the standard that you want to view controls for.
Pattern: `.*\S.*`

## Request Body
<a name="API_ListSecurityControlDefinitions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSecurityControlDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SecurityControlDefinitions": [
      {
         "CurrentRegionAvailability": "string",
         "CustomizableProperties": [ "string" ],
         "Description": "string",
         "ParameterDefinitions": {
            "string" : {
               "ConfigurationOptions": { ... },
               "Description": "string"
            }
         },
         "Provider": "string",
         "RemediationUrl": "string",
         "SecurityControlId": "string",
         "SeverityRating": "string",
         "Title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSecurityControlDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSecurityControlDefinitions_ResponseSyntax) **   <a name="securityhub-ListSecurityControlDefinitions-response-NextToken"></a>
 A pagination parameter that's included in the response only if it was included in the request.
Type: String

 ** [SecurityControlDefinitions](#API_ListSecurityControlDefinitions_ResponseSyntax) **   <a name="securityhub-ListSecurityControlDefinitions-response-SecurityControlDefinitions"></a>
 An array of controls that apply to the specified standard.
Type: Array of [SecurityControlDefinition](API_SecurityControlDefinition.md) objects

## Errors
<a name="API_ListSecurityControlDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListSecurityControlDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListSecurityControlDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListSecurityControlDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListSecurityControlDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListSecurityControlDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListSecurityControlDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListSecurityControlDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListSecurityControlDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListSecurityControlDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListSecurityControlDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListSecurityControlDefinitions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
