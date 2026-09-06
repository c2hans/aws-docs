---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListResponsePlans.html
---

# ListResponsePlans
<a name="API_ListResponsePlans"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists all response plans in your account.

## Request Syntax
<a name="API_ListResponsePlans_RequestSyntax"></a>

```
POST /listResponsePlans HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListResponsePlans_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListResponsePlans_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListResponsePlans_RequestSyntax) **   <a name="IncidentManager-ListResponsePlans-request-maxResults"></a>
The maximum number of response plans per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListResponsePlans_RequestSyntax) **   <a name="IncidentManager-ListResponsePlans-request-nextToken"></a>
The pagination token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_ListResponsePlans_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "responsePlanSummaries": [
      {
         "arn": "string",
         "displayName": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResponsePlans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListResponsePlans_ResponseSyntax) **   <a name="IncidentManager-ListResponsePlans-response-nextToken"></a>
The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [responsePlanSummaries](#API_ListResponsePlans_ResponseSyntax) **   <a name="IncidentManager-ListResponsePlans-response-responsePlanSummaries"></a>
Details of each response plan.
Type: Array of [ResponsePlanSummary](API_ResponsePlanSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListResponsePlans_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_ListResponsePlans_Examples"></a>

### Example
<a name="API_ListResponsePlans_Example_1"></a>

This example illustrates one usage of ListResponsePlans.

#### Sample Request
<a name="API_ListResponsePlans_Example_1_Request"></a>

```
POST /listResponsePlans HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.list-response-plans
X-Amz-Date: 20210811T172723Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 461

{
	"nextToken": "AAMA-EFRSURBSGhxbUdFUS9sMGNSNUQwM1RCak1VM3FiUVpneVdwRHFlVGp0czk0cFg4MEdRSFM1cWQzSDZuOGFtNGt2ZXFkRHVoYkFBQUFmakI4QmdrcWhraUc5dzBCQndhZ2J6QnRBZ0VBTUdnR0NTcUdTSWIzRFFFSEFUQWVCZ2xnaGtnQlpRTUVBUzR3RVFRTVR3VGcreXpmN0NiUFZvSmJBZ0VRZ0R1ck5hL093U1dxVnRKa0hwNXptNkgrcWxuNk9tNFZnRS9iSzl1cVE5KzR4bmlZd2ZMQnZIYUlFVU1yY0x6OC80ZVlrTVQ2VFdOVzFTaU41dz09SeLKmN9a12em-UlGoYDbWb_1keR-kIBvT4Al40KQqiAxUEMCIJ_15yckvywELqL2WiYQBKkjMjyMyjhwkFAu3sfu_Wg4jRUTUA8hEA4lbhXk"
}
```

#### Sample Response
<a name="API_ListResponsePlans_Example_1_Response"></a>

```
{
    "responsePlanSummaries": [
        {
            "arn": "arn:aws:ssm-incidents::111122223333:response-plan/example-response",
            "displayName": "Example response plan",
            "name": "example-response"
        }
    ]
}
```

## See Also
<a name="API_ListResponsePlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/ListResponsePlans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/ListResponsePlans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ListResponsePlans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/ListResponsePlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ListResponsePlans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/ListResponsePlans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/ListResponsePlans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/ListResponsePlans)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/ListResponsePlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ListResponsePlans)
