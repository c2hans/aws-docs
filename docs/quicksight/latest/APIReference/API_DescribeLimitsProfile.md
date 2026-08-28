---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeLimitsProfile.html
---

# DescribeLimitsProfile
<a name="API_DescribeLimitsProfile"></a>

Describes the properties of an existing limits profile.

## Request Syntax
<a name="API_DescribeLimitsProfile_RequestSyntax"></a>

```
GET /governance/limits/accounts/{{accountId}}/profiles/{{profileId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeLimitsProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_DescribeLimitsProfile_RequestSyntax) **   <a name="QS-DescribeLimitsProfile-request-uri-accountId"></a>
The ID of the AWS account that contains the limits profile.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [profileId](#API_DescribeLimitsProfile_RequestSyntax) **   <a name="QS-DescribeLimitsProfile-request-uri-profileId"></a>
The unique identifier for the limits profile.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `lp-[a-f0-9-]+`
Required: Yes

## Request Body
<a name="API_DescribeLimitsProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeLimitsProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "profile": {
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
}
```

## Response Elements
<a name="API_DescribeLimitsProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [profile](#API_DescribeLimitsProfile_ResponseSyntax) **   <a name="QS-DescribeLimitsProfile-response-profile"></a>
The details of the requested limits profile, including its name, description, resource limits, and metadata.
Type: [LimitsProfile](API_LimitsProfile.md) object

## Errors
<a name="API_DescribeLimitsProfile_Errors"></a>

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

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DescribeLimitsProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeLimitsProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeLimitsProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeLimitsProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeLimitsProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeLimitsProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeLimitsProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeLimitsProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeLimitsProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeLimitsProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeLimitsProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
