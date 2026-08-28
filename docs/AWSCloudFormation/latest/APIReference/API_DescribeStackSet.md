---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackSet.html
---

# DescribeStackSet
<a name="API_DescribeStackSet"></a>

Returns the description of the specified StackSet.

**Note**
This API provides *strongly consistent* reads meaning it will always return the most up-to-date data.

## Request Parameters
<a name="API_DescribeStackSet_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CallAs **
[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.
By default, `SELF` is specified. Use `SELF` for StackSets with self-managed permissions.
+ If you are signed in to the management account, specify `SELF`.
+ If you are signed in to a delegated administrator account, specify `DELEGATED_ADMIN`.

  Your AWS account must be registered as a delegated administrator in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the * AWS CloudFormation User Guide*.
Type: String
Valid Values: `SELF | DELEGATED_ADMIN`
Required: No

 ** StackSetName **
The name or unique ID of the StackSet whose description you want.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeStackSet_ResponseElements"></a>

The following element is returned by the service.

 ** StackSet **
The specified StackSet.
Type: [StackSet](API_StackSet.md) object

## Errors
<a name="API_DescribeStackSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** StackSetNotFound **
The specified StackSet doesn't exist.
HTTP Status Code: 404

## Examples
<a name="API_DescribeStackSet_Examples"></a>

### DescribeStackSet
<a name="API_DescribeStackSet_Example_1"></a>

This example illustrates one usage of DescribeStackSet.

#### Sample Request
<a name="API_DescribeStackSet_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeStackSet
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_DescribeStackSet_Example_1_Response"></a>

```
<DescribeStackSetResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DescribeStackSetResult>
    <StackSet>
      <Capabilities>
        <member>CAPABILITY_IAM</member>
      </Capabilities>
      <StackSetId>stack-set-example:c14cd6d1-cd17-40bd-82ed-ff97example</StackSetId>
      <TemplateBody>
        [details omitted]
      </TemplateBody>
      <StackSetName>stack-set-example</StackSetName>
      <Description>Enable AWS Config</Description>
      <Parameters>
        <member>
          <ParameterKey>AllSupported</ParameterKey>
          <UsePreviousValue>false</UsePreviousValue>
          <ParameterValue>true</ParameterValue>
        </member>
        <member>
          <ParameterKey>DeliveryChannelName</ParameterKey>
          <UsePreviousValue>false</UsePreviousValue>
          <ParameterValue><Generated></ParameterValue>
        </member>
        <member>
          <ParameterKey>Frequency</ParameterKey>
          <UsePreviousValue>false</UsePreviousValue>
          <ParameterValue>24hours</ParameterValue>
        </member>
        <member>
          <ParameterKey>IncludeGlobalResourceTypes</ParameterKey>
          <UsePreviousValue>false</UsePreviousValue>
          <ParameterValue>true</ParameterValue>
        </member>
        <member>
          <ParameterKey>NotificationEmail</ParameterKey>
          <UsePreviousValue>false</UsePreviousValue>
          <ParameterValue><None></ParameterValue>
        </member>
        <member>
          <ParameterKey>ResourceTypes</ParameterKey>
          <UsePreviousValue>false</UsePreviousValue>
          <ParameterValue><All></ParameterValue>
        </member>
        <member>
          <ParameterKey>TopicArn</ParameterKey>
          <UsePreviousValue>false</UsePreviousValue>
          <ParameterValue><New Topic></ParameterValue>
        </member>
      </Parameters>
      <Tags>
        <member>
          <Value>marketing</Value>
          <Key>business-unit</Key>
        </member>
      </Tags>
      <StackSetDriftDetectionDetails>
        <DriftDetectionStatus>COMPLETED</DriftDetectionStatus>
        <InSyncStackInstancesCount>5</InSyncStackInstancesCount>
        <FailedStackInstancesCount>0</FailedStackInstancesCount>
        <DriftStatus>IN_SYNC</DriftStatus>
        <TotalStackInstancesCount>5</TotalStackInstancesCount>
        <DriftedStackInstancesCount>0</DriftedStackInstancesCount>
        <InProgressStackInstancesCount>0</InProgressStackInstancesCount>
        <LastDriftCheckTimestamp>2019-12-03T20:00:27.877Z</LastDriftCheckTimestamp>
      </StackSetDriftDetectionDetails>
      <Status>ACTIVE</Status>
    </StackSet>
  </DescribeStackSetResult>
  <ResponseMetadata>
    <RequestId>48d13e76-794b-11e7-95e6-f946example</RequestId>
  </ResponseMetadata>
</DescribeStackSetResponse>
```

### How to view which Regions a StackSet has stack instances deployed to.
<a name="API_DescribeStackSet_Example_2"></a>

Use the `DescribeStackSets` API to output a list of Regions. This list consists of Regions where a given StackSet has stack instances deployed.

In the following example, the StackSet named "MyStackSet" has stack instances deployed in Regions "us-east-1" and "us-west-2":

```
{
    "StackSet": {
        "StackSetName": "MyStackSet",
        //...
        "Regions": [
            "us-east-1",
            "us-west-2"
        ]
    }
}
```

## See Also
<a name="API_DescribeStackSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeStackSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/DescribeStackSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeStackSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeStackSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeStackSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeStackSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeStackSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeStackSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeStackSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeStackSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
