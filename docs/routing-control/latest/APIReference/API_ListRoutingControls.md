---
source_url: https://docs.aws.amazon.com/routing-control/latest/APIReference/API_ListRoutingControls.html
---

# ListRoutingControls
<a name="API_ListRoutingControls"></a>

List routing control names and Amazon Resource Names (ARNs), as well as the routing control state for each routing control, along with the control panel name and control panel ARN for the routing controls. If you specify a control panel ARN, this call lists the routing controls in the control panel. Otherwise, it lists all the routing controls in the cluster.

A routing control is a simple on/off switch in Route 53 ARC that you can use to route traffic to cells. When a routing control state is set to ON, traffic flows to a cell. When the state is set to OFF, traffic does not flow.

Before you can create a routing control, you must first create a cluster, and then host the control in a control panel on the cluster. For more information, see [ Create routing control structures](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.create.html) in the Amazon Route 53 Application Recovery Controller Developer Guide. You access one of the endpoints for the cluster to get or update the routing control state to redirect traffic for your application.

 *You must specify Regional endpoints when you work with API cluster operations to use this API operation to list routing controls in Route 53 ARC.*

Learn more about working with routing controls in the following topics in the Amazon Route 53 Application Recovery Controller Developer Guide:
+  [ Viewing and updating routing control states](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.update.html)
+  [Working with routing controls in Route 53 ARC](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html)

## Request Syntax
<a name="API_ListRoutingControls_RequestSyntax"></a>

```
{
   "ControlPanelArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRoutingControls_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ControlPanelArn](#API_ListRoutingControls_RequestSyntax) **   <a name="r53recovery-ListRoutingControls-request-ControlPanelArn"></a>
The Amazon Resource Name (ARN) of the control panel of the routing controls to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[A-Za-z0-9:.\/_-]*$`
Required: No

 ** [MaxResults](#API_ListRoutingControls_RequestSyntax) **   <a name="r53recovery-ListRoutingControls-request-MaxResults"></a>
The number of routing controls objects that you want to return with this call. The default value is 500.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListRoutingControls_RequestSyntax) **   <a name="r53recovery-ListRoutingControls-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8096.
Pattern: `[\S]*`
Required: No

## Response Syntax
<a name="API_ListRoutingControls_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RoutingControls": [
      {
         "ControlPanelArn": "string",
         "ControlPanelName": "string",
         "Owner": "string",
         "RoutingControlArn": "string",
         "RoutingControlName": "string",
         "RoutingControlState": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRoutingControls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRoutingControls_ResponseSyntax) **   <a name="r53recovery-ListRoutingControls-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8096.
Pattern: `[\S]*`

 ** [RoutingControls](#API_ListRoutingControls_ResponseSyntax) **   <a name="r53recovery-ListRoutingControls-response-RoutingControls"></a>
The list of routing controls.
Type: Array of [RoutingControl](API_RoutingControl.md) objects

## Errors
<a name="API_ListRoutingControls_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
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

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 400

 ** ValidationException **
There was a validation error on the request.
HTTP Status Code: 400

## See Also
<a name="API_ListRoutingControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-recovery-cluster-2019-12-02/ListRoutingControls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-recovery-cluster-2019-12-02/ListRoutingControls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-recovery-cluster-2019-12-02/ListRoutingControls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-recovery-cluster-2019-12-02/ListRoutingControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-recovery-cluster-2019-12-02/ListRoutingControls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-recovery-cluster-2019-12-02/ListRoutingControls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-recovery-cluster-2019-12-02/ListRoutingControls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-recovery-cluster-2019-12-02/ListRoutingControls)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-recovery-cluster-2019-12-02/ListRoutingControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-recovery-cluster-2019-12-02/ListRoutingControls)
