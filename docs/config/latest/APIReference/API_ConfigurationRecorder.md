---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationRecorder.html
---

# ConfigurationRecorder
<a name="API_ConfigurationRecorder"></a>

Records configuration changes to the resource types in scope.

For more information about the configuration recorder, see [https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html) in the * AWS Config Developer Guide*.

## Contents
<a name="API_ConfigurationRecorder_Contents"></a>

 ** arn **   <a name="config-Type-ConfigurationRecorder-arn"></a>
The Amazon Resource Name (ARN) of the specified configuration recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** connectorArn **   <a name="config-Type-ConfigurationRecorder-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector that specifies the connection between a third-party cloud service provider and AWS Config.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** name **   <a name="config-Type-ConfigurationRecorder-name"></a>
The name of the configuration recorder.
For customer managed configuration recorders, AWS Config automatically assigns the name of "default" when creating a configuration recorder if you do not specify a name at creation time.
For service-linked configuration recorders, AWS Config automatically assigns a name that has the prefix "`AWSConfigurationRecorderFor`" to a new service-linked configuration recorder.
 **Changing the name of a configuration recorder**
To change the name of the customer managed configuration recorder, you must delete it and create a new customer managed configuration recorder with a new name.
You cannot change the name of a service-linked configuration recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** recordingGroup **   <a name="config-Type-ConfigurationRecorder-recordingGroup"></a>
Specifies which resource types are in scope for the configuration recorder to record.
 ** High Number of AWS Config Evaluations**
You might notice increased activity in your account during your initial month recording with AWS Config when compared to subsequent months. During the initial bootstrapping process, AWS Config runs evaluations on all the resources in your account that you have selected for AWS Config to record.
If you are running ephemeral workloads, you may see increased activity from AWS Config as it records configuration changes associated with creating and deleting these temporary resources. An *ephemeral workload* is a temporary use of computing resources that are loaded and run when needed. Examples include Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances, Amazon EMR jobs, and AWS Auto Scaling.
If you want to avoid the increased activity from running ephemeral workloads, you can set up the configuration recorder to exclude these resource types from being recorded, or run these types of workloads in a separate account with AWS Config turned off to avoid increased configuration recording and rule evaluations.
Type: [RecordingGroup](API_RecordingGroup.md) object
Required: No

 ** recordingMode **   <a name="config-Type-ConfigurationRecorder-recordingMode"></a>
Specifies the default recording frequency for the configuration recorder. AWS Config supports *Continuous recording* and *Daily recording*.
+ Continuous recording allows you to record configuration changes continuously whenever a change occurs.
+ Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded.
 **Some resource types require continuous recording**
 AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.
You can also override the recording frequency for specific resource types.
Type: [RecordingMode](API_RecordingMode.md) object
Required: No

 ** recordingScope **   <a name="config-Type-ConfigurationRecorder-recordingScope"></a>
Specifies whether the [ConfigurationItems](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html) in scope for the specified configuration recorder are recorded for free (`INTERNAL`) or if it impacts the costs to your bill (`PAID`).
Type: String
Valid Values: `INTERNAL | PAID`
Required: No

 ** roleARN **   <a name="config-Type-ConfigurationRecorder-roleARN"></a>
The Amazon Resource Name (ARN) of the IAM role assumed by AWS Config and used by the specified configuration recorder.
 **The server will reject a request without a defined `roleARN` for the configuration recorder**
While the API model does not require this field, the server will reject a request without a defined `roleARN` for the configuration recorder.
 **Policies and compliance results**
 [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) and [other policies managed in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html) can impact whether AWS Config has permissions to record configuration changes for your resources. Additionally, rules directly evaluate the configuration of a resource and rules don't take into account these policies when running evaluations. Make sure that the policies in effect align with how you intend to use AWS Config.
 **Keep Minimum Permisions When Reusing an IAM role**
If you use an AWS service that uses AWS Config, such as AWS Security Hub CSPM or AWS Control Tower, and an IAM role has already been created, make sure that the IAM role that you use when setting up AWS Config keeps the same minimum permissions as the pre-existing IAM role. You must do this to ensure that the other AWS service continues to run as expected.
For example, if AWS Control Tower has an IAM role that allows AWS Config to read S3 objects, make sure that the same permissions are granted to the IAM role you use when setting up AWS Config. Otherwise, it may interfere with how AWS Control Tower operates.
 **The service-linked IAM role for AWS Config must be used for service-linked configuration recorders**
For service-linked configuration recorders, you must use the service-linked IAM role for AWS Config: [AWSServiceRoleForConfig](https://docs.aws.amazon.com/config/latest/developerguide/using-service-linked-roles.html).
Type: String
Required: No

 ** scopeConfiguration **   <a name="config-Type-ConfigurationRecorder-scopeConfiguration"></a>
Specifies the scope of resources to record from the third-party cloud service provider connected through the connector.
Type: [ScopeConfiguration](API_ScopeConfiguration.md) object
Required: No

 ** servicePrincipal **   <a name="config-Type-ConfigurationRecorder-servicePrincipal"></a>
For service-linked configuration recorders, specifies the linked AWS service for the configuration recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

## See Also
<a name="API_ConfigurationRecorder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigurationRecorder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigurationRecorder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigurationRecorder)
