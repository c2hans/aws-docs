---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteTransitGatewayMulticastDomain.html
---

# DeleteTransitGatewayMulticastDomain
<a name="API_DeleteTransitGatewayMulticastDomain"></a>

Deletes the specified transit gateway multicast domain.

## Request Parameters
<a name="API_DeleteTransitGatewayMulticastDomain_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TransitGatewayMulticastDomainId**
The ID of the transit gateway multicast domain.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteTransitGatewayMulticastDomain_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayMulticastDomain**
Information about the deleted transit gateway multicast domain.
Type: [TransitGatewayMulticastDomain](API_TransitGatewayMulticastDomain.md) object

## Errors
<a name="API_DeleteTransitGatewayMulticastDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteTransitGatewayMulticastDomain_Examples"></a>

### Example 1
<a name="API_DeleteTransitGatewayMulticastDomain_Example_1"></a>

This example deletes the multicast domain `tgw-mcast-domain-0c4905cef7EXAMPLE`.

#### Sample Request
<a name="API_DeleteTransitGatewayMulticastDomain_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteTransitGatewayMulticastDomain
&TransitGatewayMulticastDomainId=tgw-mcast-domain-02bb79002bEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteTransitGatewayMulticastDomain_Example_1_Response"></a>

```
<DeleteTransitGatewayMulticastDomainResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>19914ba0-eb6c-43aa-9381-0bdafEXAMPLE</requestId>
    <transitGatewayMulticastDomain>
        <creationTime>2019-11-20T22:02:03.000Z</creationTime>
        <state>deleting</state>
        <transitGatewayId>tgw-0d88d2d0d5EXAMPLE</transitGatewayId>
        <transitGatewayMulticastDomainId>tgw-mcast-domain-02bb79002bEXAMPLE</transitGatewayMulticastDomainId>
    </transitGatewayMulticastDomain>
</DeleteTransitGatewayMulticastDomainResponse>
```

## See Also
<a name="API_DeleteTransitGatewayMulticastDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteTransitGatewayMulticastDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
