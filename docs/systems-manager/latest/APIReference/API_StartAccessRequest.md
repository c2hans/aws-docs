---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartAccessRequest.html
---

# StartAccessRequest
<a name="API_StartAccessRequest"></a>

Starts the workflow for just-in-time node access sessions.

## Request Syntax
<a name="API_StartAccessRequest_RequestSyntax"></a>

```
{
   "Reason": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Targets": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ]
}
```

## Request Parameters
<a name="API_StartAccessRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Reason](#API_StartAccessRequest_RequestSyntax) **   <a name="systemsmanager-StartAccessRequest-request-Reason"></a>
A brief description explaining why you are requesting access to the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [Tags](#API_StartAccessRequest_RequestSyntax) **   <a name="systemsmanager-StartAccessRequest-request-Tags"></a>
Key-value pairs of metadata you want to assign to the access request.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

 ** [Targets](#API_StartAccessRequest_RequestSyntax) **   <a name="systemsmanager-StartAccessRequest-request-Targets"></a>
The node you are requesting access to.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: Yes

## Response Syntax
<a name="API_StartAccessRequest_ResponseSyntax"></a>

```
{
   "AccessRequestId": "string"
}
```

## Response Elements
<a name="API_StartAccessRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessRequestId](#API_StartAccessRequest_ResponseSyntax) **   <a name="systemsmanager-StartAccessRequest-response-AccessRequestId"></a>
The ID of the access request.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`

## Errors
<a name="API_StartAccessRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requester doesn't have permissions to perform the requested operation.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified parameter to be shared could not be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request exceeds the service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
 ** QuotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** ResourceId **
The unique ID of the resource referenced in the failed request.
 ** ResourceType **
The resource type of the resource referenced in the failed request.
 ** ServiceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 400

 ** ThrottlingException **
The request or operation couldn't be performed because the service is throttling requests.
 ** QuotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** ServiceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 400

 ** ValidationException **
The request isn't valid. Verify that you entered valid contents for the command and try again.
 ** ReasonCode **
The reason code for the invalid request.
HTTP Status Code: 400

## See Also
<a name="API_StartAccessRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/StartAccessRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/StartAccessRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/StartAccessRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/StartAccessRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/StartAccessRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/StartAccessRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/StartAccessRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/StartAccessRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/StartAccessRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/StartAccessRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
