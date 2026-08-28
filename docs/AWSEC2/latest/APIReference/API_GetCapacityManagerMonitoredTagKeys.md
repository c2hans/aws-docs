---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetCapacityManagerMonitoredTagKeys.html
---

# GetCapacityManagerMonitoredTagKeys
<a name="API_GetCapacityManagerMonitoredTagKeys"></a>

 Retrieves the tag keys that are currently being monitored by EC2 Capacity Manager. Monitored tag keys are included as dimensions in capacity metric data, enabling you to group and filter metrics by tag values.

## Request Parameters
<a name="API_GetCapacityManagerMonitoredTagKeys_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MaxResults**
 The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `NextToken` value. If not specified, up to 1000 results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 **NextToken**
 The token for the next page of results. Use the value returned from a previous call to retrieve additional results.
Type: String
Required: No

## Response Elements
<a name="API_GetCapacityManagerMonitoredTagKeys_ResponseElements"></a>

The following elements are returned by the service.

 **capacityManagerTagKeySet**
 The list of tag keys being monitored by Capacity Manager, including their current status and metadata.
Type: Array of [CapacityManagerMonitoredTagKey](API_CapacityManagerMonitoredTagKey.md) objects

 **nextToken**
 The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetCapacityManagerMonitoredTagKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetCapacityManagerMonitoredTagKeys_Examples"></a>

### Example
<a name="API_GetCapacityManagerMonitoredTagKeys_Example_1"></a>

This example retrieves the tag keys currently being monitored by Capacity Manager.

#### Sample Request
<a name="API_GetCapacityManagerMonitoredTagKeys_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetCapacityManagerMonitoredTagKeys
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetCapacityManagerMonitoredTagKeys_Example_1_Response"></a>

```
<GetCapacityManagerMonitoredTagKeysResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <capacityManagerTagKeySet>
        <item>
            <tagKey>Environment</tagKey>
            <status>activated</status>
            <statusMessage/>
            <capacityManagerProvided>false</capacityManagerProvided>
            <earliestDatapointTimestamp>2025-12-23T20:00:00+00:00</earliestDatapointTimestamp>
        </item>
        <item>
            <tagKey>aws:autoscaling:groupName</tagKey>
            <status>activated</status>
            <statusMessage/>
            <capacityManagerProvided>true</capacityManagerProvided>
            <earliestDatapointTimestamp>2025-12-23T20:00:00+00:00</earliestDatapointTimestamp>
        </item>
    </capacityManagerTagKeySet>
</GetCapacityManagerMonitoredTagKeysResponse>
```

## See Also
<a name="API_GetCapacityManagerMonitoredTagKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetCapacityManagerMonitoredTagKeys)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
