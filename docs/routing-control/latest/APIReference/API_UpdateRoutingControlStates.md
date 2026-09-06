---
source_url: https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStates.html
---

# UpdateRoutingControlStates
<a name="API_UpdateRoutingControlStates"></a>

Set multiple routing control states. You can set the value for each state to be ON or OFF. When the state is ON, traffic flows to a cell. When it's OFF, traffic does not flow.

With Route 53 ARC, you can add safety rules for routing controls, which are safeguards for routing control state updates that help prevent unexpected outcomes, like fail open traffic routing. However, there are scenarios when you might want to bypass the routing control safeguards that are enforced with safety rules that you've configured. For example, you might want to fail over quickly for disaster recovery, and one or more safety rules might be unexpectedly preventing you from updating a routing control state to reroute traffic. In a "break glass" scenario like this, you can override one or more safety rules to change a routing control state and fail over your application.

The `SafetyRulesToOverride` property enables you override one or more safety rules and update routing control states. For more information, see [ Override safety rules to reroute traffic](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

 *You must specify Regional endpoints when you work with API cluster operations to get or update routing control states in Route 53 ARC.*

To see a code example for getting a routing control state, including accessing Regional cluster endpoints in sequence, see [API examples](https://docs.aws.amazon.com/r53recovery/latest/dg/service_code_examples_actions.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.
+  [ Viewing and updating routing control states](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.html)
+  [Working with routing controls overall](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html)

## Request Syntax
<a name="API_UpdateRoutingControlStates_RequestSyntax"></a>

```
{
   "SafetyRulesToOverride": [ "{{string}}" ],
   "UpdateRoutingControlStateEntries": [
      {
         "RoutingControlArn": "{{string}}",
         "RoutingControlState": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateRoutingControlStates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SafetyRulesToOverride](#API_UpdateRoutingControlStates_RequestSyntax) **   <a name="r53recovery-UpdateRoutingControlStates-request-SafetyRulesToOverride"></a>
The Amazon Resource Names (ARNs) for the safety rules that you want to override when you're updating routing control states. You can override one safety rule or multiple safety rules by including one or more ARNs, separated by commas.
For more information, see [ Override safety rules to reroute traffic](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.override-safety-rule.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[A-Za-z0-9:.\/_-]*$`
Required: No

 ** [UpdateRoutingControlStateEntries](#API_UpdateRoutingControlStates_RequestSyntax) **   <a name="r53recovery-UpdateRoutingControlStates-request-UpdateRoutingControlStateEntries"></a>
A set of routing control entries that you want to update.
Type: Array of [UpdateRoutingControlStateEntry](API_UpdateRoutingControlStateEntry.md) objects
Required: Yes

## Response Elements
<a name="API_UpdateRoutingControlStates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRoutingControlStates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ConflictException **
There was a conflict with this request. Try again.
HTTP Status Code: 400

 ** EndpointTemporarilyUnavailableException **
The cluster endpoint isn't available. Try another cluster endpoint.
HTTP Status Code: 400

 ** InternalServerException **
There was an unexpected error during processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a routing control or control panel that was not found.
HTTP Status Code: 400

 ** ServiceLimitExceededException **
The request can't update that many routing control states at the same time. Try again with fewer routing control states.
 ** limitCode **
The code of the limit that was exceeded.
 ** resourceId **
The resource identifier of the limit that was exceeded.
 ** resourceType **
The resource type of the limit that was exceeded.
 ** serviceCode **
The service code of the limit that was exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 400

 ** ValidationException **
There was a validation error on the request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRoutingControlStates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-recovery-cluster-2019-12-02/UpdateRoutingControlStates)
