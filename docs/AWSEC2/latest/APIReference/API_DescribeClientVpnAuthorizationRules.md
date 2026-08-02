---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnAuthorizationRules.html
---

# DescribeClientVpnAuthorizationRules
<a name="API_DescribeClientVpnAuthorizationRules"></a>

Describes the authorization rules for a specified Client VPN endpoint.

## Request Parameters
<a name="API_DescribeClientVpnAuthorizationRules_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. Filter names and values are case-sensitive.
+  `description` - The description of the authorization rule.
+  `destination-cidr` - The CIDR of the network to which the authorization rule applies.
+  `group-id` - The ID of the Active Directory group to which the authorization rule grants access.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the nextToken value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeClientVpnAuthorizationRules_ResponseElements"></a>

The following elements are returned by the service.

 **authorizationRule**
Information about the authorization rules.
Type: Array of [AuthorizationRule](API_AuthorizationRule.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeClientVpnAuthorizationRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeClientVpnAuthorizationRules_Examples"></a>

### Example
<a name="API_DescribeClientVpnAuthorizationRules_Example_1"></a>

This example describes the authorization rules for a specific Client VPN endpoint.

#### Sample Request
<a name="API_DescribeClientVpnAuthorizationRules_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeClientVpnAuthorizationRules
&ClientVpnEndpointId.1=cvpn-endpoint-EXAMPLEc8db8d3536
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeClientVpnAuthorizationRules_Example_1_Response"></a>

```
<DescribeClientVpnAuthorizationRulesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>9d5c69db-763e-4b63-88ee-EXAMPLE</requestId>
    <authorizationRule>
        <item>
            <accessAll>true</accessAll>
            <description>auth-rule-one</description>
            <destinationCidr>10.0.0.0/16</destinationCidr>
            <clientVpnEndpointId>cvpn-endpoint-EXAMPLEc8db8d3536</clientVpnEndpointId>
            <groupId/>
            <status>
                <code>active</code>
            </status>
        </item>
    </authorizationRule>
</DescribeClientVpnAuthorizationRulesResponse>
```

## See Also
<a name="API_DescribeClientVpnAuthorizationRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeClientVpnAuthorizationRules)
