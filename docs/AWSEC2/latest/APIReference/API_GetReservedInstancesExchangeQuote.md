---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetReservedInstancesExchangeQuote.html
---

# GetReservedInstancesExchangeQuote
<a name="API_GetReservedInstancesExchangeQuote"></a>

Returns a quote and exchange information for exchanging one or more specified Convertible Reserved Instances for a new Convertible Reserved Instance. If the exchange cannot be performed, the reason is returned in the response. Use [AcceptReservedInstancesExchangeQuote](API_AcceptReservedInstancesExchangeQuote.md) to perform the exchange.

## Request Parameters
<a name="API_GetReservedInstancesExchangeQuote_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ReservedInstanceId.N**
The IDs of the Convertible Reserved Instances to exchange.
Type: Array of strings
Required: Yes

 **TargetConfiguration.N**
The configuration of the target Convertible Reserved Instance to exchange for your current Convertible Reserved Instances.
Type: Array of [TargetConfigurationRequest](API_TargetConfigurationRequest.md) objects
Required: No

## Response Elements
<a name="API_GetReservedInstancesExchangeQuote_ResponseElements"></a>

The following elements are returned by the service.

 **currencyCode**
The currency of the transaction.
Type: String

 **isValidExchange**
If `true`, the exchange is valid. If `false`, the exchange cannot be completed.
Type: Boolean

 **outputReservedInstancesWillExpireAt**
The new end date of the reservation term.
Type: Timestamp

 **paymentDue**
The total true upfront charge for the exchange.
Type: String

 **requestId**
The ID of the request.
Type: String

 **reservedInstanceValueRollup**
The cost associated with the Reserved Instance.
Type: [ReservationValue](API_ReservationValue.md) object

 **reservedInstanceValueSet**
The configuration of your Convertible Reserved Instances.
Type: Array of [ReservedInstanceReservationValue](API_ReservedInstanceReservationValue.md) objects

 **targetConfigurationValueRollup**
The cost associated with the Reserved Instance.
Type: [ReservationValue](API_ReservationValue.md) object

 **targetConfigurationValueSet**
The values of the target Convertible Reserved Instances.
Type: Array of [TargetReservationValue](API_TargetReservationValue.md) objects

 **validationFailureReason**
Describes the reason why the exchange cannot be completed.
Type: String

## Errors
<a name="API_GetReservedInstancesExchangeQuote_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetReservedInstancesExchangeQuote_Examples"></a>

### Example
<a name="API_GetReservedInstancesExchangeQuote_Example_1"></a>

This example describes the output of requesting whether a potential exchange is valid.

#### Sample Request
<a name="API_GetReservedInstancesExchangeQuote_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetReservedInstancesExchangeQuote
&ReservedInstanceId.1=649fd0c8-7768-46b8-8f84-a6400EXAMPLE
&TargetConfiguration.1.OfferingId=24167194-6541-4041-9e31-bc7c5984aa53
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetReservedInstancesExchangeQuote_Example_1_Response"></a>

```
<GetReservedInstancesExchangeQuoteResponse>
  <requestId>d072f652-cc57-458c-89e0-e6c02EXAMPLE</requestId>
  <outputReservedInstancesWillExpireAt>2019-05-17T12:32:53Z</outputReservedInstancesWillExpireAt>
  <reservedInstanceValueSet>
    <item>
        <reservedInstancesId>649fd0c8-7768-46b8-8f84-a6400EXAMPLE</reservedInstanceId>
        <reservationValue>
            <remainingTotalValue>98.048402</remainingTotalValue>
            <hourlyPrice>0.018000</hourlyPrice>
            <remainingUpfrontValue>631.0</remainingUpfrontValue>
        </reservationValue>
    </item>
  </reservedInstanceValueSet>
  <targetConfigurationValueSet>
  <isValidExchange>false</isValidExchange>
  <paymentDue>-448.416438</paymentDue>
  <targetConfigurationValueRollup>
          <remainingTotalValue>0</remainingTotalValue>
          <hourlyPrice>0</hourlyPrice>
          <remainingUpfrontValue>0</remainingUpfrontValue>
  <targetConfigurationValueRollup>
  <reservedInstanceValueRollup>
          <remainingTotalValue>873.504438</remainingTotalValue>
          <hourlyPrice>0.018000</hourlyPrice>
          <remainingUpfrontValue>448.416438</remainingUpfrontValue>
  </reservedInstanceValueRollup>
  <currencyCode>USD</currencyCode>
  <validationFailureReason>The target configuration value is less than the input</validationFailureReason>
</GetReservedInstancesExchangeQuoteResponse>
```

## See Also
<a name="API_GetReservedInstancesExchangeQuote_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetReservedInstancesExchangeQuote)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetReservedInstancesExchangeQuote)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetReservedInstancesExchangeQuote)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetReservedInstancesExchangeQuote)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetReservedInstancesExchangeQuote)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetReservedInstancesExchangeQuote)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetReservedInstancesExchangeQuote)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetReservedInstancesExchangeQuote)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetReservedInstancesExchangeQuote)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetReservedInstancesExchangeQuote)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
