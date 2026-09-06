---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_GetResourcePolicies.html
---

# GetResourcePolicies
<a name="API_GetResourcePolicies"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves the resource policies attached to the specified response plan.

## Request Syntax
<a name="API_GetResourcePolicies_RequestSyntax"></a>

```
POST /getResourcePolicies?resourceArn={{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetResourcePolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_GetResourcePolicies_RequestSyntax) **   <a name="IncidentManager-GetResourcePolicies-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the response plan with the attached resource policy.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: Yes

## Request Body
<a name="API_GetResourcePolicies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_GetResourcePolicies_RequestSyntax) **   <a name="IncidentManager-GetResourcePolicies-request-maxResults"></a>
The maximum number of resource policies to display for each page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetResourcePolicies_RequestSyntax) **   <a name="IncidentManager-GetResourcePolicies-request-nextToken"></a>
The pagination token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_GetResourcePolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "resourcePolicies": [
      {
         "policyDocument": "string",
         "policyId": "string",
         "ramResourceShareRegion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetResourcePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetResourcePolicies_ResponseSyntax) **   <a name="IncidentManager-GetResourcePolicies-response-nextToken"></a>
The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [resourcePolicies](#API_GetResourcePolicies_ResponseSyntax) **   <a name="IncidentManager-GetResourcePolicies-response-resourcePolicies"></a>
Details about the resource policy attached to the response plan.
Type: Array of [ResourcePolicy](API_ResourcePolicy.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_GetResourcePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_GetResourcePolicies_Examples"></a>

### Example
<a name="API_GetResourcePolicies_Example_1"></a>

This example illustrates one usage of GetResourcePolicies.

#### Sample Request
<a name="API_GetResourcePolicies_Example_1_Request"></a>

```
POST /getResourcePolicies?resourceArn=arn%3Aaws%3Assm-incidents%3A%111122223333%3Aresponse-plan%2Fexample-response HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.get-resource-policies
X-Amz-Date: 20210810T230018Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210810/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_GetResourcePolicies_Example_1_Response"></a>

```
{
	"nextToken":null,
    "resourcePolicies": [
        {
            "policyDocument": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"ExampleResourcePolciy\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::444455556666:root\"},\"Action\":[\"ssm-incidents:GetResponsePlan\",\"ssm-incidents:StartIncident\",\"ssm-incidents:UpdateIncidentRecord\",\"ssm-incidents:GetIncidentRecord\",\"ssm-incidents:CreateTimelineEvent\",\"ssm-incidents:UpdateTimelineEvent\",\"ssm-incidents:GetTimelineEvent\",\"ssm-incidents:ListTimelineEvents\",\"ssm-incidents:UpdateRelatedItems\",\"ssm-incidents:ListRelatedItems\"],\"Resource\":[\"arn:aws:ssm-incidents:*:111122223333:response-plan/example-response\",\"arn:aws:ssm-incidents:*:111122223333:incident-record/example-incident/*\"]}]}",
            "policyId": "72f95d0502d05ebf6e7d2c30ee0445cf",
            "ramResourceShareRegion": "us-east-1"
        }
    ]
}
```

## See Also
<a name="API_GetResourcePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/GetResourcePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/GetResourcePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/GetResourcePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/GetResourcePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/GetResourcePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/GetResourcePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/GetResourcePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/GetResourcePolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/GetResourcePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/GetResourcePolicies)
