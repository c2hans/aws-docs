---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_PutCoreNetworkPolicy.html
---

# PutCoreNetworkPolicy
<a name="API_PutCoreNetworkPolicy"></a>

Creates a new, immutable version of a core network policy. A subsequent change set is created showing the differences between the LIVE policy and the submitted policy.

## Request Syntax
<a name="API_PutCoreNetworkPolicy_RequestSyntax"></a>

```
POST /core-networks/{{coreNetworkId}}/core-network-policy HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "LatestVersionId": {{number}},
   "PolicyDocument": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutCoreNetworkPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [coreNetworkId](#API_PutCoreNetworkPolicy_RequestSyntax) **   <a name="networkmanager-PutCoreNetworkPolicy-request-uri-CoreNetworkId"></a>
The ID of a core network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: Yes

## Request Body
<a name="API_PutCoreNetworkPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_PutCoreNetworkPolicy_RequestSyntax) **   <a name="networkmanager-PutCoreNetworkPolicy-request-ClientToken"></a>
The client token associated with the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Description](#API_PutCoreNetworkPolicy_RequestSyntax) **   <a name="networkmanager-PutCoreNetworkPolicy-request-Description"></a>
a core network policy description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [LatestVersionId](#API_PutCoreNetworkPolicy_RequestSyntax) **   <a name="networkmanager-PutCoreNetworkPolicy-request-LatestVersionId"></a>
The ID of a core network policy.
Type: Integer
Required: No

 ** [PolicyDocument](#API_PutCoreNetworkPolicy_RequestSyntax) **   <a name="networkmanager-PutCoreNetworkPolicy-request-PolicyDocument"></a>
The policy document.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000000.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_PutCoreNetworkPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CoreNetworkPolicy": {
      "Alias": "string",
      "ChangeSetState": "string",
      "CoreNetworkId": "string",
      "CreatedAt": number,
      "Description": "string",
      "PolicyDocument": "string",
      "PolicyErrors": [
         {
            "ErrorCode": "string",
            "Message": "string",
            "Path": "string"
         }
      ],
      "PolicyVersionId": number
   }
}
```

## Response Elements
<a name="API_PutCoreNetworkPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CoreNetworkPolicy](#API_PutCoreNetworkPolicy_ResponseSyntax) **   <a name="networkmanager-PutCoreNetworkPolicy-response-CoreNetworkPolicy"></a>
Describes the changed core network policy.
Type: [CoreNetworkPolicy](API_CoreNetworkPolicy.md) object

## Errors
<a name="API_PutCoreNetworkPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 409

 ** CoreNetworkPolicyException **
Describes a core network policy exception.
 ** Errors **
Describes a core network policy exception.
HTTP Status Code: 400

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_PutCoreNetworkPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/PutCoreNetworkPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/PutCoreNetworkPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/PutCoreNetworkPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/PutCoreNetworkPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/PutCoreNetworkPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/PutCoreNetworkPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/PutCoreNetworkPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/PutCoreNetworkPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/PutCoreNetworkPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/PutCoreNetworkPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
