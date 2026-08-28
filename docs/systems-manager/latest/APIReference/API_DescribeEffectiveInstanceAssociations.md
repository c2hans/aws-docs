---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeEffectiveInstanceAssociations.html
---

# DescribeEffectiveInstanceAssociations
<a name="API_DescribeEffectiveInstanceAssociations"></a>

All associations for the managed nodes.

## Request Syntax
<a name="API_DescribeEffectiveInstanceAssociations_RequestSyntax"></a>

```
{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEffectiveInstanceAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceId](#API_DescribeEffectiveInstanceAssociations_RequestSyntax) **   <a name="systemsmanager-DescribeEffectiveInstanceAssociations-request-InstanceId"></a>
The managed node ID for which you want to view all associations.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** [MaxResults](#API_DescribeEffectiveInstanceAssociations_RequestSyntax) **   <a name="systemsmanager-DescribeEffectiveInstanceAssociations-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** [NextToken](#API_DescribeEffectiveInstanceAssociations_RequestSyntax) **   <a name="systemsmanager-DescribeEffectiveInstanceAssociations-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribeEffectiveInstanceAssociations_ResponseSyntax"></a>

```
{
   "Associations": [
      {
         "AssociationId": "string",
         "AssociationVersion": "string",
         "Content": "string",
         "InstanceId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeEffectiveInstanceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Associations](#API_DescribeEffectiveInstanceAssociations_ResponseSyntax) **   <a name="systemsmanager-DescribeEffectiveInstanceAssociations-response-Associations"></a>
The associations for the requested managed node.
Type: Array of [InstanceAssociation](API_InstanceAssociation.md) objects

 ** [NextToken](#API_DescribeEffectiveInstanceAssociations_ResponseSyntax) **   <a name="systemsmanager-DescribeEffectiveInstanceAssociations-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_DescribeEffectiveInstanceAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeEffectiveInstanceAssociations_Examples"></a>

### Example
<a name="API_DescribeEffectiveInstanceAssociations_Example_1"></a>

This example illustrates one usage of DescribeEffectiveInstanceAssociations.

#### Sample Request
<a name="API_DescribeEffectiveInstanceAssociations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeEffectiveInstanceAssociations
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240326T144721Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240326/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 37

{
    "InstanceId": "i-02573cafcfEXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeEffectiveInstanceAssociations_Example_1_Response"></a>

```
{
    "Associations": [
        {
            "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
            "InstanceId": "i-02573cafcfEXAMPLE",
            "Content": "{\n    \"schemaVersion\": \"1.2\",\n    \"description\": \"Update the Amazon SSM Agent to the latest version or specified version.\",\n--truncated--",
            "AssociationVersion": "1"
        }
    ]
}
```

## See Also
<a name="API_DescribeEffectiveInstanceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeEffectiveInstanceAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
