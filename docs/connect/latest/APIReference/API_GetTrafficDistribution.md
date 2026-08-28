---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetTrafficDistribution.html
---

# GetTrafficDistribution
<a name="API_GetTrafficDistribution"></a>

Retrieves the current traffic distribution for a given traffic distribution group.

## Request Syntax
<a name="API_GetTrafficDistribution_RequestSyntax"></a>

```
GET /traffic-distribution/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTrafficDistribution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetTrafficDistribution_RequestSyntax) **   <a name="connect-GetTrafficDistribution-request-uri-Id"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z-]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_GetTrafficDistribution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTrafficDistribution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AgentConfig": {
      "Distributions": [
         {
            "Percentage": number,
            "Region": "string"
         }
      ]
   },
   "Arn": "string",
   "Id": "string",
   "SignInConfig": {
      "Distributions": [
         {
            "Enabled": boolean,
            "Region": "string"
         }
      ]
   },
   "TelephonyConfig": {
      "Distributions": [
         {
            "Percentage": number,
            "Region": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetTrafficDistribution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentConfig](#API_GetTrafficDistribution_ResponseSyntax) **   <a name="connect-GetTrafficDistribution-response-AgentConfig"></a>
The distribution of agents between the instance and its replica(s).
Type: [AgentConfig](API_AgentConfig.md) object

 ** [Arn](#API_GetTrafficDistribution_ResponseSyntax) **   <a name="connect-GetTrafficDistribution-response-Arn"></a>
The Amazon Resource Name (ARN) of the traffic distribution group.
Type: String
Pattern: `^arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [Id](#API_GetTrafficDistribution_ResponseSyntax) **   <a name="connect-GetTrafficDistribution-response-Id"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
Type: String
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [SignInConfig](#API_GetTrafficDistribution_ResponseSyntax) **   <a name="connect-GetTrafficDistribution-response-SignInConfig"></a>
The distribution that determines which AWS Regions should be used to sign in agents in to both the instance and its replica(s).
Type: [SignInConfig](API_SignInConfig.md) object

 ** [TelephonyConfig](#API_GetTrafficDistribution_ResponseSyntax) **   <a name="connect-GetTrafficDistribution-response-TelephonyConfig"></a>
The distribution of traffic between the instance and its replicas.
Type: [TelephonyConfig](API_TelephonyConfig.md) object

## Errors
<a name="API_GetTrafficDistribution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_GetTrafficDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetTrafficDistribution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetTrafficDistribution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetTrafficDistribution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetTrafficDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetTrafficDistribution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetTrafficDistribution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetTrafficDistribution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetTrafficDistribution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetTrafficDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetTrafficDistribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
