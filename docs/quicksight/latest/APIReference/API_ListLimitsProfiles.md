---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListLimitsProfiles.html
---

# ListLimitsProfiles
<a name="API_ListLimitsProfiles"></a>

Lists all limits profiles in an Amazon Quick Sight account. Results are paginated. Use the `maxResults` parameter to limit the number of results returned in a single call, and use the `nextToken` parameter to retrieve the next page of results.

## Request Syntax
<a name="API_ListLimitsProfiles_RequestSyntax"></a>

```
GET /governance/limits/accounts/{{accountId}}/profiles?maxResults={{maxResults}}&nextToken={{nextToken}}&resourceType={{resourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLimitsProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_ListLimitsProfiles_RequestSyntax) **   <a name="QS-ListLimitsProfiles-request-uri-accountId"></a>
The ID of the AWS account that contains the limits profiles.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [maxResults](#API_ListLimitsProfiles_RequestSyntax) **   <a name="QS-ListLimitsProfiles-request-uri-maxResults"></a>
The maximum number of results to return in a single call. If you don't specify a value, the service uses the default maximum.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListLimitsProfiles_RequestSyntax) **   <a name="QS-ListLimitsProfiles-request-uri-nextToken"></a>
The token for the next set of results, or null if there are no more results.

 ** [resourceType](#API_ListLimitsProfiles_RequestSyntax) **   <a name="QS-ListLimitsProfiles-request-uri-resourceType"></a>
An optional filter that limits the results to profiles that contain the specified resource type. If you don't specify a value, the operation returns all profiles.
Valid Values: `INDEX_STORAGE | AGENT_HOURS`

## Request Body
<a name="API_ListLimitsProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLimitsProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "profiles": [
      {
         "accountId": "string",
         "arn": "string",
         "createdAt": number,
         "description": "string",
         "profileId": "string",
         "profileName": "string",
         "resourceLimits": {
            "string" : {
               "maxValue": number,
               "unit": "string"
            }
         },
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListLimitsProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [profiles](#API_ListLimitsProfiles_ResponseSyntax) **   <a name="QS-ListLimitsProfiles-response-profiles"></a>
A list of limits profiles.
Type: Array of [LimitsProfile](API_LimitsProfile.md) objects

 ** [nextToken](#API_ListLimitsProfiles_ResponseSyntax) **   <a name="QS-ListLimitsProfiles-response-nextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String

## Errors
<a name="API_ListLimitsProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_ListLimitsProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListLimitsProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListLimitsProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListLimitsProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListLimitsProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListLimitsProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListLimitsProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListLimitsProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListLimitsProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListLimitsProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListLimitsProfiles)
